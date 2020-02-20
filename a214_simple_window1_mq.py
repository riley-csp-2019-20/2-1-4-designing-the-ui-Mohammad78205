##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window

root = tk.Tk()
root.title("Authorization")
root.wm_geometry("200x200")

# create empty frame
frame_login = tk.Frame(root)
frame_login.grid(column = 0, row = 0, sticky = "NSWE")

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack(pady = 0, padx=68)


ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text='Password:')
lbl_password.pack(pady = 0, padx = 68)


ent_password = tk.Entry(frame_login, show="*", width=20, bd=3)
ent_password.pack(pady=5)

def test_my_button():
    frame_auth.tkraise()

    password = ent_password.get()
    lbl_display_pass.config(text = password)


btn_login = tk.Button(frame_login, text = "Login", command=test_my_button)
btn_login.pack(pady = 10)

frame_auth = tk.Frame(root)
frame_auth.grid(column = 0, row = 0, sticky = "news")

lbl_display_pass = tk.Label(frame_auth, text = "test")
lbl_display_pass.pack()

frame_login.tkraise()

root.mainloop()