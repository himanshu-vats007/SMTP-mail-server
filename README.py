import smtplib

sender_email = "xyz@gmail.com"
sender_passwd = "fgkjhhjvkhlkhhjk"
reciver_email = "xyz@gmail.com"
subject = "hello"


s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login(sender_email,sender_passwd)
s.sendmail(sender_email,reciver_email,subject)
s.quit()
