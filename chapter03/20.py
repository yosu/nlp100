#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    article = json.loads(line)
    if article['title'] == 'イギリス':
        print(article['text'])
