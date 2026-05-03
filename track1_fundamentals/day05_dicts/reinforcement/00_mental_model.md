# The Dict Mental Model — Read This Before Every Session

A dictionary is a lookup table.
Every entry has exactly two parts: a key and a value.
The key is HOW you find things.
The value is WHAT you find.

## The 5 operations — write these from memory before every session:

    d = {}                    # CREATE empty dict
    d[key] = value            # ADD or UPDATE
    thing = d[key]            # ACCESS
    if key in d:              # CHECK existence
    for key, value in d.items():  # LOOP
    del d[key]                # DELETE

## The dict of lists pattern — the one that broke you:
s
    groups = {}
    for item in items:
        key = decide_key(item)
        if key not in groups:
            groups[key] = []       # create the list FIRST
        groups[key].append(item)   # then append to the list

## Rule — write this as a comment BEFORE any code:
    # key   = ?
    # value = ?
    # structure = { key: value }

## Return vs print rule:
    Functions RETURN.
    Scripts PRINT.
    If someone else needs the result — return it.
    Print only at the very end in the main block.

## Common mistakes to avoid:
    WRONG: d["name": value]         RIGHT: d["name"] = value
    WRONG: d.append(item)           RIGHT: d[key].append(item)
    WRONG: print inside function    RIGHT: return from function, print in main
    WRONG: code before structure    RIGHT: define key/value in comments first
