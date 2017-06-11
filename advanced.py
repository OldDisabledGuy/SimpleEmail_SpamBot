try:
    import smtplib
    import time
    import getpass
except ImportError, err:
    print "Ah, %s." % err
else:
    import smtplib
    import time
    import getpass
    
email_number = 0
email_delay = 0

class Setup(object):

    def __init__(self):
        
       pass
        
    gmail_account = raw_input("\nYour gmail: ")

    if "@gmail.com" in gmail_account:
        pass
    else:
        gmail_account += "@gmail.com"

    
    gmail_password = getpass.getpass("\nYour password: ")

    spam_to = raw_input("\nTarget's email: ")

    spam_subject = raw_input("\nEmail subject: ")

    spam_message = raw_input("\nEmail message: ")

    what_lol = True

    while what_lol:
        
        spam_delay = raw_input("\nDelay between every mail: ")

        try:
            int_spam_delay = int(spam_delay)
            email_delay = int_spam_delay

        except ValueError:
            print "\nCome on, dude! Type a number, a number!"

        else:
            email_delay = int(spam_delay)
            what_lol = False # rip dank memes
            break


class Spam(Setup):
    setup = Setup()
    
    fromaddr = "%s" % setup.gmail_account
    toaddrs = "%s" % setup.spam_to
    msg = "\r\n".join([
        "From: %s",
        "To: %s",
        "Subject: %s",
        "",
        "%s"
        ]) % (setup.gmail_account, setup.spam_to, setup.spam_subject, setup.spam_message)
    
    
    
    username = "%s" % setup.gmail_account
    password = "%s" % setup.gmail_password
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)

    while True:
        server.sendmail(fromaddr, toaddrs, msg)
        email_number += 1
        print "\nMAIL SENT. #%d" % email_number
        print setup.email_delay
        time.sleep(setup.email_delay)
    
    
