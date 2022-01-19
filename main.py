from tkinter import*
import random
from tkinter import messagebox
import linecache
r= random.Random()

screen = Tk()
canvas = Canvas(width = 100, height = 67)
screen.minsize(250,280)







#let user generate a password
def gen_pass():
    pass_entry.delete(0,END)
    letter_characs =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","q","r","s","t","u","v","w","x","y","z"]
    num_characs =["1","2","3","4","5","6","7","8","9","0"]
    spex_characs =["#","$","!","*","&","~","%","_","+"]


    letter_rng = r.randint(5,5)
    num_rng = r.randint(2,3)
    spex_rng = r.randint(2,3)

    rand_letters = [r.choice(letter_characs) for item in range(letter_rng)]
    rand_num = [r.choice(num_characs) for item in range(num_rng)]
    rand_spex = [r.choice(spex_characs) for item in range(spex_rng)]
    rand_cap = (r.choice(rand_letters)).upper()

    pswd = rand_letters + rand_num + rand_spex
    r.shuffle(pswd)
    pswd.insert(0,rand_cap)
    pswd ="".join(pswd)
    pass_entry.insert(0,pswd)


#save user data
def save_data():
    web = web_entry.get()
    user = user_entry.get()
    passw = pass_entry.get()

    authorizeed = messagebox.askyesno(title="Authorize Procedure", message=f"Save The Entered Data?\nEmail: {user}\nWebsite: {web}\nPassword: {passw}")

    if authorizeed:
        with open("user_data", "a+") as data:
            data.write(f"{user} | {web} |  {passw}\n")

        web_entry.delete(0,END)
        pass_entry.delete(0,END)



#view user data in a new window
def open_data():
    with open("user_data") as data:
        data = data.readlines()


    new_screen = Toplevel(screen)
    new_screen.minsize(300,100)
    new_screen.title("Password Log")

    scroll_bar = Scrollbar(new_screen)
    scroll_bar.pack(side=RIGHT, fill=Y)

    list_box = Listbox(new_screen)
    list_box.pack(fill = BOTH)
    list_box_data = [list_box.insert(END,li) for li in data]

    list_box.config(yscrollcommand = scroll_bar.set)
    scroll_bar.config(command = list_box.yview)





#setup screen
image =PhotoImage(file="logo.png")
canvas.create_image(52, 35,image=image)
canvas.place(x = 97,y=15)

#add email/user label and input box
user_lable =Label(text="Email")
user_lable.place(x=20,y=100)
user_entry = Entry(width=25)
user_entry.place(x=60,y=102)

    #load user/email
user = linecache.getline("user_data",2).split()
if user == []:
        user="email"
elif user != []:
    user = user[0].split()
    user = user[0]

user_entry.insert(0,user)


#add web label and input box
web_lable =Label(text="Website")
web_lable.place(x=10,y=127)
web_entry = Entry(width=25)
web_entry.place(x=60,y=130)

#add pswd inputbox and label
pass_lable =Label(text="Password")
pass_lable.place(x=3,y=157)
pass_entry = Entry(width=25)
pass_entry.place(x=60,y=160)




#create buttons + let user use button

#creates random password
generate_button = Button(text="Generate",width=7, bg="red", fg="white", command = gen_pass)
generate_button.place(x=26,y=190)

#use to save data
save_button = Button(text="Save",width=7, bg="red", fg="white", command = save_data)
save_button.place(x=100,y=190)

#view saved data
see_data_button = Button(text="See Saved",width=7, bg="red", fg="white", command = open_data)
see_data_button.place(x=170,y=190)





screen.mainloop()