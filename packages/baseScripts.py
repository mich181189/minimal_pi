import utils

def get_baseScripts(globalDefs):
    baseScripts = utils.basePackage("baseScripts")

    copyRule = utils.makefileRule(".basescripts_copy")
    copyRule.addCommand("sudo env PATH=$$PATH cp -rpf packages/baseScripts/* "+globalDefs["AbsTargetDir"])
    copyRule.addCommand("touch .basescripts_copy")
    copyRule.addCleanCommand("rm -f .basescripts_copy")
    baseScripts.addRule(copyRule)


    return baseScripts