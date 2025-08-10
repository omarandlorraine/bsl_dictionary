#!/usr/bin/env python3

""" A script that prompts the user for a youtube links and a list of
timestamps, and then adds those to the dictionary. """

import link
import dictionary

def parse(ts, url):
    # So ts could be something like "1:23 meaning of word" and here we separate "1:23" and "meaning of word"
    time = ts.split(' ')[0]
    lemma = ' '.join(ts.split(' ')[1:])

    # next figure out number of seconds
    try:
        (minutes, seconds) = time.split(':')
        (minutes, seconds) = (int(minutes), int(seconds))
        cgi = f"?t={minutes * 60 + seconds}s"
    except ValueError:
        print(f"Warning: couldn't figure out the timestamp for {ts}")
        return None

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
    print("Now enter the timestamps; one on each line.")
    print("type `end` when you're done")

    ts = input(": ")
    while ts != "end":
        timestamps += ts.split("\n")
        ts = input(": ")

    return [entry for entry in [parse(ts, url) for ts in timestamps if ts] if entry is not None]

def prompts():
    dictionary.append_many(prompt_for_timestamps(prompt_for_link()))

if __name__ == "__main__":
    prompts()
