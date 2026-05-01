# Problem: Given a flat list [x1, y1, z1, x2, y2, z2, ...] convert it into
#          [(x1, y1, z1), (x2, y2, z2), ...] using a loop.
# Concept: Grouping flat data into structured chunks by stepping through indices.
# You are done when:
#   [ ] You consume the flat list in groups of 3
#   [ ] Each group becomes a tuple
#   [ ] You use a loop (not zip or slicing tricks)
#   [ ] All test cases print PASS
# Hint: Loop with range(0, len(flat), 3) to step through in groups of three.


def flat_to_tuples(flat):
    """
    Convert a flat list of floats (length divisible by 3) into a list of (x, y, z) tuples.
    """

# first approach without llm i got it working 
    # store = []

    # for numbers in range(int(len(flat)/3)): # loop should run 3 times  
        
    #     # store the first 3 
    #     print(flat[0:3])

    #     tupe = tuple(flat[0:3])
    #     store.append(tupe)

    #     print(f"this is stored: {store} \n")

    #     # after adding we are popping the first 3 elements 
    #     flat.pop(2)
    #     flat.pop(1)
    #     flat.pop(0)

    #     # reviewing the popped elements 
    #     print(f"flat updated: {flat} \n")
    #     print(f"final: {store}")
    
    # return store 

# llm told me to correct my solution and use slicing lets give that a try 

    store =[]

    for i in range(0,len(flat),3): # this goes like 0,3,6 in terms of index so 0:[1.0] , 3:[4.0].... 

        #print(f"{i}\n")

        store.append(tuple(flat[i:i+3])) # from i to :i+1 as i is not included 
    
    print(store)
    return store

# idk its flowing natrually rn im happy  

if __name__ == "__main__":
    flat = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    result = flat_to_tuples(flat)
    expected = [(1.0, 2.0, 3.0), (4.0, 5.0, 6.0), (7.0, 8.0, 9.0)]
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")

    flat2 = [0.0, 0.0, 0.0]
    result2 = flat_to_tuples(flat2)
    expected2 = [(0.0, 0.0, 0.0)]
    print("PASS" if result2 == expected2 else f"FAIL — got {result2}, expected {expected2}")
