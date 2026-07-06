#StirngsFunctons
#str.endswith("kuch char")  return true/false

name="ekansh Bhardwaj"
print(name)
print(name.endswith("aj"))
print(name.endswith("sh"))

#str.capatalize()  first word capital aiga  nyi string m change krega 
# matalb nnyi string banake karega 
print(name.capitalize())

#str.replace(old,new)  old value ko new value se change krna 
print(name.replace("a","o"))
print(name.replace("Bhardwaj",""))

#str.find(word)  jha p sabse phle mil gya uska index return krdega
print(name.find("B"))
print(name.find("l")) # exist nhi krta -1 aaiga 

#str.count(word ) kitni baar exist krta h wo count
print(name.count("a"))
print(name.count("ekansh"))

name2=input("Enter ur name :")
print("Lenght of ur name is :",len(name2))