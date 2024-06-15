import hou

obj = hou.node("/obj")

mysel = hou.selectedNodes()

for node in mysel:
    name = node.name()
    number = node.digitsInName()
    print(number)
    mynames = name.split("_")
    
    if "box" in mynames:
        node.setColor(hou.Color(1,0,0))
        node.setName("box_" + str(number))
    if "tube" in mynames:
        node.setColor(hou.Color(0,1,0))
        node.setName("tube_" + str(number))
    if "sphere" in mynames:
        node.setColor(hou.Color(0,0,1))
        node.setName("sphere_" + str(number))