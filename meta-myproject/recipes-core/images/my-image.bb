DESCRIPTION = "My custom image with Python and MQTT"

LICENSE = "MIT"

inherit core-image

IMAGE_INSTALL += " \
    python3 \
    python3-paho-mqtt \
    telemetry \
"
