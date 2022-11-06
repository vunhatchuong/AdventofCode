# python AoC-Input-Downloader.python 1 2021

import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

if len(sys.argv) != 3:
    print("Wrong number of argument!")
    exit(0)

day = int(sys.argv[1])
year = int(sys.argv[2])

SESSION_CODE = os.getenv("AOC_SESSION")
user = {"session": SESSION_CODE}
url = f"https://adventofcode.com/{year}/day/{day}/input"


print(f"Downloading Day:{day} Year:{year} input")
s = requests.Session().get(url, cookies=user)
if s.ok:
    print("Success")
else:
    print("Error")

with open(f"./{year}/input/Day{day:02}.in", "w+") as f:
    f.write(s.text)
