# Warmup Day 02 — Lists + Loops
# 4 problems. Target: 5-10 minutes total.

# ── Problem 1 (Lists) ─────────────────────────────────────────────────────────
# Concept: list mutation — append
# Given a list, append the value 99 to it and return the list.

def append_99(lst):

    lst.append(99)
    #print(lst)
    return lst
   
    

r1 = append_99([1, 2, 3])
print("W02-P1 PASS" if r1 == [1, 2, 3, 99] else f"W02-P1 FAIL — got {r1}")

# ── Problem 2 (Lists) ─────────────────────────────────────────────────────────
# Concept: list mutation — remove by index
# Given a list, remove the element at index 1 and return the list.

def remove_index_1(lst):
    
    # there is delete and remove but do not use remove as it remove the first value 

    lst.pop(1)

    return lst

r2 = remove_index_1([10, 20, 30, 40])
print("W02-P2 PASS" if r2 == [10, 30, 40] else f"W02-P2 FAIL — got {r2}")

# ── Problem 3 (Loops) ────────────────────────────────────────────────────────
# Concept: loop with condition — collect elements > 5
# Return a list of all numbers greater than 5 using a for loop.

def collect_gt5(numbers):
    
    lst = [number for number in numbers if number > 5]
    return lst

r3 = collect_gt5([1, 6, 3, 8, 5, 9])
print("W02-P3 PASS" if r3 == [6, 8, 9] else f"W02-P3 FAIL — got {r3}")

# ── Problem 4 (Loops) ────────────────────────────────────────────────────────
# Concept: enumerate loop
# Return a list of (index, value) pairs using enumerate.

def indexed_pairs(lst):
    
    store = []

    for x in enumerate(lst):
        
        store.append(x)

    return store

r4 = indexed_pairs(["a", "b", "c"])
print("W02-P4 PASS" if r4 == [(0, "a"), (1, "b"), (2, "c")] else f"W02-P4 FAIL — got {r4}")
