# Problem: Create a dict mapping cone names to positions. Add a new cone, update an
#          existing one, and delete one. Return the final dict.
# Concept: Dict creation, insertion, update, and deletion with del.
# You are done when:
#   [ ] You start with at least 3 key-value pairs
#   [ ] You add a new key that did not exist before
#   [ ] You update a value for an existing key
#   [ ] You delete one key using del
#   [ ] All test cases print PASS
# Hint: d[key] = value both inserts and updates; del d[key] removes a key entirely.


def build_cone_dict():
    """
    Return a dict of cone names to (x, y, z) positions after:
      - starting with cones: 'A': (1.0, 0.0, 0.0), 'B': (2.0, 1.0, 0.0), 'C': (3.0, 0.0, 0.0)
      - adding cone 'D': (4.0, -1.0, 0.0)
      - updating cone 'B' to (2.0, 2.0, 0.0)
      - deleting cone 'C'
    """
    cone = {
        'A': (1.0, 0.0, 0.0), 
        'B': (2.0, 1.0, 0.0), 
        'C': (3.0, 0.0, 0.0)
    }

    print(f"initial: {cone}")

    cone["D"] = (4.0, -1.0, 0.0)
    print(cone)

    # cone["B"] = (2.0, 2.0, 0.0)
    cone.update({"B": (2.0, 2.0, 0.0)})
    print(cone)

    

    del cone["C"]
    print(f"final: {cone}")

    return cone

if __name__ == "__main__":
    result = build_cone_dict()
    expected = {
        "A": (1.0, 0.0, 0.0),
        "B": (2.0, 2.0, 0.0),
        "D": (4.0, -1.0, 0.0),
    }
    print("PASS" if result == expected else f"FAIL — got {result}, expected {expected}")
