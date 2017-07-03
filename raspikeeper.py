#!/bin/python

import smtplib
from urllib2 import urlopen
from email.mime.text import MIMEText
from email.header import Header

#you need to update the following value.
mail_user=""
mail_passwd=""

if mail_user == "" or mail_passwd == "":
    print "Please modify this script with your mail account. Currently, support 126 mail.\n"
    exit()

def getlastip():
    try:
        lf=open('ipfile','r+')
    except:
        print "can't get the last ip, local file would be create again"
        return 'ERROR'
    lip = lf.read().strip()
    lf.close()
    return lip

def getexip():
    return urlopen('http://1212.ip138.com/ic.asp').read()

def setlastip(ip):
    try:
        lf=open('ipfile','w')
        lf.write(ip)
        lf.flush()
        lf.close()
    except:
        return 1
    return 0

class mailhandler:
    sender = mail_user
    receivers = ['bolo809@126.com']
    mail_host = 'smtp.126.com'
    mail_pass = mail_passwd
    
    def sendmail(self,message):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender,self.receivers,message)
        except smtplib.SMTPException:
            print "Can't connect mail host and login."
            return 110
        return 0

if __name__ == '__main__':
    print "START"
    
    exip=getexip()
    if getlastip() in exip:
        print "External IP is not changed yet."
        exit(666)
    setlastip(exip[exip.index('[')+1:exip.index(']')])
    
    #send exip.
    message = MIMEText(exip, 'plain', 'utf-8')
    message['From'] = Header("RaspiKeeper", 'utf-8')
    message['To'] = Header("Test", 'utf-8')

    subject = 'Raspi external IP report'
    message['Subject'] = Header(subject, 'utf-8')
    
    mail=mailhandler()
    mail.sendmail(message.as_string())
    
    print "Done"
