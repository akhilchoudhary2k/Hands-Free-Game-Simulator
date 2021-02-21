# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'v2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#



import cv2
import time

from PyQt5.QtGui import QImage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import numpy as np
from pynput.keyboard import Key, Controller




work = False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 827)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 821, 81))
        
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(26)
        
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(10, 700, 221, 61))
        
        font = QtGui.QFont()
        font.setPointSize(22)
        
        self.b1.setFont(font)
        self.b1.setAutoFillBackground(False)
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(570, 700, 221, 61))
        
        font = QtGui.QFont()
        font.setPointSize(22)
        
        self.b2.setFont(font)
        self.b2.setAutoFillBackground(False)
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(310, 700, 171, 61))

        self.b1.setStyleSheet("background-color : green")
        self.b2.setStyleSheet("background-color : red")
        self.b3.setStyleSheet("background-color : yellow")

        # connect the buttons
        self.b1.clicked.connect(self.start_it)
        self.b2.clicked.connect(self.stop_it)
        self.b3.clicked.connect(self.tutorial)
        # define some variables
        # cap = cv2.VideoCapture(0)

        font = QtGui.QFont()
        font.setPointSize(22)
        
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.cam = QtWidgets.QLabel(self.centralwidget)
        self.cam.setGeometry(QtCore.QRect(10, 110, 781, 571))
        self.cam.setText("")

        self.cam.setPixmap(QtGui.QPixmap("images/face.png"))
        
        self.cam.setScaledContents(True)
        self.cam.setObjectName("cam")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Team: sin(θ)"))
       
        self.label.setText(_translate("MainWindow", "Welcome to Hands Free Gaming !!"))
        self.b1.setText(_translate("MainWindow", "Start "))
        self.b2.setText(_translate("MainWindow", "Stop "))
        self.b3.setText(_translate("MainWindow", "Tutorial"))

    def start_it(self):
        # print("clicked")
        # self.cam.setPixmap(QtGui.QPixmap("../../Downloads/kgp.jpg"))


        ################ logic of opencv code ########
        keyboard = Controller()
        # faceCascade = cv2.CascadeClassifier('trained_ML_model.xml')
        faceCascade = cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')

        p1_x = 260
        p1_y = 240
        p2_x = 300
        p2_y = 275


        global work
        work = True
        # print("once")
        cap = cv2.VideoCapture(0)
        flag = 1   

        while(work):
            ret, frame = cap.read()
            # cv2.imshow('frame',frame)
            frame = cv2.flip(frame,1)

            if ret == True:
                imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
                centre_new = []
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 1)
                    centre_new = [int((x + w + x)/2), int((y + h + y)/2)]
                
                cv2.rectangle(frame, (p1_x, p1_y), (p2_x, p2_y), (255, 0, 0), 2)
                cv2.circle(frame, (centre_new[0], centre_new[1]), 0, (0,0,255), 5)

                if centre_new[0] > p1_x and centre_new[1] > p1_y and centre_new[0] < p2_x and centre_new[1] < p2_y:
                    flag=0

                if flag == 0 :

                    if  centre_new[0] > p2_x : 
                        keyboard.press(Key.right)
                        keyboard.release(Key.right)
                        print('RIGHT')
                        flag = 1

                    if  centre_new[0] < p1_x : 
                        keyboard.press(Key.left)
                        keyboard.release(Key.left)
                        print('LEFT')
                        flag = 1

                    if  centre_new[1] < p1_y : 
                        keyboard.press(Key.up)
                        keyboard.release(Key.up)
                        print('UP')
                        flag = 1

                    if  centre_new[1] > p2_y : 
                        keyboard.press(Key.down)
                        keyboard.release(Key.down)
                        print('DOWN')
                        flag = 1

            # displaying the image
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # height, width, channel = frame.shape
            # step = channel * width
            # qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
            cv2.imshow('frame',frame)

            # self.cam.setPixmap(QPixmap.fromImage(qImg))
            # self.cam.setPixmap(QtGui.QPixmap(qImg))
            
            if cv2.waitKey(1) & 0xFF == ord('q') & work==True:
                break

        cap.release()
        cv2.destroyAllWindows()


    def stop_it(self):
        global work
        work = False
        # print("set to false")
        self.cam.setPixmap(QtGui.QPixmap("images/face.png"))


    def tutorial(self):
        msg = QMessageBox()
        # msg.setGeometry(400,300, 900, 900)
        msg.setWindowTitle("How to use:")
        msg.setText("1) Move your face in UP, DOWN, LEFT, RIGHT and it will simulate \n    that key press\n2) Your nose must come back in the square each time\n3) Your background must be clear\n4) Detailed instructions are given in PPT")

        x = msg.exec_()




if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())

