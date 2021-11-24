import sqlite3
import sys
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QAction, QTableWidgetItem


class add_university(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled 2.ui', self)
        self.setModal(True)
        self.cancel.clicked.connect(self.go_away_1)
        self.add.clicked.connect(self.addition_1)

        self.db = sqlite3.connect('database_un.db')
        self.cursor = self.db.cursor()
        query = """ CREATE TABLE IF NOT EXISTS univer(id INTEGER, name TEXT, specialty TEXT, score INTEGER,
         numbers INTEGER)"""
        self.cursor.execute(query)
        self.db.commit()

        query = """ SELECT * FROM univer"""
        self.cursor.execute(query)
        self.n = len(self.cursor.fetchall())

    def addition_1(self):
        self.n += 1
        query = """ INSERT INTO univer(id, name, specialty, score, numbers) VALUES ( ?, ?, ?, ?, ?)"""
        data = (self.n, self.university_name.text(), self.specialty_name.text(), int(self.min_scores.text()),
                int(self.student_numbers.text()))
        self.cursor.execute(query, data)
        self.university_name.setText('')
        self.specialty_name.setText('')
        self.min_scores.setText('')
        self.student_numbers.setText('')

    def go_away_1(self):
        self.db.commit()
        self.db.close()
        self.close()


class add_student(QDialog):

    def __init__(self):
        super().__init__()
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        uic.loadUi('untitled 3.ui', self)
        self.setModal(True)
        self.specialty_name_1.setReadOnly(True)
        self.specialty_name_2.setReadOnly(True)
        self.specialty_name_3.setReadOnly(True)
        self.cancel_1.clicked.connect(self.go_away_2)
        self.add_1.clicked.connect(self.addition_2)

        self.db1 = sqlite3.connect('database_st.db')
        self.cursor1 = self.db1.cursor()
        query = """CREATE TABLE IF NOT EXISTS abit(id INTEGER, FIO TEXT, sscore INTEGER, specialty1 INTEGER,
         specialty2 INTEGER, specialty3 INTEGER)"""
        self.cursor1.execute(query)
        self.db1.commit()
        query = """ SELECT * FROM abit"""
        self.cursor1.execute(query)
        self.n = len(self.cursor1.fetchall())

        self.db = sqlite3.connect('database_un.db')
        self.cursor = self.db.cursor()
        ppp = self.cursor.execute('''SELECT * FROM univer''')
        i = 0
        for elem in ppp:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(elem[1])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(elem[2])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(elem[3])))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(elem[4])))
            i += 1

        self.add1n.clicked.connect(self.napr1)
        self.add2n.clicked.connect(self.napr2)
        self.add3n.clicked.connect(self.napr3)

    def napr1(self):
        if self.tableWidget.selectedIndexes() != []:
            i = self.tableWidget.selectedIndexes()[0].row()
            self.specialty_name_1.setText(self.tableWidget.item(i, 0).text() + '-' + self.tableWidget.item(i, 1).text())
            self.n1 = i

    def napr2(self):
        if self.tableWidget.selectedIndexes() != []:
            i = self.tableWidget.selectedIndexes()[0].row()
            self.specialty_name_2.setText(self.tableWidget.item(i, 0).text() + '-' + self.tableWidget.item(i, 1).text())
            self.n2 = i

    def napr3(self):
        if self.tableWidget.selectedIndexes() != []:
            i = self.tableWidget.selectedIndexes()[0].row()
            self.specialty_name_3.setText(self.tableWidget.item(i, 0).text() + '-' + self.tableWidget.item(i, 1).text())
            self.n3 = i

    def addition_2(self):
        pass
        self.n += 1
        print (self.n, self.FIO.text(), int(self.score.text()), self.n1, self.n2 , self.n3)
        query = """ INSERT INTO abit(id, FIO, sscore, specialty1, specialty2, specialty3) VALUES ( ?, ?, ?, ?, ?, ?)"""
        data = (self.n, self.FIO.text(), int(self.score.text()), self.n1, self.n2 , self.n3) # self.n, self.specialty_name_2.text(), self.specialty_name_3.text())
        self.cursor1.execute(query, data)
        self.FIO.setText('')
        self.score.setText('')
        self.specialty_name_1.setText('')
        self.specialty_name_2.setText('')
        self.specialty_name_3.setText('')

    def go_away_2(self):
        self.db1.commit()
        self.db1.close()
        self.close()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled 1.ui', self)
        self.Qadd_university.triggered.connect(self.university)
        self.Qadd_student.triggered.connect(self.student)

    def university(self):
        a = add_university()
        a.show()
        a.exec_()

    def student(self):
        a = add_student()
        a.show()
        a.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


