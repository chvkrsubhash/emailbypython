import smtplib
def send_email(to,subject,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("youremail","password")
    server.sendmail("youremail",to,f"Subject:{subject}\n\n\nMessage:{message}")
    server.quit()
email = input("Enter sender email:")
subject = input("Enter Subject:")
message = input("Enter Message:")
send_email(email,subject,message)
