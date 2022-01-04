import smtplib
from constants import MAIL_ACCOUNT_PW

# variables
smtp_address = 'smtp.www19.servertown.ch'
smtp_port = 465
user_name = 'coaching@wavehoover.com'
password = MAIL_ACCOUNT_PW

summary_message = 'Hi ..., thanks for signing up. This is your confirmation.'

# function to send the actual message
def summary_mail(address):
    server = smtplib.SMTP_SSL(smtp_address, smtp_port)
    server.login(user_name, password)
    server.sendmail(user_name, address, summary_message)
    server.quit()