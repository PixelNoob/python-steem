# Memo.py is used to send memos in the Steem Blockchain.

from steem import Steem
s = Steem(keys=["YOUR ACTIVE KEY", "YOUR MEMO KEY"])
send_to = input("Send to: ")
memo = input("Memo: ") # add a "#" before you message to send an encrypted message.
s.commit.transfer(
    send_to, 
    0.001, 
    "SBD", 
    memo= memo, 
    account="YOUR ACCOUNT"
)
