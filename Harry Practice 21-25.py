# ------------------------------------21. Function Arguments----------------------------------------------
# Default arguments
# def average(a=8,b=9):
#     print("The average of two numbers is ",(a+b)/2)

# average(7,9)    
# # Keyword arguments
# average(b=21,a=90)
# Agar uper a=8ki jaga a likha ho to yeh aik -------required argument--------------bn jai ga

# Variable length arguments
# pehle tuple k lehaz se
# * ka matlab hai k variable can accept arguments as tuple
# def average1(*numbers):
#     sum=0
#     print(type(numbers))
#     # Tuple will come
#     for i in numbers:
#         sum=sum+i
#     print("The average is ",sum/len(numbers))

# average1(2,3,4,5,76,78,9,0)       
# Ab dictionary k liye
# ** ho ga dictionary k liye is se yeh jo b key=value de ga wo as a dictionay mil jai gi

# def average2(**numbers):
#     print("Hello",numbers)

# average2(name="Ahmad",fname="mubashir",cast="Gujjar")   

# -------------------------------------22. Lists---------------------------------------------------------

# marks=[22,4,3,2,1,6,7]
# print(len(marks))
# -------for checking value in list
# if 7 in marks:
#      print("Yes")
#      print(marks.index(7))
# else:
#      print("no")

#Same thing applies for string
# print(marks)
# print(marks[:])
# print(marks[1:-1]) 
# print(marks[3:])
# print(marks[:-3])
# print(marks[::-1])
# ----------------List Comprehension-----------------------------
# lst=[i*i for i in range(10) if i%2==0]
# print(lst)

# -----------------------------------------23.Operations on Lists--------------------------------------------

# marks.append(89)
# print(marks)
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)
# marks.reverse()
# print(marks)
# print(marks.index(6))
# print(marks.count(6))
# # m=marks
# # m[0]=0
# # print(marks)
# # m=marks.copy()
# # m[0]=0
# # print(marks)
# marks.insert(1,899)
# print(marks)
# m=[100,200,300]
# marks.extend(m)
# print(marks)
# k=marks+m
# print(k)

# ------------------------------------------24. Tuples---------------------------------------------------------
# tup=(1,2,3,4,5)
# tup[0]=88
# The above change not possible
# print(type(tup),tup)
# if 2 in tup:
#     print("Yes 2 is present")

# -------------------------------------25. Tuples Operations-----------------------------------------------------
# temp=list(tup)   
# # We convert tuple to list above
# # temp.append("Russia")
# # temp.pop(2)
# print(temp.index(2,0,4))
# # countries=tuple(temp)
# # We convert list to tuple above
# # print(type(countries),countries)

# # subcontinent=("India","Pakistan","Bangladesh")
# # middleEast=("Iran","Iraq","Qatar")
# # Asia=subcontinent+middleEast
# # print(Asia)
# a=(1,2,1,1,1,1,3,4,5,6,7)
# print(a.index(1,2,6))
# print(Asia.count("Iran"))
