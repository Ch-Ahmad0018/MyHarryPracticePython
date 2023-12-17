# --------------------------------------26. Exericse----------------------------------------------
# import time
# timestamp=time.strftime("%H:%M:%S")
# print(timestamp)
# timestamp=time.strftime("%H")
# print(timestamp)
# ---------------------------------27. Kaun bne ga Crorepati---------------------------------------
# ----------------------------------------28. F strings--------------------------------------------
# --------------------------------------29. Doc Strings--------------------------------------------
# def square(n):
#     '''Takes in a number n and returns the the square'''
#     print(n**2)

# square(5)    
# print(square.__doc__)

# # ----------------------------------------30. Recursion---------------------------------------------
# # factorial example
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
factorial(3)
factorial(4)
factorial(5)
# That's called recursion function ko function k andar call krna

# fibonacci series example 

# def fibonacci(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# fibonacci(5)