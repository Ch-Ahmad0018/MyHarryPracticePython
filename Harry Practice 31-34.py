# ----------------------------------------------31. Sets------------------------------------------------------------
# s={2,3,4,5,6,7}
# print(type(s))
# # Dictionary will come
# # But to create Empty set
# h=set()
# print(type(h))
# # For accessing sets we use for loop
# for l in s:
#     print(l)

# # ---------------------------------------------32. Sets Methods-----------------------------------------------------
# # --------------------------------Union and Update method---------------------------
# s1={2,4,6,8}
# s2={3,5,6,8}
# s3=s1.union(s2)
# print(s1.union(s2))
# print(s3)
# # Mainly nai variable mein donun dalne k liye
# s1.update(s2)
# # Usi main dalne k liye Update
# print(s1,s2)

# # -------------------------------Intersection and Intersection Update-----------------
# cities={'a','b','c','d'}
# cities2={'b','c','d','e','f'}
# cities3=cities.intersection(cities2)
# print(cities3)   
# cities.intersection_update(cities2)
# print(cities)

# # --------------------------- Symmetric and Symmetric diiference Update----------------
# cities={'a','b','c','d'}
# cities2={'b','c','d','e','f'}
# cities3=cities.symmetric_difference(cities2)
# print(cities3)
# cities.symmetric_difference_update(cities2)
# print(cities)

# # -------------------------------Difference and Difference Update------------------------
# cities={'a','b','c','d'}
# cities2={'b','c','d','e','f'}
# cities3=cities.difference(cities2)
# print(cities3)
# cities.difference_update(cities2)
# print(cities)

# # # -------------------------------IsDisjoint and IsSuper Method----------------------------
# cities.isdisjoint(cities2)
# cities.issuperset(cities2)

# # Is sUBSET mETHOD
# # -------------------------------Add,remove,discard and pop  Method---------------------------
# cities.add("A")
# print(cities)
# c=cities.pop()
# print(c)
# print(cities)
# del cities
# print(cities2)
# if 'b' in cities2:
#     print('True')

# --------------------------------------------33. Dictionary------------------------------------------------

# dic={
#     1:"Chaudhry",
#     2:"Ahmad",
#     3:"Mubashir"
# }
# print(dic[1])

# # print(dic.keys(),dic.values())

# for i in dic.keys():
#     print(f"The value corresponding to {i} are {dic[i]}")

# # for j in dic.values():
# #     print(j)

# print(dic.items())


# for i,j in dic.items():
#      print(f"The values are {i} and {j}")
# # Using Enumerate function
# for key,j in enumerate(dic):
#      print(key+1,dic[j])

# -----------------------------------------34. Dictionary Methods-------------------------------------------
ep1={'Ahmad':1024,
          'SherAfgan':1042,
          'AbdulManan':1045}
ep2={
          'HamnaMehboob':1077
     }
ep1.update(ep2)
ep3=ep2.copy()
ep3.clear()
print(ep1)
print(ep2)
print(ep3)

