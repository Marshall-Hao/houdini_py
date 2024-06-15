import hou

obj = hou.node("/obj")

mynodes = []
# subnet = obj.createNode("subnet", "myspheres")

for x in range(0,6):
    geosphere = obj.createNode("geo", "geo_sphere_" + str(x+1))
    mynodes.append(geosphere)

subnet = obj.collapseIntoSubnet(mynodes, "myspheres")
subnet.layoutChildren()

