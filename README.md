# nautobot-plugin-chatops-ansible

A plugin for [Nautobot](https://github.com/nautobot/nautobot) [Chatops Plugin](https://github.com/nautobot/nautobot-plugin-chatops/)

## Build Status

| Branch      | Status |
|-------------|------------|
| **main** | [![Build Status](https://www.travis-ci.com/nautobot/nautobot-plugin-chatops-ansible.svg?token=D7kytCzfCypoGoueSBqJ&branch=main)](https://www.travis-ci.com/github/nautobot/nautobot-plugin-chatops-ansible) |
| **develop** | [![Build Status](https://www.travis-ci.com/nautobot/nautobot-plugin-chatops-ansible.svg?token=D7kytCzfCypoGoueSBqJ&branch=develop)](https://www.travis-ci.com/github/nautobot/nautobot-plugin-chatops-ansible) |
## Summary

The Nautobot Chatops Ansible plugin extends the capabilities of the Nautobot Chatops plugin to include a new command available to the plugin. This is done by registering to the Python entry point in Nautobot Plugin Chatops, that provides functionality to the code written to interact with Ansible. This plugin introduces the following sub commands to the `ansible` command:

* get_dashboard
* get_inventory
* get_projects
* get_job_templates
* run_job_template
* get_jobs

### Dashboard

The dashboard command provides an Ansible Tower/AWX status dashboard. This gives a summary of:
* How many hosts are on the Tower system
* How many failed hosts (last job is failed)
* Total number of inventories
* How many inventories have failed
* How many project sync failures have occurred

### Inventory

The inventory sub-command provides for having inventory details. Providing what hosts are in what inventory.

### Get Projects

Get projects will gather information about the projects available within the Ansible Tower/AWX instance. Information such as the name, description, SCM URL, and SCM branch are provided.

### Job Templates

This gathers the information about the defined job templates on the Ansible Tower/AWX instance. It will provide the name, description, project, and the associated inventory with the Job Template configured.

### Run Job Template

The natural progression of gathering job templates is then to execute a particular job template. If a templates does not need any extra vars or surveys to be completed, it will be able to be executed. The response from Ansible Tower/AWX of the job number will then be provided back via chat to know what job number was executed.

### Get Job

The get jobs sub command will ask Tower for the last number of jobs, with a default count of the last 10 jobs. This will give the status of the jobs including:

* Job ID
* Name of the Job
* User that launched the job
* Created
* Finish time
* Status of the job

## Installation

The plugin is available as a Python package in PyPI and can be installed with pip

```shell
pip install git+https://github.com/nautobot/nautobot-plugin-chatops-ansible.git
```

This ChatOps Plugin to Nautobot ChatOps Plugin requires the following list of environment variables to be added into the environment.

- `NAUTOBOT_TOWER_URI`: Ansible Tower HTTP URI
- `NAUTOBOT_TOWER_USERNAME`: Ansible Tower username
- `NAUTOBOT_TOWER_PASSWORD`: Ansible Tower password

Once you have updated your environment file, restart both nautobot and nautobot-worker

```
$ sudo systemctl restart nautobot nautobot-worker
```

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
  tests            Run all tests.
  pydocstyle       Run pydocstyle to validate docstring formatting adheres to NTC defined standards.
  bandit           Run bandit to validate basic static code security analysis.
  black            Run black to check that Python files adhere to its style standards.
  unittest         Run Django unit tests for the plugin.
```

## Questions

For any questions or comments, feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).
Sign up [here](http://slack.networktocode.com/)
