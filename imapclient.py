#!/usr/bin/env python
# Simple script for testing POP
# Please add to the repo and help out! :)

import email
import poplib
import sys
import textwrap
import argparse
from argparse import RawTextHelpFormatter
from email.parser import Parser
import pprint
pp = pprint.PrettyPrinter(indent=4, depth=6)

email_parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        **********************************************************
        * Basic POP client for testing mail from command line.   *
        *                                                        *
        * You can also use the verbose option (either 1 or 2)    *
        * for more logging detail. Default is debug 0.           *
        *                                                        *
        * Examples:                                              *
        * $ python pop_client.py <user> <pass> <server>          *
        * $ python pop_client.py <user> <pass> <server> -v 1     *
        *                                                        *
        **********************************************************
        '''))
email_parser.add_argument("user", help="Account username")
email_parser.add_argument("password", help="Account password")
email_parser.add_argument("server", help="POP server")
email_parser.add_argument("-v", "--verbose", default=0, type=int, choices=[1, 2], help="Verbose output")
args = email_parser.parse_args()

def returnPop(user,password,server,verbose):
    pop3_mail = poplib.POP3_SSL(server)
    pop3_mail.set_debuglevel(verbose)
    pop3_mail.user(user)
    pop3_mail.pass_(password)
    pop3_stat = pop3_mail.stat()

    currentMail, totalSize = (pop3_stat)
    print "Total New Mail: %s (size %s bytes)" % pop3_stat
    latest_email = pop3_mail.retr(currentMail)
    pop3_mail.quit()

    # pp.pprint(latest_email)

    latest_email = "\n".join(latest_email[1])
    latest_email = email.parser.Parser().parsestr(latest_email)



    print 'To: %s' % latest_email['to']
    print 'From: %s' % latest_email['from']
    print 'Subject: %s' % latest_email['subject']
    print 'Date: %s' % latest_email['date']

print returnPop(args.user, args.password, args.server, args.verbose)
