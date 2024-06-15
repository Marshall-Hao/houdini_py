import hou
node = hou.node("/obj").createNode("subnet")
# create parmtemplate group
group = node.parmTemplateGroup()
# create parms folder
folder = hou.FolderParmTemplate("folder", "My Parms")
folderSettings = hou.FolderParmTemplate("settings", "Settings")
# set parm (name, label, 1 slot, default value, min, max)
intensity = hou.FloatParmTemplate("intensity" , "Intensity" , 2, (1,10,0), 0, 10)
seed = hou.IntParmTemplate("seed" , "Seed" , 1,(10,0,0), 0, 10)
enable = hou.ToggleParmTemplate("enable", "Enable", 1, help= "enable all lights" )

# add parm to the parms folder
folder.addParmTemplate(enable)
folderSettings.addParmTemplate(intensity)
folderSettings.addParmTemplate(seed)

folder.addParmTemplate(folderSettings)
# add foler to the group
group.append(folder)
# hide
group.hideFolder("Transform",1)
# set it to the node
node.setParmTemplateGroup(group)

# disable condition
condition = (hou.parmCondType.DisableWhen, '{ enable == 0}')
folderSettings.setConditional(condition[0],condition[1])
node.replaceSpareParmTuple(folderSettings.name(), folderSettings)
# intensity.setConditional(condition[0],condition[1])
# node.replaceSpareParmTuple(intensity.name(), intensity)

# intensity.setConditional(condition[0],condition[1])
# node.replaceSpareParmTuple(intensity.name(), intensity)

# seed.setConditional(condition[0],condition[1])
# node.replaceSpareParmTuple(seed.name(), seed)
# seed.setConditional(condition[0],condition[1])
# node.replaceSpareParmTuple(seed.name(), seed)

