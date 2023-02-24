from web3 import Web3

# Accesses ethereum through infura node through HTTP and sets it to variable called w3
w3 = Web3(Web3.HTTPProvider(''))

# Sets the block number used in other variables
block_number = 12000000

# Accesses the information of a given block
block = w3.eth.get_block(block_number)

# Accesses the hex value of all the transactions in the given block
block_transactions = block['transactions']

# Accesses a specific transaction in the block
transaction = w3.eth.get_transaction(block_transactions[0])

# Accesses the hash of the given transaction
transaction_hash = transaction['hash']

# Retrieves the information of the transaction selected also known as the transaction receipt
transaction_receipt = w3.eth.get_transaction_receipt(transaction_hash)

# Retrieves the price paid for gas
transaction_gas_price = transaction_receipt["effectiveGasPrice"]

# Retrieves the total gas used 
transaction_gas_used = transaction_receipt["cumulativeGasUsed"]

# Calculates the cost of the transaction
transaction_cost = transaction_gas_price * transaction_gas_used

print(transaction_cost)