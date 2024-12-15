import getpass
import imaplib
import pprint
'''
getpass: Used to securely prompt the user for their password without echoing it to the console.
imaplib: Provides functions for interacting with an IMAP server (protocol used for email retrieval).
pprint: Used for printing data structures (emails) in a more readable format.
'''

GOOGLE_IMAP_SERVER = 'imap.googlemail.com' #address of the Gmail IMAP server
IMAP_SERVER_PORT = 993 #standard IMAP port number


def check_email(username, password):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, IMAP_SERVER_PORT)
    mailbox.login(username, password)
    mailbox.select('Inbox')
    tmp, data = mailbox.search(None,'ALL')
    for num in data[0].split():
        # Specifies retrieval in RFC 822 format, the standard format for email messages.
        tmp, data = mailbox.fetch(num,'(RFC822)')
        
        print('Email: {0}\n'.format(num))
        pprint.pprint(data[0][1])
    mailbox.close()
    mailbox.logout()
    
if __name__=='__main__':
    username = input("enter email account: ")
    print("password: ")
    password = getpass.getpass(prompt="enter password: ")
    check_email(username, password)