# strings can be stored in single ,double or triple quotes
#mostly we used double quotes
str1="this is string"
str2='this is also a strings' 
str3="""this is also avalid stirng"""

# escape sequence characters  == means formatting k liye use krte h ie next line k liye
# \n for next line \t for tab 
Str="i m using it \n dekha ab next line hogyi h "
print(Str)

#concatenation of strings= ie simple +:  str1+str2

final_str=str1+str2
print(final_str)

#length of string  len(sting name) space is also counted 
print(len(final_str))
length1=len(Str)
print(length1)

#indecing of a sring  start from 0
# 0 1 2 3 4 5 6 
name="Ekansh Bhardwaj"
print(name[0] ,"\t",name[4] )

#Slicing = Accessing part of a string
#ie  strname[strting index : ending index]  strting index included indono k beech wala hissa ajaiga
print(name[7:len(name)])
print(name[7:]) #[7:len(name)]
print(name[:6]) #[0:6]

#Slicing -ve index : A  p  p  l  e
#                   -5 -4 -3 -2 -1
print(name[-9:-1])



