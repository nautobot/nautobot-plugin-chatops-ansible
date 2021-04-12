# nautobot-plugin-chatops-ansible

A plugin for [Nautobot](https://github.com/nautobot/nautobot).

## Installation

### Build Status

| Branch      | Status |
|-------------|------------|
| **main** | [![Build Status](https://travis-ci.com/networktocode-llc/nautobot-plugin-chatops-ansible.svg?token=BknroZ7vxquiYcUvP8RC&branch=main)](https://travis-ci.com/networktocode-llc/nautobot-plugin-chatops-ansible) |
| **develop** | [![Build Status](https://travis-ci.com/networktocode-llc/nautobot-plugin-chatops-ansible.svg?token=BknroZ7vxquiYcUvP8RC&branch=develop)](https://travis-ci.com/networktocode-llc/nautobot-plugin-chatops-ansible) |

The plugin is available as a Python package in pypi and can be installed with pip

```shell
pip install git+https://github.com/nautobot/nautobot-plugin-chatops.git
```

> The plugin is compatible with Nautobot 1.0.0 and higher

Once installed, the plugin needs to be enabled in your `configuration.py`:

```python
# In your configuration.py
PLUGINS = ["nautobot_chatops", "nautobot_plugin_chatops_ansible"]

PLUGINS_CONFIG = {
  "nautobot_chatops": {
    # ...
  },
  "nautobot_plugin_chatops_ansible": {
    # ADD YOUR SETTINGS HERE
  }
}
```

The plugin requires the following list of settings (to be added to the `nautobot_plugin_chatops_ansible` key above).

- `tower_uri`: Ansible Tower HTTP URI
- `tower_username`: Ansible Tower username
- `tower_password`: Ansible Tower password

## Usage

### Command setup

Add a slash command to Slack called `/ansible`.
See the [nautobot-chatops installation guide](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/docs/chat_setup.md) for instructions on adding a slash command to your Slack channel.

You may need to adjust your [Access Grants in Nautobot](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/docs/chat_setup.md#grant-access-to-the-chatbot) depending on your security requirements.

## Contributing

Pull requests are welcomed and automatically built and tested against multiple version of Python and multiple version of Nautobot through TravisCI.

The project is packaged with a light development environment based on `docker-compose` to help with the local development of the project and to run the tests within TravisCI.

The project is following Network to Code software development guideline and is leveraging:

- Black, Pylint, Bandit and pydocstyle for Python linting and formatting.
- Django unit test to ensure the plugin is working properly.

### CLI Helper Commands

The project is coming with a CLI helper based on [invoke](http://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories `dev environment`, `utility` and `testing`.

Each command can be executed with `invoke <command>`. All commands support the arguments `--nautobot-ver` and `--python-ver` if you want to manually define the version of Python and Nautobot to use. Each command also has its own help `invoke <command> --help`

#### Local dev environment

```no-highlight
  build            Build all docker images.
  debug            Start Nautobot and its dependencies in debug mode.
  destroy          Destroy all containers and volumes.
  start            Start Nautobot and its dependencies in detached mode.
  stop             Stop Nautobot and its dependencies.
```

#### Utility

```no-highlight
  cli              Launch a bash shell inside the running Nautobot container.
  create-user      Create a new user in django (default: admin), will prompt for password.
  makemigrations   Run Make Migration in Django.
  nbshell          Launch a nbshell session.
```

#### Testing

```no-highlight
  tests            Run all tests for this plugin.
  pydocstyle       Run pydocstyle to validate docstring formatting adheres to NTC defined standards.
  bandit           Run bandit to validate basic static code security analysis.
  black            Run black to check that Python files adhere to its style standards.
  unittest         Run Django unit tests for the plugin.
```

## Questions

For any questions or comments, feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).
Sign up [here](http://slack.networktocode.com/)
