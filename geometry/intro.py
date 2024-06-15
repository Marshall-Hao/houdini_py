import hou

mysel =  hou.selectedNodes()[0]

geo = mysel.geometry()

#mypt = geo.point(15)

# mypts = geo.globPoints("15-20")

# mypts = geo.globPoints("group1")
# for pt in mypts:
#     myattr =  pt.attribValue("N")
#     print("the point is " + str(pt.number()) + " " + str(myattr))
    
for prim in geo.prims():
    # myPrimAttr = prim.attribValue("shop_materialpath")
    # print(myPrimAttr)
    attribs =  geo.primAttribs()
    
    for attr in attribs:
        print(attr)
    