#
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage

#if len(sys.argv) != 2:
#    print "usage: %prog <pic.jpg>".replace("%prog", sys.argv[0])
#    sys.exit(1)

#fname = sys.argv[1]

usr = "tor@platypus.com"
pwd = "PlueF1zz"

smtp_srv = "mail.platypus.com"
smtp_prt = 26

msg = MIMEMultipart()
msg['From'] = usr
msg['To'] = usr
msg['Subject'] = 'test email'
msg.preamble = 'real test\n'

#fp = open(fname,'rb')
#img = MIMEImage(fp.read(), "jpeg")
#fp.close()
#msg.attach(img)

smtpObj = smtplib.SMTP(smtp_srv, smtp_prt)
#smtpObj.ehlo()
#smtpObj.starttls()
smtpObj.login(usr,pwd)
smtpObj.sendmail(usr, usr, msg.as_string())
smtpObj.quit()
