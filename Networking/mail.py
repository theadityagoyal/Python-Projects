import smtplib
from email.mime.text import MIMEText

#body text for our mail
body='''This is my text mail. This is sent to you from my Python Program'''

#create MIMEText class object with body text
msg=MIMEText(body)

#from which address the mail is sent
fromaddr="goyallala02@gmail.com"

#to which address the mail is sent
toaddr="madhavvyasit@gmail.com"

#store the addresses into msg object
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']="Hello this is me"

#connect to gmail.com server using 587 port number
server=smtplib.SMTP('smtp.gmail.com',587)

#put the smtp connection in TLS mode
server.starttls()

#login to your server with your correct password
server.login(fromaddr,"Aditya1234@")
#send the message to the server
server.send_message(msg)
print('mail sent...')

#close connection
server.quit()
