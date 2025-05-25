from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json

notes = {}

def show_notes():
    name = notes_list.selectedItems()[0].text()
    main_input.setText(notes[name]['text'])


app = QApplication([])
main_win = QWidget()

main_input = QTextEdit()
notes_list = QListWidget()
add_note = QPushButton('Добавить заметку')
del_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить заметку')

main_layout = QHBoxLayout()
right_layout = QVBoxLayout()
buttons_layout = QHBoxLayout()

buttons_layout.addWidget(add_note)
buttons_layout.addWidget(del_note)



right_layout.addWidget(notes_list)
right_layout.addLayout(buttons_layout)
right_layout.addWidget(save_note)

main_layout.addWidget(main_input)
main_layout.addLayout(right_layout)

main_win.setLayout(main_layout)

main_win.resize(900,500)
main_win.show()

def save_notes():
    with open("notes_data.json", 'w', encoding='utf8') as file:
        json.dump(notes, file, indent=4)

def save_note_text():
    name = notes_list.selectedItems()[0].text()
    notes[name]['text'] = main_input.toPlainText()
    save_notes()

def create_note():
    note_name, ok = QInputDialog.getText(
        main_win, 'Добавить заметку', 'Название заметки:'
        )
    if ok and note_name != '':
        notes[note_name] = {'text':''}
        save_notes()
        get_notes()

def remove_notes():
    name = notes_list.selectedItems()[0].text()
    del notes[name]
    save_notes()
    get_notes()

def get_notes():
    notes_list.clear()
    global notes
    with open("notes_data.json", 'r', encoding='utf8') as file:
        notes = json.load(file)
        notes_list.addItems(notes.keys())
get_notes()


notes_list.itemClicked.connect(show_notes)
save_note.clicked.connect(save_note_text)
add_note.clicked.connect(create_note)
del_note.clicked.connect(remove_notes)
app.exec_()