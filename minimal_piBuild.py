#Minimal Pi metabuild system

import utils
import os

globalConf =    {  
                    "DownloadDir":"downloads",
                    "Architecture": os.environ["MINIMALPI_ARCH"],
                    "RelTargetDir": "target",
                    "AbsTargetDir": os.environ["MINIMALPI_ROOT"]+"/target",
                    "BuildDir": "buildPkgs",
                    "BaseDir": os.environ["MINIMALPI_ROOT"],
                    "EnvVars": {
                                "CFLAGS":"-I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include "+
                                            "-I"+os.environ["MINIMALPI_ROOT"]+"/target/opt/vc/include",
                                "CPPFLAGS":"-I"+os.environ["MINIMALPI_ROOT"]+"/target/usr/include "+
                                            "-I"+os.environ["MINIMALPI_ROOT"]+"/target/opt/vc/include",
                                "LDFLAGS":"-L"+os.environ["MINIMALPI_ROOT"]+"/target/usr/lib "
                                            +"-L"+os.environ["MINIMALPI_ROOT"]+"/target/lib "
                                            +"-L"+os.environ["MINIMALPI_ROOT"]+"/target/opt/vc/lib "
                                            +"--sysroot="+os.environ["MINIMALPI_ROOT"]+"/target",
                    }
                }

DIRECTORIES =   [
                    globalConf["DownloadDir"],
                    globalConf["BuildDir"],
                    globalConf["RelTargetDir"]+"/"+"root",
                    globalConf["RelTargetDir"]+"/"+"proc",
                    globalConf["RelTargetDir"]+"/"+"sys",
                    globalConf["RelTargetDir"]+"/"+"boot",
                    globalConf["RelTargetDir"]+"/"+"dev",
                ]

from packages import *
packageDict = {
                "libtirpc":libtirpc.get_libtirpc(globalConf),
                "rasPiExtras":rasPiExtras.getRasPiExtras(globalConf),
                "busybox":busybox.get_busybox(globalConf),
                "dhcpcd":dhcpcd.get_dhcpcd(globalConf),
                "baseScripts":baseScripts.get_baseScripts(globalConf),
                "jpeg":jpeg.get_jpeg(globalConf),
                "icu":icu.get_icu(globalConf),
                "kernelHeaders":kernelHeaders.get_kernelHeaders(globalConf),
                "libffi":libffi.get_libffi(globalConf),
                "zlib":zlib.get_zlib(globalConf),
                "libpng":libpng.get_png(globalConf),
                "libtiff":libtiff.get_tiff(globalConf),
                "libwebp":libwebp.get_libwebp(globalConf),
                "freetype_noharfbuzz":freetype.get_freetype_noharfbuzz(globalConf),
                "ncurses":ncurses.get_ncurses(globalConf),
                "nano":nano.get_nano(globalConf),
                "htop":htop.get_htop(globalConf),
                "glib":glib.get_glib(globalConf),
                "expat":expat.get_expat(globalConf),
                "fontconfig":fontconfig.get_fontconfig(globalConf),
                "harfbuzz":harfbuzz.get_harfbuzz(globalConf),
                "freetype":freetype.get_freetype(globalConf),
                "libdrm":libdrm.get_libdrm(globalConf),
                "directfb":directfb.get_directfb(globalConf),
                }

#TEMP_PROFILE
TEMP_PROFILE = ["libtirpc","rasPiExtras","busybox","dhcpcd","baseScripts","jpeg","icu","kernelHeaders",
                "libffi","zlib","libpng","libtiff","libwebp","freetype","ncurses","nano","htop",
                "glib","expat","fontconfig","harfbuzz","freetype_noharfbuzz","libdrm","directfb"]

#write the makefile

makefile = open("Makefile","w")

##################################################
# Top Level Rules                                #
##################################################
all_rule = utils.makefileRule("all")
all_rule.depends = DIRECTORIES+["packages"]

rules = [all_rule]

packages_rule = utils.makefileRule("packages")
packages_rule.depends = TEMP_PROFILE
rules.append(packages_rule)

##################################################
# Target directory rules                         #
##################################################
print "Adding rules for target directory"
target_rule = utils.makefileRule(globalConf["RelTargetDir"])
target_rule.addDependency("."+globalConf["RelTargetDir"]+"_created")
target_real_rule = utils.makefileRule("."+globalConf["RelTargetDir"]+"_created")
target_real_rule.addCleanCommand("rm -f ."+globalConf["RelTargetDir"]+"_created")
target_real_rule.addCommand("mkdir -p "+globalConf["RelTargetDir"])
target_real_rule.addCommand("sudo env PATH=$$PATH cp -rp toolchain/"+globalConf["Architecture"]+"/"+globalConf["Architecture"]+"/sysroot/* "+globalConf["RelTargetDir"])
target_real_rule.addCommand("touch ."+globalConf["RelTargetDir"]+"_created")

rules.append(target_rule)
rules.append(target_real_rule)

##################################################
# Package Rules                                  #
##################################################
for packageName in TEMP_PROFILE:
    print "Inserting rules for " + packageName
    DIRECTORIES = DIRECTORIES + packageDict[packageName].dirs
    rules = rules + packageDict[packageName].getRules()

##################################################
# Directory Structure Rules                      #
##################################################
createdDirs = [globalConf["RelTargetDir"]]
for directory in DIRECTORIES:
    soFar = ""
    deps = []
    for part in directory.split("/"):
        if soFar == "":
            soFar = part
        else:
            soFar = soFar+"/"+part
        if not soFar in createdDirs:
            print "Adding rule to create directory " + soFar
            dirRule = utils.makefileRule(".created_"+soFar.replace("/","."))
            dirRule.addCommand("mkdir -p "+soFar)
            dirRule.addCommand("touch .created_"+soFar.replace("/","."))
            dirRule.addCleanCommand("rm -f .created_"+soFar.replace("/","."))
            dirRule_dummy = utils.makefileRule(soFar)
            dirRule_dummy.addDependency(".created_"+soFar.replace("/","."))
            for dep in deps:
                dirRule_dummy.addDependency(dep)
            createdDirs.append(soFar)
            deps.append(soFar)
            rules.append(dirRule)
            rules.append(dirRule_dummy)

##################################################
# Cleanup rule                                   #
##################################################
cleanRule = utils.makefileRule("clean")
for rule in rules:
    cleanRule.commands = cleanRule.commands + rule.clean_commands
cleanRule.addCommand("rm -rf "+globalConf["RelTargetDir"])
cleanRule.addCommand("rm -rf "+globalConf["BuildDir"])

rules.append(cleanRule)

for rule in rules:
    rule.write(makefile)

makefile.close()