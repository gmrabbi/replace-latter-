from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Replace latter")


lbl1 = Label(root, font=("arial", 15, "bold"), text="Phase : ")
phase_entry = Entry(root, font=("arial", 15, "bold"), bd=5)
lbl1.grid(row=0, column=0)
phase_entry.grid(row=0, column=1)

lbl_ltr = Label(root, font=("arial", 15, "bold"), text="Starting latter : ")
str_ltr = Entry(root, font=("arial", 15, "bold"), bd=5)
lbl_ltr.grid(row=1, column=0)
str_ltr.grid(row=1, column=1)

btn = Button(root, font=("arial", 18, "bold"),
             text="Submit", bd=5)
btn.grid(row=2, column=1)

mainloop()

# user_input = input("Enter your phase : ").lower()
# start_latter = (input("Enter the starting latter : ").lower())[0]

# alphabet = []

# for i in range(97, 122 + 1):
#     alphabet += chr(i)


# user_alphabet = []
# for i in range((ord(start_latter)), 122 + 1):
#     user_alphabet += chr(i)

# firt_latter = user_alphabet[0]
# if len(user_alphabet) < 26:
#     for i in range(97, ord(firt_latter)):
#         user_alphabet += chr(i)


# latter_num = alphabet.index(user_input[0])

# output = ""
# for latter in user_input:
#     if latter in alphabet:
#         num = alphabet.index(latter)
#         output += (user_alphabet[num - latter_num]).upper()
#     else:
#         output += latter

# print(output)
