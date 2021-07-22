Fruits =['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("Count before Append->",len(Fruits))

#list.append(x)
Fruits.append("Water Melon")
print("Count After Append->",len(Fruits))
sum=len(Fruits)
for l in range(0,sum):
 print("[",l,"]->",Fruits[l])