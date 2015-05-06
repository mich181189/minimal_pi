import utils

def get_glib(globalDefs):
    glib = utils.configureMakePackage(globalDefs,
                                        "glib",
                                        "http://ftp.gnome.org/pub/gnome/sources/glib/2.44/glib-2.44.0.tar.xz",
                                        "glib-2.44.0",
                                        "--cache-file=glib.cache")
    glib.addDependency("libffi")
    glib.extraFixRule = utils.makefileRule(globalDefs["BuildDir"]+"/"+glib.workingDirectory+"/glib.cache")
    glib.extraFixRule.addCommand("autoreconf --install --force",globalDefs["BuildDir"]+"/"+glib.workingDirectory)
    glib.extraFixRule.addCommand("cp packages/glib.cache "+glib.extraFixRule.name)
    glib.extraFixRule.addDependency("packages/glib.cache")
    return glib