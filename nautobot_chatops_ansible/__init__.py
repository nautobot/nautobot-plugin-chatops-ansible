"""Plugin declaration for nautobot_chatops_ansible."""

__version__ = "1.0.1"

from nautobot.extras.plugins import PluginConfig


class NautobotAnsibleConfig(PluginConfig):
    """Plugin configuration for the nautobot_chatops_ansible plugin."""

    name = "nautobot_chatops_ansible"
    verbose_name = "Nautobot Nautobot Ansible Tower integration"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobot Nautobot Ansible Tower integration."
    base_url = "nautobot_ansible"
    required_settings = []
    min_version = "1.0.0b1"
    default_settings = {}
    caching_config = {}


config = NautobotAnsibleConfig  # pylint:disable=invalid-name
