#!/usr/bin/python3
""" Show Type And the Content Using Request """
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(r.text), r.text))
