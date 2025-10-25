#int numeric data types in Python
x = 1
y = 356562225548877112
z = -3255522522588771123        
print(type(x))
print(type(y))          
print(type(z))

#float or flotting point numeric data types in Python
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

# float scientific numbers
x = 5e3
c = 5j       
y = 12E4
z = -87.7e100   
print(type(x))
print(type(c))
print(type(y))  
print(type(z))

# complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j  
z = -5j
print(type(x))  
print(type(y))
print(type(z))

# type conversion
x = 1    # int
y = 2.8  # float    
z = 1j   # complex
a = float(x)      # convert from int to float
b = int(y)        # convert from float to int       
c = complex(x)    # convert from int to complex
print(a)
print(b)    
print(c)
print(type(a))  
print(type(b))
print(type(c))

# random number
import random
print(random.randrange(1, 10))
