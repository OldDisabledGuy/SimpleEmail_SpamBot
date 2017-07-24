__version__ = "0.4" # ENGINE

try:
    import time
    import smtplib
    import sys
    from sys import exit
    import os
    import ConfigParser
    import io

except ImportError, err:
    print "Sorry, %s." % err

config = ConfigParser.RawConfigParser()
path = "config.cfg"
config.read(path)

account = config.get("account", "email")
password = config.get("account", "password")

spam_delay = config.get("spamfo", "delay")
spam_subject = config.get("spamfo", "subject")
spam_message = config.get("spamfo", "message")

tragets = []
targets = config.get("targets", "targets")
targets = targets.split(", ")

_all = [account, password, spam_delay, spam_subject, spam_message]

class Engine():

    def __init__(self):
        pass

    def check(self):
        if account != "" and password != "" and spam_delay != "" and spam_subject != "" and spam_message != "" and len(targets) != 0:
            if "@gmail.com" in account:
                return "1"
            elif "@outlook.com" in account:
                return "2"
            elif "@icloud.com" in account:
                return "3"
            else:
                return "x"
        else:
            print "y"

    def thespam(self):
        msg = "\r\n".join([
            "From: %s",
            "To: %s",
            "Subject: %s",
            "",
            "%s"
        ]) % (account, targets, spam_subject, spam_message)

        if self.check() == "1":
            server = smtplib.SMTP("smtp.gmail.com:587")

        elif self.check() == "2":
            server = smtplib.SMTP("smtp-mail.outlook.com:587")

        elif self.check() == "3":
            server = smtplib.SMTP("smtp.mail.me.com:587")

        elif self.check() == "x":
            print "Unsupported email."
            exit(0)

        elif self.check == "y":
            print "Something's wrong. Check your config.cfg maybe?"
            exit(0)

        else:
            print "I don't know. Try again."
            exit(0)

        server.ehlo()
        server.starttls()
        try:
            server.login(account, password)
        except smtplib.SMTPAuthenticationError:
            print "Wrong password or email."
            exit(0)
        email_number = 0
        while True:
            server.sendmail(account, targets, msg)
            email_number += 1
            print "\nMail Sent #%d" % email_number
            time.sleep(float(spam_delay))

if sys.argv[0] != "SESB0.5.py" or sys.argv[0] == "engine.py":
    print "Please use the SESB0.5.py script"
    exit(0)
else:
    pass
