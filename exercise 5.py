from PyQt5.QtWidgets import QApplication,QWidget, QLabel, QRadioButton, QMessageBox

app = QApplication([])
win=QWidget()

win.setWindowTitle("Ютуб-канал Crazy People хоче зробити окремий міні-конкурс для спонсорів каналу.")
win.resize(600, 400)
win.move(100,100)

text=QLabel(win)
text.setText('Як звали першого ютуб-блогера, який набрав 100000000 підписників?')
text.move(50, 10)

button1 = QRadioButton(win)
button1.setText('Рет і Лінк')
button1.move(100,60)

button2 = QRadioButton(win)
button2.setText('SlivkiShow')
button2.move(200,60)

button3 = QRadioButton(win)
button3.setText('TheBrianMaps')
button3.move(100,120)

button4 = QRadioButton(win)
button4.setText('Mister Max')
button4.move(200,120)

button5 = QRadioButton(win)
button5.setText('EeOneGuy')
button5.move(300,180)

button6 = QRadioButton(win)
button6.setText('PewDiePie')
button6.move(200,180)

def show_win():
    box = QMessageBox()
    box.setText('Ви виграли зустріч з творцями каналу!')
    box.exec_()

def show_lose():
    box = QMessageBox()
    box.setText('Пощастить іншим разом!')
    box.exec_()

button1.clicked.connect(show_lose)
button2.clicked.connect(show_lose)
button3.clicked.connect(show_lose)
button4.clicked.connect(show_lose)
button5.clicked.connect(show_lose)
button6.clicked.connect(show_win)

win.show()
app.exec()