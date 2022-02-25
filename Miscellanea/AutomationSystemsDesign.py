import os
class Add(object):
#Set of functions for adding child and adult members to their respective files.
    
          def __init__(self):
              #Constructor function: Initializes the arguments of current object
              
              self.name=None
              self.id=0
              self.dob=None
              self.age=0
              self.sex=None
              self.rel=None
              self.adp=0
              self.state=None
              self.work=None
              self.edu=None
              self.hobby=None
          

          def addChild(self):
              #Checks existence of file, generates identity number, writes details of child members into the file.
              
              if not os.path.isfile('Hope.Add1.CSV'):
                  self.id=1
              else:
                  wFile1=open('Hope.Add1.CSV','r')
                  L=wFile1.readlines()
                  self.id=1+len(L)
                  wFile1.close()
                  
                
              self.name=input("Name of the member: ")
              self.dob=input("Enter the DOB(dd.mm.yyyy): ")
              self.age=int(input("Age of the member: "))
              self.sex=input("Male/Female: ")
              self.rel=input("Name of the relative: ")
              self.adp=int(input("Mobile/Phone no.: "))
              self.state=input("Native state: ")
          

              wFile1=open('Hope.Add1.CSV','a')
            wFile1.write(self.name+','+(str(self.id))+','+self.dob+','+(str(self.age))+','+self.sex+','+self.rel+','+(str(self.adp))+','+self.state+'\n')
              wFile1.close()


import os
class Add(object):
#Set of functions for adding child and adult members to their respective files.
    
          def __init__(self):
              #Constructor function: Initialises the arguments of current 
               object.
              
              self.name=None
              self.id=0
              self.dob=None
              self.age=0
              self.sex=None
              self.rel=None
              self.adp=0
              self.state=None
              self.work=None
              self.edu=None
              self.hobby=None
          

          def addChild(self):
              #Checks existence of file, generates identity number, writes details of 
                child members into the file.
              
              if not os.path.isfile('Hope.Add1.CSV'):
                  self.id=1
              else:
                  wFile1=open('Hope.Add1.CSV','r')
                  L=wFile1.readlines()
                  self.id=1+len(L)
                  wFile1.close()
                  
                
              self.name=raw_input("Name of the member: ")
              self.dob=raw_input("Enter the DOB(dd.mm.yyyy): ")
              self.age=int(input("Age of the member: "))
              self.sex=raw_input("Male/Female: ")
              self.rel=raw_input("Name of the relative: ")
              self.adp=int(input("Mobile/Phone no.: "))
              self.state=raw_input("Native state: ")
          

              wFile1=open('Hope.Add1.CSV','a')
              wFile1.write(self.name+','+(str(self.id))+','+self.dob+','+(str(self.age))+','+self.sex+','+self.rel+','+(str(self.adp))+','+self.state+'\n')
              wFile1.close()
              print"Data recorded successfully"
              print"Data recorded successfully)
              
              
 
          def addAdult(self):
              #Checks existence of file, generates identity number, writes details of 
                adult members into the file.
              
              if not os.path.isfile('Hope.Add2.CSV'):
                  self.id=1001
              else:
                  wFile2=open('Hope.Add2.CSV','r')
                  L=wFile2.readlines()
                  self.id=1001+len(L)
                  wFile2.close()
              
              self.name=raw_input("Name of the member: ")
              self.dob=raw_input("Enter the DOB (dd.mm.yyyy): ")
              self.age=int(input("Age of the member: "))
              self.sex=raw_input("Male/Female: ")
              self.rel=raw_input("Name of the relative: ")
              self.adp=int(input("Mobile/Phone no.: "))
              self.state=raw_input("Native state: ")
              self.work=raw_input("Enter member's occupation: ")
              self.edu=raw_input("Enter member's academic qualifications: ")
              self.hobby=raw_input("Enter member's hobbies: ")
          
              wFile2 = open('Hope.Add2.CSV','a')
              wFile2.write(self.name+','+(str(self.id)+','+self.dob+','+(str(self.age))+','+self.sex+','+self.rel+','+(str(self.adp))+','+self.state+','+self.work+','+self.edu+','+self.hobby+'\n'))                      
              wFile2.close()
              print"Data recorded successfully"


import os
class Existence(object):
#Set of functions for viewing, updating and deleting details of existing 
  members.
    

      def View(self):
          #Displays details of existing members.
          
          wFile1=open('Hope.Add1.CSV','r')
          child_list = wFile1.readlines()
          wFile1.close()
          name=raw_input("Enter the name of the member whose details 
                                         you want to view: ")
          if not os.path.exists('Hope.Add1.CSV'):
              print"File not found"
              return
              
          for record in child_list:
              L = record.rstrip('\n').split(',')
              if str(name) == str(L[0]):
                  found=True
                  ide=(L[1])
                  dob=(L[2])
                  age=(L[3])
                  sex=(L[4])
                  rel=(L[5])
                  adp=(L[6])
                  state=(L[7])
                  x = [ide,name,dob,age,sex,rel,adp,state]
                  print" "
                  print" Identity number: ",x[0]
                  print" Name of child  : ",x[1]
                  print" Date of birth  : ",x[2]
                  print" Age of child   : ",x[3]
                  print" Sex of child   : ",x[4]
                  print" Relations      : ",x[5]
                  print" Phone number   : ",x[6]
                  print" Native state   : ",x[7]

          
          wFile2=open('Hope.Add2.CSV','r')
          adult_list = wFile2.readlines()
          wFile2.close()
          if not os.path.exists('Hope.Add2.CSV'):
              print"File not found"
              return
              
          for record in adult_list:
              L = record.rstrip('\n').split(',')
              if name == (L[0]):
                  found=True
                  ide=(L[1])
                  dob=(L[2])
                  age=(L[3])
                  sex=(L[4])
                  rel=(L[5])
                  adp=(L[6])
                  state=(L[7])
                  work=(L[8])
                  edu=(L[9])
                  hobby=(L[10])
                  x = [ide,name,dob,age,sex,rel,adp,state,work,edu,hobby]
                  print" "
                  print" Identity number       : ",x[0]
                  print" Name of adult         : ",x[1]
                  print" Date of birth         : ",x[2]
                  print" Age of adult          : ",x[3]
                  print" Sex of adult          : ",x[4]
                  print" Relations             : ",x[5]
                  print" Phone number     : ",x[6]
                  print" Native state          : ",x[7]
                  print" Occupation           : ",x[8]
                  print" Academic Qualification: ",x[9]
                  print" Interests and hobbies : ",x[10]
                  
      def Updatechild(self):
          #Offers platform for updation of the values of certain arguments of 
          a child member.
          
          if not os.path.exists('Hope.Add1.CSV'):
              print"File not found..."
              return

          rfile = open('Hope.Add1.CSV','r')
          tfile = open('Temp.CSV','w')

          name = raw_input("Enter the name to be updated: ")
          found = False

          for record in rfile:
              L = record.split(',')
              if name == str(L[0]):
                  found = True
                  age = int(input("Enter the age: "))
                  rel = raw_input("Enter the relations: ")
                  phno = int(input("Enter the phone number: "))
                  tfile.write(L[0]+','+(str(L[1]))+','+L[2]+','+(str(age))+','+L[4]+','+rel+','+(str(phno))+','+L[7])
              else:
                  tfile.write(record)

          rfile.close()
          tfile.close()

          if found:
              print"Member ",name," updated successfully..."
              os.remove('Hope.Add1.CSV')
              os.rename('Temp.CSV','Hope.Add1.CSV')
          else:
              print"Member ",name," not found..."
                  
      def Updateadult(self):
          #Offers platform for updation of the values of certain arguments of 
          an adult member.
          
          if not os.path.exists('Hope.Add2.CSV'):
              print"File not found..."
              return

          rfile = open('Hope.Add2.CSV','r')
          tfile = open('Temp.CSV','w')

          name = raw_input("Enter the name to be updated: ")
          found = False

          for record in rfile:
              L = record.split(',')
              if name == str(L[0]):
                  found = True
                  age = int(input("Enter the age: "))
                  rel = raw_input("Enter the relations: ")
                  phno = int(input("Enter the phone number: "))
                  occ = raw_input("Enter occupation: ")
                  acaq = raw_input("Enter academic qualifications: ")
                  inth = raw_input("Enter interests and hobbies: ")
                  tfile.write(L[0]+','+(str(L[1]))+','+L[2]+','+(str(age))+','+L[4]+','+rel+','+(str(phno))+','+L[7]+','+occ+','+acaq+','+inth)
              else:
                  tfile.write(record)

          rfile.close()
          tfile.close()

          if found:
              print"Member ",name," updated successfully..."
              os.remove('Hope.Add2.CSV')
              os.rename('Temp.CSV','Hope.Add2.CSV')
          else:
              print"Member ",name," not found..."


      def Deletechild(self):
          #Offers platform for deletion of all data of a child member.
          
          if not os.path.exists('Hope.Add1.CSV'):
              print"File not found."
              return

          rfile = open('Hope.Add1.CSV','r')
          tfile = open('Temp.CSV','w')

          name = raw_input("Enter the name you wish to delete: ")
          found = False

          for record in rfile:
              L = record.split(',')
              if name == str(L[0]):
                  found = True
              else:
                  tfile.write(record)

          rfile.close()
          tfile.close()

          if found:
              print"Member ",name," deleted successfully..."
              os.remove('Hope.Add1.CSV')
              os.rename('Temp.CSV','Hope.Add1.CSV')
          else:
              print"Member ",name," not found..."


      def Deleteadult(self):
          #Offers platform for deletion of all data of an adult member.
          
          if not os.path.exists('Hope.Add2.CSV'):
              print"File not found."
              return

          rfile = open('Hope.Add2.CSV','r')
          tfile = open('Temp.CSV','w')

          name = raw_input("Enter the name you wish to delete: ")
          found = False

          for record in rfile:
              L = record.split(',')
              if name == str(L[0]):
                  found = True
              else:
                  tfile.write(record)

          rfile.close()
          tfile.close()

          if found:
              print"Member ",name," deleted successfully..."
              os.remove('Hope.Add2.CSV')
              os.rename('Temp.CSV','Hope.Add2.CSV')
          else:
              print"Member ",name," not found..."

               
import os
class Track:
#Helps in the tracking of details of all members by the maintenance 
  department(admin staff).
    

          def track(self):
              #Helps maintenance department access data of a particular  
              member.
              
              wFile1=open('Hope.Add1.CSV','r')

              name=raw_input("Enter the name of the member: ")
              if not os.path.exists('Hope.Add1.CSV'):
                 print"File not found"
                 return
              
              for record in wFile1:
                  L=record.split(',')
                  if name == (L[0]):
                     found=True
                     dob=(L[1])
                     age=(L[2])
                     sex=(L[3])
                     rel=(L[4])
                     adp=(L[5])
                     state=(L[6])
                     entry=(L[7])
                     print[name,dob,age,sex,rel,adp,state,entry]
              wFile1.close()
              
              wFile2=open('Hope.Add2.CSV','r')
              if not os.path.exists('Hope.Add2.CSV'):
                 print"File not found"
                 return
              
              for record in wFile2:
                  L=record.split(',')
                  if name == (L[0]):
                     found=True
                     name=(L[0])
                     dob=(L[1])
                     age=(L[2])
                     sex=(L[3])
                     rel=(L[4])
                     adp=(L[5])
                     state=(L[6])
                     work=(L[7])
                     edu=(L[8])
                     hobby=(L[9])
                     entry=(L[10])
                     print[name,dob,age,sex,rel,adp,state,work,edu,hobby,entry]
              wFile2.close()
              

import os
class Feedback:
#Serves as a platform for the maintenance department to communicate 
  details pertaining to a child member to his or her guardian.
    
    def __init__(self):
        #Constructor function: Initialises the arguments of current object.
        
        self.name=None
        self.imp=None
        self.app=None
        self.sugg=None
        self.comm=None
        self.rate=None
        self.math=None
        self.lang=None
        self.art=None
        self.sci=None

    def inp(self):
        #Platform for admin staff: Entering and storing feedback of a child.
        
        self.name=raw_input("Name of the student: ")
        self.app=raw_input("Appreciation: ")
        self.sugg=raw_input("Suggestion: ")
        self.comm=raw_input("Comment: ")
        self.rate=raw_input("Rating of the student: ")
        wFile1=open('Hope.feedback.CSV','a')
        wFile1.write(self.name+','+self.app+','+self.sugg+','+\
                           self.comm+','+self.rate+'\n')
        wFile1.close()
        print "Data recorded successfully"

    def marks(self):
        #Platform for admin staff: Entering and storing marks of a child.
        
        self.name = raw_input("Enter student name: ")
        self.math = raw_input("Marks scored in maths: ")
        self.lang = raw_input("Marks scored in languages: ")
        self.art = raw_input("Marks scored in art: ")
        self.sci = raw_input("Marks scored in science: ")
        wFile1=open('Hope.marks.CSV','a')
        wFile1.write(self.name+','+self.math+','+self.lang+','+\
                           self.art+','+self.sci+'\n')
        wFile1.close()
        print "Data recorded successfully"

    def displayinp(self):
          #Platform for customer: Viewing stored details of feedback of a 
          child
        
          wFile1=open('Hope.feedback.CSV','r')
          thelist = wFile1.readlines()
          wFile1.close()
          name=raw_input("Enter the name of the member whose details 
                                        you  want to view: ")
          if not os.path.exists('Hope.feedback.CSV'):
              print"File not found"
              return
              
          for record in thelist:
              L = record.rstrip('\n').split(',')
              if str(name) == str(L[0]):
                  found=True
                  app=(L[1])
                  sugg=(L[2])
                  comm=(L[3])
                  rate=(L[4])
 
                  x = [name,app,sugg,comm,rate]
                  print"STUDENT FEEDBACK REPORT "
                  print" Name of child  : ",x[0]
                  print" Appreciation   : ",x[1]
                  print" Suggestions    : ",x[2]
                  print" Comments       : ",x[3]
                  print" Rate out of 10 : ",x[4]

    def displaymarks(self):
          #Platform for customer: Viewing stored details of marks of a child.
        
          wFile1=open('Hope.marks.CSV','r')
          thelist = wFile1.readlines()
          wFile1.close()
          name=raw_input("Enter the name of the member whose marks you 
                                       want to view: ")
          if not os.path.exists('Hope.marks.CSV'):
              print"File not found"
              return
              
          for record in thelist:
              L = record.rstrip('\n').split(',')
              if str(name) == str(L[0]):
                  found=True
                  math=(L[1])
                  lang=(L[2])
                  art=(L[3])
                  sci=(L[4])
 
                  x = [name,math,lang,art,sci]
                  print"STUDENT FEEDBACK REPORT "
                  print" Name of child  : ",x[0]
                  print" Maths marks    : ",x[1]
                  print" Language marks : ",x[2]
                  print" Art marks      : ",x[3]
                  print" Science marks  : ",x[4]

          
import os
class Bind(Add,Existence,Track,Feedback):
#Derived class: Inherits the properties of all the previously defined classes,
  binding the methods in one master unit
    
    def __init__(self):
        Add.__init__(self)

    def addChild(self):
        Add.addChild(self)

    def addAdult(self):
        Add.addAdult(self)

    def query(self):
        Existence.View(self)

    def updatechild(self):
        Existence.Updatechild(self)

    def updateadult(self):
        Existence.Updateadult(self)

    def deletechild(self):
        Existence.Deletechild(self)

    def deleteadult(self):
        Existence.Deleteadult(self)

    def track(self):
        Track.track(self)

    def inputfeedback(self):
        Feedback.inp(self)

    def inputmarks(self):
        Feedback.marks(self)

    def feedback(self):
        Feedback.displayinp(self)

    def marks(self):
        Feedback.displaymarks(self)




#Main environment
        
b = Bind()

print("WELCOME TO HOPE ORPHANAGE...HOMAGE MANAGEMENT SYSTEM")
print("")
print("INTRODUCTION")
print("HOPE Orphanage is a global charity that serves the poor in \
more than 20 states. It is a registered in some other states.\
HOPE Orphanage began its work in India in 2000. Its program \
has expanded from mobile clinic. The Vision of the Orphanage is \
“Bringing Hope....Changing Lives”. HOME Management system \
is an online aid for registration of orphans.")
print("")
    

while True:
    print("1. If you are a guardian, enter 1...")
    print("2. If you are an admin member, enter 2...")
    print("3. If you wish to exit the system, enter 3...")
    c = int(input("Enter your choice: "))
    if c==1:
        print("Welcome dear visitor, please select from the following...")
        print("1. To register a new ward, enter 1...")
        print("2. To view details of an existing ward, enter 2")
        print("3. To update details of an existing ward, enter 3...")
        print("4. To delete details of an existing ward, enter 4...")
        print("5. To view the feedback/marks of your ward(child), enter 5...")
        print("6. To exit the system, enter 6...")
        ch = int(input("Enter your choice: "))
        if ch==1:
            print("If you want to register a child(age<18), enter 1...")
            print("If you want to register an adult(age>=18), enter 2...")
            ch1 =int(input("Enter your choice: "))
            if ch1==1:
                b.addChild()
            elif ch1==2:
                b.addAdult()
            else:
                print("Invalid Entry...try again!")
        elif ch==2:
            b.query()
        elif ch==3:
            print("If ward in question is a child, enter 1...")
            print("If ward in question is an adult, enter 2...")
            ch2 = int(input("Enter your choice: "))
            if ch2==1:
                b.updatechild()
            elif ch2==2:
                b.updateadult()
            else:
                print("Invalid Entry...try again!")
        elif ch==4:
            print("If ward in question is a child, enter 1...")
            print("If ward in question is an adult, enter 2...")
            ch3 = int(input("Enter your choice: "))
            if ch3==1:
                b.deletechild()
            elif ch3==2:
                b.deleteadult()
            else:
                print("Invalid Entry...try again!")
        elif ch==5:
            print("To view the feedback report of your child, enter 1...")
            print("To view the academic progress/marks of your child, enter 
                       2...")
            ch4 = int(input("Enter your choice: "))
            if ch4==1:
                b.feedback()
            elif ch4==2:
                b.marks()
            else:
                print("Invalid Entry...try again!")
        elif ch==6:
            print("Exiting HOPE Orphanage...THANKYOU FOR VISITING!!")
            break
        else:
            print("Invalid Entry...try again!")

    elif c==2:
        
        p = raw_input("Enter the admin password: ")
        if str(p)=="adminalka":
            print("Welcome to admin...")
            print("1. To track member details, enter 1...")
            print("2. To input a certain child's feedback, enter 2...")
            print("3. To input a certain child's marks, enter 3...")
            print("4. To exit from system, enter 4...")
            ce = int(input("Enter your choice: "))
            if ce==1:
                b.track()
            elif ce==2:
                b.inputfeedback()
            elif ce==3:
                b.inputmarks()
            elif ce==4:
                print("Exiting HOPE Orphanage...")
                break
            else:
                print("Invalid Entry...try again!")
        else:
            print("Wrong password...retry!")

    elif c==3:
        print("Exiting HOPE Orphanage...THANKYOU FOR VISITING!!")
        break
    else:
        print("Invalid Entry...try again!")
