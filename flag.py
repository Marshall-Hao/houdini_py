import hou

obj = hou.node("/obj")

lib =  obj.node("LIBRARY")
nodes = lib.allSubChildren()

for n in nodes:
    type = n.type().description()
    print(type)
    if type == "Geometry":
            file = n.node("file")
            print(file)
            path = file.parm("file").eval()
            # path = path.split("/")
            # index = path.index("Midpoly")
            print(path)
       
