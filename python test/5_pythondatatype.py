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