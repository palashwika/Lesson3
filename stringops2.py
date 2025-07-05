#find LENGTH of string (includes spaces, special characters, and numbers if any)
a="ice cream"
print(len(a))

#SLICING, represents the position of a character in a string. index begins with 0; use variable
b="icecream"
print(b[:3])
print(b[2:])
print(b[::3]) #every third, 
#i  c  e  c  r  e  a  m
#0  1  2  3  4  5  6  7
print(b[::-3]) #backwards, first left blank starts with m=0, a=-1, etc
print(b[::-1])

#others: v.lower(), v.upper(), v.join(), v.split(), v.find, v.replace()