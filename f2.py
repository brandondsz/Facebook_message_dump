#!/usr/bin/python


import sys

from facepy import GraphAPI
from facepy import exceptions

#Acces token with expire time = 60days
LONG_LIVE_ACCESS_TOKEN = 'CAATxpFDnE6IBAFdqbDfNVV6k0plCjWsbkKeRGbfSTp9OeOyQ7AwGFugUZB50UQAypZCFXp9V3Log2nacwwZBu8yNdfr60zdbPS9qi1mJ8fLOHd17ZB6pbDVcZC25ck79FpUWrKKBnZBGBZAAxPbDMxxZBRY44zzoG6FQCiAnbqi9YDZABXCWhXJXNrmiBNHxQmo0ZD'

#Facebook app id and secret from http://developer.facebook.com/apps
APP_ID = ''
SECRET_KEY = ''
#1391587941094306
#f26f0ec4dd654de641126a71cf28df7f
def user_id_to_username(userid):

    """ Function to convert facebook USERID to username. """

    if userid is not None:

        userid = '/{0}'.format(userid)
        try:
            return  graph.get(userid)['name']

        except (exceptions.FacebookError, exceptions.OAuthError) as e:
            print e.message
            sys.exit(0)

def get_message_author(message_list):

    """ Function to get the author of message."""

    return user_id_to_username(message_list['snippet_author'])


def get_message_author_id(message_list):

    """ Function to get the author ID."""

    return message_list['snippet_author']


def get_message_body(message_list):

    """ Function to get the message or message body."""

    return message_list['body']


def get_recipients_list(message_list):

    """ Function to get all the recipients of a message."""

    author = get_message_author_id(message_list)
    temp = message_list['recipients']

    #Facebook includes author as a recipient too. So, we are going to remove it from the
    #list of recepients.
    temp.remove(author)
    return ", ".join(map(user_id_to_username, temp))


def pretty_print(message_list):

    """ Function which prints the o/p in a specified format."""

    for message in message_list:

        print "from:     ", get_message_author(message)
        print "to:       ", get_recipients_list(message)
        print "Message:  ", get_message_body(message)
        print "-" * 140


def get_thread(thread_list):
	return thread_list['thread_id']


#Creating facebook GraphAPI object using the long live token.
graph = GraphAPI(LONG_LIVE_ACCESS_TOKEN)

#Output of the facebook query language(FQL)
#This FQL queries for message body, author, recipients for unread messages.
try:
    json_thread = graph.fql('SELECT thread_id FROM thread WHERE folder_id = 1  limit 10 ')
except exceptions.OAuthError as e:
    print e.message
    sys.exit(0)

thread_list=json_thread['data']
"""for t in thread_list:
	print get_thread(t)"""
#print thread_list

for t in  thread_list:
	try:
		json_output = graph.fql('select body,viewer_id,author_id from message where thread_id = ' + get_thread(t))
		message_list = json_output['data']
		for m in message_list: 			
			print get_message_body(m)
	except exceptions.OAuthError as e:
    		print e.message
    		sys.exit(0)	
#Extracting the data content part from the returned json response. The data part will
#contain snippet, author, recepients.

#

#Checking if empty or not.
"""if message_list:
	pretty_print(message_list)
	#m = message_list[snippet]	
	#print m	
else:
    print "No New Messages"
    sys.exit(0)"""
