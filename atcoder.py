#!/usr/bin/env python3

import random
import requests

nums = [f"{n:03}" for n in range(1, 1000)]

while True:
    url = f"https://atcoder.jp/contests/abc{random.choice(nums)}"

    if response := requests.get(url):
        print(url)
        break
    
    print(f"Error requesting {url}:", response)
    ans = input("Re-run the script? (y/N) ").lower()

    if not ans or ans[0] != "y":
        break
