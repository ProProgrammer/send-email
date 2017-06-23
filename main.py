"""
A quick handy script that allows you to send email by specifying email address as command line arguments as follows:
python manage.py -e email1 -e email2....

Note: Please update smtp server address and port number if you are using non google apps email account
"""


import smtplib
import argparse
import os
from config import SUBJECT, MESSAGE


parser = argparse.ArgumentParser()
parser.add_argument('-e', action='append', dest='collection', default=[], help='Add repeated values to a list',)
args = parser.parse_args()

gmail_user = os.environ['SPB_EMAIL']
gmail_pwd = os.environ['SPB_APP_PWD']

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(gmail_user, gmail_pwd)

to_email = ', '.join(args.collection)

MESSAGE_FORMAT = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (gmail_user, to_email, SUBJECT, MESSAGE)
print MESSAGE_FORMAT
server.sendmail(gmail_user, to_email, MESSAGE_FORMAT)

server.close()
