#!/usr/bin/python3
from brownie import HelloWorld, accounts, config, network, Contract
from scripts.utils import get_account, get_verify_status

def deploy_hello_world():
    account = get_account()
    print(f"You are using the account {account}")
    verify = get_verify_status()
    deployed_contract = HelloWorld.deploy({"from": account}, publish_source=verify)
    if type(deployed_contract) is network.transaction.TransactionReceipt:
        deployed_contract.wait(3)
        deployed_contract = Contract.from_abi("HelloWorld", deployed_contract.contract_address, HelloWorld.abi)
    return deployed_contract

def main():
    hello_world = deploy_hello_world()
    print(hello_world.get())