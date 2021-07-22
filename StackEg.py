Stack=[4,7,9]
print('count before append',len(Stack))
Stack.append(21)
Stack.append(44)
print('count after append',len(Stack))
for s1 in range(0,len(Stack)):
 print(Stack[s1],end="->\n")
Stack.pop()
Stack.pop()

print('stack after pop-up')
for s2 in range(0,len(Stack)):
 print(Stack[s2],end="->\n")