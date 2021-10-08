from tkinter import *
import sqlite3 as db
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time
import os
import sqlite3
from io import BytesIO

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData():
    try:
        sqliteConnection = sqlite3.connect('__IAMRI__.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        cursor.execute("""SELECT * from new_employee where Id ="""+dwonload_name_search.get())
        #cursor.execute(sql_fetch_blob_query, (dwonload_name_search.get(),))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            resumeFile = row[3]

            print("Storing employee image and resume on disk \n")
            photoPath =name + "001.jpeg"
            resumePath =name + "002.pdf"
            writeTofile(photo, photoPath)
            writeTofile(resumeFile, resumePath)
            

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

#readBlobData('smith')
#readBlobData(2)
#fetting all data related to querry 
def revert():
    sqliteConnection = sqlite3.connect('__IAMRI__.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")

    cursor.execute("""SELECT * from new_employee where name like '%"""+name_search.get()+"""%'""")
    #cursor.execute(sql_fetch_blob_query, (name_search.get(),))
    list0=cursor.fetchall()
    cursor.close()
    sqliteConnection.close()
    output=''
    for x in list0:
        if type(x[0])==int:
            one=str(x[0])
        if type(x[2])==bytes:
            two=str(x[2])
        if type(x[3])==bytes:
            three=str(x[3])
        output=output+one+' '+x[1]+'\n'
    return output

    status.set('Data Fetch  sucessfully ☻☻☻')
#creating a GUI window
master=Tk()
master.title("Employee Database create by Tarun kumar")
master.geometry("500x500")

name_search=StringVar()
status=StringVar()
dwonload_name_search=StringVar()
#creating a label
l1=Label(master,text="Employee Database",font=("Arial Bold",25))
l1.grid(row=0,column=0,columnspan=2,sticky=W)

l2=Label(master,text="Enter the name to search:",font=("Arial Bold",15))
l2.grid(row=1,column=0)


#creating text Box for better handeling for user
text=Text(master,width=50,height=10)
text.grid(row=7,columnspan=6) 

Entry(master,textvariable=name_search).grid(row=1,column=1)
Button(master,text="Search",command=lambda:text.insert(END,revert())).grid(row=3,columnspan=2)
l3=Label(master,text="Looking for Dwonload",font=("Arial Bold",15))
l3.grid(row=5,column=0)
l4=Label(master,text="Search Result Are Shown on dwon :",font=("Arial Bold",10))
l4.grid(row=4,column=0)
Button(master,text="Dwonload",command=lambda:readBlobData()).grid(row=6,columnspan=2)
Entry(master,textvariable=dwonload_name_search).grid(row=5,column=1)







master.mainloop()


