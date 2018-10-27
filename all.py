#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 00:53:43 2018

@author: songqun

"""

from PyQt5.QtWidgets import (QTextEdit,QMainWindow,QCheckBox,QWidget, QCalendarWidget,QLineEdit,QGridLayout,
    QLabel, QApplication, QHBoxLayout,QVBoxLayout,QPushButton,QMessageBox,QTableWidget,QTableWidgetItem)
from PyQt5.QtCore import QDate,Qt
import sys
import datetime
import requests
import pymysql

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
import pymysql
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 314)
        MainWindow.setMinimumSize(QtCore.QSize(550, 314))
        MainWindow.setMaximumSize(QtCore.QSize(550, 314))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Crab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("border-image: url(bg);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setEnabled(False)
        self.graphicsView.setGeometry(QtCore.QRect(40, 50, 191, 201))
        self.graphicsView.setStyleSheet("border-image: url(calendar);")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(290, 70, 131, 21))
        self.label.setStyleSheet("border-image: \\*url();")
        self.label.setObjectName("label")
        self.ID = QtWidgets.QLineEdit(self.centralWidget)
        self.ID.setGeometry(QtCore.QRect(290, 90, 201, 25))
        self.ID.setTabletTracking(True)
        self.ID.setStyleSheet("border-image: \\*url();\n"
"")
        self.ID.setObjectName("ID")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(290, 140, 131, 21))
        self.label_2.setStyleSheet("border-image: \\*url();")
        self.label_2.setObjectName("label_2")
        self.ID_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.ID_2.setGeometry(QtCore.QRect(290, 160, 201, 25))
        self.ID_2.setStyleSheet("border-image: \\*url();")
        self.ID_2.setObjectName("ID_2")
        self.ID_2.setEchoMode(QLineEdit.Password)
        
        self.lgbutton = QtWidgets.QPushButton(self.centralWidget)
        self.lgbutton.setGeometry(QtCore.QRect(420, 220, 70, 25))
        font = QtGui.QFont()
        font.setFamily(".SF NS Text")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lgbutton.setFont(font)
        self.lgbutton.setStyleSheet("border-image: \\*url();\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(147, 126, 83, 199), stop:1 rgba(255, 255, 255, 255));")
        self.lgbutton.setObjectName("lgbutton")
        self.lgbutton.clicked.connect(self.word_get)

        self.cancel = QtWidgets.QPushButton(self.centralWidget)
        self.cancel.setGeometry(QtCore.QRect(290, 220, 70, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("border-image: \\*url();\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(147, 126, 83, 199), stop:1 rgba(255, 255, 255, 255));")
        self.cancel.setObjectName("cancel")
        self.cancel.clicked.connect(self.cancel_get)
        
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SuperCalender-login"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">User Account：</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Password：</span></p></body></html>"))
        self.lgbutton.setText(_translate("MainWindow", "Login"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        
    def word_get(self):
        login_user = self.ID.text()
        login_password = self.ID_2.text()
        
        db=pymysql.connect('localhost','root','hellonihaoma','test')
        cursor=db.cursor()
        sql="SELECT * FROM test.Login;"
        cursor.execute(sql)
        results=cursor.fetchall()
        db.close()
      
        if login_user == results[0][0] and login_password == str(results[0][1]):
        #login_user=self.ID.text()
        #login_password=self.ID_2.text()
        #print (login_user,login_password)
        #if login_user == 'admin' and login_password == '123':
            MainWindow.close()
            ex.show()
        else:
            pop=QWidget()
            QMessageBox.warning(pop,
                    "Warning",
                    "Wrong user ID or Password！",
                    QMessageBox.Yes)
            self.lineEdit.setFocus()
            
    def cancel_get(self):
        MainWindow.close()
        

class Bus(QWidget):
        
    
        
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
       
        
        pict=QPixmap('map.png')
        repict=pict.scaled(750,750,aspectRatioMode=Qt.KeepAspectRatio)
        self.looplb=QLabel(self)
        self.looplb.setPixmap(repict)
        
        pict2=QPixmap('bus.png')
        repict2=pict2.scaled(70,45,aspectRatioMode=Qt.KeepAspectRatio)
        
        self.looplb2=QLabel(self)
        self.looplb2.setPixmap(repict2)
        self.looplb2.move(465,685)
        
        pghlb=QLabel('PGH',self)
        admlb=QLabel('N6',self)
        fstlb=QLabel('FST',self)

        pghlb.move(430,700)
        admlb.move(245,30)
        fstlb.move(75,90)
        self.looplb.move(65,25)
       
        self.reButton = QPushButton('Refresh',self)
        self.reButton.move(450,740)
        self.reButton.clicked.connect(self.on_click)
        #looplb2.move(230,70)#pgh
        #looplb2.move(100,190)#adm
        #looplb2.move(240,350)#fst
        #looplb2.move(150,150) #pgh and adm
        #looplb2.move(150,250)#adm and fst
        #looplb2.move(400,200)#fst and pgh
        '''
        grid=QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(reButton,2,2,1,1)
        self.setLayout(grid)
        '''
   
        
        #basic
        self.setGeometry(100, 50, 600, 800)
        self.setWindowTitle('Bus Information')
        #self.setWindowIcon(QIcon('web.png'))        
        #self.show()
        
       
    def on_click(self):
        
        #time2_get=datetime.datetime.now()
        #time2=time2_get.strftime('%Y-%m-%dT%H:%M:%S')
    
        #time1_get=time2_get-datetime.timedelta(minutes=10)
        #time1=time1_get.strftime('%Y-%m-%dT%H:%M:%S')

        #url='https://api.data.umac.mo/service/facilities/shuttle_bus_arrival_time/v1.0.0/all?date_from='+time1 \
        #+'&date_to='+time2
        url='https://api.data.umac.mo/service/facilities/shuttle_bus_arrival_time/v1.0.0/all'
        args={'Accept':'application/json','Authorization':'Bearer 1e8ca74b-97c8-33c1-af96-05a04b79a93d'}
        r=requests.get(url,headers=args)
        print('on_click')
        print(r.reason)
        
         #prepare the time sections
        t=datetime.datetime.now()
        '''
        t_0730=datetime.datetime.strptime(str(t.date())+'07:30:00','%Y-%m-%d%H:%M:%S')#string to time
        t_0830=datetime.datetime.strptime(str(t.date())+'08:30:59','%Y-%m-%d%H:%M:%S')#string to time
        t_1000=datetime.datetime.strptime(str(t.date())+'10:00:00','%Y-%m-%d%H:%M:%S')#string to time
        t_1200=datetime.datetime.strptime(str(t.date())+'12:00:00','%Y-%m-%d%H:%M:%S')#string to time
        t_1500=datetime.datetime.strptime(str(t.date())+'15:00:00','%Y-%m-%d%H:%M:%S')#string to time
        t_1730=datetime.datetime.strptime(str(t.date())+'17:30:00','%Y-%m-%d%H:%M:%S')#string to time
        t_1930=datetime.datetime.strptime(str(t.date())+'19:30:00','%Y-%m-%d%H:%M:%S')#string to time
        t_2315=datetime.datetime.strptime(str(t.date())+'23:15:59','%Y-%m-%d%H:%M:%S')#string to time
        '''
        if r.reason=='OK':
            
            r_dict=r.json()
            #roh=r_dict['_returned']
            status=r_dict['_embedded']
            s_dict=status[0]
            datetime_record_get=datetime.datetime.strptime(s_dict['datetime'],'%Y-%m-%dT%H:%M:%S+08:00')
            print('record time:'+s_dict['datetime'])
            
            if datetime_record_get>=datetime.datetime.strptime(str(t.date())+'07:30:00','%Y-%m-%d%H:%M:%S') and \
            datetime_record_get<=datetime.datetime.strptime(str(t.date())+'23:15:59','%Y-%m-%d%H:%M:%S'):
            
                datetime_now_get=datetime.datetime.now()
                print('now time:'+datetime.datetime.strftime(datetime_now_get,'%Y-%m-%dT%H:%M:%S+08:00'))
                #diff=datetime_now_get-datetime_record_get
                ''' 
                if s_dict['station']=='研究生宿舍':
                    if (datetime_now_get>=datetime.datetime.strptime(str(t.date())+'07:30:00','%Y-%m-%d%H:%M:%S') and \
                    datetime_now_get<=datetime.datetime.strptime(str(t.date())+'08:30:59','%Y-%m-%d%H:%M:%S')) or \
                        (datetime_now_get>=datetime.datetime.strptime(str(t.date())+'10:00:00','%Y-%m-%d%H:%M:%S') and \
                         datetime_now_get<=datetime.datetime.strptime(str(t.date())+'12:00:59','%Y-%m-%d%H:%M:%S')) or \
                         (datetime_now_get>=datetime.datetime.strptime(str(t.date())+'15:00:00','%Y-%m-%d%H:%M:%S') and \
                         datetime_now_get<=datetime.datetime.strptime(str(t.date())+'17:30:59','%Y-%m-%d%H:%M:%S')) or \
                          (datetime_now_get>=datetime.datetime.strptime(str(t.date())+'19:30:00','%Y-%m-%d%H:%M:%S') and \
                         datetime_now_get<=datetime.datetime.strptime(str(t.date())+'23:15:59','%Y-%m-%d%H:%M:%S')):
                        if datetime_record_get.minute<15 and datetime_record_get.minute>0:
                            self.looplb2.move(230,70)#pgh
                        elif datetime_record_get.minute<30 and datetime_record_get.minute>15:
                            self.looplb2.move(230,70)#pgh
                        elif datetime_record_get.minute<45 and datetime_record_get.minute>30:
                            self.looplb2.move(230,70)#pgh
                        else:
                            self.looplb2.move(150,150) #pgh and adm
                    if (datetime_now_get>=datetime.datetime.strptime(str(t.date())+'08:31:00','%Y-%m-%d%H:%M:%S') and \
                    datetime_now_get<=datetime.datetime.strptime(str(t.date())+'09:59:59','%Y-%m-%d%H:%M:%S')) or \
                        (datetime_now_get>=datetime.datetime.strptime(str(t.date())+'12:01:00','%Y-%m-%d%H:%M:%S') and \
                         datetime_now_get<=datetime.datetime.strptime(str(t.date())+'14:59:59','%Y-%m-%d%H:%M:%S')) or \
                         (datetime_now_get>=datetime.datetime.strptime(str(t.date())+'17:31:00','%Y-%m-%d%H:%M:%S') and \
                         datetime_now_get<=datetime.datetime.strptime(str(t.date())+'19:29:59','%Y-%m-%d%H:%M:%S')):
                        if datetime_record_get.minute<10 and datetime_record_get.minute>0:
                            self.looplb2.move(230,70)#pgh
                        elif datetime_record_get.minute<20 and datetime_record_get.minute>10:
                            self.looplb2.move(230,70)#pgh
                        elif datetime_record_get.minute<30 and datetime_record_get.minute>20:
                            self.looplb2.move(230,70)#pgh
                        elif datetime_record_get.minute<40 and datetime_record_get.minute>30:
                            self.looplb2.move(230,70)#pgh
                        elif datetime_record_get.minute<50 and datetime_record_get.minute>40:
                            self.looplb2.move(230,70)#pgh
                        else:
                            self.looplb2.move(150,150) #pgh and adm
                '''
                if s_dict['station']=='研究生宿舍':
                    #if diff>datetime.timedelta(minutes=1):
                    if datetime_now_get.minute>datetime_record_get.minute:
                        self.looplb2.move(490,250) #pgh and adm
                    #looplb2.move(230,70)#pgh
                    #looplb2.move(100,190)#adm
                    #looplb2.move(240,350)#fst
                    #looplb2.move(150,150) #pgh and adm
                    #self.looplb2.move(150,250)#adm and fst
                    #looplb2.move(400,200)#fst and pgh
                   #print('The bus is running between 行政樓 and FST')
                   #print('The bus is now at '+s_dict['station'])
                    
                   #if diff<=datetime.timedelta(minutes=1):
                    if datetime_now_get.minute==datetime_record_get.minute:
                        self.looplb2.move(465,685)#pgh
                        #self.looplb2.move(100,190)#adm
                                    
                if s_dict['station']=='行政樓':
                    #if diff>datetime.timedelta(minutes=1):
                    if datetime_now_get.minute>datetime_record_get.minute:
                    #looplb2.move(230,70)#pgh
                    #looplb2.move(100,190)#adm
                    #looplb2.move(240,350)#fst
                    #looplb2.move(150,150) #pgh and adm
                        self.looplb2.move(130,13)#adm and fst
                    #looplb2.move(400,200)#fst and pgh
                   #print('The bus is running between 行政樓 and FST')
                   #print('The bus is now at '+s_dict['station'])
                    
                   #if diff<=datetime.timedelta(minutes=1):
                    if datetime_now_get.minute==datetime_record_get.minute:
                        self.looplb2.move(195,13)#adm
                    
                if s_dict['station']=='FST':
                    #if diff>datetime.timedelta(minutes=1):
                    if datetime_now_get.minute>datetime_record_get.minute:
                    #looplb2.move(230,70)#pgh
                    #looplb2.move(100,190)#adm
                    #looplb2.move(240,350)#fst
                    #looplb2.move(150,150) #pgh and adm
                    #looplb2.move(150,250)#adm and fst
                        self.looplb2.move(75,495)#fst and pgh
                   #print('The bus is running between FST and 研究生宿舍')
                   #print('The bus is now at '+s_dict['station'])
                    #if diff<=datetime.timedelta(minutes=1):
                    if datetime_now_get.minute==datetime_record_get.minute:
                        self.looplb2.move(63,95)#fst
                    
            else:
                self.looplb2.move(270,200)
                #print('There is no information available!')

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

        
    def initUI(self):      
        
        
        
        v_main=QVBoxLayout()
        
        hbox = QHBoxLayout()
        
        
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)#click the date
        
        hbox.addWidget(cal)
        
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        
        self.hlabelbox=QHBoxLayout()
        
        self.lbl = QLabel(self)
        self.date = cal.selectedDate()
        self.lbl.setText(self.date.toString())
        
        self.jiaqi=QLabel(self)
        self.jiaqi.setText('*')
        
        self.shijian=QLabel(self)
        self.shijian.setText('*')
        
        self.hlabelbox.addWidget(self.lbl)
        self.hlabelbox.addWidget(self.jiaqi)
        self.hlabelbox.addWidget(self.shijian)
        #------
        self.busbut=QPushButton('Shuttle Bus Router')
        self.busbut.clicked.connect(self.bus_get)
       
        #------event show
        self.table_title=QTableWidget(self)
        self.table_title.setColumnCount(1)
        self.headers_title=['Title']
        self.table_title.setHorizontalHeaderLabels(self.headers_title)
        
        
        self.table_time=QTableWidget(self)
        self.table_time.setColumnCount(3)
        self.headers_time=['Time From','Time To','Location']
        self.table_time.setHorizontalHeaderLabels(self.headers_time)
       
        #self.table_title.resizeRowsToContents()
        #self.table_time.resizeRowsToContents()
        
        #-------
        vbox.addWidget(self.table_title)
        vbox.addWidget(self.table_time)
        vbox.addLayout(self.hlabelbox)
        #self.table_title.show()
        #self.table_time.show()
        vbox.addWidget(self.busbut)
        
        hbox.addLayout(vbox)
        
        
        v_main.addLayout(hbox)
        #----event title show
        self.table=QTableWidget(self)
        self.table.setColumnCount(5)
        self.headers=['Title','Organizer','Like','Score','Detail']
        self.table.setHorizontalHeaderLabels(self.headers)
        
        
        #-----
        
        v_main.addWidget(self.table)
        
        
        self.setLayout(v_main)
        
        self.setGeometry(30, 50, 800, 700)
        self.setWindowTitle('Calendar')
        
    def bus_get(self):
        shuttle.show()
   
     
    def showDate(self,date):     
        #-----show date-------
        self.lbl.setText(date.toString())
        #-----show holiday-------
        
        click_date=date.toString()
        date_d=datetime.datetime.strptime(click_date[3:len(click_date)],'%m月 %d %Y')#string to time
        start_d=date_d.date()
        start_s=str(start_d)
        
        url='https://api.data.umac.mo/service/aboutum/public_holidays/v1.0.0/all?format&date_from='+start_s+'&date_to='+start_s
        args={'Accept':'application/json','Authorization':'Bearer b96275c2-e0c7-3993-be76-25be9fdc8e9d'}
        r=requests.get(url,headers=args)
        r_dict=r.json()
        #print(len(r_dict))
        #print(r_dict)
        #noh=r_dict['_returned']
        if r_dict['_returned']==1:
           em=r_dict['_embedded']
           if em[0]['holiday']=='W':
              self.jiaqi.setText('Whole day is a public holiday')
           if em[0]['holiday']=='1':
              self.jiaqi.setText('Morning session is public holiday')
           if em[0]['holiday']=='2':
              self.jiaqi.setText('Afternoon session is public holiday')
        if r_dict['_returned']==0:
           self.jiaqi.setText('Not a holiday')
       #-----show events------
        url2='https://api.data.umac.mo/service/media/events/v1.0.0/all?date_from='+start_s+'&date_to='+start_s
        args2={'Accept':'application/json','Authorization':'Bearer b96275c2-e0c7-3993-be76-25be9fdc8e9d'}
        r2=requests.get(url2,headers=args2)
        r2_dict=r2.json()
        self.shijian.setText('There are '+str(r2_dict['_returned'])+' events')
        self.date=date
       #-----show events-----
        url3='https://api.data.umac.mo/service/media/events/v1.0.0/all?date_from='+start_s+'&date_to='+start_s
        args3={'Accept':'application/json','Authorization':'Bearer b96275c2-e0c7-3993-be76-25be9fdc8e9d'}
        r3=requests.get(url3,headers=args3)
        r3_dict=r3.json()
        self.noe=r3_dict['_returned']
        emb=r3_dict['_embedded']
        self.table.setRowCount(self.noe)
            
        for i in range(self.noe):
            event=emb[i]
            exec('self.iden_'+str(i)+'=event[\'_id\']')#identifier
            
            common=event['common']
            details=event['details'][0]#only used English Version
            
            exec('self.tp_'+str(i)+'=details[\'title\']')
            exec('self.zuzhizhe_'+str(i)+'=details[\'organizedBys\'][0]')
            
            #--------
            db=pymysql.connect('localhost','root','hellonihaoma','test')
            cursor=db.cursor()
            cursor.execute("SELECT * FROM test.Event_His where identify= %s",event['_id'])
            results=cursor.fetchall()
            heyhuan=results[0][1]
            fenshu=results[0][5]
            db.close()
            #-------------
            
            likelabel=QLabel()
            h2=QHBoxLayout()
            h2.setAlignment(Qt.AlignCenter)
            h2.addWidget(likelabel)
            w2 = QWidget()
            w2.setLayout(h2)
            likelabel.setText(str(heyhuan))
            
            scorelabel=QLabel()
            h = QHBoxLayout()
            h.setAlignment(Qt.AlignCenter)
            h.addWidget(scorelabel)
            w = QWidget()
            w.setLayout(h)
            scorelabel.setText(str(fenshu))
            
            detailbutton=QPushButton('Detail')
            detailbutton.setObjectName(str(i))
                #exec('like_'+str(i)+'=QPushButton(\'Like\')')
            h3=QHBoxLayout()
            h3.setAlignment(Qt.AlignCenter)
            h3.addWidget(detailbutton)
            #eval('h2.addWidget(like_'+str(i)+')')
            w3 = QWidget()
            w3.setLayout(h3)
            #self.num=i
            #print(self.num)
       
            detailbutton.clicked.connect(self.OpenLink)
        
            #------varible needed-----
            s1=common['dateFrom']
            s2=common['dateTo']
            s=s1+'to'+s2
            exec('self.datetime_'+str(i)+'=s')
            date_d1=datetime.datetime.strptime(s1,'%Y-%m-%dT%H:%M:%S+08:00')#string to time
            date_d2=datetime.datetime.strptime(s2,'%Y-%m-%dT%H:%M:%S+08:00')#string to time
            
            dian1=date_d1.date()
            dian2=date_d2.date()
            
            timming=str(dian1)+'to'+str(dian2)
            
            exec('self.time_'+str(i)+'=timming')#time
            exec('self.didian_'+str(i)+'=details[\'venues\'][0]')#location
            exec('self.person_'+str(i)+'=details[\'contactName\']')#person
            exec('self.dianhua_'+str(i)+'=details[\'contactPhone\']')#phone
            exec('self.email_'+str(i)+'=details[\'contactEmail\']')#email
            
            if 'posterUrl' in common.keys():
                    exec('self.lianjie_'+str(i)+'=common[\'posterUrl\']')#poster
            else:
                    exec('self.lianjie_'+str(i)+'=\'https://www.umac.mo/wp-content/uploads/2016/02/img-elements_of_the_university_identity-2.png\'')
                    
            if details['locale']=='en_US':
                    exec('self.yuyan_'+str(i)+'=\'English\'')#language
            if details['locale']=='zh_TW':
                    exec('self.yuyan_'+str(i)+'=\'Traditional Chinese\'')
                    
            if details['locale']=='pt_PT':
                    exec('self.yuyan_'+str(i)+'=\'Portuguese\'')
            
            #-------------------------
            
            

           
            eval('self.table.setItem(i,0,QTableWidgetItem(self.tp_'+str(i)+'))')
            eval('self.table.setItem(i,1,QTableWidgetItem(self.zuzhizhe_'+str(i)+'))')
            self.table.setCellWidget(i,3,w)
            self.table.setCellWidget(i,2,w2)
            self.table.setCellWidget(i,4,w3)
            
            self.table.setColumnWidth(0,425)
            self.table.setColumnWidth(1,150)
            self.table.setColumnWidth(2,50)
            self.table.setColumnWidth(3,50)
            self.table.setColumnWidth(4,60)
            
            self.table.resizeRowsToContents()
            

        #-----show ziji events-----
        db=pymysql.connect('localhost','root','hellonihaoma','test')
        cursor=db.cursor()
        sql="SELECT * FROM test.Event;"
        cursor.execute(sql)
        results=cursor.fetchall()
        db.close()
    
        count=0
        for j in range(len(results)):
            #2018-09-06T00:00:00+08:00to2018-10-31T00:00:00+08:00
            things=results[j]
            start_date_s=things[1][0:10]
            #print(start_date_s)
            end_date_s=things[1][27:37]
            #print(end_date_s)
            start_date=datetime.datetime.strptime(start_date_s,'%Y-%m-%d')#string to time
            end_date=datetime.datetime.strptime(end_date_s,'%Y-%m-%d')
            
            start_date_d=start_date.date()
           
            end_date_d=end_date.date()
           
            
          
            if start_d>=start_date_d and start_d<=end_date_d:
                count=count+1
                 

        hang=0
        self.table_time.setRowCount(count)
        self.table_title.setRowCount(count)
        for j in range(len(results)):
            #2018-09-06T00:00:00+08:00to2018-10-31T00:00:00+08:00
            things=results[j]
            start_date_s=things[1][0:10]
            #print(start_date_s)
            end_date_s=things[1][27:37]
            #print(end_date_s)
            start_date=datetime.datetime.strptime(start_date_s,'%Y-%m-%d')#string to time
            end_date=datetime.datetime.strptime(end_date_s,'%Y-%m-%d')
            
            start_date_d=start_date.date()
           
            end_date_d=end_date.date()
           
            
          
            if start_d>=start_date_d and start_d<=end_date_d:
                
                 #print(type(things[9]))
                 self.table_title.setItem(hang,0,QTableWidgetItem(things[9]))
                 self.table_time.setItem(hang,0,QTableWidgetItem(things[1][11:16]))
                 self.table_time.setItem(hang,1,QTableWidgetItem(things[1][38:43]))
                 self.table_time.setItem(hang,2,QTableWidgetItem(things[7]))
                 hang=hang+1
                 self.table_title.setColumnWidth(0,357)
                 self.table_time.setColumnWidth(2,223)
                 self.table_time.setColumnWidth(0,67)
                 self.table_time.setColumnWidth(1,67)
                 self.table_time.resizeRowsToContents()
                 self.table_title.resizeRowsToContents()
                 
                 
        
        
    def OpenLink(self):
        #ev=EventWin()
    
        print(ev.isVisible())
        if not ev.isVisible():
            sending_button = self.sender()
          
            num=int(sending_button.objectName())
            
            dateandtime=getattr(self,'datetime_%d'%num)
            time=getattr(self,'time_%d'%num)
            unit=getattr(self,'zuzhizhe_%d'%num)
            lang=getattr(self,'yuyan_%d'%num)
            url=getattr(self,'lianjie_%d'%num)
            phone=getattr(self,'dianhua_%d'%num)
            location=getattr(self,'didian_%d'%num)
            ren=getattr(self,'person_%d'%num)
            #print(location)
            identify=getattr(self,'iden_%d'%num)
            timu=getattr(self,'tp_%d'%num)
            email=getattr(self,'email_%d'%num)
            
            ev.timeshow.setText(time)
            
            ev.locshow.setText(location)
            ev.unitshow.setText(unit)
            ev.lanshow.setText(lang)
            ev.emshow.setText(email)
            ev.phshow.setText(phone)
            ev.titlelabel.setText(timu)
            
            #ev.img_src=url
            ev.iden=identify
            #--------
            db=pymysql.connect('localhost','root','hellonihaoma','test')
            cursor=db.cursor()
            cursor.execute("SELECT * FROM test.Event_His where identify= %s",identify)
            results=cursor.fetchall()
            xihuan=results[0][1]
            xuanze=results[0][4]
            cm=results[0][3]
            db.close()
            #----------
            ev.likeshow.setText(str(xihuan)+' likes')
            ev.selshow.setText(str(xuanze)+' selects')
            ev.cmlabel.setText(cm)
            #---------
            req = requests.get(url)
            photo = QPixmap()
            photo.loadFromData(req.content)
            repict=photo.scaled(600,600,aspectRatioMode=Qt.KeepAspectRatio)
            ev.imagelb.setPixmap(repict)
            #--------
            ev.time_t=dateandtime
            ev.unit_t=unit
            ev.lang_t=lang
            ev.phone_t=phone
            ev.person_t=ren
            ev.location_t=location
            ev.identify_t=identify
            ev.timu_t=timu
            ev.url_t=url
            #--------
            ev.show()
            print('show')
            
            
class EventWin(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

        
    def initUI(self):
        #--------
        self.time_t=''
        self.unit_t=''
        self.lang_t=''
        self.phone_t=''
        self.person_t=''
        self.location_t=''
        self.identify_t=''
        self.timu_t=''
        self.url_t=''

        #-------
        self.iden=0
        
        img_src='http://news.umac.mo/nrs/binary?id=47_2Bhlt_2BMKhTj_2BRSk8eSovvEOk2XBwZ2BpGKyx_2Bb2f8w_3D'
        
       
        req = requests.get(img_src)
        photo = QPixmap()
    #photo.loadFromData(req.content, "JPG")
        photo.loadFromData(req.content)
     

        repict=photo.scaled(600,600,aspectRatioMode=Qt.KeepAspectRatio)
        
        self.imagelb=QLabel(self)
        self.imagelb.setPixmap(repict)
        
        
        #-----------
        self.titlelayout=QVBoxLayout()
        
        self.titlelabel=QLabel()
        
        self.titlelayout.addWidget(self.titlelabel)
        
        
        
        self.timelabel=QLabel('Date:')
        self.timeshow=QLabel()
        
        self.loclabel=QLabel('Location:')
        self.locshow=QLabel()
        
        self.unitlabel=QLabel('Organizer:')
        self.unitshow=QLabel()
        
        self.lanlabel=QLabel('Language:')
        self.lanshow=QLabel()
        
        self.emlabel=QLabel('E-Mail:')
        self.emshow=QLabel()
        
        self.phlabel=QLabel('Phone No.:')
        self.phshow=QLabel()
        
        #self.likelabel=QLabel('Like')
        self.likeshow=QLabel()
        self.likebut=QPushButton('Like')
        self.likebut.clicked.connect(self.like_get)
        #self.sellabel=QLabel('Select')
        self.selshow=QLabel()
        self.selbut=QPushButton('Select')
        self.selbut.clicked.connect(self.select_get)
        
        
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        
        self.grid.addWidget(self.timelabel, 1, 0)
        self.grid.addWidget(self.timeshow, 1, 1)
        self.grid.addWidget(self.loclabel, 1, 2)
        self.grid.addWidget(self.locshow, 1, 3)
        
        self.grid.addWidget(self.unitlabel, 2, 0)
        self.grid.addWidget(self.unitshow, 2, 1)
        self.grid.addWidget(self.lanlabel, 2, 2)
        self.grid.addWidget(self.lanshow, 2, 3)
        
        self.grid.addWidget(self.emlabel, 3, 0)
        self.grid.addWidget(self.emshow, 3, 1)
        self.grid.addWidget(self.phlabel, 3, 2)
        self.grid.addWidget(self.phshow, 3, 3)
        
        self.grid.addWidget(self.likebut, 4, 0)
        self.grid.addWidget(self.selbut, 4, 2)
        self.grid.addWidget(self.likeshow, 4, 1)
        self.grid.addWidget(self.selshow, 4,3)
        
        
        self.titlelayout.addLayout(self.grid)
        
        #-----------------

        
        
        self.eventlayout=QHBoxLayout()
        self.eventlayout.addWidget(self.imagelb)
        self.eventlayout.addLayout(self.titlelayout)
        
        self.mainlayout=QVBoxLayout()
        self.mainlayout.addLayout(self.eventlayout)
        
        #-------------
        self.grid2=QGridLayout()
        
        pingfen = QLabel('Score')
        remark = QLabel('Comments')

        self.pingfenEdit = QLineEdit()
        self.remarkEdit = QTextEdit()

       

        self.grid2.addWidget(pingfen, 1, 0)
        self.grid2.addWidget(self.pingfenEdit, 1, 1)

        self.grid2.addWidget(remark, 2, 0)
        self.grid2.addWidget(self.remarkEdit, 2, 1, 3, 1)
        
        okButton = QPushButton("submit")
        okButton.clicked.connect(self.ok_get)
        self.grid2.addWidget(okButton,4,0)
        #-------------
        self.mainlayout.addLayout(self.grid2)
        #--------------------
        self.cmlabel=QLabel()
        #----------------
        self.mainlayout.addWidget(self.cmlabel)
        self.setLayout(self.mainlayout)
        self.setGeometry(80, 100,550, 1200)
        self.setWindowTitle('Event')
        
    def like_get(self):
        db=pymysql.connect('localhost','root','hellonihaoma','test')
        cursor=db.cursor()
        cursor.execute("SELECT * FROM test.Event_His where identify= %s",self.iden)
        results=cursor.fetchall()
        xihuan=results[0][1]
        xihuan=xihuan+1
        #UPDATE `test`.`Event_His` SET `like` = '1' WHERE (`id` = '1');
        cursor.execute("UPDATE test.Event_His SET `like` = %s WHERE identify = %s",(xihuan,self.iden))
        db.commit()
        db.close()
        self.likeshow.setText(str(xihuan)+' likes')
        
    def select_get(self):
        db=pymysql.connect('localhost','root','hellonihaoma','test')
        cursor=db.cursor()
        cursor.execute("SELECT * FROM test.Event_His where identify= %s",self.iden)
        results=cursor.fetchall()
        xuanze=results[0][4]
        xuanze=xuanze+1
        #UPDATE `test`.`Event_His` SET `like` = '1' WHERE (`id` = '1');
        cursor.execute("UPDATE test.Event_His SET `select` = %s WHERE identify = %s",(xuanze,self.iden))
        db.commit()
        db.close()
        self.selshow.setText(str(xuanze)+' selects')
        
        
        #-------
        
        db=pymysql.connect('localhost','root','hellonihaoma','test')
        cursor=db.cursor()
        sql_insert="insert into test.Event(time,unit,lang,url,phone,person,location,iden,title) values(%s,%s," \
                "%s,%s,%s,%s,%s,%s,%s)"
            
        cursor.execute(sql_insert,(self.time_t,self.unit_t,self.lang_t,self.url_t,self.phone_t,self.person_t,self.location_t,self.identify_t,self.timu_t))
        db.commit()
        db.close()   

        
        
        
        
    def ok_get(self):
        
        db=pymysql.connect('localhost','root','hellonihaoma','test')
        cursor=db.cursor()
        pf=self.pingfenEdit.text()
        liuyan=self.remarkEdit.toPlainText()
        cursor.execute("UPDATE test.Event_His SET `score` = %s,comments=%s WHERE identify = %s",(pf,liuyan,self.iden))
        db.commit()
        db.close()
     

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    shuttle=Bus()
    ex=Example()
    ev=EventWin()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #ex.show()    
    
    sys.exit(app.exec_())
