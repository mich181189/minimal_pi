import utils

def get_busybox(globalDefs):
    busyboxPackage = utils.configureMakePackage(  globalDefs,
                                        "busybox",
                                        "http://busybox.net/downloads/busybox-1.23.2.tar.bz2",
                                        "busybox-1.23.2")

    busyboxPackage.configureRule = utils.makefileRule(".busybox_configUpdate")
    busyboxPackage.configureRule.addCommand("cp packages/busybox.config "+globalDefs["BuildDir"]+"/"+
                                    busyboxPackage.workingDirectory+"/.config")
    busyboxPackage.configureRule.addCommand("python ../../packages/fixBusyboxConfig.py",
                                            globalDefs["BuildDir"]+"/"+busyboxPackage.workingDirectory)
    busyboxPackage.configureRule.addCommand("touch .busybox_configUpdate")
    busyboxPackage.configureRule.addCleanCommand("rm -f .busybox_configUpdate")

    flist = ["inittab","inetd.conf","mdev.conf"]

    for f in flist:
        busyboxPackage.makeInstallRule.addCommand("sudo env PATH=$$PATH cp -p "+
            globalDefs["BuildDir"]+"/"+busyboxPackage.workingDirectory+"/examples/"+f
            +" "+globalDefs["AbsTargetDir"]+"/etc/")
    return busyboxPackage