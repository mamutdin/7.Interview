import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class E_mail:
    def __init__(self, login: str, password: str):
        self.gmail_smtp = 'smtp.gmail.com'
        self.gmail_imap = 'imap.gmail.com'
        self.login = login
        self.password = password

    def send_msg(self, subject: str, message: str, recipients: list):
        mail_text = MIMEMultipart()
        mail_text['From'] = self.login
        mail_text['To'] = ', '.join(recipients)
        mail_text['Subject'] = subject
        mail_text.attach(MIMEText(message))
        send_connection = smtplib.SMTP(self.gmail_smtp, 587)
        send_connection.ehlo()
        send_connection.starttls()
        send_connection.ehlo()
        send_connection.login(self.login, self.password)
        send_connection.sendmail(self.login, recipients, mail_text.as_string())
        send_connection.quit()

    def receive_msg(self, header=None):
        receive_connection = imaplib.IMAP4_SSL(self.gmail_imap)
        receive_connection.login(self.login, self.password)
        receive_connection.list()
        receive_connection.select('inbox')
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = receive_connection.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = receive_connection.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        receive_connection.logout()
        return email_message


if __name__ == '__main__':
    login_mail = 'login@gmail.com'
    password = 'qwerty'
    topic = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    text = 'Message'

    email = E_mail(login_mail, password)
    email.send_msg(topic, text, recipients)
    print(email.receive_msg())
