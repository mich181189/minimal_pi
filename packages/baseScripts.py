import utils

def get_baseScripts(globalDefs):
    baseScripts = utils.basePackage("baseScripts")

    copyRule = utils.makefileRule(".basescripts_copy")
    copyRule.addCommand("sudo env PATH=$$PATH cp -rf packages/baseScripts/* "+globalDefs["AbsTargetDir"])
    copyRule.addCommand("sudo env PATH=$$PATH chmod +x "+globalDefs["AbsTargetDir"]+"/etc/init.d/rcS")
    copyRule.addCommand("sudo env PATH=$$PATH chmod 600 "+globalDefs["AbsTargetDir"]+"/etc/shadow")
    copyRule.addCommand("sudo env PATH=$$PATH chown root "+globalDefs["AbsTargetDir"]+"/etc/shadow")
    copyRule.addCommand("touch .basescripts_copy")
    copyRule.addCleanCommand("rm -f .basescripts_copy")
    baseScripts.addRule(copyRule)


    return baseScripts