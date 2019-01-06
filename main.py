import requests
from tkinter import *

window = Tk()
window.geometry('400x400+100+200')
app_id = '751x17b0'
app_key = 'b851375d71ec30e9879cd02b4488762ab'
language = 'en'


lbl = Label(window, text="Phika | Oxford Dictionary").pack()
lbl_n = Label(window, text="")
lbl_n.pack(side=LEFT)

text = Text(window, width=40, height=15, wrap='word')
text.place(x=10, y=100)


def clicked():
    try:
        text.delete(1.0, END)
        word_id = word_entry.get()
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
        r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
        print(r.text)
        meaning = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        list_ = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0][
            'examples']


        examples = 'Examples:\n'
        for item in list_:
            examples += '- ' + item['text'] + '\n'

        result = word_id + '\n- ' + meaning + '\n\n' + examples
        print(result)
        text.insert(END, result)
    except Exception as e:
        text.insert(END, 'Error:\n- {}'.format(e))


word = StringVar()
word_entry = Entry(window, textvariable=word, width=20)
word_entry.place(x=10, y=50)

btn = Button(window, text="Translate This", command=clicked)
btn.place(x=200, y=50)

window.mainloop()
