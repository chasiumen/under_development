#!/usr/bin/python
#DNS differ

import argparse, sys, os, smtplib, base64
from email.mime.text import MIMEText
from email.mime.multi import MIMEMultipart

#-----------------------ARGUMENT PARSE---------------------
parser = argparse.ArgumentParser(description='DNS-DIFFER')
parser.add_argument('-v', metavar='--verbose', nargs='?', action='store', help='increase output verbosity')
args = parser.parse_args()


#--------------------VARIABLES------------------------------
##list of dns servers
#dhcp_servers = ['128.103.200.99', '128.103.1.7', '140.247.233.163', '140.247.233.194']

##date
d = datetime.datetime.today()
date = d.strftime("%m/%d/%Y %H:%M:%S")

####### Scripts #######
tar='/bin/tar'


####### Directory ######
git='~/temp/dns_backup/'


####### infoblox ######
#api_user = 'api'
#api_pass = 'api321'
#api_host = '128.103.200.3'
api_user = 'morinor'
p_hash = 'HASH'
api_pass = base64.b64decode(p_hash)
api_host = '128.103.200.106'

####### github #######
git_host = 'https://git.noc.harvard.edu/api/v3/'
git_user =''
gp_hash = 'HASH'
git_pass = base64.b64decode(gp_hash)


#######  SMTP  #######
smtpserver = 'netop3.harvard.edu'
subj_prefix = 'DHCP-DIFFER'
#from_addr = 'root@ibbff.noc.harvard.edu'
#to_addr = 'DHCP-DIFFER@noc.harvard.edu'
from_addr = 'root@ibbff.noc.harvard.edu'
to_addr = 'rymorino@gmail.com'


###### github #######
git_host = 'https://git.noc.harvard.edu/api/v3/'
git_user =''
gp_hash = 'HASH'
git_pass = base64.b64decode(gp_hash)


#######  SMTP  #######
smtpserver = 'netop3.harvard.edu'
subj_prefix = 'DHCP-DIFFER'
#from_addr = 'root@ibbff.noc.harvard.edu'
#to_addr = 'DHCP-DIFFER@noc.harvard.edu'
from_addr = 'root@ibbff.noc.harvard.edu'
to_addr = 'rymorino@gmail.com'



#---------------------FUNCTION-----------------------
#SEND MAIL
def mailer(from_addr, to_addr, subject, text) :
#create message container
    msg = MIMEMultipart()
    msg['Subject'] = subject

    #mail content
    #text = "Hello World! from SMTP\n This is a script test\n"
    txt = MIMEText(text, 'plain')

    #attach contents to a mail
    msg.attach(txt)

    #send mail
    try:
        server = smtplib.SMTP(smtpserver, timeout=5)
        server.ehlo()
        server.starttls()
#       server.sendmail(from_addr, to_addr, msg.as_string())
    except smtplib.SMTPException:
        print "Error! Unable to send mail"
    server.quit
    print "sent mail"

