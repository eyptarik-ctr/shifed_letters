from tkinter import*
# font
font_family = "Helvetica"
font_size = 16
font_weight = "bold"
custom_font = (font_family, font_size, font_weight)

# alfabets
alfabetSmalcase = [chr(s) for s in range(97, 123)]
alfabetUppercase = [chr(s) for s in range(65, 91)]

# root
root = Tk()
root.title("Secret note")
root.config(height=550 ,width=250)
root.config(bg="#58CFB2")

# information label
def infoLabel():
    info_label = Label(root)
    info_label.config(text="write your note below",bg="#CF5858" ,fg="#31D1B9" ,font=custom_font)
    info_label.place(x=18 ,y=12)

# note entry
def noteEntry():
    note_entry = Entry(root)
    note_entry.place(x=62, y=48)
    note_entry.config(bg="#611B86")

# shift number entry
def shiftAmount():
    shift_info_entry = Entry(root)
    shift_info_entry.place(x=62 ,y=110)
    shift_info_entry.config(bg="#4FEC30")

# shift amount mesage
def shiftAmountMesage():
    shift_mesage_lb = Label(root)
    shift_mesage_lb.config(text="Enter shift amount", font=custom_font, bg="#8530EC", fg="#31D1B9")
    shift_mesage_lb.place(x=27 ,y=72 )
# encode mesage
def encryptedMesage():
    encrypted_mesage = Label(root)
    encrypted_mesage.config(text="Encrypted text" ,font=custom_font ,bg="#A28461" ,fg="#31D1B9")
    encrypted_mesage.place(x=46 , y=135)

# screen
def screenFunction():
    screen_lb = Entry(root)

# encode

# edcode


# buttons
encode_button = Button(text="Encode" , font=custom_font)
encode_button.place(x=120 , y=300)

# function calls
infoLabel()
noteEntry()
shiftAmountMesage()
encryptedMesage()
screenFunction()
shiftAmount()









root.mainloop()