import utils

def getRasPiExtras(globalDefs):
    package = utils.basePackage("rasPiExtras")

    cloneRule = utils.makefileRule(globalDefs["DownloadDir"]+"/firmware/README")
    cloneRule.addCommand("git clone https://github.com/raspberrypi/firmware.git --depth=1",globalDefs["DownloadDir"])
    package.addRule(cloneRule)
    package.addDirectory(globalDefs["RelTargetDir"]+"/opt")


    copyDocsRule = utils.makefileRule(".copiedRasPiFwDocs")
    copyDocsRule.addDependency(cloneRule.name)
    copyDocsRule.addCommand("sudo env PATH=$$PATH cp -pr "+globalDefs["DownloadDir"]+"/firmware/documentation "+globalDefs["RelTargetDir"]+"/opt/")
    copyDocsRule.addCommand("touch .copiedRasPiFwDocs")
    copyDocsRule.addCleanCommand("rm -f .copiedRasPiFwDocs")
    package.addRule(copyDocsRule)

    copyHardFPRule = utils.makefileRule(".copiedRasPiFwHardFP")
    copyHardFPRule.addDependency(cloneRule.name)
    copyHardFPRule.addCommand("sudo env PATH=$$PATH cp -pr "+globalDefs["DownloadDir"]+"/firmware/hardfp/opt/* "+globalDefs["RelTargetDir"]+"/opt/")
    copyHardFPRule.addCommand("touch .copiedRasPiFwHardFP")
    copyHardFPRule.addCleanCommand("rm -f .copiedRasPiFwHardFP")
    package.addRule(copyHardFPRule)

    return package
