from tkinter import *
import os

st = Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="blue")

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown -/s /t 1")
# Relief is used for a 3D effect.

r_button = Button(st, text = "Restart", font = ("Time New Roman", 20, "bold"),relief = RAISED, cursor="plus",command =restart)
r_button.place(x=150,y=60,height = 50,width = 200)

r_button = Button(st, text = "Restart Time", font = ("Time New Roman", 20, "bold"),relief = RAISED, cursor="plus",command =restart_time)
r_button.place(x=150,y=170,height = 50,width = 200)

r_button = Button(st, text = "Log Out", font = ("Time New Roman", 20, "bold"),relief = RAISED, cursor="plus",command = logout)
r_button.place(x=150,y=270,height = 50,width = 200)

r_button = Button(st, text = "Shutdown", font = ("Time New Roman", 20, "bold"),relief = RAISED, cursor="plus",command = shutdown)
r_button.place(x=150,y=370,height = 50,width = 200)












st.mainloop()