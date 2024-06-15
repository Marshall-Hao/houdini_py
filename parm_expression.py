import hou

node = hou.node("obj/subnet1")

lgt = node.createNode("envlight")
path = node.parm("intensityx").path()
myexpression = f'ch("{path}")'
lgt.parm("light_intensity").setExpression(myexpression)

myparm = node.parm("intensityx")
lgt.parm("light_explosure").setFromParm(myparm)