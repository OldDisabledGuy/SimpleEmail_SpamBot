from __future__ import print_function

# 0.7, MORE STUFF.

"""SimpleEmail_SpamBot or SESB is a script that lets you spam people using Gmail, Outlook or/and iCloud"""

# TODO:
# https://serversmtp.com/en/signup
# from __future__ import print_function X
# manual:xxx.xxx.xxx:xxx
# py2exe

# I will stop maintaining this script soon.
# Nobody uses this it anyways.

# I might actually give it a GUI.

__author__ = "DizAzTor"
__license__ = "MIT"
__version__ = "v0.7"

try:
    import ConfigParser
    import io
    import smtplib
    import getpass
    import time
    import sys
    import os
    import imaplib
    from sys import exit
    import urllib

except ImportError:
    print("Import error.")

# A stupid way to do it, i know.
email_number = 0  # DO NOT CHANGE THIS PLEASE.
spam_delay = 0  # DEFAULT. CAN BE CHANGED.
spam_subject = ""
spam_message = ""
account_number = 0  # DO NOT CHANGE THIS PLEASE.
stop_at = 50  # DEFAULT. CAN BE CHANGED.

# lol
version = urllib.urlopen("https://dizaztor.github.io/SESB/version.txt")
read_version = version.read().rstrip()
the_m_var = "NO"

account = ""
password = ""

int_choose = 0

targets = []
targets_counter = 0
target_number = 1
command_target_number = 0

# MAX IS X ACCOUNTS.
# all_accounts = []
# usable_accounts = {}
chosen = ""
command_chosen = ""
normal = ""

stop_and_return = ""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class VersionChecker(object):

    def latestver(self):
        if __version__ == read_version:
            print("\nThis script: %s (LATEST)" % __version__)

        elif __version__ != read_version:
            print("\nThis script: %s (UPDATE AVAILABLE)" % __version__)
            print("\nLatest SESB: %s" % read_version)

        else:
            print("\nVERSION ERROR.")

    def internetconnection(self):

        try:
            print("\nChecking for internet connection...")
            github = urllib.urlopen("https://github.com/")

        except:
            print("\nNo internet connection.")
            exit(0)

class Help(object):

    def __init__(self):
        pass

    def gmail(self):
        print("\nLog in with your GMail account.")
        print("\nMake sure to enable \"less secure apps\"")
        print("\nEnable it: bit.ly/GMailSettings")

    def outlook(self):
        print("\nLog in with your OUTLOOK account.")
        print("\nMake sure to enable \"POP and IMAP\"")
        print("\nEnable it: bit.ly/OutlookSettings")

    def icloud(self):
        print("\nLog in with your ICLOUD account.")
        print("\nMake sure to use an \"app-specific password\"")
        print("\nPlease read: bit.ly/iCloudSettings")
        print("\nIt should give you enough information on using an app-specific password.")

    def yahoo(self):
        print("\nLogin with your YAHOO! account.")
        print("\nMake sure \"POP\" is selected under Access your Yahoo Mail elsewhere.")
        print("\nMore info: bit.ly/YahooSettings")

    def zoho(self):
        print("\nLog in with your Zoho Mail Suite account.")
        print("\nYou may require an application-specific password to set up-")
        print("-the account in other devices if you've enabled-")
        print("-Two-Factor Authentication.")
        print("\nApp-Specific Password: bit.ly/ZohoSettings")

    def gmx(self):
        print("\nLog in with your GMX account.")
        print("\nMake sure you enabled \"GMX via POP3 & IMAP\"")
        print("\nHome -> Email Settings -> POP3 and IMAP -> Send and receive emails via external program -> Save")

    def fastmail(self):
        print("\nLog in with your FASTMAIL account.")
        print("\nMake sure to use an app-specific password.")
        print("\nPlease read: bit.ly/FastmailSettings")
        print("\nIt should give you enough information about using an app-specific password.")


class SpamMailInfo(object):

    def __init__(self):
        pass

    def temp_text(self):

        print("\nCurrent delay is set to %s (default = 0)" % spam_delay)
        print("\nIt is recommended to change it.")
        print("\nThe server might realize that you're spamming and the script will shutdown.")
        print("\n The script might shutdown after: 80~100 emails.")
        print("\nRecommended delay is 2.")

    def set_delay(self):

        global spam_delay

        spam_delay = raw_input("\n>>> ")

        try:
            int_spam_delay = int(spam_delay)
            spam_delay = int_spam_delay

        except ValueError:
            print("\nThat's not an integer.")
            spam_delay = 0
            self.set_delay()

        else:
            int_spam_delay = int(spam_delay)
            spam_delay = int_spam_delay

    def set_subject(self):

        global spam_subject

        print("\nPlease type in your subject.")
        spam_subject = raw_input("\n>>> ")

    def set_message(self):

        global spam_message

        print("\nPlease type in your message.")
        spam_message = raw_input("\n>>> ")


class Engine(object):

    def __init__(self):
        pass

    def start_engine(self):

        print("\nSpamming from \"%s\" to: " % account)
        print("\n%s" % "\n".join(targets))

        fromaddr = "%s" % account

        msg = "\r\n".join([
            "From: %s",
            "To: %s",
            "Subject: %s",
            "",
            "%s"]) % (account, targets, spam_subject, spam_message)

        if chosen == "1" or command_chosen == "1":
            server = smtplib.SMTP("smtp.gmail.com:587")

        elif chosen == "2" or command_chosen == "2":
            server = smtplib.SMTP("smtp-mail.outlook.com:587")

        elif chosen == "3" or command_chosen == "3":
            server = smtplib.SMTP("smtp.mail.me.com:587")

        elif chosen == "4" or command_chosen == "4":
            server = smtplib.SMTP("smtp.mail.yahoo.com:587")

        elif chosen == "5" or command_chosen == "5":
            server = smtplib.SMTP("smtp.zoho.eu:587")

        elif chosen == "6" or command_chosen == "6":
            server = smtplib.SMTP("smtp.gmx.com:25")

        elif chosen == "7" or command_chosen == "7":
            server = smtplib.SMTP("mail.messagingengine.com:587")

        else:
            print("\nError: Huh. Unsupported email?")

        server.ehlo()
        server.starttls()

        try:
            server.login(account, password)

            if normal == "YES":
                server.sendmail(fromaddr, targets, msg)
                print("\nMail sent.")
            else:
                while True:
                    server.sendmail(fromaddr, targets, msg)
                    global email_number
                    email_number += 1
                    print("\nMail sent. #%s" % email_number)
                    time.sleep(float(spam_delay))

        except smtplib.SMTPAuthenticationError:
            print("\nWrong password or email.")
            print("\nHint 0: Did you enable \"less secure apps\"?")
            print("\nHint 1: Caps lock?")

        except KeyboardInterrupt:
            print("\nStopped.")

        except EOFError:
            print("\nStopped.")

    def go_back_to_cl(self):
        if the_m_var == "YES":
            return "go_back"
        else:
            exit(0)


class ImportSettings(object):

    def __init__(self):
        # Sorry for sinning.
        pass

    def importconfig(self):
        # Sorry for sinning.
        global account
        global password

        global spam_delay
        global spam_subject
        global spam_message

        global chosen
        global command_chosen

        global targets

        try:
            config = ConfigParser.RawConfigParser()
            path = "config.cfg"
            config.read(path)

            password = config.get("account", "password")
            account = config.get("account", "email")

            spam_message = config.get("spamfo", "message")
            spam_delay = config.get("spamfo", "delay")
            spam_subject = config.get("spamfo", "subject")

            targets = config.get("targets", "targets")
            targets = targets.split(", ")

            print("\nImported!")

        except ConfigParser.Error:
            print("\nCouldn't import your settings, sorry.")

        if "@gmail.com" in account:
            chosen = "1"
            command_chosen = "1"

        elif "@outlook.com" in account:
            chosen = "2"
            command_chosen = "2"

        elif "@icloud.com" in account:
            chosen = "3"
            command_chosen = "3"

        elif "@yahoo.com" in account:
            chosen = "4"
            command_chosen = "4"

        elif "@zillum.com" in account:
            chosen = "5"
            command_chosen = "5"

        elif "@gmx.com" in account or "@gmx.us" in account:
            chosen = "6"
            command_chosen = "6"

        elif "@fastmail.com" in account: #  I know Fastmail has a lot of domains. I'll add them later.
            chosen = "7"
            command_chosen = "7"

    def start_spamming(self):

        checkver = VersionChecker()
        checkver.latestver()

        x = Engine()
        x.start_engine()

class Targets(object):

    def __init__(self):
        pass

    def targets(self):
        global targets
        targets_status = ", ".join(targets)
        print("\nTargets: %s" % targets_status)
        print("\nEvery line is a new target.")
        print("\nWhen you're done, press ENTER.")

        while True:
            global target_number
            a_new_target = raw_input("\nTarget %d: " % target_number)

            if "@" in a_new_target:
                target_number += 1
                targets.append(a_new_target)

            elif a_new_target == "":

                add_info = SpamMailInfo()
                add_info.temp_text()
                add_info.set_delay()
                add_info.set_subject()
                add_info.set_message()

                start_engine = Engine()
                start_engine.start_engine()
                break

            else:
                print("\nThat's not a valid email.")


class ALL_EMAILS(object):

    def __init__(self):
        self._help_ = Help()
        self.choose_targets = Targets()

    def get_gmail(self):

        global account
        global password

        self._help_.gmail()
        account = raw_input("\nGmail account: ")
        if "@gmail.com" in account:
            # nothing to do here
            pass
        else:
            account += "@gmail.com"
        password = getpass.getpass("\nGmail Password: ")
        self.choose_targets.targets()

    def get_outlook(self):

        global account
        global password

        self._help_.outlook()
        account = raw_input("\nOutlook account: ")
        if "@outlook.com" in account:
            # nothing to do here
            pass
        else:
            account += "@outlook.com"
        password = getpass.getpass("\nOutlook password: ")
        self.choose_targets.targets()

    def get_icloud(self):

        global account
        global password

        self._help_.icloud()
        account = raw_input("\niCloud account: ")
        if "@icloud.com" in account:
            # nothing to do here
            pass
        else:
            account += "@icloud.com"
        password = getpass.getpass("\niCloud password: ")
        self.choose_targets.targets()

    def get_yahoo(self):

        global account
        global password

        self._help_.yahoo()
        account = raw_input("\nYahoo account: ")
        if "@gyahoo.com" in account:
            # nothing to do here
            pass
        else:
            account += "@yahoo.com"
        password = getpass.getpass("\nYahoo password: ")
        self.choose_targets.targets()

    def get_zoho(self):

        global account
        global password

        self._help_.zoho()
        account = raw_input("\nZoho account: ")

        # You are on your own here :)

        password = getpass.getpass("\nZoho password: ")
        self.choose_targets.targets()

    def get_gmx(self):

        global account
        global password

        self._help_.gmx()
        print("\rType in your whole email. (With the domain.)")
        print("\rDEFAULT = gmx.com")
        account = raw_input("\nGMX account: ")
        if "@gmx.com" in account or "@gmx.us" in account:
            # nothing to do here
            pass
        else:
            account += "@gmx.com"
        password = getpass.getpass("\nGMX password: ")
        self.choose_targets.targets()

    def get_fastmail(self):

        global account
        global password

        self._help_.fastmail()
        account = raw_input("\nFastmail account: ")
        if "@fastmail.com" in account:
            # nothing to do here
            pass
        else:
            account += "@fastmail.com"
        password = getpass.getpass("\nFastmail password: ")
        self.choose_targets.targets()


class Email(object):

    def __init__(self):
        pass

    def choose_email(self):
        # print "\nAccounts added: %s" % account_number
        # print "\nAccounts: %s" % ", ".join(all_accounts)
        # print "\nTO EXIT: enter 0."

        global chosen

        checkver = VersionChecker()
        checkver.latestver()

        print("\nRECOMMENDED = GMail.")
        print("\nWhat email do you wanna use?")
        print("\r\t1. GMail / @gmail.com")
        print("\r\t2. Outlook / @outlook.com")
        print("\r\t3. iCloud / @icloud.com")
        print("\r\t4. Yahoo! Mail / @yahoo.com")
        print("\r\t5. Zoho Mail / ")
        print("\r\t6. GMX / @gmx.com")
        print("\r\t7. Fastmail / @fastmail.com")
        choose = raw_input("\n>>> ")

        if choose == "clear":
            if os.name == "nt":
                os.system("cls")
                self.choose_email()

            else:
                os.system("clear")
                self.choose_email()
        try:
            global int_choose
            int_choose = int(choose)

        except ValueError:
            print("\nPlease insert an integer.")
            self.choose_email()

        else:
            please = ALL_EMAILS()
            int_choose = int(choose)

            if int_choose == 1:
                chosen = "1"
                please.get_gmail()

            elif int_choose == 2:
                chosen = "2"
                please.get_outlook()

            elif int_choose == 3:
                chosen = "3"
                please.get_outlook()

            elif int_choose == 4:
                chosen = "4"
                please.get_yahoo()

            elif int_choose == 5:
                chosen = "5"
                please.get_zoho()

            elif int_choose == 6:
                chosen = "6"
                please.get_gmx()

            elif int_choose == 7:
                chosen = "7"
                please.get_fastmail()

            else:
                print("\nPlease choose between 1 and 7.")
                self.choose_email()


class Commands(object):

    # a wild comment appears.

    def __init__(self):

        print("\nCopyright DizAzTor 2017")
        print("\nSimpleEmail_SpamBot")
        print("\nCommand Mode v0.3 BETA")

    def text_(self):
        pass

    def command_line(self):

        try:
            command = raw_input("\n>>> ")
            command = command.lower()
        except KeyboardInterrupt:
            print("\rNo service to stop.")
            print("\rCTRL+D / exit to exit.")
            self.command_line()
        except EOFError:
            print("\rGoodbye!\r")
            exit(0)

        global account
        global password

        global the_m_var

        global spam_delay
        global spam_subject
        global spam_message

        global command_chosen

        global version

        global targets
        global targets_counter
        global target_number
        global command_target_number
        global normal

        if command == "add account":
            acccount = ""

            try:
                account = raw_input("\nACCOUNT>>> ")

            except KeyboardInterrupt:
                print("\nCancelled.")
                self.command_line()

            except EOFError:
                print("\nCancelled.")
                self.command_line()

            if "@gmail.com" in account:
                chosen = "1"
                command_chosen = "1"

            elif "@outlook.com" in account:
                chosen = "2"
                command_chosen = "2"

            elif "@icloud.com" in account:
                chosen = "3"
                command_chosen = "3"

            elif "@yahoo.com" in account:
                chosen = "4"
                command_chosn = "4"

            elif "#zoho" in account:
                chosen = ""
                command_chosen = ""

            elif "@gmx.com" in account or "@gmx.us." in account:
                chosen = "6"
                command_chosen = "6"

            elif "@fastmail.com" in account:
                chosen = "7"
                command_chosen = "7"

            else:
                print("\nUnsupported email service.")

            self.command_line()

        elif command == "add password":

            password = ""
            try:
                password = getpass.getpass("\nPASSWORD>>> ")
            except KeyboardInterrupt:
                print("\nStopped.")

            except EOFError:
                print("\nStopped.")

            self.command_line()

        elif command == "help account":
            # should at least have stuff to add, ya know.
            print("\nComing in 0.8")
            self.command_line()

        elif command == "clear":

            if os.name == "nt":
                os.system("cls")
                print("\nCommand Mode v0.3")
                self.command_line()

            else:
                os.system("clear")
                print("\nCommand Mode v0.3")
                self.command_line()

        elif command == "commands":
            print(bcolors.OKGREEN + "\t add account" + bcolors.ENDC, "= Add an account.")
            print(bcolors.OKGREEN + "\t del account" + bcolors.ENDC, "= Remove your account.")
            print(bcolors.OKGREEN + "\t add password" + bcolors.ENDC, "= Set a password for your account.")
            print(bcolors.OKGREEN + "\t del password" + bcolors.ENDC, "= Remove your password.")
            print(bcolors.OKGREEN + "\t help account" + bcolors.ENDC, "= Get help on using your account.")
            print(bcolors.OKGREEN + "\t print account" + bcolors.ENDC, "= Print your account to the terminal.")
            print(bcolors.OKGREEN + "\t del passacc" + bcolors.ENDC, "= Remove the password and the account.")
            print(bcolors.OKGREEN + "\t add target" + bcolors.ENDC, "= Add one target.")
            print(bcolors.OKGREEN + "\t add target x" + bcolors.ENDC, "= Automatically add x amount of targets.")
            print(bcolors.OKGREEN + "\t del target x" + bcolors.ENDC, "= Delete a specific target.")
            print(bcolors.OKGREEN + "\t del target all" + bcolors.ENDC, "= Delete all targets.")
            print(bcolors.OKGREEN + "\t print targets" + bcolors.ENDC, "= Print all of your targets to the terminal.")
            print(bcolors.OKGREEN + "\t print target x" + bcolors.ENDC, "= Print a specific target to the terminal.")
            print(bcolors.OKGREEN + "\t set subject" + bcolors.ENDC, "= Set a subject for your email.")
            print(bcolors.OKGREEN + "\t del subject" + bcolors.ENDC, "= Remove the subject.")
            print(bcolors.OKGREEN + "\t print subject" + bcolors.ENDC, "= Print your subject to the terminal. ")
            print(bcolors.OKGREEN + "\t set message" + bcolors.ENDC, "= Set a message for your email.")
            print(bcolors.OKGREEN + "\t del message" + bcolors.ENDC, "= Remove the message.")
            print(bcolors.OKGREEN + "\t print message" + bcolors.ENDC, "= Print your message to the terminal.")
            print(bcolors.OKGREEN + "\t del submsg" + bcolors.ENDC, "= Remove the subject and the message.")
            print(bcolors.OKGREEN + "\t set delay x" + bcolors.ENDC, "= Set a delay between every message.")
            print(bcolors.OKGREEN + "\t print delay" + bcolors.ENDC, "= Check your delay.")
            print(bcolors.OKGREEN + "\t clear" + bcolors.ENDC, "= Clear the terminal.")
            print(bcolors.OKGREEN + "\t start" + bcolors.ENDC, "= Start spamming.")
            print(bcolors.OKGREEN + "\t CTRL+D / CTRL+C" + bcolors.ENDC, "= Stop the current process.")
            print(bcolors.OKGREEN + "\t CTRL+D / exit / exit() / quit / quit() / :q / :q!" + bcolors.ENDC, "= Exit the script.")
            print(bcolors.OKGREEN + "\t send email" + bcolors.ENDC, "= Send a normal email to all targets.")
            print(bcolors.OKGREEN + "\t about" + bcolors.ENDC, "= About")
            print(bcolors.OKGREEN + "\t import" + bcolors.ENDC, "= Import settings from config.cfg")
            print(bcolors.OKGREEN + "\t write" + bcolors.ENDC, "= Write your current settings to config.cfg")
            print(bcolors.OKGREEN + "\t try2login" + bcolors.ENDC, "= Check if your email or password is working.")
            print(bcolors.OKGREEN + "\t manual" + bcolors.ENDC, "= Enter manual mode.")
            print(bcolors.OKGREEN + "\t checkver" + bcolors.ENDC, "= Check this script's version.")
            print(bcolors.OKGREEN + "\t latestver" + bcolors.ENDC, "= Check the latest version.")
            print(bcolors.OKGREEN + "\t day x" + bcolors.ENDC, "= Convert days to seconds and assign the value to \"delay\"")
            print(bcolors.OKGREEN + "\t hour x" + bcolors.ENDC, "= Convert hours to seconds and assign the value to \"delay\"")
            print(bcolors.OKGREEN + "\t minute x" + bcolors.ENDC, "= Convert mins to seconds and assign the value \"delay\"")
            print(bcolors.OKGREEN + "\t reset all" + bcolors.ENDC, "= Reset everything.")
            self.command_line()

        elif command == "print account":

            if account == "":
                print("\nYou don't have an account added.")
                self.command_line()

            else:
                print("\n%s" % account)
                self.command_line()

        elif command == "print delay":

            print("\nDELAY SET TO: %d" % spam_delay)
            self.command_line()

        elif command == "print targets":

            if len(targets) == 0:

                print("\nNo targets added.")
                self.command_line()

            else:
                targets_status = ", ".join(targets)
                y = 0
                for x in targets:
                    y += 1
                    print("\r%s. %s" % (y, x))

                #print targets_status
                self.command_line()

        elif command == "del subject":
            spam_subject = ""
            print("\nDone.")
            self.command_line()

        elif command == "del message":
            spam_message = ""
            print("\nDone.")
            self.command_line()

        elif command == "del account":
            account = ""
            print("\nDone.")
            self.command_line()

        elif command == "del password":
            password = ""
            print("\nDone.")
            self.command_line()

        elif command == "del passacc":
            account = ""
            password = ""
            print("\nDone.")
            self.command_line()

        elif command == "del submsg":
            spam_subject = ""
            spam_message = ""
            print("\nDone.")
            self.command_line()

        elif command == "del target all":
            targets = []
            print("\nDone.")
            self.command_line()

        elif "print target" in command:
            command_split = command.split()

            if len(command_split) == 3 and command_split[0] == "print" and command_split[1] == "target":

                try:
                    target_number = int(command_split[2])

                    if target_number == 0 or target_number < 0:
                        print("\nPlease start from 1.")
                        self.command_line()

                    elif target_number > 0:
                        target_number -= 1
                        print("\n%d." % (target_number + 1), targets[target_number])
                        self.command_line()

                except ValueError:
                    print("\nThat's not an integer.")
                    self.command_line()

                except IndexError:
                    print("\nThat target doesn't exit.")
                    self.command_line()

            else:
                print("\nCommand not found. Try \"commands\" to see what you can do.")
                self.command_line()

        elif command == "print subject":

            if spam_subject == "":
                print("\nNo subject added.")
                self.command_line()

            else:
                print("\nSubject: \n%s" % spam_subject)
                self.command_line()

        elif command == "print message":
            if spam_message == "":
                print("\nNo message added.")
                self.command_line()

            else:
                print("\nMessage: \n%s" % spam_message)
                self.command_line()

        elif "add target" in command:
            target_list = command.split()

            if targets == "":
                targets = []
            else:
                pass

            if len(target_list) == 2 and target_list[0] == "add" and target_list[1] == "target":

                try:
                    command_target_number += 1
                    c_a_new_target = raw_input("\nTARGET %d>>> " % command_target_number)
                    targets.append(c_a_new_target)

                except KeyboardInterrupt:
                    print("\nCancelled.")
                    self.command_line()

                except EOFError:
                    print("\nCancelled.")
                    self.command_line()

                else:
                    self.command_line()

            elif len(target_list) == 3 and target_list[0] == "add" and target_list[1] == "target":

                try:
                    targets_counter = int(target_list[2])
                    print(targets_counter)
                    what_even = 0
                    while True:
                        if targets_counter != what_even:
                            command_target_number += 1
                            what_even += 1
                            c_a_new_target = raw_input("\nTARGET %d>>> " % command_target_number)
                            targets.append(c_a_new_target)

                        elif targets_counter == what_even:
                            break
                    self.command_line()

                except ValueError:
                    print("\nThat's not an integer.")
                    self.command_line()

                except KeyboardInterrupt:
                    print("\nCancelled.")
                    self.command_line()

                except EOFError:
                    print("\nCancelled.")
                    self.command_line()

                else:
                    self.command_line()

            else:
                print("\nCommand not found. Try \"commands\" to see what you can do.")
                self.command_line()

        elif "set delay" in command:
            delay_list = command.split()

            if len(delay_list) == 3 and delay_list[0] == "set" and delay_list[1] == "delay":

                try:
                    spam_delay = int(delay_list[2])
                    print("\nDELAY SET TO: %d" % spam_delay)

                except ValueError:
                    print("\nThat's not an integer.")
                    spam_delay = 0
                    self.command_line()

                else:
                    self.command_line()

            else:
                print("\nCommand not found. Try \"commands\" to see what you can do.")
                self.command_line()

        elif command == "set subject":
            try:
                spam_subject = raw_input("\nSUBJECT>>> ")

            except KeyboardInterrupt:
                print("\nStopped.")

            except EOFError:
                print("\nStopped.")

            self.command_line()

        elif command == "set message":
            try:
                spam_subject = raw_input("\nMESSAGE>>> ")

            except KeyboardInterrupt:
                print("\nStopped.")

            except EOFError:
                print("\nStopped.")

            self.command_line()

        elif command == "exit" or command == "quit" or command == "quit()" or command == "exit()" or command == ":q" or command == ":q!":
            print("\nGoodbye!\n")
            exit(0)

        elif command == "start":
            # :)

            if len(targets) != 0 and spam_subject != "" and spam_message != "" and account != "" and password != "":
                try:
                    x = Engine()
                    x.start_engine()

                except KeyboardInterrupt:
                    print("\nStopped.")
                    self.command_line()

                except EOFError:
                    print("\nStopped.")
                    self.command_line()

            elif len(targets) == 0 or spam_subject == "" or spam_message == "" or account == "" or password == "":
                print("\nA variable is empty.")
                print("\nType \"help empty_variable\" for more info.")
                self.command_line()

            else:
                print("\nThis error should not appear, but okay.")
                print("\nSeems like errros love you.")
                print("\nWhat to do? I don't know lol.")
                self.command_line()

        elif command == "send email":
            print("\nSending a normal email to targets...")
            normal = "YES"

            if spam_subject != "" and spam_message != "" and password != "" and account != "" and len(targets) != 0:

                try:
                    command_start_engine = Engine()
                    command_start_engine.start_engine()
                except KeyboardInterrupt:
                    print("\nStopped.")
                    self.command_line()

                # Just in case.
                except EOFError:
                    print("\nStopped.")
                    self.command_line()

                else:
                    self.command_line()

            elif spam_subject == "" or spam_message == "" or password == "" or account == "" or len(targets) == 0:
                print("\nSomething's empty.")
                print("\nPlease check if you have set a subject, message, a target and a password.")
                self.command_line()

            else:
                print("\nSomething's wrong. Please try again.")
                self.command_line()



        elif command == "try2login":

            try:
                if command_chosen == "1":
                    server = smtplib.SMTP("smtp.gmail.com:587")

                elif command_chosen == "2":
                    server = smtplib.SMTP("smtp-mail.outlook.com:587")

                elif command_chosen == "3":
                    server = smtplib.SMTP("smtp.mail.me.com:587")

                elif command_chosen == "4":
                    server = smtplib.SMTP("smtp.mail.yahoo.com:587")

                elif command_chosen == "5":
                    server = smtplib.SMTP("smtp.zoho.eu:587")

                elif command_chosen == "6":
                    server = smtplib.SMTP("smtp.gmx.com:25")

                elif command_chosen == "7":
                    server = smtplib.SMTP("mail.messagingengine.com:587")

                else:
                    print("\nNo email added.")
                    self.command_line()
                server.ehlo()
                server.starttls()
                server.login(account, password)

                print("\nSuccess.")

            except smtplib.SMTPAuthenticationError:
                print("\nWrong password or email.")
                print("\nHint 0: Use \"help account\" to see if you did what you need to do.")
                print("\nHint 1: Caps lock?")
                self.command_line()

            else:
                self.command_line()

        elif command == "help empty_variable":
            print("\nWhat do you think this error is?")
            print("\nPlease check if you have set a subject, message, a target and a password.")
            self.command_line()

        elif command == "latestver":

            version = urllib.urlopen("https://dizaztor.github.io/SESB/version.txt")
            read_version = version.read().rstrip()

            if __version__ == read_version:
                print("\nThis script: %s (LATEST)" % __version__)
                self.command_line()

            elif __version__ != read_version:
                print("\nThis script: %s (UPDATE AVAILABLE)" % __version__)
                print("\nLatest SESB: %s" % read_version)
                self.command_line()

            else:
                print("\nVERSION ERROR.")
                self.command_line()

        elif command == "checkver":
            print("\n", __version__)
            self.command_line()

        elif command == "manual":
            the_m_var = "YES"
            print("\nEntering manual mode.")
            x = Email()
            x.choose_email()

            dont_start_engine = Engine()
            nope = dont_start_engine.go_back_to_cl()

            if nope == "go_back":
                self.command_line()

            else:
                exit(0)

        elif command == "import":

            try:
                x_import = ImportSettings()
                x_import.importconfig()

            except ConfigParser.Error:
                print("\nError importing settings.")
                self.command_line()

            else:
                self.command_line()

        elif command == "help all":
            y = Help()
            y.gmail()
            print("\n------------------------------")
            y.outlook()
            print("\n------------------------------")
            y.icloud()
            print("\n------------------------------")
            y.yahoo()
            print("\n------------------------------")
            y.zoho()
            print("\n------------------------------")
            y.gmx()
            print("\n------------------------------")
            y.fastmail()
            print("\n------------------------------")
            self.command_line()

        elif command == "about":
            print("\nDeveloped by @dizaztor.")
            print("\nSimpleEmail_SpamBot or SESB is a script that lets you spam people")
            self.command_line()

        elif command == "write":
            try:
                config = ConfigParser.RawConfigParser()
                cfgfile = open("config.cfg", "wb")

                config.add_section("account")
                config.set("account", "email", account)
                config.set("account", "password", password)

                config.add_section("spamfo")
                config.set("spamfo", "delay", spam_delay)
                config.set("spamfo", "subject", spam_subject)
                config.set("spamfo", "message", spam_message)

                config.add_section("targets")
                yes_please = ", ".join(targets)
                config.set("targets", "targets", yes_please)

                config.write(cfgfile)

                print("\nWrote!")

            except ConfigParser.Error:
                print("\nError, couldn't write to config.cfg.")
                self.command_line()

            else:
                self.command_line()

        elif "del target" in command:
            alist = command.split()
            if len(alist) == 3 and alist[0] == "del" and alist[1] == "target":
                try:
                    which_target = int(alist[2])
                    if which_target == 0 or which_target < 0:
                        print("\nStart from 1 please.")
                        self.command_line()

                    else:
                        which_target -= 1
                        xy = targets[which_target]
                        del targets[which_target]
                        print("\nDELETED %s." % xy)
                        command_target_number -= 1
                        self.command_line()

                except ValueError:
                    print("\nThat's not an integer.")
                    self.command_line()

                except IndexError:
                    print("\nThat target doesn't exit.")
                    self.command_line()

            elif len(alist) == 2 and alist[0] == "del" and alist[1] == "target":
                print("\nPlease specify the target's number.")
                self.command_line()

            elif len(alist) == 3 and alist[0] == "del" and alist[1] == "target" and alist[2] == "all":
                targets = []
                print("\nDone.")
                self.command_line()

            else:
                print("\nCommand not found. Try \"commands\" to see what you can do.")
                self.command_line()

        elif command == "reset all":
            account = ""
            email_number = 0
            password = ""
            spam_delay = ""
            spam_subject = ""
            spam_message = ""
            targets = ""
            chosen = ""
            command_chosen = ""
            normal = ""
            command_target_number = 0
            print("\nDone.")
            self.command_line()

        elif "day" in command:
            alist = command.split()
            if len(alist) == 2 and alist[0] == "day":
                try:
                    day_value = int(alist[1])
                    spam_delay = (day_value * 86400)
                    print("\nDELAY SET TO: %d" % spam_delay)
                    alist = []
                    self.command_line()

                except ValueError:
                    print("\nThat's not an integer.")
                    alist = []
                    self.command_line()
            else:
                print("\nCommand not found. Try \"commands\" to see what you can do.")
                alist = []
                self.command_line()

        elif "minute" in command:
            alist = command.split()
            if len(alist) == 2 and alist[0] == "minute":
                try:
                    minute_value = int(alist[1])
                    spam_delay = (minute_value * 60)
                    print("\nDELAY SET TO: %d" % spam_delay)
                    alist = []
                    self.command_line()

                except ValueError:
                    print("\nThat's not an integer.")
                    alist = []
                    self.command_line()

            else:
                print("\nCommand not found. Try \"commands\" to see what you can do.")
                alist = []
                self.command_line()

        elif "hour" in command:
            alist = command.split()
            if len(alist) == 2 and alist[0] == "hour":
                try:
                    hour_value = int(alist[1])
                    spam_delay = (hour_value * 3600)
                    print("\nDELAY SET TO: %d" % spam_delay)
                    alist = []
                    self.command_line()

                except ValueError:
                    print("\nThat's not an integer.")
                    alist = []
                    self.command_line()

            else:
                print("\nCommand not found. Try \"commands\" to see what you can do.")
                alist = []
                self.command_line()

        else:
            print("\nCommand not found. Try \"commands\" to see what you can do.")
            alist = []
            self.command_line()


checkfor = VersionChecker()


if __name__ == "__main__":
    # Support Python 2 and 3 input
    # Default to Python 3's input()
    get_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

if len(sys.argv) == 2 and ((sys.argv[1] == "-c") or (sys.argv[1] == "--command")):
    checkfor.internetconnection()
    command_mode = Commands()
    command_mode.command_line()

elif len(sys.argv) == 2 and ((sys.argv[1] == "-m") or (sys.argv[1] == "--manual")):
    checkfor.internetconnection()
    start = Email()
    start.choose_email()

elif len(sys.argv) == 2 and ((sys.argv[1] == "-h") or (sys.argv[1] == "--help")):
    print("\rEnter command-mode and type \"help all\".")
    print("\rYou should get a second version of README.md.")
    exit(0)

elif len(sys.argv) == 1 and sys.argv[0] == "SESB.py":
    checkfor.internetconnection()
    x_import = ImportSettings()
    x_import.importconfig()
    x_import.start_spamming()

else:
    print("\rUnknown.")
    print("\r-c / --command == command-mode")
    print("\r-m / --manual == manual-mode")
    print("\r-h / --help == get help")
    #print "\r-r == random. (will also be available in the command-mode)" (coming in 0.8)
    
