import praw
import time
import random
import os
import config

#reddit api login
def bot_login():
    print("Logging in")
    #config files contain the following parameters for praw.reddit
    reddit = praw.Reddit(client_id=config.client_id,
                         client_secret=config.client_secret,
                         username=config.username,
                         password=config.password,
                         user_agent=config.user_agent)
    return reddit

#phrase to activate the bot
keyphrase = 'gabe'

#Things that gabes says
with open("Gabetext.txt", "r") as textfile:
    quotes = textfile.readlines()

#method to run the bot
def run_bot(reddit, replied_comments):
    for comment in reddit.subreddit('test').comments(limit=10):
        if keyphrase in comment.body and comment.id not in replied_comments and comment.author != reddit.user.me():
            print("String Found!")
            comment.reply(random.choice(quotes))
            print ("Replied to comment")

            replied_comments.append(comment.id)

            with open("replied_comments.txt", "a") as b:
                b.write(comment.id + "\n")



    #Delays for x amount of time
    time.sleep(10)


#if you have an existing txt database of comment ids you have already replied to
def get_saved_comments():
    if os.path.isfile("replied_comments.txt") != True:
        replied_comments = []
    else:
        with open("replied_comments.txt", "r") as x:
            replied_comments = x.read()
            replied_comments = replied_comments.split("\n")
    return replied_comments



reddit = bot_login()
replied_comments = get_saved_comments()

#while True:
run_bot(reddit, replied_comments)
