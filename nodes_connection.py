import hou

mydir = hou.ui.selectFile(title="choose your assests", multiple_select=1)
mydir = mydir.split(";")

obj = hou.node("/obj")

mygeo = obj.createNode("geo","myassets")

merge = mygeo.createNode("merge","merge_assets")
switch = mygeo.createNode("switch", "switch_asset")

count = 0
for asset in mydir: 
    name = asset.split("/")[-1].split(".")[0]

    file = mygeo.createNode("file",name)
    
    # create nodes
    material = mygeo.createNode("material", "material_"+name)
    pack = mygeo.createNode("pack", "pack_" + name)
    
    # connect nodes
    material.setInput(0,file)
    pack.setInput(0,material)
    
    # set nodes
    file.parm("file").set(asset)
    pack.parm("pivot").set("origin")
    merge.setInput(count, pack)
    switch.setInput(count, pack)
    count += 1

mygeo.layoutChildren()