class Student :
    college_name = "ABC College"
    def __init__(self,name , marks):
        self.name = name
        self.marks = marks 
        
    def welcome(self) :
        print("Welcome Students")

    def get_marks(self) :
        return self.marks

    

s1 = Student("karan",98)
print(s1.name ,  s1.marks)
s1.welcome()
print(s1.get_marks())

s2 = Student("Arjun",99)
print(s2.name,  s2.marks)

