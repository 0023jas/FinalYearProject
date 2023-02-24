from web3 import Web3
import random
import pandas as pd

# Blocks prior to london 12,965,000 are when EIP-1559 took place

# Accesses ethereum through infura node through HTTP and sets it to variable called w3
# w3 = Web3(Web3.HTTPProvider(''))
w3 = Web3(Web3.HTTPProvider(''))

# Defines the block the algorithm will start processing
start_block = 15000000

# Defines the number of blocks the algorithm will go through
num_of_blocks = 1

# Defines the number of transactions that will be checked in each block
transactions_per_block = 10

# Integer which defines over what time frame the average fee will be calculated
# A fee average frequency of 0 defines that no average will be taken and that all transaction fees will be recorded
# A fee average frequency of 1 defines that the average fee paid per gas will be measured per 1 block 
# A fee average frequency of 2 defines that the average fee paid per gas will be measured per 2 blocks
fee_average_frequency = 0


# Nested loop to create a set of lists that outline the transaction fee paid per gas
# Takes the start block, the number of blocks to be processed

transaction_block_number_list = []    
    
# create an empty list to store hash values of the selected transactions
transaction_hash_list = []

# create an empty list to store gas prices of the selected transactions
transaction_gas_price_list = []

transaction_base_fee_list = []

transaction_priority_fee_list = []

transaction_gas_consumption_list = []

transaction_gas_used_list = []

transaction_total_cost_list = []

transaction_type_list = []


# loop through each block in the specified range
for block_number in range(start_block, start_block+num_of_blocks):

    # retrieve the current block by its block number
    current_block = w3.eth.get_block(block_number)
    
    # retrieve the transactions of the current block
    block_transactions = current_block["transactions"]
    
    # count the number of transactions in the current block
    num_current_block_transactions = len(block_transactions)
    
    # create a list of transaction numbers in the current block
    unique_tx_num_list = list(range(num_current_block_transactions))
    
    # UN-COMMENT THE TWO LINES OF CODE BENEATH THIS TO INCLUDE A SAMPLE OF TX's
    # shuffle the list of transaction numbers
    # random.shuffle(unique_tx_num_list)
    
    # take only the first `transactions_per_block` elements of the shuffled list
    # unique_tx_num_list = unique_tx_num_list[:transactions_per_block]
    
    # check if the start block is before a specific block number (12965000)
    if(start_block < 12965000):
        
        # loop through each selected transaction number
        for transaction_number in unique_tx_num_list:
            
            print("Tx Process Start: " + str(transaction_number))
                    
            # retrieve the transaction by its hash value
            transaction = w3.eth.get_transaction(block_transactions[transaction_number])
            
            transaction_block = transaction["blockNumber"]
            
            # store the hash value of the transaction
            transaction_hash = transaction["hash"]
            
            # retrieve the receipt of the transaction
            transaction_receipt = w3.eth.get_transaction_receipt(transaction_hash)
            
            # store the gas price of the transaction
            transaction_gas_price = transaction_receipt["effectiveGasPrice"]
            
            block_base_fee = 0
            
            transaction_max_priority_fee = 0
            
            transaction_priority_fee = 0
            
            transaction_gas_used = transaction_receipt['gasUsed']
            
            transaction_total_cost = transaction_gas_price * transaction_gas_used
            
            transaction_type = 0
            
            transaction_hash = Web3.to_hex(transaction_hash)
                
            transaction_block_number_list.append(transaction_block)
            
            # The transaction hash is appended to the list of transaction hashes
            transaction_hash_list.append(transaction_hash)   
                
            # The gas price is appended to the list of transaction gas prices
            transaction_gas_price_list.append(transaction_gas_price)
            
            transaction_base_fee_list.append(block_base_fee)
            
            transaction_priority_fee_list.append(transaction_max_priority_fee)
            
            transaction_gas_used_list.append(transaction_gas_used)
            
            transaction_total_cost_list.append(transaction_total_cost)
            
            transaction_type_list.append(transaction_type)
            
    # if the start block is after or equal to the specific block number (12965000)
    elif(start_block >= 12965000):
        
        # loop through each selected transaction number
        for transaction_number in unique_tx_num_list:
            
            print("Tx Process Start: " + str(transaction_number))
            
            # retrieve the transaction by its hash value
            transaction = w3.eth.get_transaction(block_transactions[transaction_number])
            
            transaction_block = transaction["blockNumber"]
            
            # store the hash value of the transaction
            transaction_hash = transaction["hash"]
            
            # retrieve the base fee of the block
            block_base_fee = current_block['baseFeePerGas']
            
            transaction_receipt = w3.eth.get_transaction_receipt(transaction_hash)
            
            transaction_gas_used = transaction_receipt['gasUsed']
            
            # check if the transaction has a `maxPriorityFeePerGas` field
            if 'maxPriorityFeePerGas' in transaction:
                
                # store the value of `maxPriorityFeePerGas`
                transaction_max_priority_fee = transaction['maxPriorityFeePerGas']

                # The gas price of the transaction is calculated as the sum of the block base fee per gas and the transaction max priority fee per gas
                transaction_gas_price = block_base_fee + transaction_max_priority_fee
                
                transaction_total_cost = transaction_gas_price * transaction_gas_used
                
                transaction_type = 1
                
            else:
                
                transaction_max_priority_fee = 0
                
                # If there is no transaction max priority fee, the gas price is simply the transaction's gas price
                transaction_gas_price = transaction['gasPrice']
                
                transaction_total_cost = transaction_gas_price * transaction_gas_used
                
                transaction_type = 0
                
            transaction_hash = Web3.to_hex(transaction_hash)
                
            transaction_block_number_list.append(transaction_block)
            
            # The transaction hash is appended to the list of transaction hashes
            transaction_hash_list.append(transaction_hash)   
                
            # The gas price is appended to the list of transaction gas prices
            transaction_gas_price_list.append(transaction_gas_price)
            
            transaction_base_fee_list.append(block_base_fee)
            
            transaction_priority_fee_list.append(transaction_max_priority_fee)
            
            transaction_gas_used_list.append(transaction_gas_used)
            
            transaction_total_cost_list.append(transaction_total_cost)
            
            transaction_type_list.append(transaction_type)
    
    # The final lists of transaction gas prices and transaction hashes are printed
    # print(transaction_block_number_list)
    
    # print(transaction_hash_list)
    
    # print(transaction_gas_price_list)
    
    # print(transaction_base_fee_list)
    
    # print(transaction_priority_fee_list)
    
    # print(transaction_gas_used_list)
    
    # print(transaction_total_cost_list)
    
    # print(transaction_type_list)
    
df = pd.DataFrame({
    'transaction_block_number': transaction_block_number_list,
    'transaction_hash': transaction_hash_list,
    'transaction_gas_price': transaction_gas_price_list,
    'transaction_base_fee': transaction_base_fee_list,
    'transaction_priority_fee': transaction_priority_fee_list,
    'transaction_gas_used': transaction_gas_used_list,
    'transaction_total_cost': transaction_total_cost_list,
    'transaction_type_list': transaction_type_list
})

csv_title = str(start_block) + "_" + str(start_block+num_of_blocks) + "_" + str(transactions_per_block) + "_" + str(fee_average_frequency) + ".csv"

df.to_csv(csv_title, index=False)
    
# What is needed from the transaction data with fee average 0:
#     - The block number the transaction was sent during X X
#     - The transaction hash X X
#     - The total cost per gas of a transaction X X
#     - The transaction base fee X X
#     - The transaction priority fee (0 for legacy transactions) X X
#     - The total amount of gas used in the transaction X X
#     - The total transaction cost X X
#     - The type of transaction (Legacy or New) X X
    
# What is needed from the transaction data with fee average above 0:
#     - The start block number the transaction was sent during
#     - The end block number the transaction was sent during (would be identical for both 0 fee avereage frequencies and 1 fee average frequencies)
#     - The average total cost per gas of a transaction
#     - The average transaction base fee of none legacy transactions
#     - The average transaction priority fee of none legacy transactions
#     - The total amount of gas used in the transaction
#     - The total transaction cost
#     - The fee average frequency (i.e. individual transactions, average of a block, average of a set of blocks)  




    
    




