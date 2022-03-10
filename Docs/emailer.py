import smtplib
import cgi
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
form = cgi.FieldStorage()

sendaddr = str(form.getvalue("Email"))
bodiee = str(form.getvalue("Message"))
subj = form.getvalue("Subject")
name = str(form.getvalue("Name"))

fromaddr = 'robhausbot@gmail.com'
toaddr = 'goodeve@rob.haus'
msg = MIMEMultipart()
msg['From'] = str(fromaddr)
msg['To'] = str(toaddr)
msg['Subject'] = str(subj)

body = " my name is " + name + " my email is " + sendaddr + " message:" + bodiee
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('robhausbot@gmail.com', "secret")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
