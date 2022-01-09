import smtplib

from email.mime.multipart import MIMEMultipart

from constants import MAIL_constant

# variables
smtp_address =      MAIL_constant.post_in_server
smtp_port =         MAIL_constant.port
sender_address =    MAIL_constant.mail_user_in
password =          MAIL_constant.MAIL_ACCOUNT_PW

# function to send the actual message
def summary_mail(recipient_name, summary, recipient_address):

    subject = 'Coaching Bot | Confirmation - sign up complete'

    summary_message =   f"""Hi {recipient_name}, thanks for signing up. This is the confirmation for your sign up with the coaching program by wavehoover. \n\n'
        Cheers,\nYour wavehoover Team"""

    server = smtplib.SMTP_SSL(smtp_address, smtp_port)
    # server.starttls()
    # server.ehlo() # not sure, what this does
    server.login(sender_address, password)

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = recipient_address
    message['Subject'] = subject

    server.sendmail(message['From'], message['To'], message.as_string())
    server.quit()


# if __name__ == '__main__':
#     summary_mail('Subject: Automated e-mail', 'my_test_email@test.com', 'Automated email from the coaching Bot by wavehoover.')