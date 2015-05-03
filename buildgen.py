#Generates the MinimalPi Makefile
# Why? because the MakeFile ended up being really repetetive!

import os

#first, some settings

DIR_ROOT="target"
DIR_DOWNLOAD="downloads"
DIR_BUILD="buildPkgs"

#Package Definitions
from packageDefs.busybox import busybox
from packageDefs.libtirpc import libtirpc

#Package list
PACKAGES=[libtirpc,busybox]

#functions for writing a makefile
def writeRule(f,target,dependencies,rules):
    f.write(target+": ")
    for dependency in dependencies:
        f.write(dependency + " ")
    f.write("\n")
    for rule in rules:
        f.write("\t"+rule+"\n")
    f.write("\n")

def downloadSource(f,toget):
    deps = []
    destFile = DIR_DOWNLOAD+"/"+toget.rsplit("/",1)[1]
    rules = ["cd " + DIR_DOWNLOAD + " && wget " + toget]
    writeRule(f,destFile,deps,rules)
    return destFile

def copyFile(f,src,dest):
    deps = [src]
    rules = ["cp " + src + " " + dest]
    writeRule(f,dest,deps,rules)

def writePackageRules(f,package):
    global cleanCommands,installCommands
    print "Writing rules for " + package["name"]
    deps = []
    rules = []
    rules.append("cd " + DIR_BUILD)
    if "source" in package:
        srcfile = downloadSource(f,package["source"])
        deps.append(srcfile)
        rules.append("if [ ! -d "+package["buildDir"]+" ]; then tar -xf ../" + srcfile + "; fi")
        cleanCommands.append("rm -rf "+DIR_BUILD+"/"+package["buildDir"])
    
    #copy any extra files needed by this package
    if "extraFiles" in package:
        for src,dest in package["extraFiles"].iteritems():
            rules.append("cp ../packageDefs/"+src+" " + package["buildDir"]+"/"+dest)

    #Head on into build directory itself and start work
    rules.append("cd " + package["buildDir"])

    #Call any extra scripts this package needs for setup
    if "extraScripts" in package:
        for script in package["extraScripts"]:
            rules.append("python ../../packageDefs/"+script)

    for dep in package["dependencies"]:
        deps.append(dep)
    
    #set some defaults
    if not "configure" in package:
        package["configure"] = "./configure --prefix="+os.environ["MINIMALPI_ROOT"]+"/" \
        +DIR_ROOT+"/usr --host="+os.environ["MINIMALPI_ARCH"] + \
        " --with-sysroot="+os.environ["MINIMALPI_ROOT"]+"/"+DIR_ROOT

        if "extraconfig" in package:
            package["configure"] = package["configure"] + " " + package["extraconfig"]

    rules.append(package["configure"])
    
    #Otherwise we'll do a normal recursive make
    extraMakeRules = []
    if "make" in package:
        extraMakeRules.append("cd " + DIR_BUILD+"/"+package["buildDir"] + " && " + package["make"])
    else:
        extraMakeRules.append("$(MAKE) -j4 -C " + DIR_BUILD+"/"+package["buildDir"])

    if "make_install" in package:
        extraMakeRules.append("cd " + DIR_BUILD+"/"+package["buildDir"] + " && " + package["make_install"])
    else:
        extraMakeRules.append("sudo env PATH=$$PATH $(MAKE) -C " + DIR_BUILD+"/"+package["buildDir"] + " install")

    realrules = ""

    for rule in rules:
        if realrules != "" and rule != "":
            realrules = realrules + "; \\\n\t"
        realrules = realrules + rule

    extraMakeRules[:0] = [realrules]

    if "extraInstall" in package:
        writeRule(f,package["name"]+"_main",deps,extraMakeRules)
        extraDeps = [package["name"]+"_main"]
        for src,dest in package["extraInstall"].iteritems():
            writeRule(f,DIR_ROOT+dest,[DIR_BUILD+"/"+package["buildDir"]+"/"+src],
                ["sudo env PATH=$$PATH cp "+DIR_BUILD+"/"+package["buildDir"]+"/"+src+" "+DIR_ROOT+dest])
            extraDeps.append(DIR_ROOT+dest)
        writeRule(f,package["name"],extraDeps,[])

    else:
        writeRule(f,package["name"],deps,extraMakeRules)
    

#scratch variable to hold the directories we've created rules for
doneDirs = []
def createDirectory(f,directory):
    global doneDirs
    deps = []
    soFar = ""
    for part in directory.split("/"):
      if soFar == "":
          soFar = part
      else:
          soFar = soFar+"/"+part
      if not soFar in doneDirs:
        print "Writing rules to create " + directory
        writeRule(f,soFar,deps,['mkdir -p '+soFar])
        doneDirs.append(soFar)
      deps.append(soFar)

def createLink(f,src,dest):
    print "Writing rules to create link from " + dest + " to " + src
    deps = [dest,src.rsplit("/",1)[0]]
    createDirectory(f,src.rsplit("/",1)[0])
    writeRule(f,src,deps,["ln -sf " + dest + " " + src])
    
#####################################################
# main logic
#####################################################
print "MinimalPi Makefile Generator"
print ""
#figure out what targets we need to build by default
mainTargets = ["directories","packages"]
dirTargets = [DIR_DOWNLOAD,DIR_BUILD]
linkTargets = []
cleanCommands = ["rm -rf "+DIR_ROOT]
packageDeps = []

for package in PACKAGES:
    packageDeps.append(package["name"])

#Write the makefile
makefile = open("Makefile","w")

print "Making top level rules"
#first the default targets
makefile.write("####################################################\n")
makefile.write("# Top level rules\n")
makefile.write("####################################################\n")
writeRule(makefile,"all",mainTargets,[])
writeRule(makefile,"directories",dirTargets,[])
writeRule(makefile,"packages",packageDeps,[])

#now the directory tree
print "Making the directory tree"
makefile.write("####################################################\n")
makefile.write("# Directory rules\n")
makefile.write("####################################################\n")

target_rules = [
                "mkdir -p " + DIR_ROOT,
                "cp -rp toolchain/"+os.environ['MINIMALPI_ARCH']+"/"+os.environ['MINIMALPI_ARCH']+"/sysroot/* "+DIR_ROOT
                ]
writeRule(makefile,"target",[],target_rules)

createDirectory(makefile,DIR_DOWNLOAD)
createDirectory(makefile,DIR_BUILD)

makefile.write("####################################################\n")
makefile.write("# Package rules\n")
makefile.write("####################################################\n")
for package in PACKAGES:
    writePackageRules(makefile,package)

#write the clean rule
makefile.write("####################################################\n")
makefile.write("# Cleanup rules\n")
makefile.write("####################################################\n")
writeRule(makefile,"clean",[],cleanCommands)

makefile.close()
