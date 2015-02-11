import smtplib

fromname = 'CSJ'

fromaddr = 'christophe.s.james@gmail.com'

toname = 'CJames'

toaddr = 'christophe_jms@yahoo.com'

subject = 'initial message'

msg = 'my message'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""

messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'christophe.s.james@gmail.com'

password = 'hbxibgcbudhtkumc'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()