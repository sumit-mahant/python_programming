# name="sumit"
# country="India"
# print(f"my name is {name},I am from {country}")
# print(f"my name is {{name}},I am from {{country}}")
# price=49.0021
# txt=f"for only {price:.2f} "
# print(txt)
# print(f"{2*30}")
#docstring
def square(n):#docstring should be right above than function body 
    # print(n) now docstring not will be printed
    '''takes in a number n,returns the square of n '''
    print(n**2)
square(5)
print(square.__doc__)
