from tkinter import *
from tkinter import messagebox
from database.PacemakerDatabase import PacemakerDatabase
from account.RegisterPage import registerPage

windowUsername ="[User]"

def Loginpage(my_frame):#my_frame is root
    userDatabase= PacemakerDatabase.get_instance()#database


    ###SIGN IN LOGIC, activated when sign in button pressed
    def signin():
        #user input
        username=user.get()
        password=code.get()

        #If user exists
        if (userDatabase.user_exists(username)):
            #check password
            if((userDatabase.get_password(username))==password):
                #load new screen when login successful (TO DO, connect back to windows)
                global windowUsername
                windowUsername=username
                #messagebox.showerror("Sign In", "Sign In Successful!", COMMAND=frame.quit())
                frame.quit()
                my_frame.destroy()
                return
            else:#wrong password, existing user
                messagebox.showerror("Invalid", "Invalid password")
        else:#user doesn't exist, promp registration
            messagebox.showerror("Invalid", "Invalid username. Register using the sign up button below.")


    frame=Frame(my_frame, width=350, height=350, bg="white")
    frame.place(x=70, y=70)


    heading=Label(frame, text="Sign in", fg='#57a1f8', bg="white", font=('Microsoft Yahei UI Light', 23,'bold'))
    heading.place(x=100, y=5)

    ######## user -----------------------

    #event functions
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0, 'Username')


    #user textbox
    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0,'Username')

    #event listener
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    #textbox lines
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ######## passoword -------------------
    #event functions
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0, 'Password')


    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0,'Password')

    #event listeners
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ########## sign in button ----------
    #command=sign in for login verification
    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
    label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light',9))
    label.place(x=40, y=270)

    #registration window, called when sign up button pressed
    def openRegister():
        registerWindow=Toplevel(my_frame)
        registerWindow.title("Registration")
        registerWindow.geometry('500x500')
        registerPage(registerWindow)
        return

    sign_up=Button(frame, width=6, text="Sign up", border=0, bg='white', cursor='hand2', fg='#57a1f8', command=lambda:openRegister())
    sign_up.place(x=200, y=270)

    my_frame.mainloop()
    return 0

def getUser():

    return windowUsername
