"""Plugin declaration for netbox_nautobot_ansible."""

__version__ = "0.2.0"

from extras.plugins import PluginConfig


class NautobotAnsibleConfig(PluginConfig):
    """Plugin configuration for the netbox_nautobot_ansible plugin."""

    name = "netbox_nautobot_ansible"
    verbose_name = "NetBox Nautobot Ansible Tower integration"
    version = __version__
    author = "Network to Code, LLC"
    description = "NetBox Nautobot Ansible Tower integration."
    base_url = "nautobot_ansible"
    required_settings = []
    min_version = "2.8.3"
    default_settings = {}
    caching_config = {}


config = NautobotAnsibleConfig  # pylint:disable=invalid-name
