# ---------------------------------------52. Lamda Functions-------------------------------------------------------
# def double(x):
#     return x*2

# def apply(fx,value):
#     return 6+fx(value)
# double= lambda x:x*2
# cube= lambda x:x*x*x
# avg= lambda x,y=7:(x+y)/2
# print(double(5))
# print(cube(5))
# print(avg(5))
# print(apply(cube,2))

# add10=lambda x:x+10

# def add10(x):
#     return x+10

# mult =lambda x,y:x*y
# --------------------------------------------Lambda with sorted method-------------------------------------------
# -----------------With lambda-------------------------
# points2D= [(1,2),(15,1),(5,-1),(10,4)]
# points2DSorted=sorted(points2D,key= lambda x:x[1])
# print(points2D)
# print(points2DSorted)

# ----------------Without Lambda------------------------
# def sort_by_y(x):
#     return x[1]

# points2DSorted=sorted(points2D,key= sort_by_y)
# print(points2D)
# print(points2DSorted)

# ---------------With lambda---------------------------

# points2DSorted=sorted(points2D,key= lambda x:x[0]+x[1])
# print(points2DSorted)

# --------------------------------------------Lambda with map function-------------------------------------------
# map(func.seq)
# a=[1,2,3,4,5]
# # b= map(lambda x:x*2,a)
# # print(b)
# # print(list(b))

# # -----By list comprehension
# # c=[x*2 for x in a]
# # print(c)

# # --------------------------------------------Lambda with filter function-------------------------------------------
# a=[1,2,3,4,5,6]
# b=filter(lambda x:x%2==0,a)
# print(list(b))

# # ----By list comprehension
# c=[x for x in a if(x%2==0)]
# print(c)

# # --------------------------------------------Lambda with reduce function----------------------------------------

from functools import reduce
a=[1,2,3,4]
product_a=reduce(lambda x,y:x*y,a)
print(product_a)

# --------------------------------------------------Map function---------------------------------------------

def cube(x):
    return x*x*x

l=[1,2,3,4,5]
newL=[]
for item in l:
    newL.append(cube(item))
print(newL)
# ---Using map

# newL=list(map(cube,l))
newL=list(map(lambda x:x*x*x,l))
print(newL)

# ------------------------------------------------Filter Function------------------------------------------------

l1=[2,4,3,5,6,1]
def filter_function(a):
    return a>2

newnewL=list(filter(lambda x:x>2,l))
print(newnewL)


