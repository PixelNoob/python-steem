# This script sends a $1 bid to @dailyupvotes upvote bot

from steem import Steem
s = Steem(keys=["YOUR ACTIVE KEY", "YOUR MEMO KEY"])
print ("welcome to dailyupvotes")
memo = input("Please provide the URL of your Post: ")
s.commit.transfer(
    "dailyupvotes", 
    1.00, 
    "SBD", 
    memo= memo, 
    account="YOUR ACCOUNT"
)
print ("your post has been succesfully submitted, thank you for using our services")
