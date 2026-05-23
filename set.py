s={3,7,3,9,1,"Aman"} #it ignore duplicate value
print(s)
print(type(s))
print(len(s))

#----------METHODS----------

collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.remove(1)
collection.add("Aman")
collection.add((2,4,6)) #tuple
print(collection)
collection.pop() #pop random element
print(collection)
collection.clear()
print(len(collection))

