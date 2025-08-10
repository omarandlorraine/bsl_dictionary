#!/usr/bin/env python3

""" mpdule for handling the dictionary file. In particular, other scripts can
use this to add word/links to the dictinoary. """

from link import Link

def load():
    with open("dictionary.md", "r") as f:
        return f.readlines()

def sort(entries):
    return sorted(entries, key=str.casefold)

def save(entries):
    with open("dictionary.md", "w") as f:
        for entry in entries:
            f.write(entry)

def add(link):
    entries = load()
    entries += [link.markdown()]
    save(sort(entries))

def add_many(entries):
    for entry in entries:
        add(entry)

def check():
    entries = load()
    def extract_lemma(e):
        return e.split(']')[0].removeprefix(" - [")

    kv = {}
    for i in entries:
        l = extract_lemma(i)
        if l in kv.keys():
            print("duplicated lemma:")
            print(kv[l])
            print(i)
        else:
            kv[l] = i
    return entries == sort(entries)

if __name__ == "__main__":
    import sys
    command = sys.argv[1]
    if command == "check":
        sys.exit(0 if check() else 1)
    elif command == "sort":
        save(sort(load()))
    elif command == "add":
        lemma = sys.argv[2]
        url = sys.argv[3]
        add(Link(lemma, url))
    else:
        print(f"Unknown subcommand {command}")
        sys.exit(1)
