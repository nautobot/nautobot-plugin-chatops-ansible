"""Nautobot configuration file overrides specific to the latest v1.0.0 version."""

# Make the django-debug-toolbar always visible when DEBUG is enabled,
# except when we're running Django unit-tests.
import sys  # pylint: disable=wrong-import-order

TESTING = len(sys.argv) > 1 and sys.argv[1] == "test"
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda: DEBUG and not TESTING}  # pylint: disable=undefined-variable

# Overrides specific to this version go here
