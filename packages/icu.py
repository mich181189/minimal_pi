import utils

def get_icu(globalConf):
    url = "http://download.icu-project.org/files/icu4c/55.1/icu4c-55_1-src.tgz"
    workdir = "icu"
    icu = utils.basePackage("icu")

    downloadRule = utils.makeDownloadRule(globalConf,url)
    icu.addRule(downloadRule)

    extractRule = utils.makeExtractRule(globalConf,url)
    extractRule.addDependency(downloadRule.name)
    icu.addRule(extractRule)

    host_mkdir = utils.makefileRule(".icu_host_workdir")
    host_mkdir.addCommand("mkdir -p "+globalConf["BuildDir"]+"/"+workdir+"/host")
    host_mkdir.addCommand("touch .icu_host_workdir")
    host_mkdir.addCleanCommand("rm -f .icu_host_workdir")
    host_mkdir.addDependency(extractRule.name)
    icu.addRule(host_mkdir)

    host_configure = utils.makefileRule(".icu_host_configure")
    host_configure.addCommand("../source/configure",globalConf["BuildDir"]+"/"+workdir+"/host")
    host_configure.addCommand("touch .icu_host_configure")
    host_configure.addCleanCommand("rm -f .icu_host_configure")
    host_configure.addDependency(host_mkdir.name)
    icu.addRule(host_configure)

    host_make = utils.makeMakeRule(globalConf,"icu_host",workdir+"/host")
    host_make.addDependency(host_configure.name)
    icu.addRule(host_make)

    target_configure = utils.makeConfigureRule(globalConf,"icu_target",workdir+"/source"
                    ,"--with-cross-build="+globalConf["BaseDir"]+"/"+globalConf["BuildDir"]+"/"+workdir+"/host")
    target_configure.addDependency(host_make.name)
    icu.addRule(target_configure)

    target_make = utils.makeMakeRule(globalConf,"icu_target",workdir+"/source")
    target_make.addDependency(target_configure.name)
    icu.addRule(target_make)

    target_make_install = utils.makeInstallRule(globalConf,"icu_target",workdir+"/source")
    target_make_install.addDependency(target_make.name)
    icu.addRule(target_make_install)

    return icu




