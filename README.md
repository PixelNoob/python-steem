# python-steem

## 1. Scripts

A list of python scripts that use the [Steem-Python library](https://github.com/steemit/steem-python).
<br>

## 2. memo-sender.sh

Memo-Sender.sh is a tool that allows you to send multiple txs to different accounts. It can be used for marketing purposes.

**How to use it** 

1. Install the Python-Steem Library and set up your steempy command line https://steem.readthedocs.io/en/latest/install.html 
2. Edit the /memo-sender/memo-sender.sh file to specify your desired memo. Make sure to add your personal Steempy passphrase in the "UNLOCK" variable (that way you wont get asked for it everytime it sends a tx).
3. Modify the sender.csv file to specify the account list you wish to send the memos to. 
4. From the terminal run the memo sender .sh and specify the sender.csv file as the path:
````./memo.sender.sh sender.csv````

**NOTE:** Make sure you make the .sh executable (chmod +x memo-sender.sh) for it to work. 

____

This repository has been created and is currently maintained by Steem witness @chitty
<br>
www.steemit.com/@chitty
