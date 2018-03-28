from steem.account import Account

account = input("name of your account: ")

print ("your reputation is ", Account(account).rep)
