from imap_tools import MailBox
import util

# TODO: replace with your email address
imap_server = "imap.gmail.com"
sender_email = "Enter email here"
password = 'Passwod here'


def getCode():
    settings = util.get_settings()
    emailCreds = settings['emailCredentials']
    email = emailCreds["email"].strip()
    password = emailCreds["appPassword"].strip()
    print(email)
    with MailBox(imap_server).login(email, password, 'INBOX') as mailbox:
        for msg in mailbox.fetch(limit=1, reverse=True):
            return msg.subject[-6:]
