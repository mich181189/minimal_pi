import utils

def get_libtirpc(globalDefs):
    return utils.configureMakePackage(  globalDefs,
                                        "libtirpc",
                                        "http://downloads.sourceforge.net/project/libtirpc/libtirpc/0.2.5/libtirpc-0.2.5.tar.bz2",
                                        "libtirpc-0.2.5",
                                        "--disable-gssapi --sysconfdir=/etc")