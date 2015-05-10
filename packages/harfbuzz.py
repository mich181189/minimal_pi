import utils

def get_harfbuzz(globalDefs):
    globalDefs["EnvVars"]["CFLAGS"] += " -I"+globalDefs["AbsTargetDir"]+"/usr/include/freetype2 "
    globalDefs["EnvVars"]["CPPFLAGS"] += " -I"+globalDefs["AbsTargetDir"]+"/usr/include/freetype2 "
    globalDefs["EnvVars"]["LDFLAGS"] += " -L"+globalDefs["AbsTargetDir"]+"/usr/lib -L"+globalDefs["AbsTargetDir"]+"/lib "
    harfbuzz =  utils.configureMakePackage(globalDefs,
                                        "harfbuzz",
                                        "http://www.freedesktop.org/software/harfbuzz/release/harfbuzz-0.9.40.tar.bz2",
                                        "harfbuzz-0.9.40",
                                        "--with-cairo=no --with-sysroot="+globalDefs["AbsTargetDir"])
    harfbuzz.addDependency("icu")
    harfbuzz.addDependency("freetype_noharfbuzz")
    harfbuzz.addDependency("glib")
    harfbuzz.addDependency("fontconfig")
    return harfbuzz