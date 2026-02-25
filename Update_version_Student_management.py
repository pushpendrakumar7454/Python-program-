import  json
import string
import random

class StudentManagementStytem:
    database='data.json'
    data=[]
    
    
    try:
        with open(database) as fs:
            data=json.loads(fs.read())
    except Exception as err:
        print(err)
        
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(StudentManagementStytem.data)) 
    @classmethod
    def __idinfo(cls):
        length = random.randint(1, 6)
        id=random.choices(string.digits,k=length)
        random.shuffle(id)
        return "".join(id)
    
    @classmethod
    def __books(cls,sub):
        course={
                "bca":"C Language, Python ,Data stucture using python",
                "frountend":"Css,html,react,js",
                "backend":"Django,flask,next.js,tailwindcss",
                "bsc":"Chemstry,bio,physics,math" 
            }
        return course.get(sub.lower(),[])
        
    
    def addstudent(self):
        rollno=int(input("Enter your roll no-::"))
        
        for i in StudentManagementStytem.data:
           if i['rollno']==rollno:
               print("Do not enter again same roll no. This roll number already exists.")
               return
        
        course=input("Enter your course name-::")
        info={
            'id':StudentManagementStytem.__idinfo(),
            "name":input("Enter the name-::"),
            'Fathersname':input("Enter father's name-"),
            "collegename":input("Enter your college name-::"),
            "gender":input("Enter your Gender-::"),
            'age':int(input("ENter the age-::")),
            'course':course,
            "Subject":StudentManagementStytem.__books(course),
            "rollno":rollno,
        }
        print("Student addeed Succefully")
        
        StudentManagementStytem.data.append(info)
        StudentManagementStytem.__update()
    
    def Searchstudent(self):
        rollno=int(input("Enter the roll no-::"))
        userdata=[]
        
        for i in StudentManagementStytem.data:
            if i['rollno']==rollno:
                userdata=i
        for i in userdata:
            print(f'{i} : {userdata[i]}')
            
    def UpdateStudent(self):
        rollno=int(input("Enter roll no.-::"))
        userdata=[]
        for i in StudentManagementStytem.data:
            if i['rollno']==rollno:
                userdata.append(i)
        if not userdata:
            print("Student not found")
        else:
            name=input("Enter your new name-::")
            age=int(input("Enter your new age-::"))  
            
            if userdata[0]['name']=='':
                name=userdata[0]['name']
            if userdata[0]['age']=='':
                age=userdata[0]['age']
            else:
                age=int(age)
                userdata[0]['name']=name
                userdata[0]['age']=age
              
                
                print("Student updated")
                StudentManagementStytem.__update()     
                
    def Deletestudent(self):
        rollno=int(input("Enter the roll no-::"))
        userdata=[]
        
        for i in StudentManagementStytem.data:
            if i['rollno']==rollno:
                userdata.append(i)
        if not userdata:
            print("Student not found")
        else:
            check=input("Enter your choice y used too delete and n used to bypassd-::")
            if check=="n":
                print("bypassed")
            else:
                index=StudentManagementStytem.data.index(userdata[0])
                StudentManagementStytem.data.pop(index)
                print("Student Deleted")
                StudentManagementStytem.__update()    
            
                                              
                 
                     
        
student=StudentManagementStytem()

while True:
    print("""
------Student MAnagement System------
       1.Add Student
       2.Search Student
       3.Update Student
       4.Delete Student
       6.Exit             
""")
    choice=int(input("Enter your Choice-::"))

    if choice==1:
        student.addstudent()
    elif choice==2:
        student.Searchstudent()   
    elif choice==4:
        student.Deletestudent()
    elif choice==3:
        student.UpdateStudent()    

    elif choice==6:
        print("thank you|Exit")
        break    

        
                  
                




        
        
    
                
                        
            