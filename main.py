from tkinter import *

# Alfabe
alfabet = [chr(s) for s in range(97, 123)]
font_family = "Helvetica"
font_size = 16
font_weight = "bold"
custom_font = (font_family, font_size, font_weight)

# Tkinter
root = Tk()
root.title("Encrypted text")
root.config(width=359, height=500)
root.config(bg="#9B25AE")

# Info Label
enter_text_lb = Label(root)
enter_text_lb.config(text="Enter your text", bg="#25AE65", fg="#9B25AE", font=custom_font)
enter_text_lb.place(x=100, y=12)

# Enter Text
text_entry = Entry(root)
text_entry.config(bg="#AEAE25")
text_entry.place(x=120, y=45)

# Functions
get_text = ""
end_text = ""
re_text = ""

def GetText():
    global get_text
    get_text = text_entry.get()

def EncryptText(start_text, shift_amount):
    global end_text
    end_text = ""
    for char in start_text:
        if char in alfabet:
            position = alfabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alfabet[new_position]
        else:
            end_text += char

def CopyFun():
    global end_text
    root.clipboard_clear()
    root.clipboard_append(end_text)
    root.update()


copy_info_lb = Label(root)
def Call_function():
    GetText()
    EncryptText(start_text=get_text, shift_amount=5)
    CopyFun()
    # info label
    copy_info_lb.config(text="Your encrypted text is copied ", bg="#25AE65", fg="#9B25AE", font=custom_font)
    copy_info_lb.place(x=30, y=122)
# Encode button
encode_button = Button(root)
encode_button.config(text="ENCODE", bg="#2591AE", font=custom_font, command=Call_function)
encode_button.place(x=125, y=74)

#decode entry
decode_entry = Entry()
decode_entry.config(bg="#7B113F")
decode_entry.place(x=120,y=160)

#decode
def DecodeFun(crypto_text , re_amount):
    global re_text
    re_text = ""
    for char in crypto_text:
        get_position = alfabet.index(char)
        re_position = (get_position - re_amount)
        re_text += alfabet[re_position]
def CopyFun2():
    global re_text
    root.clipboard_clear()
    root.clipboard_append(re_text)
    root.update()
#decrypt mesage
decrypt_mesaage = Label(root)
def Decrypt_lb():
    decrypt_mesaage.config(text="Your decoded text copied",bg="#27A485" ,fg="#9B25AE",font=custom_font)

def CallFun2():
    global end_text
    DecodeFun(crypto_text=end_text ,re_amount=5)
    CopyFun2()




#decode button
decode_button = Button(root)
decode_button.config(text="DECODE",bg="#AE2593",font=custom_font,command=CallFun2)
decode_button.place(x=125,y=200)

root.mainloop()
