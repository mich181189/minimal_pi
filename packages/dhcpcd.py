import utils

def get_dhcpcd(globalDefs):
    return utils.configureMakePackage(globalDefs,
                                        "dhcpcd",
                                        "http://roy.marples.name/downloads/dhcpcd/dhcpcd-6.8.2.tar.bz2",
                                        "dhcpcd-6.8.2",
                                        "--without-udev --sysconfdir=/etc")