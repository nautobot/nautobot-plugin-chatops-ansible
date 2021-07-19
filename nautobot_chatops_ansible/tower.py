"""All interactions with Ansible AWX/Tower."""
import json
import logging
import os

import requests

from nautobot.core.settings_funcs import is_truthy

logger = logging.getLogger("rq.worker")


class Tower:  # pylint: disable=too-many-function-args
    """Representation and methods for interacting with Ansible Tower/AWX."""

    def __init__(
        self,
        origin,
        tower_uri=os.getenv("NAUTOBOT_TOWER_URI"),
        username=os.getenv("NAUTOBOT_TOWER_USERNAME"),
        password=os.getenv("NAUTOBOT_TOWER_PASSWORD"),
        verify_ssl=is_truthy(os.getenv("NAUTOBOT_TOWER_VERIFY_SSL", "true")),
    ):  # pylint: disable=too-many-arguments
        """Initialization of Tower class.

        Args:
            origin (namedtuple): Contains platform name and slug
            tower_uri (str): URI of Tower/AWX instance
            username (str): Username to log into Ansible Tower
            password (str): Password to log into Ansible Tower
            verify_ssl (bool): Verify SSL connections. Defaults to True.
        """
        if tower_uri:
            self.uri = tower_uri.rstrip()
        else:
            self.uri = None
        self.username = username
        self.password = password
        self.tower_verify_ssl = verify_ssl
        self.headers = {"Content-Type": "application/json"}
        self.origin = origin
        self.extra_vars = {}
        if not self.uri or not self.username or not self.password:
            raise ValueError(
                "Missing required parameters for Tower access - check environment and plugin configuration"
            )

    def _launch_job(self, template_name, extra_vars):
        """Launch a playbook in Ansible Tower.

        Args:
            template_name(str): Name of the template in Ansible tower which will be called
            extra_vars(dict): extra variables that will be passed to Ansible at run time
        """
        extra_vars["origin"] = self.origin.name
        extra_vars["chat_type"] = self.origin.slug
        url = f"{self.uri}/api/v2/job_templates/{template_name}/launch/"
        logger.info("Launch URL: %s", url)
        logger.info("Launch Extra Vars: %s", extra_vars)
        response = requests.post(
            url,
            auth=requests.auth.HTTPBasicAuth(self.username, self.password),
            headers=self.headers,
            data=json.dumps({"extra_vars": extra_vars}),
            verify=self.tower_verify_ssl,
        )
        response.raise_for_status()
        logger.info("Job submission to Ansible Tower:")
        logger.info(response.json())

        return response.json()

    def _get_tower(self, api_path, **kwargs):
        """Issues get to Ansible Tower at the api path specified.

        Args:
            api_path (str): API path to get data from

        Returns:
            (JSON): JSON data for the response
        """
        response = requests.get(f"{self.uri}/api/v2/{api_path}", auth=(self.username, self.password), **kwargs)
        return response.json()

    def get_tower_inventories(self):
        """Gets inventory of devices in Ansible Tower."""
        return self._get_tower("inventories/")

    def get_tower_inventory_id(self, inventory_name: str):  # pylint: disable=inconsistent-return-statements
        """Gets Tower inventory ID from list of inventories.

        Args:
            inventory_name (str): Name of the inventory to get

        Returns:
            (int): Inventory ID
        """
        inventories = self.get_tower_inventories()["results"]
        for inventory in inventories:
            if inventory["name"] == inventory_name:
                return inventory["id"]

    def get_tower_inventory_groups(self, inventory):
        """Gets Tower groups from inventory.

        Args:
            inventory (str): Name of the inventory

        Returns:
            (json): JSON data of the Tower groups
        """
        return self._get_tower(f"inventories/{inventory}/groups/")

    def get_tower_group_id(self, inventory_id: int, group_name: str):  # pylint: disable=inconsistent-return-statements
        """Gets Group ID from groups.

        Args:
            group_name (str): Name of the desired group
            inventory_id (str): The inventory ID
        """
        groups = self.get_tower_inventory_groups(inventory=inventory_id)["results"]
        for group in groups:
            if group["name"] == group_name:
                return group["id"]

    def get_tower_inventory_hosts(self, group_id):
        """Gets hosts for a given Tower inventory.

        Args:
            group (str): Group Name

        Returns:
            (json): JSON data of the Tower hosts
        """
        return self._get_tower(f"groups/{group_id}/hosts/")

    def get_tower_dashboard(self):
        """Gets dashboard data from Ansible Tower.

        This is likely to be deprecated in the future per docs.

        Returns:
            dict: Dictionary results
        """
        return self._get_tower("dashboard/")

    def get_tower_jobs(self, count: int):
        """Gets Tower Job results.

        Args:
            count (int): Number of jobs to get

        Returns:
            dict: Job results
        """
        response = self._get_tower("jobs/", params={"order_by": "-created", "page_size": str(count)})
        return response["results"]

    def get_tower_projects(self):
        """Gets tower projects.

        Returns:
            dict: Tower projects return
        """
        response = self._get_tower("projects/")
        return response["results"]

    def run_tower_template(self, dispatcher, template_name):
        """Executes a tower template.

        Args:
            dispatcher (dispatcher): Information about the dispatcher (chat client)
            template_name (str): Name of the template

        Returns:
            Requests.response: Response of requests
        """
        response = self._launch_job(
            template_name=template_name,
            extra_vars={"channel": dispatcher.context.get("channel_name")},
        )
        return response

    def get_tower_template(self, template_name):
        """Gets tower template from a name.

        Args:
            template_name (str): Name of the template to get

        Returns:
            requests.response: Requests response
        """
        return self._get_tower("job_templates/", params={"name": template_name})

    def retrieve_job_templates(self):
        """Get job template listing from Ansible."""
        response = self._get_tower("job_templates/")
        return response["results"]
