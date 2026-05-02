# Problem: Check if a key exists before accessing it. Show what happens when you access a missing key.
# Concept: KeyError on missing access, safe lookup with `in` or .get().
# You are done when:
#   [ ] You use `in` to check for a key before accessing it
#   [ ] You demonstrate that accessing a missing key raises KeyError
#   [ ] You use .get() to return a default when the key is absent
#   [ ] All test cases print PASS
# Hint: d.get(key, default) returns default instead of raising an error when key is missing.


def safe_lookup(d, key):
    """
    Return the value for key if it exists, otherwise return None.
    Do not raise KeyError.
    """

    # key in d <- this checks if key is in Dict we can do ("A" in d : but that is hardcoded)
    
    
    # use this if you dont care about the value because it will return none even if the value is set to none 
    # this returns none if no value set so it does not crash the program 
    return d.get(key)

   

def key_exists(d, key):
    """
    Return True if key is in d, False otherwise.
    """
     # Use key in d when you care whether the key exists
    return key in d
    


if __name__ == "__main__":
    cones = {"A": (1.0, 0.0, 0.0), "B": (2.0, 1.0, 0.0)}

    print("PASS" if key_exists(cones, "A") is True else "FAIL key_exists True")
    print("PASS" if key_exists(cones, "Z") is False else "FAIL key_exists False")
    print("PASS" if safe_lookup(cones, "A") == (1.0, 0.0, 0.0) else "FAIL safe_lookup found")
    print("PASS" if safe_lookup(cones, "Z") is None else "FAIL safe_lookup missing")

    try:
        _ = cones["Z"]
        print("FAIL — should have raised KeyError")
    except KeyError:
        print("PASS KeyError raised as expected")
