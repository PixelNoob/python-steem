# This script calculates all the SP received by a witness. Courtesy of @emrebeyler

from steem import Steem
from steem.account import Account
from steem.amount import Amount
from steem.converter import Converter

import logging

logger = logging.getLogger('producer rewards')
logger.setLevel(logging.INFO)
logging.basicConfig()


def calculate_producer_rewards(steemd_instance, witness_account):
    account = Account(witness_account,steemd_instance=steemd_instance)

    total_vests = 0

    for producer_reward in account.history_reverse(filter_by=["producer_reward"]):
        total_vests += Amount(producer_reward["vesting_shares"]).amount

    converter = Converter(steemd_instance=s)
    total_sp = converter.vests_to_sp(total_vests)

    return total_vests, total_sp


if __name__ == '__main__':
    s = Steem(nodes=["https://api.steemit.com"])
    witness_account = 'WITNESS ACCOUN NAME'
    vests, sp = calculate_producer_rewards(s, witness_account)
    print("Account: %s, Total Vests: %s, Total SP: %s" % (
        witness_account, round(vests, 2), round(sp, 2)))
