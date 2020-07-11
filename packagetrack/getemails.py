#!/usr/bin/env python

from __future__ import print_function
import pickle
import os
#imports needed for pulling emails from google api
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
#imports needed for email
from datetime import datetime, timedelta
import base64
import email
#imports needed for text parsing
from bs4 import BeautifulSoup
import re
from re import search
#imports needed for iterating through lists
import itertools
import sys

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

"""List all Messages of the user's mailbox matching the query."""

def ListMessagesMatchingQuery(service, user_id, query=''):
    """
    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

    Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
    """
    response = service.users().messages().list(userId=user_id,
                                           q=query).execute()
    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])

    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
        messages.extend(response['messages'])
   
    # print("We scanned your email for tracking numbers. There were " + str(len(messages)) + " messages that matched the query string " + query)
    final_list = []
    for message in messages:
        final_list.append(message["id"])
    return final_list

"""Get Message with given ID.
"""

def GetMessageDate(service, user_id, msg_id):
    """Get a Message with given ID.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

    Returns:
    The date that a message was sent
    """
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()
    internalDatestr = message["internalDate"]
    date = int(internalDatestr) / 1000
    finaldate = datetime.fromtimestamp(date).strftime("%Y/%m/%d")
    #print("The date of this email is: " + finaldate)
    return finaldate

def GetMimeMessage(service, user_id, msg_id):
    """Get a Message and use it to create a MIME Message.

    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

    Returns:
    A MIME Message, consisting of data from Message.
    """
    
    message = service.users().messages().get(userId=user_id, id=msg_id, format='raw').execute()
    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
    mime_msg = email.message_from_bytes(msg_str)
    return(mime_msg)
""" Parse Message to get Tracking Number """

def ParseRegMessage(msg_id, message):
    payload = message['payload']
    body = payload['body']
    try: 
        print(body)
    except:
        print('regular message body empty')

def ParseMimeMessage(msg_id, message):
    plaintext = ""
    #hard coding in regex expressions for common usps, ups, fedex, dhl tracking #s 
    regex = ["^(94)[0-9]{20}$", "^(92)[0-9]{20}$", "^[0-9]{20}$", "^(1Z)[0-9A-Z]{16}$", 
            "^[0-9]{9}$", "^[0-9]{26}$", "^[0-9]{15}$", "^[0-9]{12}$", "^[0-9]{22}$",
            "^(EC)[0-9]{9}(US)$"] 
    for part in message.walk():                                                                    
        if (part.get_content_type() == "text/plain"):
            text = part.get_payload()
            for word in text.split():
                for expr in regex:
                    if re.match(expr, word):
                        plaintext=word
                        #print(word)
                        continue
        if (part.get_content_type() == "text/html"):
            ''' parses all of the html into plaintext using beautiful soup '''
            soup = BeautifulSoup(part.get_payload(), features="lxml")
            text = soup.get_text()
            for word in text.split():
                for expr in regex:
                    if re.match(expr, word):
                        plaintext=word
                        #print(word)

    return plaintext


"""Shows basic usage of the Gmail API.
"""
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
try:    
    os.makedirs("/Users/ian/.package-track/bin")
except:
    pass

os.chdir("/Users/ian/.package-track/bin")

checkEmail = input("Do you want package-track to automatically find tracking numbers from your email? [y / n] ")
if (checkEmail == "y"):
    if os.path.exists('/Users/ian/.package-track/bin/token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/ian/.package-track/bin/credentials.json', SCOPES)
            except:
                sys.exit("It looks like you haven't downloaded the credentials.json file from Gmail's API. Please visit the README for more information on how to authenticate!")
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    #get list of messages that mention the phrase tracking number
    messageList = ListMessagesMatchingQuery(service, "me", query="tracking number")

    outputarray = []
    datearray = []

    #iterating through messages in list to filter
    for messageid in messageList:
        # print(messageid)
        date = GetMessageDate(service, "me", messageid)
        datearray.append(date)
        message = GetMimeMessage(service, "me", messageid)
        output = ParseMimeMessage(messageid, message)
        if output != "":
            outputarray.append(output)
        else:
            #add placeholder value (only used to make arrays
            #the same length for iteration below)
            outputarray.append(".")
    #writing to a new output file
    with open ('/Users/ian/.package-track/bin/tracking_from_email.txt', 'w') as filehandle:  
        prev = ""
        for (item, date) in zip(outputarray, datearray):
            timeframe = datetime.today() - timedelta(days=28)
            date = datetime.strptime(date, "%Y/%m/%d")
            if (timeframe < date):
                if ((item != prev) & (item != ".")):
                    filehandle.write('%s\n' % item)
            prev = item

