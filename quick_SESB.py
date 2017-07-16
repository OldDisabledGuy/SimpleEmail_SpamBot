# 0.3, Rewritten

"""SimpleEmail_SpamBot or SESB is a script that lets you spam people using Gmail, Outlook or/and iCloud"""

__author__ = "DizAzTor"
__copyright__ = "Copyright 2017, SimpleEmail_SpamBot, DizAzTor"

__license__ = "CC"
__version__ = "0.2"
__maintainer__ = "DizAzTor"

try:
    import smtplib
    import getpass
    import time
    import sys
    import os
    from sys import exit
    import ConfigParser
    import io

except ImportError, err:
    print "%s." % err
    print "Exiting..."
    exit(0)


email_number = 0
spam_delay = 0
spam_subject = ""
spam_message = ""
# stop_at = 0 (I will add this later)

account = ""

password = ""

chosen = ""

targets = []
settings_targets = ""
target_number = 0


class Help(object):

    def __init__(self):
        pass

    def gmail(self):
        print "\nLog in with your GMail account."
        print "\nMake sure to enable \"less secure apps\""
        print "\nEnable it: https://myaccount.google.com/lesssecureapps"

    def outlook(self):
        print "\nLog in with your OUTLOOK account."
        print "\nMake sure to enable \"POP and IMAP\""
        print "\nEnable it: https://outlook.live.com/owa/?path=/options/popandimap"

    def icloud(self):
        print "\nLog in with your ICLOUD account."
        print "\nMake sure to use \"app specific password\""
        print "\nPlease read: https://support.apple.com/en-us/HT204397"
        print "\nIt should give you enough information on using an app-specific password"


class SpamMailInfo(object):

    def __init__(self):
        pass

    def set_subject(self):

        global spam_subject

        spam_subject = raw_input("\nSubject>>> ")

    def set_message(self):

        global spam_message

        spam_subject = raw_input("\nMessage>>> ")


class Engine(object):

    # SESB ENGINE (0.3)
    # ENGINE USED IN SESB.py = 0.2

    def __init__(self):
        pass

    def account(self):

        fromaddr = "%s" % account
        msg = "\r\n".join([
            "From: %s",
            "To: %s",
            "Subject: %s",
            "",
            "%s"
        ]) % (account, targets, spam_subject, spam_message)

        username = "%s" % account
        engine_password = "%s" % password

        if chosen == "1" or chosen == "GMAIL":
            server = smtplib.SMTP("smtp.gmail.com:587")

        elif chosen == "2" or chosen == "OUTLOOK":
            server = smtplib.SMTP("smtp-mail.outlook.com:587")

        elif chosen == "3" or chosen == "ICLOUD":
            server = smtplib.SMTP("smtp.mail.me.com:587")

        else:
            print "Unsupported email."

        server.ehlo()
        server.starttls()
        server.login(username, engine_password)

        while True:
            server.sendmail(fromaddr, targets, msg)
            global email_number
            email_number += 1
            print "\nMail sent. #%s" % email_number
            time.sleep(float(spam_delay))


class Targets(object):

    def __init__(self):
        pass

    def targets(self):
        global target_number
        global targets
        target_status = ", ".join(targets)
        target_number += 1
        while True:
            a_new_target = raw_input("\nTarget %s>>> " % target_number)

            if "@" in a_new_target:
                target_number += 1
                targets.append(a_new_target)

            elif a_new_target == "":

                start_engine = Engine()
                start_engine.account()


class Account(object):

    def __init__(self):
        print "DELAY SET TO %d" % spam_delay

    def get_account(self):
        global account
        global password
        help_maybe = Help()
        mailinfo = SpamMailInfo()

        if chosen == "GMAIL":

            help_maybe.gmail()

            account = raw_input("\n%s>>> " % chosen)

            if "@gmail.com" in account:
                pass

            else:
                account += "@gmail.com"

            password = getpass.getpass("\nPASSWORD>>> ")
            mailinfo.set_subject()
            mailinfo.set_message()

            add_targetsX = Targets()
            add_targetsX.targets()

        elif chosen == "OUTLOOK":

            help_maybe.outlook()

            account = raw_input("\n%s>>> " % chosen)

            if "@outlook.com" in account:
                pass

            else:
                account += "outlook.com"

            password = getpass.getpass("\nPASSWORD>>> ")
            mailinfo.set_subject()
            mailinfo.set_message()

            add_targetsX = Targets()
            add_targetsX.targets()

        elif chosen == "ICLOUD":

            help_maybe.icloud()

            account = raw_input("\n%s>>> " % chosen)

            if "@icloud.com" in account:
                pass

            else:
                account += "@icloud.com"

            password = getpass.getpass("\nPASSWORD>>> ")
            mailinfo.set_subject()
            mailinfo.set_message()

            add_targetsX = Targets()
            add_targetsX.targets()

        else:
            print "\nSomething happened. Something happened."


class Email(object):

    def __init__(self):
        pass

    def email(self):
        pass

custom_error = """That's not really how it works.
   * Usage of this script:
   0. python SESB_quick.py -d x y
   1. -d is for delay
   2. x is used to set the delay
   3. y is used to specifiy an email provider

   * Or you can just use settings.cfg (please do)
   0. python quick_SESB.py"""

try:

    if len(sys.argv) == 4 and sys.argv[1] == "-d":

        try:
            spam_delay = int(sys.argv[2])

        except ValueError:
            print "That's not really an integer."

        else:
            spam_delay = int(sys.argv[2])
            account_heh = Account()
            if sys.argv[3] == "1":
                chosen = "GMAIL"
                account_heh.get_account()

            elif sys.argv[3] == "2":
                chosen = "OUTLOOK"
                account_heh.get_account()

            elif sys.argv[3] == "3":
                chosen = "ICLOUD"
                account_heh.get_account()

            else:
                print "\nYou can only chooose between 1, 2 and 3."
                print "\n1. GMAIL"
                print "\n2. OUTLOOK"
                print "\n3. ICLOUD"

    elif len(sys.argv) == 1:
        print "No args added. Trying to find settings.cfg"

        try:
            config = ConfigParser.RawConfigParser()
            config_file_path = "settings.cfg"
            config.read(config_file_path)

            account = config.get("email", "account")
            password = config.get("email", "password")

            delay = config.get("spam_mail_info", "delay")

            spam_subject = config.get("spam_mail_info", "spam_subject")
            spam_message = config.get("spam_mail_info", "spam_message")

            settings_targets = config.get("targets", "targets")
            targets = settings_targets.split(", ")

            start = Engine()

            if account != "" and password != "" and spam_subject != "" and spam_message != "" and len(targets) != 0:

                if "@gmail.com" in account:
                    chosen = "1"
                    start.account()

                elif "@outlook.com" in account:
                    chosen = "2"
                    start.account()

                elif "@icloud.com" in account:
                    chosen = "3"
                    start.account()

                else:
                    print "Found an unsupported email."
                    exit(0)

        except ConfigParser.Error as cfgerror:
            print "Error, %s" % cfgerror

        else:
            pass


except RuntimeError:
    print "error."

else:
    print custom_error
