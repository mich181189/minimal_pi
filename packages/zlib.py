import utils

#zlib is *nearly* a standard configure rule
def makeConfigureRule_zlib(globalDefs,pkgName,workDir,extraArgs):
    rule = utils.makefileRule("."+pkgName+"_configured")
    commandText = ""
    for env,val in globalDefs["EnvVars"].iteritems():
        commandText = commandText+env+"=\""+val+"\" "

    commandText = commandText + "CC="+globalDefs["Architecture"]+"-gcc "

    rule.addCommand(commandText+"./configure "
                                " --prefix=/usr --includedir=/usr/include "+extraArgs,
                                globalDefs["BuildDir"]+"/"+workDir)

    rule.addCommand("touch ."+pkgName+"_configured")
    rule.addCleanCommand("rm -f ."+pkgName+"_configured")
    return rule

def get_zlib(globalDefs):
    zlib = utils.configureMakePackage(globalDefs,
                                        "zlib",
                                        "http://zlib.net/zlib-1.2.8.tar.gz",
                                        "zlib-1.2.8")

    zlib.configureRule = makeConfigureRule_zlib(globalDefs,"zlib","zlib-1.2.8","")

    return zlib