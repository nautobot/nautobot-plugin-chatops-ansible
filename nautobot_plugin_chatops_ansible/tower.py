"""All interactions with Ansible AWX/Tower."""
import os

import requests

TOWER_URI = os.getenv("NAUTOBOT_TOWER_URI")
TOWER_USERNAME = os.getenv("NAUTOBOT_TOWER_USERNAME")
TOWER_PASSWORD = os.getenv("NAUTOBOT_TOWER_PASSWORD")


def tower_api(action, api_path, **kwargs):
    """Make a call to the AWX / Tower REST API.

    Args:
      action (str): HTTP action "POST", "GET" etc.
      api_path (str): API path such as "jobs/"; "{TOWER_URI}/api/v2/" will be automatically prepended.
      **kwargs: Passed through to requests.request() call.

    Returns:
      requests.Response
    """
    if not TOWER_URI or not TOWER_USERNAME or not TOWER_PASSWORD:
        raise ValueError("Missing required parameters for Tower access - check environment and plugin configuration")

    if "headers" not in kwargs:
        kwargs["headers"] = {}
    if "Accept" not in kwargs["headers"]:
        kwargs["headers"]["Accept"] = "application/json"

    return requests.request(action, f"{TOWER_URI}/api/v2/{api_path}", auth=(TOWER_USERNAME, TOWER_PASSWORD), **kwargs)


def retrieve_job_templates():
    """Get job template listing from Ansible."""
    response = tower_api("GET", "job_templates/")
    data = response.json()
    return data["results"]
