
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
from os import system
  
class colors:
	OKGREEN = '\033[92m'
        BLUE = '\033[94m'


system('clear')
  

msg = MIMEMultipart()

print colors.BLUE + 'To send an email you must have less secure apps enabled in your account \nhttps://myaccount.google.com/lesssecureapps'
 
 
msg['From'] = raw_input (colors.OKGREEN + '\nYour Email: ')  
user = msg['From']
passwd = getpass.getpass(colors.OKGREEN + 'Password: ') 

 
msg['To'] = raw_input (colors.OKGREEN + 'To: ')
to = msg['TO']
 


subject = raw_input (colors.OKGREEN + 'Subject: ')
 

body = raw_input (colors.OKGREEN + 'Message: ') 

message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body


msg.attach(MIMEText(message, 'plain'))

 
 

filename = raw_input (colors.OKGREEN + 'Name of file with extension: ')
try:
		
		path = 'attachments/' + filename
                attachment = open(path, "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 		msg.attach(p)
		

except:
                
		print 'The email will be sent without any attachments'
                
	



 

 

s = smtplib.SMTP('smtp.gmail.com', 587)
 

s.starttls()
 

s.login(user, passwd)
 

text = msg.as_string()


 
# sending the mail
s.sendmail(user, to, text)
print 'Email sent'
 

s.quit()
