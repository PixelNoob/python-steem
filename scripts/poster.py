# This bot will post content on the steem blockchain

from steem import Steem
import json

print ("posting on the steem blockchain...")
s = Steem(keys=["YOUR_PRIV_POSTING_KEY"])
s.commit.post(
    "Posting using Steem Python Lib", # title
    "This is a test and should not be taken seriously", # body
    "vinotinto", # account
    tags=["spam", "test"] # tags
)

print ("Posted to the the Blockchain!)
