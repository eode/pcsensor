"""Constants for TEMPer Sensors for Temperature and Humidity."""
# Base component constants
NAME = "TEMPer Sensors for Temperature and Humidity"
DOMAIN = "temper_sensors"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"

ATTRIBUTION = ""
ISSUE_URL = "https://github.com/eode/temper-sensors/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
