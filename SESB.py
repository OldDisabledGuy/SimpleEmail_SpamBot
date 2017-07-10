# 0.4, Rewritten.

"""SimpleEmail_SpamBot or SESB is a script that lets you spam people using Gmail, Outlook or/and iCloud"""

__author__ = "DizAzTor"
__copyright__ = "Copyright 2017, SimpleEmail_SpamBot, DizAzTor"
__credits__ = "DizAzTor"

__license__ = "CC"
__version__ = "0.4"
__maintainer__ = "DizAzTor"

try:
	import smtplib
	import getpass
	import time
	import sys
	import os
	import imaplib
	from sys import exit

except ImportError, err:
	print "Ah, %s." % err


email_number = 0  # DO NOT CHANGE THIS PLEASE.
spam_delay = 0  # DEFAULT. CAN BE CHANGED.
spam_subject = ""
spam_message = ""
account_number = 0  # DO NOT CHANGE THIS PLEASE.
stop_at = 50  # DEFAULT. CAN BE CHANGED.

gmail_account = ""
outlook_account = ""
icloud_account = ""

gmail_password = ""
outlook_password = ""
icloud_password = ""

targets = []
target_number = 1
command_target_number = 0

# MAX IS X ACCOUNTS.
# all_accounts = []
# usable_accounts = {}
chosen = ""
command_chosen = ""


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
		print "\nMake sure to use an \"app-specific password\""
		print "\nPlease read: https://support.apple.com/en-us/HT204397"
		print "\nIt should give you enough information on using an app-specific password."


class SpamMailInfo(object):

	def __init__(self):
		pass

	def temp_text(self):

		print "\nCurrent delay is set to %s (default = 0)" % spam_delay
		print "\nIt is recommended to change it."
		print "\nThe server might realize that you're spamming and the script will shutdown."
		print "\n (Gmail) Script might shutdown after: 80~100 emails."
		print "\n (Outlook) Script might shutdown after: N/A"
		print "\n (iCloud) Script might shutdown after: N/A"
		print "\nRecommended delay is 2."

	def set_delay(self):

		global spam_delay

		spam_delay = raw_input("\n>>> ")

		try:
			int_spam_delay = int(spam_delay)
			spam_delay = int_spam_delay

		except ValueError:
			print "\nThat's not an integer."
			spam_delay = 0
			self.set_delay()

		else:
			int_spam_delay = int(spam_delay)
			spam_delay = int_spam_delay

	def set_subject(self):

		global spam_subject

		print "\nPlease type in your subject."
		spam_subject = raw_input("\n>>> ")

	def set_message(self):

		global spam_message

		print "\nPlease type in your message."
		spam_message = raw_input("\n>>> ")


class Engine(object):

	# ENGINE SHOULD WORK
	# ENGINE VERSION 0.2

	def __init__(self):
		pass

	def google(self):

		fromaddr = "%s" % gmail_account
		msg = "\r\n".join([
			"From: %s",
			"To: %s",
			"Subject: %s",
			"",
			"%s"
		]) % (gmail_account, targets, spam_subject, spam_message)

		username = "%s" % gmail_account
		password = "%s" % gmail_password

		server = smtplib.SMTP("smtp.gmail.com:587")
		server.ehlo()
		server.starttls()
		server.login(username, password)

		while True:
			server.sendmail(fromaddr, targets, msg)
			global email_number
			email_number += 1
			print "\nMail sent. #%s" % email_number
			time.sleep(float(spam_delay))

	def outlook(self):

		print "\nSpamming from \"%s\" to: " % outlook_account
		print "\n%s" % "\n".join(targets)

		fromaddr = "%s" % outlook_account
		msg = "\r\n".join([
			"From: %s",
			"To: %s",
			"Subject: %s",
			"",
			"%s"
		]) % (outlook_account, targets, spam_subject, spam_message)

		username = "%s" % outlook_account
		password = "%s" % outlook_password

		server = smtplib.SMTP("smtp-mail.outlook.com:587")
		server.ehlo()
		server.starttls()
		server.login(username, password)

		while True:
			server.sendmail(fromaddr, targets, msg)
			global email_number
			email_number += 1
			print "\nMail sent. #%s" % email_number
			time.sleep(float(spam_delay))

	def icloud(self):

		fromaddr = "%s" % icloud_account
		msg = "\r\n".join([
			"From: %s",
			"To: %s",
			"Subject: %s",
			"",
			"%s"
		]) % (icloud_account, targets, spam_subject, spam_message)

		username = "%s" % icloud_account
		password = "%s" % icloud_password

		server = smtplib.SMTP("smtp.mail.me.com:587")
		server.ehlo()
		server.starttls()
		server.login(username, password)

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
		global targets
		targets_status = ", ".join(targets)
		print "\nTargets: %s" % targets_status
		print "\nEvery line is a new target, please don't type them all in one line."
		print "\nWhen you're done, press ENTER."

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

				if chosen == "1":
					start_engine.google()

				elif chosen == "2":
					start_engine.outlook()

				elif chosen == "3":
					start_engine.icloud()

				else:
					print "\nI actually do not know why you got this error."
					print "\nExiting for no reason."
					exit(0)

			else:
				print "\nThat's not a valid email."


class iCloud(object):

	def __init__(self):
		pass

	def get_icloud_account(self):
		icloud_help = Help()
		icloud_help.icloud()
		global icloud_account
		icloud_account = raw_input("\niCloud Email: ")

		if "@icloud.com" in icloud_account:
			pass
		else:
			icloud_account += "@icloud.com"

		global icloud_password
		icloud_password = getpass.getpass("\niCloud Password: ")

		# global account_number
		# account_number += 1

		# global all_accounts
		# global usable_accounts
		# all_accounts.append(icloud_account)

		choose_targets = Targets()
		choose_targets.targets()


class Gmail(object):

	def __init__(self):
		pass

	def get_gmail_account(self):
		gmail_help = Help()
		gmail_help.gmail()
		global gmail_account
		gmail_account = raw_input("\nGmail Account: ")

		if "@gmail.com" in gmail_account:
			# nothing to do here
			pass
		else:
			gmail_account += "@gmail.com"

		global gmail_password
		gmail_password = getpass.getpass("\nGmail Password: ")

		# global account_number
		# account_number += 1

		# global all_accounts
		# global usable_accounts
		# all_accounts.append(gmail_account)

		choose_targets = Targets()
		choose_targets.targets()


class Outlook(object):

	def __init__(self):
		pass

	def get_outlook_account(self):

		outlook_help = Help()
		outlook_help.outlook()
		global outlook_account
		outlook_account = raw_input("\nOutlook Email: ")

		if "@outlook.com" in outlook_account:
			pass
		else:
			outlook_account += "@outlook.com"

		global outlook_password
		outlook_password = getpass.getpass("\nOutlook Password: ")

		# global account_number
		# account_number += 1

		# global all_accounts
		# global usable_accounts
		# all_accounts.append(outlook_account)

		choose_targets = Targets()
		choose_targets.targets()


class Email(object):

	def __init__(self):
		pass

	def choose_email(self):
		# print "\nAccounts added: %s" % account_number
		# print "\nAccounts: %s" % ", ".join(all_accounts)
		# print "\nTO EXIT: enter 0."
		global chosen
		print "\nRECOMMENDED = GMail."
		print "\nWhat email do you wanna use?"
		print "\n\t1. GMail."
		print "\n\t2. Outlook."
		print "\n\t3. iCloud."
		choose = raw_input("\n>>> ")

		try:
			int_choose = int(choose)
		except ValueError:
			print "\nPlease insert an integer."
			self.choose_email()
		else:
			int_choose = int(choose)

			if int_choose == 1:
				chosen = "1"
				gmail = Gmail()
				gmail.get_gmail_account()
				# self.choose_email()

			elif int_choose == 2:
				chosen = "2"
				outlook = Outlook()
				outlook.get_outlook_account()
				# self.choose_email()

			elif int_choose == 3:
				chosen = "3"
				icloud = iCloud()
				icloud.get_icloud_account()
				# self.choose_email()

			# elif int_choose == 0:
				# pass

			else:
				print "\nSorry; you can only choose between these three for now."
				self.choose_email()


class Commands(object):

	def __init__(self):

		print "\nCopyright DizAzTor 2017"
		print "\nSimpleEmail_SpamBot"
		print "\nCommand Mode v0.1 BETA"

	def text_(self):
		pass

	def command_line(self):

		command = raw_input("\n>>> ")
		command = command.lower()

		global gmail_account
		global outlook_account
		global icloud_account

		global gmail_password
		global outlook_password
		global icloud_password

		global spam_delay
		global spam_subject
		global spam_message

		global command_chosen

		global targets
		global target_number
		global command_target_number

		if command == "add gmail":

			if outlook_account == "" and icloud_account == "":
				command_chosen = "1"
				gmail_account = raw_input("\nGMAIL>>> ")

				if "@gmail.com" in gmail_account:
					pass
				else:
					gmail_account += "@gmail.com"

				self.command_line()

			else:
				print "\n\"outlook_account\" and \"icloud_account\" are not empty."
				print "\nResetting them."
				outlook_account = ""
				icloud_account = ""
				print "\nDone. Type in your command again."
				self.command_line()

		elif command == "add outlook":

			if gmail_account == "" and icloud_account == "":
				command_chosen = "2"
				outlook_account = raw_input("\nOUTLOOK>>> ")

				if "@outlook.com" in outlook_account:
					pass
				else:
					outlook_account += "@outlook.com"

				self.command_line()

			else:
				print "\n\"gmail_account\" and \"icloud_account\" are not empty."
				print "\nResetting them."
				gmail_account = ""
				icloud_account = ""
				print "\nDone. Type in your command again."
				self.command_line()

		elif command == "add icloud":

			if gmail_account == "" and outlook_account == "":
				command_chosen = "3"
				icloud_account = raw_input("\nICLOUD>>> ")

				if "@icloud.com" in icloud_account:
					pass
				else:
					icloud_account += "@icloud.com"

				self.command_line()

			else:
				print "\n\"gmail_account\" and \"outlook_account\" are not empty."
				print "\nResetting them."
				gmail_account = ""
				outlook_account = ""
				print "\nDone. Type in your command again."
				self.command_line()

		elif command == "password gmail":

			gmail_password = ""
			gmail_password = getpass.getpass("\nPASSWORD>>> ")
			self.command_line()

		elif command == "password outlook":

			outlook_password = ""
			outlook_password = getpass.getpass("\nPASSWORD>>> ")
			self.command_line()

		elif command == "password icloud":

			icloud_password = ""
			icloud_password = getpass.getpass("\nPASSWORD>>> ")
			self.command_line()

		elif command == "help gmail":

			help_gmail = Help()
			help_gmail.gmail()
			self.command_line()

		elif command == "help outlook":

			help_outlook = Help()
			help_outlook.outlook()
			self.command_line()

		elif command == "help icloud":

			help_icloud = Help()
			help_icloud.icloud()
			self.command_line()

		elif command == "clear":

			if os.name == "nt":
				os.system("cls")
				print "\nCommand Mode v0.1"
				self.command_line()

			else:
				os.system("clear")
				print "\nCommand Mode v0.1"
				self.command_line()

		elif command == "commands":

			print "\t add gmail = Add a GMail account."
			print "\t add outlook = Add an Outlook account."
			print "\t add icloud = Add an iCloud account."
			print "\t password gmail = Set a password for your GMail account."
			print "\t password outlook = Set a password for your Outlook account."
			print "\t password icloud = Set a password for your iCloud account."
			print "\t help gmail = Get help on using GMail."
			print "\t help outlook = Get help on using Outlook."
			print "\t help icloud = Get help on using iCloud."
			print "\t print gmail = Print your GMail account to the terminal."
			print "\t print outlook = Print your Outlook account to the terminal."
			print "\t print icloud = print your iCloud account to the terminal."
			print "\t add target = Add one target."
			print "\t set subject = Set a subject for your email."
			print "\t set message = Set a message for your email."
			print "\t set delay = Set a delay between every message."
			print "\t print targets = Print all of your targets to the terminal."
			print "\t print subject = Print your subject to the terminal. "
			print "\t print message = Print your message to the terminal."
			print "\t print delay = Check your delay."
			print "\t clear = Clear the terminal."
			print "\t start = Start spamming."
			self.command_line()

		elif command == "print gmail":

			if gmail_account == "":
				print "\nYou don't have a GMAIL account added."
				self.command_line()

			else:
				print "\n%s" % gmail_account
				self.command_line()

		elif command == "print outlook":

			if outlook_account == "":
				print "\nYou don't have an Outlook account added."
				self.command_line()

			else:
				print "\n%s" % outlook_account
				self.command_line()

		elif command == "print icloud":

			if icloud_account == "":
				print "\nYou don't have an iCloud acccount added."
				self.command_line()

			else:
				print "\n%s" % outlook_account
				self.command_line()

		elif command == "print delay":

			print "\nDELAY SET TO: %d" % spam_delay
			self.command_line()

		elif command == "print targets":

			if len(targets) == 0:

				print "\nNo targets added."
				self.command_line()

			else:
				targets_status = "\n".join(targets)
				print targets_status
				self.command_line()

		elif command == "print subject":

			if spam_subject == "":
				print "\nNo subject added."
				self.command_line()

			else:
				print "\nSubject: \n%s" % spam_subject
				self.command_line()

		elif command == "print message":
			if spam_message == "":
				print "\nNo message added."
				self.command_line()

			else:
				print "\nMessage: \n%s" % spam_message
				self.command_line()

		elif command == "add target":

			command_target_number += 1
			c_a_new_target = raw_input("\nTARGET %d>>> " % command_target_number)
			targets.append(c_a_new_target)
			self.command_line()

		elif command == "set delay":

			spam_delay = raw_input("\nDELAY>>> ")

			try:
				int_spam_delay = int(spam_delay)
				spam_delay = int_spam_delay
				self.command_line()

			except ValueError:
				print "\nThat's not an integer."
				spam_delay = 0
				self.command_line()

			else:
				int_spam_delay = int(spam_delay)
				spam_delay = int_spam_delay
				self.command_line()

		elif command == "set subject":
			spam_subject = raw_input("\nSUBJECT>>> ")
			self.command_line()

		elif command == "set message":
			spam_message = raw_input("\nMESSAGE>>> ")
			self.command_line()

		elif command == "quit" or command == "exit":
			print "\nGoodbye!\n"
			exit(0)

		elif command == "start":

			if command_chosen == "1":

				if spam_subject != "" and spam_message != "" and gmail_password != "" and gmail_account != "" and len(targets) != 0:
					command_start_engine = Engine()
					command_start_engine.google()

				elif spam_subject == "" or spam_message == "" or gmail_password == "" or gmail_account == "" or len(targets) == 0:
					print "\nSomething's empty."
					print "\nPlease check if you have set a subject, message, a target and a password."
					self.command_line()

				else:
					print "\nSomething's wrong. Please try again."
					self.command_line()

			elif command_chosen == "2":

				if spam_subject != "" and spam_message != "" and outlook_password != "" and outlook_account != "" and len(targets) != 0:
					command_start_engine = Engine()
					command_start_engine.outlook()

				elif spam_subject == "" or spam_message == "" or outlook_password == "" or outlook_account == "" or len(targets) == 0:
					print "\nSomething's empty."
					print "\nPlease check if you have set a subject, message, a target and a password."
					self.command_line()

				else:
					print "\nSomething's wrong. Please try again."
					self.command_line()

			elif command_chosen == "3":

				if spam_subject != "" and spam_message != "" and icloud_password != "" and icloud_account != "" and len(targets) != 0:
					command_start_engine = Engine()
					command_start_engine.icloud()

				elif spam_subject == "" or spam_message == "" or icloud_password == "" or icloud_account == "" or len(targets) == 0:
					print "\nSomething's empty."
					print "\nPlease check if you have set a subject, message, a target and a password."
					self.command_line()

				else:
					print "\nSomething's wrong. Please try again."
					self.command_line()

			else:
				print "\nNo email added."
				self.command_line()

		else:
			print "\nCommand not found. Try \"commands\" to see what you can do."
			self.command_line()


if len(sys.argv) == 2 and sys.argv[1] == "-c":
	command_mode = Commands()
	command_mode.command_line()

else:
	start = Email()
	start.choose_email()
