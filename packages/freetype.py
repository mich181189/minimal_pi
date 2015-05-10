import utils

freetype_workDir="freetype-2.5.5"

def get_freetype_noharfbuzz(globalDefs):
    #the usual settings we use confuse libtool so we use these env variables instead
    globalDefs["EnvVars"]["INSTALLDIR"]=globalDefs["AbsTargetDir"]+"/usr"
    globalDefs["EnvVars"]["LDFLAGS"]= "--sysroot="+globalDefs["AbsTargetDir"]
    freetype = utils.configureMakePackage(globalDefs,
                                        "freetype_noharfbuzz",
                                        "http://download.savannah.gnu.org/releases/freetype/freetype-2.5.5.tar.bz2",
                                        freetype_workDir,
                                        "--without-harfbuzz --includedir=/usr/include")
    freetype.addDependency("zlib")
    freetype.addDependency("libpng")
    return freetype

def get_freetype(globalDefs):
    #the usual settings we use confuse libtool so we use these env variables instead
    globalDefs["EnvVars"]["INSTALLDIR"]=globalDefs["AbsTargetDir"]+"/usr"
    globalDefs["EnvVars"]["LDFLAGS"]= "--sysroot="+globalDefs["AbsTargetDir"]
    freetype = utils.configureMakePackage(globalDefs,
                                        "freetype",
                                        "",
                                        freetype_workDir,
                                        "--includedir=/usr/include")
    freetype.configureRule.addCommand("make clean",globalDefs["BuildDir"]+"/"+freetype_workDir)
    freetype.addDependency("zlib")
    freetype.addDependency("libpng")
    freetype.addDependency("harfbuzz")
    return freetype