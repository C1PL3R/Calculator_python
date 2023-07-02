import customtkinter as tk

root = tk.CTk()
root.title("Калькулятор")
root.geometry("360x600+400+30")
tk.set_appearance_mode('dark')
root.resizable(False, False)
root.iconbitmap("Image/calculator.ico")


def button_click(number):
    current = entry.get()
    entry.delete(0, "end")
    entry.insert("end", current + str(number))

a = 0

def button_clear():
    global a
    current_text = entry.get()
    if a == 1:
        entry.delete(0, tk.END)
        a = 0
    else:
        new_text = current_text[:-1]
        entry.delete(0, tk.END)
        entry.insert(0, new_text)
        

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        global a
        a = 1
    except Exception:
        entry.configure(textvariable="Error")
    
entry = tk.CTkEntry(root, 
                    width=360, 
                    height=132,
                    border_width=0,
                    fg_color="#676767",
                    corner_radius=0,
                    font=("News Times", 40))
entry.place(x=0, y=0)

number_color = "#FF9900"
arithmetic_sumbol_color = "#D9D9D9"
text_number_color = "white"
text_arithmetic_sumbol_color = "black"
hover_color_1 = "FFFFFF"
hover_color_2 = "FFAB2E"

buttons = [
    ("1", 0, 210, number_color, text_number_color, hover_color_2),
    ("2", 90, 210, number_color, text_number_color, hover_color_2),
    ("3", 180, 210, number_color, text_number_color, hover_color_2),
    ("4", 0, 288, number_color, text_number_color, hover_color_2),
    ("5", 90, 288, number_color, text_number_color, hover_color_2),
    ("6", 180, 288, number_color, text_number_color, hover_color_2),
    ("7", 0, 366, number_color, text_number_color, hover_color_2),
    ("8", 90, 366, number_color, text_number_color, hover_color_2),
    ("9", 180, 366, number_color, text_number_color, hover_color_2),
    ("0", 90, 444, number_color, text_number_color, hover_color_2),
    ("+", 270, 210, arithmetic_sumbol_color, text_arithmetic_sumbol_color, hover_color_1),
    ("-", 270, 288, arithmetic_sumbol_color, text_arithmetic_sumbol_color, hover_color_1),
    ("*", 270, 366, arithmetic_sumbol_color, text_arithmetic_sumbol_color, hover_color_1),
    ("/", 270, 444, arithmetic_sumbol_color, text_arithmetic_sumbol_color, hover_color_1),
    ("(", 0, 132, arithmetic_sumbol_color, text_arithmetic_sumbol_color, hover_color_1),
    (")", 180, 132, arithmetic_sumbol_color, text_arithmetic_sumbol_color, hover_color_1)
]


for button_text, x, y, color, text_color, text_hover in buttons:
    button = tk.CTkButton(root, 
                          text=button_text, 
                          width=90, height=78, 
                          command=lambda text=button_text: button_click(text),
                          fg_color=color,
                          border_color="#474747",
                          border_width=1,
                          corner_radius=0,
                          font=("News Times", 40),
                          text_color=text_color,
                          hover_color=f"#{text_hover}")
    button.place(x=x, y=y)

clear_button = tk.CTkButton(root, 
                            text="C", 
                            width=90, height=78, 
                            command=button_clear,
                            fg_color="#D60101",
                            border_color="#474747",
                            border_width=1,
                            corner_radius=0,
                            font=("News Times", 40),
                            hover_color="#FF0000")
clear_button.place(x=269, y=132)

equal_button = tk.CTkButton(root, 
                            text="=", 
                            width=360, height=77, 
                            command=button_equal,
                            fg_color="#6F6F6F",
                            corner_radius=0,
                            font=("News Times", 40),
                            hover_color="#959595")
equal_button.place(x=0, y=523)

root.mainloop()