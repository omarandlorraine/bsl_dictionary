#!/usr/bin/env python3

"""A script for adding entries from Mr. Bearscots youtube videos"""

import link
import dictionary

def parse(ts, url):
    # So ts could be something like "1:23 meaning of word" and here we separate "1:23" and "meaning of word"
    time = ts[0]
    lemma = ts[1]

    # next figure out number of seconds
    try:
        (minutes, seconds) = time.split(':')
        (minutes, seconds) = (int(minutes), int(seconds))
        cgi = f"?t={minutes * 60 + seconds}s"
    except ValueError:
        print(f"Warning: couldn't figure out the timestamp for {ts}")
        return None

    # The captions seem to always start with the prefix "SIGN:"
    if lemma.startswith("SIGN: "):
        lemma = lemma.removeprefix("SIGN: ").lower()

        # and then timestamp the URL.
        (minutes, seconds) = time.split(':')
        (minutes, seconds) = (int(minutes), int(seconds))
        cgi = f"&t={minutes * 60 + seconds}s"
        url = f"{url}{cgi}"

        return link.Link(lemma, url)

def prompt_for_link():
    url = input("Enter the link to the video:")
    if url.startswith("https://www.youtube.com"):
        # remove playlist and user and whatnot from the link
        url = url.split('&')[0]
    return url

def prompt_for_timestamps(url):
    timestamps = []
    print("Now copy paste the captions, which have the timestamps and \"SIGN:\"")
    print("type `end` when you're done")

    ts = input(": ")
    while ts != "end":
        timestamps += ts.split("\n")
        ts = input(": ")

    while not timestamps[0]:
        timestamps = timestamps[1:]
    entries = [(timestamps[i], timestamps[i+1]) for i in range(0, len(timestamps), 2) if timestamps[i] and timestamps[i+1]]
    return [entry for entry in [parse(ts, url) for ts in entries] if entry]

def prompts():
    dictionary.add_many(prompt_for_timestamps(prompt_for_link()))

if __name__ == "__main__":
    prompts()
