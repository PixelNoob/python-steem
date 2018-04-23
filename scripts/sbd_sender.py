# PYTHON quick SBD sender
from steem import Steem
s = Steem(
	nodes=["http://rpc.buildteam.io"],
	keys=["PRIV POSTING", "PRIV ACTIVE"]
)
print ("welcome to quick SBD Sender")
to = input("Please provide receiver account: ")
amount1 = input("Please provide amount to send: ")
amount = float(amount1)
memo = input("Please provide a memo (optional) or press enter to continue: ")

s.commit.transfer(
    to, 
    amount, 
    "SBD", 
    memo= memo, 
    account="YOUR ACCOUNT"
)
print (amount1 + " SBD has been sent to " + to)
