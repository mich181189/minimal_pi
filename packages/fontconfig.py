import utils

def get_fontconfig(globalDefs):
    globalDefs["EnvVars"]["CFLAGS"] += " -I"+globalDefs["AbsTargetDir"]+"/usr/include/freetype2 "
    globalDefs["EnvVars"]["CPPFLAGS"] += " -I"+globalDefs["AbsTargetDir"]+"/usr/include/freetype2 "
    fontconfig =  utils.configureMakePackage(globalDefs,
                                        "fontconfig",
                                        "http://www.freedesktop.org/software/fontconfig/release/fontconfig-2.11.93.tar.bz2",
                                        "fontconfig-2.11.93",
                                        "--disable-docs")
    fontconfig.addDependency("expat")
    return fontconfig