import os

Replacements={
	"CONFIG_CROSS_COMPILER_PREFIX":"\""+os.environ['MINIMALPI_ARCH']+"-"+"\"",
	"CONFIG_SYSROOT":"\""+os.environ['MINIMALPI_ROOT']+"/target"+"\"",
	"CONFIG_PREFIX":"\""+os.environ['MINIMALPI_ROOT']+"/target"+"\"",
}

confFile = open(".config","r")
tempConfFile = open("temp.config","w")

for line in confFile:
	replaced = False
	for key,val in Replacements.iteritems():
		if line.startswith(key):
			tempConfFile.write(key+"="+val+"\n")
			replaced = True
	if not replaced:
		tempConfFile.write(line)

confFile.close()
tempConfFile.close()

os.rename("temp.config",".config")
