#Lists are mutable in python unlike String
marks=[94.5,94.1,94.8,97.7] 
print(marks)
print(type(marks))
print(len(marks))
print(marks[1])

student=["Aman",94.3,19,"Japan"]
print(student)
student[0]="Arie"
print(student)

#----------ListSlicing-----------
print(marks[0:2])
print(marks[2:])
print(marks[-3:-1])

#----------ListMethod-----------
list=[7,1,8]
list.append(9) 
print(list)
print(list.sort()) 
print(list)
list.sort(reverse=True)
print(list)

anotherList=["b","l","a"]
anotherList.sort()
print(anotherList)

rev=[9,1,3,2]
rev.reverse()
print(rev)

ins=[0,9,3,1]
ins.insert(2,7)
print(ins)

ins.remove(9) #it will check where is 9 and delete it
print(ins)

ins.pop(2) #it will delete at index 2
print(ins) 