import hou

class lightcontrol():
   
class lightcontrol():
    
    def __init__(self):
        print("init light control")
        
    def light_control(self):
        sel = hou.selectedNodes()
        #evaluate parrameters
        val_intensity = sel[0].parm("light_intensity").eval()
        val_exposure = sel[0].parm("light_exposure").eval()
        val_enable = sel[0].parm("light_enable").eval()
        val_color = sel[0].parmTuple("light_color").eval()
        val_radiusx =  sel[0].parm("areasize1").eval()
        val_radiusy =  sel[0].parm("areasize2").eval()
        root = sel[0].parent()
        # collapse will make them disappear
        node = root.collapseIntoSubnet(sel,sel[0].name())
        
        
        # create parmtemplate group
        group = node.parmTemplateGroup()
        # create parms folder
        folder = hou.FolderParmTemplate("folder", "LIGHT CONTROL")
        folderSettings = hou.FolderParmTemplate("settings", "Settings")
        # set parm (name, label, 1 slot, default value, min, max)
        intensity = hou.FloatParmTemplate("intensity" , "Intensity" , 1, (val_intensity,0,0), 0, 10)
        exposure = hou.FloatParmTemplate("exposure" , "Exposure" , 1, (val_exposure,0,0), 0, 10)
        radius = hou.FloatParmTemplate("radius" , "Radius" , 2, (val_radiusx,val_radiusy,0), 0, 10)
        # color
        color = hou.FloatParmTemplate("color", "Color",3,default_value=val_color, look= hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
        
        enable = hou.ToggleParmTemplate("enable", "Enable", val_enable, help= "enable all lights" )
        # add parm to the parms folder
        folder.addParmTemplate(enable)
        folderSettings.addParmTemplate(intensity)
        folderSettings.addParmTemplate(exposure)
        folderSettings.addParmTemplate(radius)
        folderSettings.addParmTemplate(color)
        folder.addParmTemplate(folderSettings)
        # add foler to the group
        group.append(folder)
        # hide
        group.hideFolder("Transform",1)
        group.hideFolder("Subnet",1)
        # set it to the node
        node.setParmTemplateGroup(group)
        
        # disable condition
        condition = (hou.parmCondType.DisableWhen, '{ enable == 0}')
        folderSettings.setConditional(condition[0],condition[1])
        node.replaceSpareParmTuple(folderSettings.name(), folderSettings)
        
        # Link parameters to the lights
        
        for lgt in node.children():
          lgt.parm("light_intensity").setExpression('ch("../intensity")')
          lgt.parm("light_exposure").setExpression('ch("../exposure")')
          lgt.parm("light_enable").setExpression('ch("../enable")')
          
          lgt.parm("light_colorr").setExpression('ch("../colorr")')
          lgt.parm("light_colorg").setExpression('ch("../colorg")')
          lgt.parm("light_colorb").setExpression('ch("../colorb")')
          
          lgt.parm("areasize1").setExpression('ch("../radiusx")')
          lgt.parm("areasize2").setExpression('ch("../radiusy")')
          
lightcontrol().light_control() 
    def __init__(self):
        print("init light control")
        
    def light_control(self):
        sel = hou.selectedNodes()
        #evaluate parrameters
        val_intensity = sel[0].parm("light_intensity").eval()
        val_exposure = sel[0].parm("light_exposure").eval()
        val_enable = sel[0].parm("light_enable").eval()
        val_color = sel[0].parmTuple("light_color").eval()
        val_radiusx =  sel[0].parm("areasize1").eval()
        val_radiusy =  sel[0].parm("areasize2").eval()
        root = sel[0].parent()
        # collapse will make them disappear
        node = root.collapseIntoSubnet(sel,sel[0].name())
        
        
        # create parmtemplate group
        group = node.parmTemplateGroup()
        # create parms folder
        folder = hou.FolderParmTemplate("folder", "LIGHT CONTROL")
        folderSettings = hou.FolderParmTemplate("settings", "Settings")
        # set parm (name, label, 1 slot, default value, min, max)
        intensity = hou.FloatParmTemplate("intensity" , "Intensity" , 1, (val_intensity,0,0), 0, 10)
        exposure = hou.FloatParmTemplate("exposure" , "Exposure" , 1, (val_exposure,0,0), 0, 10)
        radius = hou.FloatParmTemplate("radius" , "Radius" , 2, (val_radiusx,val_radiusy,0), 0, 10)
        # color
        color = hou.FloatParmTemplate("color", "Color",3,default_value=val_color, look= hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
        
        enable = hou.ToggleParmTemplate("enable", "Enable", val_enable, help= "enable all lights" )
        # add parm to the parms folder
        folder.addParmTemplate(enable)
        folderSettings.addParmTemplate(intensity)
        folderSettings.addParmTemplate(exposure)
        folderSettings.addParmTemplate(radius)
        folderSettings.addParmTemplate(color)
        folder.addParmTemplate(folderSettings)
        # add foler to the group
        group.append(folder)
        # hide
        group.hideFolder("Transform",1)
        group.hideFolder("Subnet",1)
        # set it to the node
        node.setParmTemplateGroup(group)
        
        # disable condition
        condition = (hou.parmCondType.DisableWhen, '{ enable == 0}')
        folderSettings.setConditional(condition[0],condition[1])
        node.replaceSpareParmTuple(folderSettings.name(), folderSettings)
        
        # Link parameters to the lights
        
        for lgt in node.children():
          lgt.parm("light_intensity").setExpression('ch("../intensity")')
          lgt.parm("light_exposure").setExpression('ch("../exposure")')
          lgt.parm("light_enable").setExpression('ch("../enable")')
          
          lgt.parm("light_colorr").setExpression('ch("../colorr")')
          lgt.parm("light_colorg").setExpression('ch("../colorg")')
          lgt.parm("light_colorb").setExpression('ch("../colorb")')
          
          lgt.parm("areasize1").setExpression('ch("../radiusx")')
          lgt.parm("areasize2").setExpression('ch("../radiusy")')
          
lightcontrol().light_control()