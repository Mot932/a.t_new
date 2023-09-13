import tkinter 
import analiz


def run():
    analiz.TextAnalyser(file_name='text.txt', pos_list=['VERB', 'NOUN'], chislo=int(entry_amount.get()))

window = tkinter.Tk()
label = tkinter.Label(window, text="Анализатор текста", font=("Impact", 19))
button = tkinter.Button(window, font=("Impact", 17), background="#DAA520", text="сделать вордклауд", command=run)
entry_amount = tkinter.Entry(window, font=("Impact", 18))
label.pack(anchor="nw", padx=6, pady=6)
entry_amount.pack(anchor="nw", padx=6, pady=6)
button.pack(anchor="nw", padx=6, pady=6)


window.mainloop()