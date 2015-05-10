
class makefileRule:

    def __init__(self,name):
        self.name = name
        self.depends = []
        self.commands = []
        self.clean_commands = []
        self.addCommand("sudo -v")


    def addDependency(self,dependency):
        self.depends.append(dependency)

    def addCommand(self,command,directory=""):
        if directory != "":
            command = "cd " + directory + " && " + command
        self.commands.append(command)

    def addCleanCommand(self,command,directory=""):
        if directory != "":
            command = "cd " + directory + " && " + command
        self.clean_commands.append(command)

    def write(self,makefile):
        makefile.write(self.name + ":")
        for dep in self.depends:
            makefile.write(" " + dep)

        for command in self.commands:
            makefile.write("\n\t"+command)

        makefile.write("\n\n")

class basePackage:

    def __init__(self,name):
        self.name = name
        self.depends = []
        self.rules = []
        self.dirs = []
        self.entryPoint = ""

    def addDependency(self,dependency):
        self.depends.append(dependency)

    def addRule(self,rule):
        self.rules.append(rule)

    def addDirectory(self,dirName):
        self.dirs.append(dirName)
        self.depends.append(dirName)

    def getRules(self):
        #create top level rule for package
        topRule = makefileRule(self.name+"_top")
        for rule in self.rules:
            topRule.addDependency(rule.name)
        nameRule = makefileRule(self.name)
        nameRule.addCommand("$(MAKE) "+self.name+"_top")
        for dependency in self.depends:
            nameRule.addDependency(dependency)

        if self.entryPoint != "":
            topRule.addDependency(self.entryPoint)

        return [topRule,nameRule]+self.rules

def makeDownloadRule(globalDefs,downloadFile):
    rule = makefileRule(globalDefs["DownloadDir"]+"/"+downloadFile.rsplit("/",1)[1])
    rule.addCommand("wget " + downloadFile,globalDefs["DownloadDir"])
    return rule

def makeExtractRule(globalDefs,downloadFile):
    rule = makefileRule("."+downloadFile.rsplit("/",1)[1]+"_extracted")
    rule.addCommand("tar -xf "+globalDefs["BaseDir"]+"/"+globalDefs["DownloadDir"]+"/"+downloadFile.rsplit("/",1)[1],globalDefs["BuildDir"])
    rule.addCommand("touch "+rule.name)
    rule.addDependency(".created_"+globalDefs["BuildDir"])
    rule.addCleanCommand("rm -f ."+downloadFile.rsplit("/",1)[1]+"_extracted")
    return rule

def makeConfigureRule(globalDefs,pkgName,workDir,extraArgs):
    rule = makefileRule("."+pkgName+"_configured")
    commandText = ""
    for env,val in globalDefs["EnvVars"].iteritems():
        commandText = commandText+env+"=\""+val+"\" "

    rule.addCommand(commandText+"./configure --host="+globalDefs["Architecture"]+
                                " --prefix=/usr --includedir=/usr/include "+extraArgs,
                                globalDefs["BuildDir"]+"/"+workDir)

    rule.addCommand("touch ."+pkgName+"_configured")
    rule.addCleanCommand("rm -f ."+pkgName+"_configured")
    return rule

def makeMakeRule(globalDefs,pkgName,workingDirectory):
    rule = makefileRule("."+pkgName+"_make")
    rule.addCommand("$(MAKE) -C "+globalDefs["BuildDir"]+"/"+workingDirectory)
    rule.addCommand("touch ."+pkgName+"_make")
    rule.addCleanCommand("rm -f ."+pkgName+"_make")
    return rule

def makeInstallRule(globalDefs,pkgName,workingDirectory):
    rule = makefileRule("."+pkgName+"_makeInstall")
    rule.addCommand("sudo env PATH=$$PATH $(MAKE) DESTDIR="+globalDefs["AbsTargetDir"]+" -C "+globalDefs["BuildDir"]+"/"+workingDirectory+" install")
    rule.addCommand("touch ."+pkgName+"_makeInstall")
    rule.addCleanCommand("rm -f ."+pkgName+"_makeInstall")
    return rule

class configureMakePackage(basePackage):

    def __init__(self,globalDefs,name,downloadFile,workingDirectory,extraConfigureArgs="",dependencies=[]):
        basePackage.__init__(self,name)
        self.downloadFile = downloadFile
        self.workingDirectory = workingDirectory
        self.dependencies = dependencies
        self.globalDefs = globalDefs
        self.extraConfigureArgs = extraConfigureArgs

        if self.downloadFile != "":
            self.downloadRule = makeDownloadRule(self.globalDefs,self.downloadFile)
            self.extractRule = makeExtractRule(self.globalDefs,self.downloadFile)
        else:
            self.downloadRule = None
            self.extractRule = None
        self.extraFixRule = None
        self.configureRule = makeConfigureRule(self.globalDefs,self.name,self.workingDirectory,
                                            self.extraConfigureArgs)
        self.makeRule = makeMakeRule(self.globalDefs,self.name,self.workingDirectory)
        self.makeInstallRule = makeInstallRule(self.globalDefs,self.name,self.workingDirectory)

        self.addDependency("."+globalDefs["RelTargetDir"]+"_created")

    def _addRuleToList(self,rules,rule):
        if rule is not None:
            if len(rules) > 0:
                rule.addDependency(rules[-1].name)
            rules.append(rule)

    def getRules(self):
        rules = []
        self._addRuleToList(rules,self.downloadRule)
        self._addRuleToList(rules,self.extractRule)
        self._addRuleToList(rules,self.extraFixRule)
        self._addRuleToList(rules,self.configureRule)
        self._addRuleToList(rules,self.makeRule)
        self._addRuleToList(rules,self.makeInstallRule)

        if len(rules) > 0:
            self.entryPoint = rules[-1].name

        return rules+basePackage.getRules(self)

