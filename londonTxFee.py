from web3 import Web3

#################### London Tx Fee ####################
#                                                     #
# Retrieves the different parts of a transaction fee  #
# given a transaction and a block.                    #
#                                                     #
# Only works on transactions past the london hard     #
# fork this includes blocks past block 12,965,000.    #
#                                                     #
#################### London Tx Fee ####################

# Accesses ethereum through infura node through HTTP and sets it to variable called w3
w3 = Web3(Web3.HTTPProvider(''))

# Sets the block number used in other variables
block_number = 15000300

# Accesses the information of a given block
block = w3.eth.get_block(block_number)

# Accesses the hex value of all the transactions in the given block
block_transactions = block['transactions']

# Accesses a specific transaction in the block
transaction = w3.eth.get_transaction(block_transactions[0])

# Accesses the hash of the given transaction
transaction_hash = transaction['hash']

# Retrieving the different parts of the transaction fee
# Calculating transaction fee paid:
# (Block Base Fee + Max Priority Fee) * Gas Used
#
# Calculating transaction refund:
# Max Fee - (Block Base Fee + Paid Priority Fee)

# Retrieves the information of the transaction selected also known as the transaction receipt
transaction_receipt = w3.eth.get_transaction_receipt(transaction_hash)

# Retrieves the base fee of the block from "block"
block_base_fee = block['baseFeePerGas']

# Retrieves the priority fee paid by the transaction from "transaction"
transaction_max_priority_fee = transaction['maxPriorityFeePerGas']

# Retrieves the cumulative gas used from "transaction"
transaction_cumulative_gas_used = transaction_receipt['cumulativeGasUsed']

# Calculates the total cost of the transaction
transaction_cost = (block_base_fee + transaction_max_priority_fee) * transaction_cumulative_gas_used

# Retrieves the max fee the transaction is willing to pay for a transaction
transaction_max_fee = transaction['maxFeePerGas']

# Calculates the refund from a transaction
transaction_refund = (transaction_max_fee - (block_base_fee + transaction_max_priority_fee)) * transaction_cumulative_gas_used

print("")
print("################ Transaction Fee ################")
print("block base fee: " + str(block_base_fee))
print("max priority fee: " + str(transaction_max_priority_fee))
print("gas used: " + str(transaction_cumulative_gas_used))
print("total transaction cost: " + str(transaction_cost))

print("")

print("################ Transaction Refund ################")
print("transaction max fee: " + str(transaction_max_fee))
print("transaction refund: " + str(transaction_refund))
print("")
