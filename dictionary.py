#!/usr/bin/env python3

""" mpdule for handling the dictionary file. In particular, other scripts can
use this to add word/links to the dictinoary. """

from link import Link

def append_one(entry):
    print(entry.markdown())
    with open("dictionary.md", "a") as f:
        f.write(entry.markdown())

def append_many(entries):
    for entry in entries:
        append_one(entry)

def writeback(entries):
    entries = sorted(entries, key=str.casefold)
    with open("dictionary.md", "w") as f:
        for entry in entries:
            f.write(entry)

def add(link):
    entries = []
    with open("dictionary.md", "r") as f:
        entries = f.readlines()
    entries += [link.markdown()]
    writeback(entries)

if __name__ == "__main__":
    import sys
    command = sys.argv[1]
    if command == "check":
        check()
    elif command == "add":
        lemma = sys.argv[2]
        url = sys.argv[3]
        add(Link(lemma, url))
    else:
        print(f"Unknown subcommand {command}")
        sys.exit(1)
