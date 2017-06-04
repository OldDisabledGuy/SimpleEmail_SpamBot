# SimpleEmailSpamBot
# DizAzTor

import smtplib
import getpass

x = 0
print "\nLog in with your gmail account. Make sure to enable \"less secure apps\""
print "\nGoogle it if you don't know what it is."
gmail_account = raw_input("\n>>>: ")

print "\nNow type in your password."
gmail_password = getpass.getpass("\n>>>: ")

print "\nWho do you want to spam this message to?"
spam_to = raw_input("\n>>>: ")

print "\nType in your subject."
spam_subject = raw_input("\n>>>: ")

print "\nFinally, uh, type in your message."
spam_message = raw_input("\n>>>: ")

print "\nALWAYS REMEMBER TO HIT CTRL-C TO STOP THE SPAM."

print "\nI will start spamming now. "

import smtplib
fromaddr = '%s' % gmail_account
toaddrs = '%s' % spam_to
msg = "\r\n".join([
    "From: %s",
    "To: %s",
    "Subject: %s",
    "",
    "%s"
]) % (gmail_account, spam_to, spam_subject, spam_message)
username = '%s' % gmail_account
password = '%s' % gmail_password
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username, password)

while True:
    server.sendmail(fromaddr, toaddrs, msg)
    x += 1
    print "\nMail sent. Mail number: %d" % x
