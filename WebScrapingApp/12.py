from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from newSite.OxuAz import OxuAz
from newSite.OxuAz import XpathConfig


# creating a class
# that inherits the QDialog class
class Window(QDialog):

    # constructor
    def __init__(self):
        super(Window, self).__init__()

        # setting window title
        self.setWindowTitle("Python")

        # setting geometry to the window
        self.setGeometry(100, 100, 500, 400)

        # creating a group box
        self.formGroupBox = QGroupBox("Form 1")

        self.newsListLink = QLineEdit()

        self.newsList = QLineEdit()

        self.newsLink = QLineEdit()

        self.newsTitle = QLineEdit()

        self.newsImg = QLineEdit()

        # calling the method that create the form
        self.createForm()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # adding action when form is accepted
        self.buttonBox.accepted.connect(self.getInfo)

        # addding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)

        # creating a vertical layout
        mainLayout = QVBoxLayout()

        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)

        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)

        # setting lay out
        self.setLayout(mainLayout)

    # get info method called when form is accepted
    def getInfo(self):
        w = QWidget()
        b = QLabel(w)
        b.setText("Hello World!")
        w.setGeometry(100, 100, 500, 400)
        b.move(50, 20)
        w.setWindowTitle("PyQt5")
        w.show()
        # printing the form information
        print("newsListLink : {0}".format(self.newsListLink.text()))
        print("newsList : {0}".format(self.newsList.text()))
        print("newsTitle: {0}".format(self.newsTitle.text()))
        print("newsImg: {0}".format(self.newsImg.text()))

        x = XpathConfig()

        x.newsList = self.newsList.text()
        x.title = self.newsTitle.text()
        x.link = self.newsLink.text()
        x.img = self.newsImg.text()
        site = OxuAz(self.newsListLink.text(), x)
        site.newsLists()
        for i in site.news_list:
            print(i)

        # closing the window
        # self.close()

    # creat form method
    def createForm(self):
        # creating a form layout
        layout = QFormLayout()

        # adding rows
        # for name and adding input text

        self.newsListLink = QLineEdit()

        self.newsLink = QLineEdit()

        self.newsTitle = QLineEdit()

        self.newsImg = QLineEdit()

        layout.addRow(QLabel("newsListLink"), self.newsListLink)
        layout.addRow(QLabel("newsList"), self.newsList)
        layout.addRow(QLabel("newsLink"), self.newsLink)
        layout.addRow(QLabel("newsTitle"), self.newsTitle)
        layout.addRow(QLabel("newsImg"), self.newsImg)

        # setting layout
        self.formGroupBox.setLayout(layout)


# main method
if __name__ == '__main__':
    # create pyqt5 app
    app = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # showing the window
    window.show()

    # start the app
    sys.exit(app.exec())
