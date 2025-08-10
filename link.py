#!/usr/bin/python3

import re

class Link:
    def __init__(self, lemma, url, sublemma=None):
        self.lemma = lemma.strip()
        self.url = url
        self.sublemma = sublemma

    def parse(string):
        """ Parses the lemma in markdown format """
        string = string.removeprefix(" - ")
        match = re.match(r"\[(.*?)\]\((.*?)\)", string)
        lemma = match.group(1)
        url = match.group(2)
        return Link(lemma, url)

    def markdown(self):
        return f" - [{self.lemma}]({self.url})"

            
