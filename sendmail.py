import  smtplib
#these function takes two argument server name and port address
server=smtplib.SMTP('smtp.gmail.com',587)
#verifying to start tls
server.starttls()
#takes 2 argument email and password
server.login('example@gmail.com','PASSWORD')
#takes 3 argument email id from which mail is sent to destinated email with messages 
server.sendmail('example@gmail.com','example@yahoo.com','hi man')
##try to look at spam folder