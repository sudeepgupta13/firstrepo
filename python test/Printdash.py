from platform import java_ver
import IPython


print("-" *20)


print(" hell0 " *20)

str1 = "Python language"
print(len(str1))

str1="PYTHON"
print(str1.lower())

str1="PYTHON"
print(str1.upper())

str = "Java is a object oriented program"
str2 = str.replace( "java", "python" )
print("old string: \n", str)
print("new string: \n", str2)
str3 = str.replace("Java", "Python", 1)
print("\n Old string: \n", str)
print("New string: \n", str3)

str1 = "python is a programming language"
str2 = str1.find("is")
str3 = str1.find("Java")
str4 = str1.find("p",5)
str5 = str1.find("i",5,25)
print(str2,str3,str4,str5)

my_list=[1,2,3]
print(id(my_list))
print(my_list)
my_list.append(4)
print(my_list)
