import smtplib

fromaddr = 'dilipkumarvignesh.py@gmail.com'
toaddrs  = 'dilipkumarvignesh@gmail.com'

subject=""
body=""
msg = "\r\n".join([
  subject,body
  ])

print(msg)
# Credentials (if needed)
username = 'dilipkumarvignesh.py'
password = 'saibaba_047'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
