from tkinter import *


morse_code = {
 'a': '. -',
 'b':'- . .',
 'c':'- . - .',
 'd':'-..',
 'e':'.',
 'f':'..-.',
 'g':'--.',
 'h':'....',
 'i':'..',
 'j':'.---',
 'k':'-.-',
 'l':'.-..',
 'm':'--',
 'n':'-.',
 'o':'---',
 'p':'.--.',
 'q':'--.-',
 'r':'.-.',
 's':'...',
 't':'-',
 'u':'..-',
 'v':'...-',
 'w':'.--',
 'x':'-..-',
 'y':'-.--',
 'z':'--..',
 '0':'-----',
 '1':'.----',
 '2':'..---',
 '3':'...--',
 '4':'....-',
 '5':'.....',
 '6':'-....',
 '7':'--...',
 '8':'---..',
 '9':'----.'
}

def text_to_morse():
    user_input = entry.get()
    morse_data = [morse_code.get(i.lower(), '') for i in user_input]
    result = ' '.join(morse_data)
    morse_label.config(text=result)

window = Tk()
window.title("Text To Morse")
window.geometry("650x300")
window.config(padx=20, pady=20, bg="#f0f0f0")

for i in range(4):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

text_label = Label(window, text="Text To Morse Code Generator", font=("Arial", 15), bg="#f0f0f0")
text_label.grid(row=1, column=0, columnspan=4, pady=(0, 10), sticky="n")

morse_label = Label(window, text="", font=("Arial", 15, "bold"), fg="blue", bg="#f0f0f0")
morse_label.grid(row=2, column=0, columnspan=4, pady=(0, 20), sticky="n")

entry = Entry(window, width=30, font=("Arial", 12))
entry.grid(row=3, column=0, columnspan=4, pady=(0, 10), sticky="n")

button = Button(window, text="Convert", command=text_to_morse, font=("Arial", 12), bg="#4CAF50", fg="white")
button.grid(row=4, column=0, columnspan=4, pady=(0, 20), sticky="n")

new_morse_label = Label(window, text="", font=("Arial", 15, "bold"), fg="blue", bg="#f0f0f0")
new_morse_label.grid(row=5, column=0, columnspan=4, sticky="n")

window.mainloop()
