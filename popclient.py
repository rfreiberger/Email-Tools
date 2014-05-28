#!/usr/bin/env python
# Pop client with argparse via Louis!
# Simple script for testing POP
# https://git.corp.yahoo.com/robertf/Email-Tools
# Please add to the repo and help out! :)

import email
import poplib
import sys
import textwrap
import argparse
from argparse import RawTextHelpFormatter
from email.parser import Parser
parser = argparse.ArgumentParser(
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
        * Add to the project!                                    *
        * https://git.corp.yahoo.com/robertf/Email-Tools         *
        **********************************************************
        '''))
parser.add_argument("user", help="Account username")
parser.add_argument("password", help="Account password")
parser.add_argument("server", help="POP server")
# parser.add_argument("-v", "--verbose", action="count", default=0, help="Verbose output")
parser.add_argument("-v", "--verbose", default=0, type=int, choices=[1, 2], help="Verbose output")
args = parser.parse_args()



def returnPop(user,password,server,verbose):
    pop3_mail = poplib.POP3_SSL(server)
    pop3_mail.set_debuglevel(verbose)
    pop3_mail.user(user)
    pop3_mail.pass_(password)
    pop3_stat = pop3_mail.stat()

    currentMail, totalSize = (pop3_stat)
    print "Total New Mail: %s (size %s bytes)" % pop3_stat
    latest_email = pop3_mail.retr(currentMail)
    # print latest_email
    # emailMessage = str(latest_email)
    # print emailMessage
    #msg = email.message_from_string(emailMessage)
    # print msg['from']
    # print msg['to']
    # newMail.join(latest_email)
    newMail = str(latest_email)
    headers = Parser().parsestr(newMail)
    print 'To: %s' % headers['to']
    print 'From: %s' % headers['from']
    print 'Subject: %s' % headers['subject']
    
print returnPop(args.user, args.password, args.server, args.verbose)
