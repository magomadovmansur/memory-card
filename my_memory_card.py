from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QButtonGroup, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox)
from random import shuffle, randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")
RadioGroupBox = QGroupBox("Варианты ответов")
color = QRadioButton("Масть")
color2 = QRadioButton("порода")
color3 = QRadioButton("вид")
color4 = QRadioButton("все варианты верны")
qestion = QLabel("Самый сложный вопрос в мире")
button = QPushButton("Ответить")
AnsGroupBox = QGroupBox("Результат теста")
ans = QLabel("правильно/неправильно")
ans2 = QLabel("правильный ответ")
RadioGroup = QButtonGroup()
RadioGroup.addButton(color)
RadioGroup.addButton(color2)
RadioGroup.addButton(color3)
RadioGroup.addButton(color4)
ans_layout = QVBoxLayout()
ans_layout.addWidget(ans, alignment = Qt.AlignCenter)
ans_layout.addWidget(ans2, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(ans_layout)
layotH = QHBoxLayout()
layotV = QVBoxLayout()
layotV2 = QVBoxLayout()
layotV.addWidget(color)
layotV.addWidget(color2)
layotV2.addWidget(color3)
layotV2.addWidget(color4)
layotH.addLayout(layotV)
layotH.addLayout(layotV2)
RadioGroupBox.setLayout(layotH)
line = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line.addWidget(qestion, alignment = Qt.AlignCenter)
line2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
line2.addWidget(AnsGroupBox, alignment = Qt.AlignCenter)
line3.addWidget(button, alignment = Qt.AlignCenter)
layot_line = QVBoxLayout()
layot_line.addLayout(line, stretch=2)
layot_line.addLayout(line2, stretch=8)
layot_line.addStretch(1)
layot_line.addLayout(line3, stretch=2)
layot_line.addStretch(1)
layot_line.setSpacing(5)
window.setLayout(layot_line)
AnsGroupBox.hide()
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText("Следующий вопрос")
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText("Ответить")
    RadioGroup.setExclusive(False)
    color.setChecked(False)
    color2.setChecked(False)
    color3.setChecked(False)
    color4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [color, color2, color3, color4]
def ask(q: Question):
    shuffle (answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    qestion.setText(q.question)
    ans2.setText(q.right_answer)
    show_question()
def show_correct(res):
    ans.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно")
        window.score += 1
        print("Статистика")
        print("Всего вопросов:", window.total)
        print("Правильных ответов:", window.score)
        print("Raiting", (window.score/window.total * 100),"%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неправильно")
qestion_list = []
qestion_list.append(Question("Какова высота Эвереста?", "8849м", "8000м", "10000", "7000м"))
qestion_list.append(Question("Отчего появляется радуга?", "когда идёт дождь и светит солнце", "когда идёт дождь", "когда солнечное затмение", "просто так"))
qestion_list.append(Question("когда случилась вторая мировая война", "1941", "1939", "1920", "1950"))
qestion_list.append(Question("кто написал картину Мона Лиза?", "Леонардо Да Винчи", "Рафаэль", "Миккиланджелло", "Донателло"))
qestion_list.append(Question("кто написал рассказ Муму?", "И.С Тургенев", "Пушкин", "Есенеин", "Толстой"))
qestion_list.append(Question("когда появился мультик Шрек?", "2001", "2010", "2006", "2000"))
qestion_list.append(Question("когда появилась PS4?", "2013", "2020", "2015", "2005"))
qestion_list.append(Question("rкогда изобрели паровоз?", "1804", "1857", "1900", "1860"))
qestion_list.append(Question("как переводится слово feedback", "обратная связь", "машина", "вулкан", "шайба"))
def next_question():
    window.total += 1
    print("Статистика")
    print("Всего вопросов:", window.total)
    print("Правильных ответов:", window.score)
    cur_question = randint(0, len(qestion_list)-1)
    q = qestion_list[cur_question]
    ask(q)
def start_test():
    if button.text() == "Ответить":
        check_answer()
    else:
        next_question() 
button.clicked.connect(start_test)
window.total = 0
window.score = 0
next_question()
window.resize(400, 200)

window.show()
app.exec_()