import utils

def get_kernelHeaders(globalDefs):
    url = "https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.18.12.tar.xz"
    workDir="linux-3.18.12"
    package = utils.basePackage("kernelHeaders")

    downloadRule = utils.makeDownloadRule(globalDefs,url)
    package.addRule(downloadRule)

    extractRule = utils.makeExtractRule(globalDefs,url)
    extractRule.addDependency(downloadRule.name)
    package.addRule(extractRule)

    installRule = utils.makefileRule(".kernelheaders_install")
    installRule.addCommand("sudo env PATH=$$PATH $(MAKE) ARCH=arm INSTALL_HDR_PATH="+
                            globalDefs["AbsTargetDir"]+"/usr -C "+globalDefs["BuildDir"]+"/"+workDir+" headers_install")
    installRule.addCommand("touch .kernelheaders_install")
    installRule.addCleanCommand("rm -f .kernelheaders_install")
    installRule.addDependency(extractRule.name)
    package.addRule(installRule)

    return package
