d={ #mutable
    "name":"Aman",
    "age":19,
    "id":101,
    "list1":["python","java","sql"],
     "tup":("bca","bba","btech"),
     12:144
}
print(d)
print(type(d)) 
print(d["name"])
print(d["tup"])
d["name"]="luffy" # change data
d["surname"]="MONKEY" # add new data
print(d)

#----------NESTED DICTIONARY----------
student={
    "name":"Aman",
    "subjects":{
      "phy":97,
      "chem":98,
      "math":100
    }
}
print(student["subjects"]["math"])