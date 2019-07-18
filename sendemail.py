import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("pankaj.ias543@gmail.com", "7310522075")

# message to be sent
message = "Message from pankaj saini"

# sending the mail
s.sendmail("pankaj.ias543@gmail.com", "armangupta0504@gmail.com", message)

# terminating the session
s.quit()
