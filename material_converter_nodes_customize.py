import hou

mysel = hou.selectedNodes()[0]

matcontext = mysel.parent()

matsubnet = matcontext.createNode("subnet", mysel.name() + "_materialX")

## define output surface
surfaceoutput = matsubnet.createNode("subnetconnector", "surface_output")
surfaceoutput.parm("parmname").set("surface")
surfaceoutput.parm("parmlabel").set("Surface")
surfaceoutput.parm("parmtype").set("surface")
surfaceoutput.parm("connectorkind").set("output")

## define output displacement
displacementoutput = matsubnet.createNode("subnetconnector", "displacement_output")
displacementoutput.parm("parmname").set("displacement")
displacementoutput.parm("parmlabel").set("Displacement")
displacementoutput.parm("parmtype").set("displacement")
displacementoutput.parm("connectorkind").set("output")

# create materialx standard
mtlx =  matsubnet.createNode("mtlxstandard_surface", "surface_mtlx")
surfaceoutput.setInput(0,mtlx)

#create albedo
path = mysel.parm("basecolor_texture").eval()
albedo = matsubnet.createNode("mtlximage", "ALBEDO")
albedo.parm("file").set(path)
mtlx.setInput(1,albedo)

#create roughness
path = mysel.parm("rough_texture").eval()
rough = matsubnet.createNode("mtlximage", "ROUGHNESS")
rough.parm("file").set(path)
# set to Float
rough.parm("signature").set("0")
mtlx.setInput(6,rough)

#create specular
if mysel.parm("reflect_useTexture").eval() == 1 :
    path = mysel.parm("reflect_texture").eval()
    spec = matsubnet.createNode("mtlximage", "SPEC")
    spec.parm("file").set(path)
    mtlx.setInput(5,spec)

#create opacity
if mysel.parm("opaccolor_useTexture").eval() == 1 :
    path = mysel.parm("opaccolor_texture").eval()
    opacity = matsubnet.createNode("mtlximage", "OPACITY")
    opacity.parm("file").set(path)
    # opacity.parm("signature").set("0")
    mtlx.setInput(38,opacity)

#create normal
if mysel.parm("baseBumpAndNormal_enable").eval() == 1 :
    path = mysel.parm("baseNormal_texture").eval()
    normal = matsubnet.createNode("mtlximage", "NORMAL")
    plugnormal = matsubnet.createNode("mtlxnormalmap", "NORMAL_MAP")
    normal.parm("file").set(path)
    plugnormal.setInput(0,normal)
    mtlx.setInput(40,plugnormal)    

# create displacement
if mysel.parm("dispTex_enable").eval() == 1 :
    path = mysel.parm("dispTex_texture").eval()
    offset =  mysel.parm("dispTex_offset").eval()
    scale =  mysel.parm("dispTex_scale").eval()
    
    disp = matsubnet.createNode("mtlximage", "DISP")
    plugdisp = matsubnet.createNode("mtlxdisplacement", "DISP_MAP")
    remapdisp = matsubnet.createNode("mtlxremap", "OFFSET_DISP")
    
    disp.parm("file").set(path)
    disp.parm("signature").set("0")
    # set the parm for offset and scale, and remap the offset range
    remapdisp.parm("outlow").set(offset)
    plugdisp.parm("scale").set(scale)
    
    plugdisp.setInput(0,remapdisp)
    remapdisp.setInput(0,disp)
    displacementoutput.setInput(0,plugdisp)
    
    
matsubnet.layoutChildren()



