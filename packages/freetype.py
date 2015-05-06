import utils

def get_freetype(globalDefs):
    #the usual settings we use confuse libtool so we use these env variables instead
    globalDefs["EnvVars"]["INSTALLDIR"]=globalDefs["AbsTargetDir"]+"/usr"
    globalDefs["EnvVars"]["LDFLAGS"]= "--sysroot="+globalDefs["AbsTargetDir"]
    freetype = utils.configureMakePackage(globalDefs,
                                        "freetype",
                                        "http://download.savannah.gnu.org/releases/freetype/freetype-2.5.5.tar.bz2",
                                        "freetype-2.5.5",
                                        "--without-harfbuzz --includedir=/usr/include")
    freetype.addDependency("zlib")
    freetype.addDependency("libpng")
    return freetype