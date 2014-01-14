#!/usr/bin/python


import sys

from facepy import GraphAPI
from facepy import exceptions

#Acces token with expire time = 60days
LONG_LIVE_ACCESS_TOKEN = ''
#'CAATxpFDnE6IBAFdqbDfNVV6k0plCjWsbkKeRGbfSTp9OeOyQ7AwGFugUZB50UQAypZCFXp9V3Log2nacwwZBu8yNdfr60zdbPS9qi1mJ8fLOHd17ZB6pbDVcZC25ck79FpUWrKKBnZBGBZAAxPbDMxxZBRY44zzoG6FQCiAnbqi9YDZABXCWhXJXNrmiBNHxQmo0ZD'

#Facebook app id and secret from http://developer.facebook.com/apps
APP_ID = ''
SECRET_KEY = ''
#'1391587941094306'
#'f26f0ec4dd654de641126a71cf28df7f'


def get_message_author(message_list):

    return message_list['author_id']




def get_message_body(message_list):
    return message_list['body']


def get_message_viewer(m,t):

    author = get_message_author(m)
    return t['recipients']

  
    




def get_thread(thread_list):
	return thread_list['thread_id']



graph = GraphAPI(LONG_LIVE_ACCESS_TOKEN)


try:
    json_thread = graph.fql('SELECT thread_id,recipients FROM thread WHERE folder_id = 1  limit 10 ')
except exceptions.OAuthError as e:
    print e.message
    sys.exit(0)

thread_list=json_thread['data']



for t in  thread_list:
	try:
		json_output = graph.fql('select body,viewer_id,author_id from message where thread_id = ' + get_thread(t) + 'and author_id= me()')
		message_list = json_output['data']
		for m in message_list: 			
			print get_message_viewer(m,t)," ",get_message_body(m)
			print "="*100
	except exceptions.OAuthError as e:
    		print e.message
    		sys.exit(0)	

