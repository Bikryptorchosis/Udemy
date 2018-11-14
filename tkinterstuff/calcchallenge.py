import tkinter


main_window = tkinter.Tk()

main_window.title('Calculator')
main_window.geometry('80x160+8+100')
main_window['padx'] = 4

calc_field = tkinter.Entry(main_window)
calc_field.grid(row=0, column=0, columnspan=4, sticky='wens')

keypad = tkinter.Frame(main_window)
keypad.grid(row=1, column=0, sticky='wens')

main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(0, weight=1)
main_window.columnconfigure(0, weight=1)

buttons = {'C': '00',
           'CE': '01',
           '7': '10',
           '8': '11',
           '9': '12',
           '+': '13',
           '4': '20',
           '5': '21',
           '6': '22',
           '-': '23',
           '1': '30',
           '2': '31',
           '3': '32',
           '*': '33',
           '0': '40',
           '=': '41',
           '/': '43'}

for x in range(0, 5):
    if x < 4:
        keypad.columnconfigure(x, weight=1)
    keypad.rowconfigure(x, weight=1)

for text, value in buttons.items():
    temp_button = tkinter.Button(keypad, text=text)
    temp_button.grid(row=int(value[0]), column=int(value[1]), sticky='wens', padx=1, pady=1)
    if value == '51':
        temp_button.grid(columnspan=2)

main_window.update()
main_window.minsize(main_window.winfo_width(), main_window.winfo_height())
main_window.maxsize(main_window.winfo_width() + 50, main_window.winfo_height() + 50)

main_window.mainloop()
