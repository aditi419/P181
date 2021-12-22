from tkinter import *
from tkinter import ttk 
from googletrans import Translator
from googletrans import LANGUAGES
root = Tk()
root.geometry('800x600')
root.config(bg='lightgreen')

label_title = Label(root,text='LANGUAGE TRANSLATOR',bg='lightgreen',font=('Sylfean',30,'bold')) 
label_title.place(relx=0.5,rely=0.1,anchor=CENTER)

label = Label(root,text='Enter Text',bg='lightgreen',font=('Sylfean',20))
label.place(relx=0.19,rely=0.3,anchor=W)

textarea = Text(root,bg='lightgreen',font=('Sylfean',18),height=10,wrap='word',width=25,padx=2,pady=2,bd=0)
textarea.place(relx=0.25,rely=0.55,anchor=CENTER)

language = list(LANGUAGES.values())
dropdown = ttk.Combobox(state='readonly',values=language,width=15)
dropdown.place(relx=0.7,rely=0.3,anchor=W)
dropdown.set('english')

label2 = Label(root,text='Output',bg='lightgreen',font=('Sylfean',20))
label2.place(relx=0.6,rely=0.3,anchor=W)

textarea2 = Text(root,bg='lightgreen',font=('Sylfean',18),height=10,wrap='word',width=25,padx=2,pady=2,bd=0)
textarea2.place(relx=0.75,rely=0.55,anchor=CENTER)

btn = Button(root,text='Translate',font=('Sylfean',20,'bold'),background='purple',activebackground='green',fg='black',relief=FLAT,pady=0.1)
btn.place(relx=0.5,rely=0.9,anchor=S)

root.mainloop()