#!/usr/bin/env python
'''
This script will upload pictures from a local folder to Tumblr
For convienence, the main varialble are global and at the top
Change dothings funciton to change the type of post
The current loop will loop through all photos in the directory and queue
them each as single posts.

'''

import yaml
import pytumblr
from os import listdir
from os.path import isfile, join


filepath = "/Users/user/Pictures/uploaddir/"
username = "username"
alltags = ["cats","Bengal Cat","bengal cats","kitten","cute","Bengal"]
onepic = "/Users/<usr>/Pictures/picture.jpg/"

#mogrify -quality 63 *.JPG
#command to lower quality of pics



def get_authenticated_api():
    '''secauthent stands for Secure Authentication.
       This function is basically a method for Authenticating
       to Twitters API.
       
       This uses YAML to read your credentials from the creds.yaml file.
       New Twitter API credentials can be obtained here.
       https://apps.twitter.com/
       
       returns the authentication needed by python-twitter
    '''

    with open('creds.yaml', 'r') as f:
        doc = yaml.load(f)

    client = pytumblr.TumblrRestClient(doc['consumer_key'],
                                       doc['consumer_secret'],
                                       doc['access_token_key'],
                                       doc['access_token_secret'])
    return(client)

def abspaths(mypath):
    '''Takes a path (mypath) and returns all the absoulte file paths for all files
    in that directory as an array (files) '''

    files = []

    for f in listdir(mypath):
        a=join(mypath,f)
        if isfile(a):
            files.append(a)

    #print files
    return(files)

def singlephoto(client,singlefile):
    '''queues a picture (singlefile) in a into a sinlge post'''
    client.create_photo(username, 
        state ="queue", 
         tags = alltags, 
         data = singlefile)
    return()


def pathpost(client):
    '''queues all pictures in a directory (global var filepath) into a sinlge post'''

    paths=abspaths(filepath)
    client.create_photo(username,
        state ="queue",
         tags = alltags,
         data = paths)
    return()

def multisingle(client,path):
    '''queues all pictures in a directory (path), into multiple posts
      each picture will be a single post so N photos will be N posts
    '''
    paths=abspaths(path)
    for p in paths:
        singlephoto(client,p)
    return()


def dothings():
    client = get_authenticated_api()

    #singlephoto(client,onepic)
    multisingle(client,filepath)



    return()


if __name__ == "__main__":
    dothings()