SUMMARY = "Telemetry MQTT Service"
LICENSE = "CLOSED"

SRC_URI = "file://telemetry.py file://telemetry-init"

S = "${WORKDIR}"

do_install() {
    install -d ${D}/opt/telemetry
    install -m 0755 ${WORKDIR}/telemetry.py ${D}/opt/telemetry/

    install -d ${D}/etc/init.d
    install -m 0755 ${WORKDIR}/telemetry-init ${D}/etc/init.d/telemetry
}

inherit update-rc.d

INITSCRIPT_NAME = "telemetry"
INITSCRIPT_PARAMS = "defaults"

FILES:${PN} += "/opt /opt/telemetry /opt/telemetry/telemetry.py /etc/init.d/telemetry"
