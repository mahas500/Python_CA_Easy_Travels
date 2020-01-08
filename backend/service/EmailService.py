import smtplib
import ssl


class EmailService:
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "saurabh.devade21@gmail.com"
    password = 'Saurabh@1995'
    context = ssl.create_default_context()
    Subject = "Easy Travels Forgot Password OTP"

    @classmethod
    def sendEmail(cls, receiver_email, message):
        try:
            print(message, receiver_email, cls.Subject)
            with smtplib.SMTP(cls.smtp_server, cls.port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=cls.context)
                server.ehlo()  # Can be omitted
                server.login(cls.sender_email, cls.password)
                server.sendmail(cls.sender_email, receiver_email, message)
            return True
        except Exception as e:
            print(e)
            return False
