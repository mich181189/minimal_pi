import utils

def get_libdrm(globalDefs):
    libdrm = utils.configureMakePackage(globalDefs,
                                        "libdrm",
                                        "http://dri.freedesktop.org/libdrm/libdrm-2.4.58.tar.gz",
                                        "libdrm-2.4.58",
                                        "--enable-cairo-tests=no --with-sysroot="+globalDefs["AbsTargetDir"])
    libdrm.addDependency("kernelHeaders")
    return libdrm