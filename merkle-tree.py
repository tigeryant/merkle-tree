import hashlib
import math

"""
- Prompt the user, asking for the number of messages to add to the tree (must be even and below a maximum)
- Assign the result to the variable message_count
- Initialise the variable layer_count to ((log message_count base 2) + 2)
- Initialise a 'tree' list. It should have layer_count number of elements. Each element is a list, so 'tree' is actually a 2d array
- Prompt the user for the messages, adding each one to the tree list at index 0
- Initialise unhashed_index to 0
- Initialise hashed_index to 1
- Initialise merge_count to (len(unhashed) / 2), where unhashed is the list at index 0 of the tree 2d array
- While merge_count > 0:
-   For merge_count:
-       Pop 2 elements from unhashed. Concatenate them. Find the SHA-256 hash of the result. Add this to hashed, which is the list at index 1 of the tree 2d array. 
-       (Add to the same end they were taken from the unhashed list)
-   unhashed_index += 1
-   hashed_index += 1
-   merge_count = (len(unhashed_list)) / 2
- Print the single element of the unhashed list. This is the merkle root



Future: Set up an interactive challenge and response between Alice and Bob - Bob asks for proof of a given message, Alice provide the necessary hashes
"""