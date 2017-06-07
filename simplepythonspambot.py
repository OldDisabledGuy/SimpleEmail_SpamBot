# SimpleEmailSpamBot
# DizAzTor
# Version: 0.3


import smtplib
import getpass
import time

email_number = 0
email_delay = 0

print "\nLog in with your GMAIL account."
print "\nMake sure to enable \"less secure apps\""
print "\nTurn it on: https://myaccount.google.com/lesssecureapps"
print "\nNo need to add \"@gmail.com\", just type in your username."
gmail_account = raw_input("\n>>>: ")

if "@gmail.com" in gmail_account:
    pass
else:
    gmail_account = gmail_account + "@gmail.com"

print "\nNow type in your password."
gmail_password = getpass.getpass("\n>>>: ")

print "\nLook, since i'm using Google SMTP..."
print "\n...you're \"only\" allowed to send 2,000 emails a day per GMAIL account."
print "\nI'll later give you the option to even add more GMAL accounts."
print "\nUse them when an account dies. KEEP SPAMMING!"
print "\n... maybe."

print "\nBut for now, just type in your target's email address."
spam_to = raw_input("\n>>>: ")

print "\nType in your subject."
spam_subject = raw_input("\n>>>: ")

print "\nFinally, uh, type in your message."
spam_message = raw_input("\n>>>: ")


print "\nALWAYS REMEMBER TO HIT CTRL-C TO STOP THE SPAM."
print "\nIt is really recommended to have a delay between every email."
print "\nOtherwise the script will stop running at the 85th email or something."
print "\nGoogle will start realizing it's a spam."
print "\nWant to set a delay?"

just_a_loop = True
while just_a_loop:
    print "\n 1. YES | 2. NO"

    what = raw_input("\n>>>: ")

    if what == "1" or what == "yes":
        print "\nAlright. Set a delay then."
        print "\nRecommended: 2 (2 seconds delay between every email)."
        print "\n ONLY ACCEPTS INTEGERS."

        email_delay = int(raw_input("\n>>>: "))
        print "\nDELAY SET TO %d." % email_delay
        just_a_loop = False
        break

    elif what == "2" or what == "no":
        print "\nAlright then. Delay set to %d" % email_delay
        just_a_loop = False
        break

    else:
        print "\nI don't really understand what you're trying to do."


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
    email_number += 1
    print "\nMAIL SENT. #%d" % email_number
    time.sleep(email_delay)
