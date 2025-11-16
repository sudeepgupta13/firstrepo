# uppercase
a= "hello"
print(a.upper())

# lowercase
b= "WORLD"
print(b.lower())

# removing whitespace
c= "   Python String Methods   "
print(c.strip())

# replacing substrings
d= "I like Java"    
print(d.replace("Java", "Python"))

# split string
e= "apple,banana,cherry"
print(e.split(","))

# concatenate strings
f= "Hello"      
g= "World"
print(f + " " + g)  

# modern concatenation
age = 25
txt = "My name is John, and I am {} years old.".format(age)
print(txt)

# format nlimited args
quantity = 3
itemno = 567    
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# format with index
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
