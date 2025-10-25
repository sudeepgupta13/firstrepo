'''text type: str
numeric types: int, float, complex
sequence types: list, tuple, range  
mapping type: dict
set types: set, frozenset
boolean type: bool
binary types: bytes, bytearray, memoryview'''


x="df"
print(type(x)) #str
y=["a","b","c"] #list
print (type(y))
z=("a","b","c") #tuple
print(type(z))
q=range(6)#range
print(type(q))
f={"name":"John","age":36}#dict
print(type(f))
g={"apple","banana","cherry"}#set
print(type(g))
c=True #bool
v=b"Hello" #bytes
print(type(v))
b=bytearray(5) #bytearray
print(type(b))
n=memoryview(bytes(5)) #memoryview
print(type(n))
x=1j #complex

#setting out the specific data types
a=str("Hello World") #str
print(type(a))
x=int(20) #int
x=float(20.5) #float
x=complex(1j) #complex
x=list(("apple","banana","cherry")) #list
x=tuple(("apple","banana","cherry")) #tuple
x=dict(name="John",age=36) #dict
x=range(6) #range
x=set(("apple","banana","cherry")) #set
x=frozenset(("apple","banana","cherry")) #frozenset
x=bool(5) #bool
x=bytes(5) #bytes   
x=bytearray(5) #bytearray
x=memoryview(bytes(5)) #memoryview
