class Student:
    # [assignment] Skeleton class. Add your code here
    
    name = str(input("What is your Name?: "))
    age = int(input("what is your age: "))
    track = list(input("What do you study: "))
    score = float(input("What is your overall score:  "))
    
    def __init__(self, Name, Age, Tracks, Score):
        self.Name = Name
        self.Age = Age
        self.Tracks = Tracks
        pass
    
    def Change_name(name):
        name = str(input("Input New Name: "))
     
    def Change_age(age):
        age = int(input("Input New Age: "))
        
    def Add_track(track):
        new_track = track.insert(input("Input Track To Add: "))
        return new_track       
        
    def get_score(score):
        return score  

# print(Student)        

Student.Change_name("")
Student.Add_track("")

# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
