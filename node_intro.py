import hou
import random
obj = hou.node("/obj")
editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
shapes = editor.nodeShapes()


# mymesh = obj.createNode("geo","myMesh")

# file = mymesh.createNode("file","myobj")

# mymesh = obj.node("mymesh")

# file =mymesh.node("myobj")

# print(file.path())
# print(mymesh.type().description())
colorUi = hou.ui.selectColor()

for x in range(0,6):
   geosphere = obj.createNode("geo", "geo_sphere_" + str(x+1))
   sphere = geosphere.createNode("sphere")
   # modify
   mypos = (2 * x,2 + x)
   geosphere.setPosition(mypos)
   # geosphere.moveToGoodPosition()
   mycoord = (x * 2, x*0.5,x)
   # geosphere.parm("tx").set(x * 2.5)
   # parm modify
   geosphere.parmTuple("t").set(mycoord)
   geosphere.parm("scale").set(x * 0.1)
  
   # color node
   geosphere.setColor(colorUi)
   # node shape modify
   geosphere.setUserData('nodeshape',"diamond")
   