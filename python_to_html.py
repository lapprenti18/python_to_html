#!/usr/bin/env python3
from yattag import Doc, indent
from bs4 import BeautifulSoup
import requests

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        with tag('span'):
            text("HELLO WORLD !")

result = doc.getvalue()
print(indent(result))