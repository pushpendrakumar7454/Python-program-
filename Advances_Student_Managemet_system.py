import json
import string
import random
import time

class StudentManagementSytem:
    admin_id='admin'
    admin_password='1234'
    database='student.json'
    student=[]  # class variable

    def __init__(self):
        self.admin_logged=False
        self.active_studnet=None

        try:
            with open(self.database) as fs:
                StudentManagementSytem.student=json.loads(fs.read())  # class variable
        except Exception as err:
                 print(err)

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(StudentManagementSytem.student,indent=4))

    @classmethod
    def __createid(cls):
        length=random.randint(1,6)
        id=random.choices(string.digits,k=length)
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def __books(cls,sub,semester):
        course={
            'bca':{
                1:['C language','html','e-comearse'],
                2: ["Python", "Flask", "Django"],
                3: ["Data Structure", "Java", "DBMS"]
            },
            'bsc':{
               1: ["Physics", "Chemistry", "Math"],
               2: ["Biology", "Statistics",'chemistry2']
            }
        }
        return course.get(sub.lower(),{}).get(semester,[])

    def addstudent(self):
        rollno=int(input('Enter your roll no-::'))

        for i in StudentManagementSytem.student:
            if i['rollno']==rollno:
                print("Do not use this roll no. because this roll number allredy used")
                return

        course=input("Enter your course name-::")
        semester=int(input("Enter you study which semester-::"))

        info={
            'Name':input("Ente your name-::"),
            'fathername':input("Enter the father's name-::"),
            'mothername':input("Enter the mother's name-::"),
            'address':input('Entet the your address-::'),
            'pin':int(input("Enter the pin-::")),
            'gender':input("Enter the your gender"),
            'rollno':rollno,
            'id':StudentManagementSytem.__createid(),
            'course':course,
            'semester':semester,
            'subjects':StudentManagementSytem.__books(course,semester)
        }

        print("Student added suceess")
        StudentManagementSytem.student.append(info)
        StudentManagementSytem.__update()

    def viewstudent(self):
        id=input("Enter your id-::")
        userdata=[]

        for i in StudentManagementSytem.student:
            if i['id']==id:
                userdata=i

        if not userdata:
            print("student not found")
        else:
            for i in userdata:
                print(f"{i} : {userdata[i]}")

    def UpdateStudent(self):
        id=input("Enter you id-::")
        userdata=[]

        for i in StudentManagementSytem.student:
            if i['id']==id:
                userdata.append(i)

        if not userdata:
            print("Student not found")
        else:
            Name=input("Enter your new name-::")
            rollno=input("Enter your new roll no-::")

            if Name=='': 
                Name=userdata[0]['Name']
            if rollno=='': 
                rollno=userdata[0]['rollno']
            else:
                rollno=int(rollno)

            userdata[0]['Name']=Name
            userdata[0]['rollno']=rollno
            print("Student update success")
            StudentManagementSytem.__update()

    def Deletestudent(self):
        id=input("Enter your id-::")
        userdata=[]

        for i in StudentManagementSytem.student:
            if i['id']==id:
                userdata.append(i)

        if not userdata:
            print("student not found")
        else:
            index=StudentManagementSytem.student.index(userdata[0])
            StudentManagementSytem.student.pop(index)
            print("Student deleted")
            StudentManagementSytem.__update()

    def ShowAllStudent(self):
        if not StudentManagementSytem.student:
            print("No student data found")
        else:
            for i in StudentManagementSytem.student:
                print("-"*30)
                for key, value in i.items():
                    print(f"{key} : {value}")

    def student_login(self):
        if self.active_studnet:
            print("Student already login")
            return

        name = input("Enter your name-::")
        id = input("Enter your id-::")

        for i in StudentManagementSytem.student:
            if i['Name'] == name and i['id'] == id:
                self.active_studnet = i
                print("Student login successful")
                return

        print("Invalid name or id")

    def student_loggout(self):
        if self.active_studnet:
            self.active_studnet=False
            print("Student logout suceesfully")
        else:
            print("do not logout")

    def admin_login(self):
        if self.admin_logged:
            print("Admin allredy login")
            return
        admin_id=input("Enter the admin id-::")
        password=input("Enter the admin password-::")

        if self.admin_id==admin_id and self.admin_password==password:
            self.admin_logged=True
            print("Admin login succefully")
        else:
            print("admin not login | please try agein later!")

    def admin_logout(self):
        if self.admin_logged:
            self.admin_logged=False
            print("Admin logout")
        else:
            print("Admin not logout")

    def total_students(self):
        print("Total Students :", len(StudentManagementSytem.student))

    def view_subject(self):
        id=input("Enter the student id-::")
        rollno=int(input("Enter the roll no.-::"))
        userdata=[]

        for i in StudentManagementSytem.student:
            if i['id']==id and i['rollno']==rollno:
                userdata.append(i)
        if not userdata:
            print("Student not found")
        else:
            print(f"{userdata[0]['Name']} Course name is :{userdata[0]['course']}  and yous subjects is : {userdata[0]['subjects']}")

    def marks(self):
        if not self.active_studnet:
            print("Please login first")
            return

        course = self.active_studnet['course']
        semester = self.active_studnet['semester']
        subjects = StudentManagementSytem.__books(course, semester)

       
        if 'marks' in self.active_studnet:
            del self.active_studnet['marks']

        if 'percentage' in self.active_studnet:
            del self.active_studnet['percentage']

        marks_dict = {}

        for sub in subjects:
            while True:
                try:
                    mark = int(input(f"Enter marks for {sub}: "))
                    if 0 <= mark <= 100:

                        if mark >= 90:
                            grade = 'A'
                        elif mark >= 60:
                            grade = 'B'
                        elif mark >= 40:
                            grade = 'C'
                        elif mark >= 33:
                            grade = 'D'
                        else:
                            grade = 'F'

                        marks_dict[sub] = {'marks': mark, 'grade': grade}
                        break
                    else:
                        print("Marks must be between 0 and 100")
                except:
                    print("Enter valid number")
        self.active_studnet['marks'] = marks_dict
        StudentManagementSytem.__update()
        print("Old marks removed. New marks saved successfully")
        
       
    def percentage(self):
            if not self.active_studnet:
                print("Please login first")
                return

            marks = self.active_studnet.get('marks', {})
            if not marks:
                print("No marks found. Please add marks first.")
                return

            
            total = sum(info['marks'] for info in marks.values())
            count = len(marks)
            percent = total / count

            self.active_studnet['percentage'] = percent
            print(f"{self.active_studnet['Name']}'s Percentage: {percent:.2f}%")
            StudentManagementSytem.__update()
           

student=StudentManagementSytem()

while True:
    if student.admin_logged:
        print("""
              --------admin panel--------
              1.view All studnet
              2.AddStudent
              3.view Student
              4.Update Student
              5.Delete Student
              6.admin Logout
              7.total_students
              8.Exit
                              """)
        choice=int(input("ente your choice-::"))
        if choice==1:
            student.ShowAllStudent()
        elif choice==2:
            student.addstudent()
        elif choice==3:
            student.viewstudent()
        elif choice==4:
            student.UpdateStudent()
        elif choice==5:    
            student.Deletestudent()    
        elif choice==6:
            student.admin_logout()
        elif choice==7:
            student.total_students()
        else:
            print("Thanku | Exit")
            exit()

    elif(student.active_studnet):
        print("""
             ------Student MAnagement System------
             1.View Student
             2.Update Student
             3.view Subject
             4.student loggout
             5.added student marks
             6.Student percentage
             7.Exit
             """)
        choice=int(input("Enter your Choice-::"))
        if choice==1:
            student.viewstudent()
        elif choice==2:
            student.UpdateStudent()
        elif choice==3:
            student.view_subject()
        elif choice==4:
            student.student_loggout()
        elif choice==5:
            student.marks()
        elif choice==6:
            student.percentage()
        else:
            print("thank you|Exit")
            break
    else:
        print("""
              ----Main menu
              1.addstudent
              2.studnet Login
              3.admin login
              4.exit
              """)
        check=int(input("Enter your choice-::"))
        if check==1:
            student.addstudent()
        elif check==2:
            student.student_login()
        elif check==3:
            student.admin_login()
        else:
            print("Thanku | Exit")
            exit()  
                  
        
                  
                




        
        
    
                
                        
                
        
                           

               

            


