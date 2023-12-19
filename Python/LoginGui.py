import tkinter as tk


#credential file
data={ 'sathi':'sathip6',
      'sathiya':'sathi',
      'raj':'ap6'
     }

#calling function
def credentialcheck():
    username=(user_entry.get())
    pwd=(pwd_entry.get())
    try:    
        if data[username]==pwd:
            print("Login Success.")
        else:
            print("Incorrect Password.")
    except:
        print("Username Not Exist.")



#Gui
window = tk.Tk()
window.geometry("540x740")
window.configure(bg='black')

username_lbl= tk.Label(window, text='Username')
pwd_lbl= tk.Label(window, text="Password")
user_entry=tk.Entry(master=window)
pwd_entry=tk.Entry(window, show='*')
login_button=tk.Button(window, text="Login", command=credentialcheck, fg='green', bg='blue')

username_lbl.pack()
user_entry.pack()
pwd_lbl.pack()
pwd_entry.pack()
login_button.pack()

window.mainloop()
