import time
import pyttsx3
import datetime
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from sample_office_Ui import Ui_MainWindow
import connect_db as cdb
  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishUser():

    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    second = int(datetime.datetime.now().second)
    if hour >= 0 and hour < 12:
        speak(f"Good morning, welcome to Engineering Ltd. sir the time is {hour} hours {minute} minutes and {second} seconds")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon, welcome to Engineering Ltd. sir the time is {hour} hours {minute} minutes and {second} seconds")
    elif hour >= 18 and hour < 20:
        speak(f"Good evening, welcome to Engineering Ltd. sir the time is {hour} hours {minute} minutes and {second} seconds")
    else:
        speak(f"Welcome to Engineering Ltd. sir the time is {hour} hours {minute} minutes and {second} seconds,we are close now please visit us tomorrow")

class MainThread(QThread):
    
    def __init__(self):
        
        super(MainThread,self).__init__()

startExecution = MainThread()
time.sleep(10)
wishUser()
speak("Please enter the required details correctly")
cdb.helper.insert_user_details(str(input('{0}'.format("Enter your User Name: "))), int(input('{0}'.format("Enter your Contact No: "))), str(input('{0}'.format("Enter your email Address: "))),str(input('{0}'.format("Enter your Location: "))))
speak("Please choose an option to proceed further")

class Gui_Start(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.pushButton.clicked.connect(self.civil_Engineering)
        self.gui.pushButton_2.clicked.connect(self.mechanical_Engineering)
        self.gui.pushButton_3.clicked.connect(self.electrical_Engineering)
        self.gui.pushButton_4.clicked.connect(self.instrumentation_Engineering)
        self.gui.pushButton_5.clicked.connect(self.computer_Engineering)
        self.gui.pushButton_6.clicked.connect(self.information_Technology)
        self.gui.pushButton_7.clicked.connect(self.ministryofHome_Affairs)
        self.gui.pushButton_8.clicked.connect(self.ministryof_Justice)
        self.gui.pushButton_9.clicked.connect(self.ministryof_Labour)
        self.gui.pushButton_10.clicked.connect(self.ministryof_Science)
        self.gui.pushButton_11.clicked.connect(self.ministryofSocial_Affairs)
        self.gui.pushButton_12.clicked.connect(self.ministryof_Sports)
        
    def civil_Engineering(self):

        cdb.helper.civil()

    def mechanical_Engineering(self):
        
        cdb.helper.mech()
        
    def electrical_Engineering(self):
        
        cdb.helper.elec()
        
    def instrumentation_Engineering(self):
        
        cdb.helper.instru()
        
    def computer_Engineering(self):
        
        cdb.helper.comp()
        
    def information_Technology(self):
        
        cdb.helper.infotec()
        
    def ministryofHome_Affairs(self):
        
        cdb.helper.moha()
        
    def ministryof_Justice(self):
        
        cdb.helper.moj()
        
    def ministryof_Labour(self):
        
        cdb.helper.mol()
        
    def ministryof_Science(self):
        
        cdb.helper.mos()
        
    def ministryofSocial_Affairs(self):

        cdb.helper.mosa()
        
    def ministryof_Sports(self):

        cdb.helper.mosp()
        
    def startTask(self):
        
        self.gui.movie = QtGui.QMovie("E:\\Python Project\\AI Assistant\\sample office\\white-wall-empty-room-with-plants-floor-3d-rendering.jpg")
        self.gui.label.setMovie(self.gui.movie)
        self.gui.movie.start()
        self.gui.movie = QtGui.QMovie("E:\\Python Project\\AI Assistant\\sample office\\welcome.png")
        self.gui.label_2.setMovie(self.gui.movie)
        self.gui.movie.start()
       
        startExecution.start()

GuiApp = QApplication(sys.argv)
MainWindow = Gui_Start()
MainWindow.show()
exit(GuiApp.exec_())