from steem.account import Account

account = input("name of your account: ")

print("your voting power is ", Account(account).current_voting_power())
