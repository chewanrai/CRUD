from tkinter import *
import sqlite3
from tkinter import messagebox

cr=Tk()
cr.title("Input Data - Facebook")
cr.iconbitmap("signup.ico")
cr.configure(bg="blue")
pr= sqlite3.connect("Facebook.db")
p=pr.cursor()
# p.execute("""CREATE TABLE User(
#     first_name text,
#     last_name text,
#     age integer,
#     address text,
#     city text,
#     zipcode integer,
#     password text,
#     gender text)""")
# print("Table created succesfully")

def submit():
    pr=sqlite3.connect("Facebook.db")
    p=pr.cursor()
    p.execute("INSERT INTO User VALUES( :first_name, :last_name, :age, :address, :city, :zipcode, :password, :gender)",
    {"first_name": f_name_entry.get(),
    "last_name": l_name_entry.get(),
    "age": age_entry.get(),
    "address": address_entry.get(),
    "city": city_entry.get(),
    "zipcode": zipcode_entry.get(),
    "password": password_entry.get(),
    "gender": gender_entry.get()})
    abc= f_name_entry.get()
    messagebox.showinfo("User's data information", f"Hi {abc}, your data has been added successfully.")
    pr.commit()
    pr.close()
    f_name_entry.delete(0, END)
    l_name_entry.delete(0, END)
    age_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    password_entry.delete(0, END)
    gender_entry.delete(0, END)
def query():
    pr = sqlite3.connect("Facebook.db")
    p= pr.cursor()
    p.execute("SELECT *, oid FROM User")
    records= p.fetchall()
    print_records=""
    for record in records:
        print_records+=str(record[0])+" "+str(record[1])+", "+str(record[3])+"\t"+str(record[8])+"\n"
    query_label= Label(cr, text=print_records,font=("Rockwell", 11), bg="blue", fg="white")
    query_label.grid(row=10, column=0, columnspan=2)
    pr.commit()
    pr.close()


def delete():
    pr= sqlite3.connect("Facebook.db")
    p= pr.cursor()

    response= messagebox.askyesno("Permission", "Do you really want to delete the data of ID no. "+delete_id_entry.get()+" ?"+"\n"+ "Data deleted from here can not be recover from anywhere.")
    if response== True:
        p.execute("DELETE from User WHERE oid="+delete_id_entry.get())
        messagebox.showinfo("info", "Your data has been deleted succesfully.")
    else:
        messagebox.showinfo("info", "Your data has not been deleted.")

    delete_id_entry.delete(0, END)
    pr.commit()
    pr.close()


def update():
    pr= sqlite3.connect("Facebook.db")
    p= pr.cursor()

    record_id= update_id_entry.get()
    p.execute("""UPDATE User SET
    first_name = :first,
    last_name= :last,
    age= :age,
    address= :address,
    city= :city,
    zipcode= :zipcode,
    password= :password,
    gender= :gender
    WHERE oid = :oid""",
    {"first": f_name_editor_entry.get(),
    "last": l_name_editor_entry.get(),
    "age": age_editor_entry.get(),
    "address": address_editor_entry.get(),
    "city": city_editor_entry.get(),
    "zipcode": zipcode_editor_entry.get(),
    "password": password_editor_entry.get(),
    "gender": gender_editor_entry.get(),
    "oid": record_id})
    
    pr.commit()
    pr.close()
    editor.destroy()

    messagebox.showinfo("Data update", "Your information has been upadated successfully.")

def edit():
    global editor
    editor= Toplevel()
    editor.title("Edit Data")
    editor.geometry("300x210")
    editor.iconbitmap("refresh.ico")
    editor.configure(bg="white")

    pr= sqlite3.connect("Facebook.db")
    p= pr.cursor()
    record_id= update_id_entry.get()
    p.execute("SELECT * FROM User WHERE oid="+record_id)
    records= p.fetchall()
    global f_name_editor_entry
    global l_name_editor_entry
    global age_editor_entry
    global address_editor_entry
    global city_editor_entry
    global zipcode_editor_entry
    global password_editor_entry
    global gender_editor_entry

    f_name_editor_label= Label(editor, text= "Firstname",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    f_name_editor_label.grid(row=0, column=0)

    l_name_editor_label= Label(editor, text= "Lastname",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    l_name_editor_label.grid(row=1, column=0)

    age_editor_label= Label(editor, text= "Age",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    age_editor_label.grid(row=2, column=0)

    address_editor_label= Label(editor, text= "Address",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    address_editor_label.grid(row=3, column=0)

    city_editor_label= Label(editor, text= "City",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    city_editor_label.grid(row=4, column=0)

    zipcode_editor_label= Label(editor, text= "Zipcode",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    zipcode_editor_label.grid(row=5, column=0)

    password_editor_label= Label(editor, text= "Password",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    password_editor_label.grid(row=6, column=0)

    gender_editor_label= Label(editor, text= "Gender",font=("Arial Rounded MT Bold", 10), bg="white", fg="black")
    gender_editor_label.grid(row=7, column=0)

    f_name_editor_entry= Entry(editor, borderwidth=2)
    f_name_editor_entry.grid(row=0, column=1)

    l_name_editor_entry= Entry(editor, borderwidth=2)
    l_name_editor_entry.grid(row=1, column=1)

    age_editor_entry= Entry(editor, borderwidth=2)
    age_editor_entry.grid(row=2, column=1)

    address_editor_entry= Entry(editor, borderwidth=2)
    address_editor_entry.grid(row=3, column=1)

    city_editor_entry= Entry(editor, borderwidth=2)
    city_editor_entry.grid(row=4, column=1)

    zipcode_editor_entry= Entry(editor, borderwidth=2)
    zipcode_editor_entry.grid(row=5, column=1)

    password_editor_entry= Entry(editor, borderwidth=2)
    password_editor_entry.grid(row=6, column=1)

    gender_editor_entry= Entry(editor, borderwidth=2)
    gender_editor_entry.grid(row=7, column=1)

    for record in records:
        f_name_editor_entry.insert(0, record[0])
        l_name_editor_entry.insert(0, record[1])
        age_editor_entry.insert(0, record[2])
        address_editor_entry.insert(0, record[3])
        city_editor_entry.insert(0, record[4])
        zipcode_editor_entry.insert(0, record[5])
        password_editor_entry.insert(0, record[6])
        gender_editor_entry.insert(0, record[7])
    save_btn= Button(editor, text= "SAVE",bg="grey55", command= update)
    save_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

f_name_label= Label(cr, text="First Name",font=("Britannic Bold", 12), bg="blue", fg="white")
f_name_label.grid(row=0, column=0)

l_name_label= Label(cr, text="Last Name",font=("Britannic Bold", 12), bg="blue", fg="white")
l_name_label.grid(row=1, column=0)

age_label= Label(cr, text="Age", bg="blue",font=("Britannic Bold", 12), fg="white")
age_label.grid(row=2, column=0)

address_label= Label(cr, text="Address",font=("Britannic Bold", 12), bg="blue", fg="white")
address_label.grid(row=3, column=0)

city_label= Label(cr, text="City",font=("Britannic Bold", 12), bg="blue", fg="white")
city_label.grid(row=4, column=0)

zipcode_label= Label(cr, text="Zipcode",font=("Britannic Bold", 12), bg="blue", fg="white")
zipcode_label.grid(row=5, column=0)

password_label= Label(cr, text="Password",font=("Britannic Bold", 12), bg="blue", fg="white")
password_label.grid(row=6, column=0)

gender_label= Label(cr, text= "Gender",font=("Britannic Bold", 12), bg="blue", fg="white")
gender_label.grid(row=7, column=0)

f_name_entry= Entry(cr, width=20,borderwidth=2, fg="grey40", font=("Segoe Print", 8))
f_name_entry.bind("<Button-1>", lambda e: f_name_entry.delete(0, END))
f_name_entry.insert(0, "Chewan")
f_name_entry.grid(row=0, column=1,pady=3)

l_name_entry= Entry(cr, width= 20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
l_name_entry.bind("<Button-1>", lambda e: l_name_entry.delete(0, END))
l_name_entry.insert(0, "Rai")
l_name_entry.grid(row=1, column= 1,pady=3)

age_entry= Entry(cr, width=20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
age_entry.bind("<Button-1>", lambda e: age_entry.delete(0, END))
age_entry.insert(0, "age")
age_entry.grid(row=2, column= 1,pady=3)

address_entry= Entry(cr, width= 20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
address_entry.bind("<Button-1>", lambda e: address_entry.delete(0, END))
address_entry.insert(0, "Kapan")
address_entry.grid(row=3, column=1,pady=3)

city_entry= Entry(cr, width= 20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
city_entry.bind("<Button-1>", lambda e: city_entry.delete(0, END))
city_entry.insert(0, "Kathmandu")
city_entry.grid(row=4, column=1,pady=3)

zipcode_entry= Entry(cr, width= 20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
zipcode_entry.bind("<Button-1>", lambda e: zipcode_entry.delete(0, END))
zipcode_entry.insert(0, "44600")
zipcode_entry.grid(row=5, column=1,pady=3)

password_entry= Entry(cr, width= 20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
password_entry.bind("<Button-1>", lambda e: password_entry.delete(0, END))
password_entry.insert(0, "Password")
password_entry.grid(row=6, column=1, pady=3)

gender_entry= Entry(cr, width= 20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
gender_entry.bind("<Button-1>", lambda e: gender_entry.delete(0, END))
gender_entry.insert(0, "Male/Female")
gender_entry.grid(row=7, column=1, pady=3)

add_btn= Button(cr, text="Add Data",borderwidth= 5, font=("Franklin Gothic Medium Cond", 15),bg="green", command= submit)
add_btn.grid(row=8, column=0, pady=10, ipadx= 35)

show_btn= Button(cr, text= "Show Data",borderwidth=5, font=("Franklin Gothic Medium Cond", 15),bg="grey50", command= query)
show_btn.grid(row=8, column=1, pady=10, ipadx=30)

delete_id_label= Label(cr, text= "Delete data",font=("Arial Rounded MT Bold", 13), bg="blue", fg="white")
delete_id_label.grid(row=12, column=0, pady=5)

delete_id_entry= Entry(cr, width=20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
delete_id_entry.bind("<Button-1>", lambda e: delete_id_entry.delete(0, END))
delete_id_entry.insert(0, "enter ID")
delete_id_entry.grid(row=12, column=1,pady=5)

delete_btn= Button(cr, text= "Delete",borderwidth=5, font=("Franklin Gothic Medium Cond", 15),bg="red", command= delete)
delete_btn.grid(row=13, column=0, columnspan=2,padx=10, pady=10, ipadx=127)

update_id_label= Label(cr, text= "Update data",font=("Arial Rounded MT Bold", 13), bg="blue", fg="white")
update_id_label.grid(row=14, column=0)

update_id_entry= Entry(cr, width=20,borderwidth=2,fg="grey40", font=("Segoe Print", 8))
update_id_entry.bind("<Button-1>", lambda e: update_id_entry.delete(0, END))
update_id_entry.insert(0, "enter ID")
update_id_entry.grid(row=14, column=1)

update_btn= Button(cr, text= "Update",borderwidth=5, font=("Franklin Gothic Medium Cond", 15),bg="grey50", command=edit)
update_btn.grid(row=15, column=0, columnspan=2,padx=10, pady=10, ipadx=123)
pr.commit()
pr.close()
cr.mainloop()