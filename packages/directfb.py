import utils

def get_directfb(globalDefs):
    globalDefs["EnvVars"]["CFLAGS"] += " -I"+globalDefs["AbsTargetDir"]+"/usr/include/freetype2 "
    globalDefs["EnvVars"]["CPPFLAGS"] += " -I"+globalDefs["AbsTargetDir"]+"/usr/include/freetype2 "
    globalDefs["EnvVars"]["LDFLAGS"] += " -L"+globalDefs["AbsTargetDir"]+"/usr/lib -L"+globalDefs["AbsTargetDir"]+"/lib "
    directfb = utils.configureMakePackage(globalDefs,
                                        "directfb",
                                        "http://directfb.org/downloads/Core/DirectFB-1.7/DirectFB-1.7.7.tar.gz",
                                        "DirectFB-1.7.7",
                                        "--disable-docs --enable-sawman=yes --enable-x11=no --with-gfxdrivers=none --with-libtool-sysroot="+globalDefs["AbsTargetDir"]+" --with-sysroot="+globalDefs["AbsTargetDir"])

    directfb.extractRule.addCommand("autoreconf --install --force",globalDefs["BuildDir"]+"/DirectFB-1.7.7")

    directfb.addDependency("freetype")
    directfb.addDependency("libdrm")
    directfb.addDependency("libtiff")
    directfb.addDependency("libwebp")

    return directfb