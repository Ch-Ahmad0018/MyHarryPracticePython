# ---------------------------------40. Short hand if else statement-----------------------------------------------
a=330
b=3303
print("A")if a>b else print("=") if a==b else print("B")

# ---------------------------------41. Enumerate Functions------------------------------------------------------

marks=[12,13,14,15,16,17,18,19,20]

# i=0
# for mark in marks:
#     print(mark)
#     if(i==3):
#         print("Harry Awesome")
#     i+=1    

# For doing it in easy way

for i,mark in enumerate(marks,start=1):
    print(mark)
    if(i==3):
        print("Harry Awesome")

fruits=["CHAUDHRY","AHMAD","MUBASHIR"]
 
for i,value in enumerate(fruits):
    print(i," ",value) 

for i in enumerate(fruits):
    print(i)     