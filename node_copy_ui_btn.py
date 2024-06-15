import hou

mysel = hou.selectedNodes()[0]

children = mysel.children()

#mysub = hou.node("/obj/empty/mysubnet")

# more ux friendly
mypath = hou.ui.selectNode(title="select des", initial_node= mysel)
mysub = hou.node(mypath)
hou.copyNodesTo(children, mysub)

confirm = hou.ui.displayMessage("your nodes have been coped to :" + mypath, buttons =("OK", "SELECT NODE" ))

if confirm == 1:
    # select the copied node, clear previous selection
    mysub.setSelected(1, clear_all_selected=1)