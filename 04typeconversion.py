#type converison : automatically kr det ah python 
a= 5  # int 
b= 5.9  # float
sum=a+b   # automatic conversion into float i.e implicit conversion
print(sum)
print(type(sum))

c="2"
#print(a+c)   # error string and flaot/int ko sum nhi kr skte


#type casting  : jabardasti karwani padti h manually 
# jabadati krwana h to value ko jisme krwana h usme pass krdo i.e int(value),float(value).str(value)
sum1=(a+int(b))
print(sum1 , type(sum1))
print(a+int(c))