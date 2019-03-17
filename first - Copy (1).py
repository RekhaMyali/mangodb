from tkinter import*
import pymongo
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
root = Tk()
root.title("Student Database Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==================================VARIABLES==========================================
FullName = StringVar()
Email = StringVar()
Contact_no = StringVar()
ADDRESS = StringVar()
USN_NO = StringVar()
Branch = StringVar()
#==================================FRAME==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, height=450)
Right.pack(side=TOP)
textV=Text(Right, height = 25,width = 300)
textV.pack()
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "Student Database Management System")
txt_title.pack()
txt_firstname = Label(Forms, text="FullName:", font=('arial', 16), bd=15)
txt_firstname.grid(row=0, stick="e")
txt_Email = Label(Forms, text="Email:", font=('arial', 16), bd=15)
txt_Email.grid(row=1, stick="e")
txt_Contact_no = Label(Forms, text="Contact_no:", font=('arial', 16), bd=15)
txt_Contact_no.grid(row=2, stick="e")
txt_address = Label(Forms, text="Address:", font=('arial', 16), bd=15)
txt_address.grid(row=3, stick="e")
txt_USN_NO = Label(Forms, text="USN_NO:", font=('arial', 16), bd=15)
txt_USN_NO.grid(row=4, stick="e")
txt_Branch = Label(Forms, text="Branch:", font=('arial', 16), bd=15)
txt_Branch.grid(row=5, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#========================================================insert function=======================================
txt_result.config(text="Fill the form to get the data entry", fg="blue")
def insertvalues():
    if  FullName.get() == "" or Email.get() == "" or Contact_no.get() == "" or address.get() == "" or USN_NO.get() == "" or Branch.get() == "":
        txt_result.config(text="Please complete the required field!", fg="red")
    else:
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client.student2018
        collection = db.Employees
        employeeId = FullName.get()
        employeeName =Email.get() 
        Contact_no1=Contact_no.get()
        employeeAge =address.get()
        employeeCountry =USN_NO.get()
        Branch1=Branch.get()
        db.Employees.insert_one(
                {
                    "FullName": employeeId,
                    "Email":employeeName,
                    "Contact_no":Contact_no1,
                    "address":employeeAge,
                    "USN_NO":employeeCountry,
                    "Branch":Branch1
            })
        print ("\nInserted data successfully\n")
        txt_result.config(text="Inserted data successfully", fg="blue")
#========================================================getdata==========================================
def ReadfromDB():
    
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.student2018
    collection = db.Employees
    try:
        empCol = db.Employees.find({},{"_id": 0,"Email":0,"Contact_no":0,"address":0, "Branch":0})
        hello="manymany"
       
        
        i=1
        textV.delete('1.0', END)
        for data in empCol:
           #print(data) 
           textV.insert(END,'\n'+str(data))
           i=i+1
           txt_result.config(text="Display only name and USN_no", fg="blue")
    except Exception:
            print ("errr")
#=======================================================update function======================
def updateDB():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.student2018
    collection = db.Employees
    txt_result.config(text="Insert Full name to be updated", fg="blue")
    try:
        if  FullName.get() == "":
            txt_result.config(text="Enter the first name to be updated", fg="blue")
        else:
            txt_result.config(text="Enter the FullName to be updated", fg="blue")
            employeeId = FullName.get()#input('Enter Employee id :')
            employeeName =Email.get() #input('Enter Name :')
            Contact_no1=Contact_no.get()
            employeeAge =address.get()# input('Enter age :')
            employeeCountry =USN_NO.get()# input('Enter Country :')
            Branch1=Branch.get()
            db.Employees.update_one(
                {"FullName": employeeId},
                    {
                        "$set":{
                        
                        "Email":employeeName,
                        "Contact_no":Contact_no1,
                        "address":employeeAge,
                        "USN_NO":employeeCountry,
                        "Branch":Branch1
                        }
                    }
                )
            
            txt_result.config(text="Data updated Sucessfully", fg="blue")
    except Exception:
        print ("error")
#==========================================Exit function===================================
def Exit():
  
        root.destroy()
        exit()
#==========================================delete function=========================

def deleteDB():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.student2018
    collection = db.Employees
    try:
        
        if  FullName.get() == "":
            txt_result.config(text="Enter the first name to be deleted", fg="blue")
        else:
            employeeId = FullName.get()
            db.Employees.delete_many({"FullName": employeeId})
            #print ("\nDeletion successful\n")
            txt_result.config(text="data deleted successfully", fg="blue")
    except Exception:
        txt_result.config(text="error", fg="red")  

#===============ENTRY FORMS===========================================================

FullName = Entry(Forms, textvariable=txt_firstname, width=30)
FullName.grid(row=0, column=1)

Email = Entry(Forms, textvariable=Email, width=30)
Email.grid(row=1, column=1)


Contact_no = Entry(Forms, textvariable=Contact_no, width=30)
Contact_no.grid(row=2, column=1)

address = Entry(Forms, textvariable=ADDRESS, width=30)
address.grid(row=3, column=1)
USN_NO = Entry(Forms, textvariable=USN_NO, width=30)
USN_NO.grid(row=4, column=1)
Branch = Entry(Forms, textvariable=Branch, width=30)
Branch.grid(row=5, column=1)

 
#==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Insert",command=insertvalues)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=ReadfromDB )
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update",command=updateDB)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete",command=deleteDB)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit",command=Exit)
btn_exit.pack(side=LEFT)


#==========================connection to database===============================
if __name__ == '__main__':
    root.mainloop()
#Sroot.mainloop()
  


