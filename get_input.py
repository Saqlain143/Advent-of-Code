#!/usr/bin/python3
import argparse
import subprocess
import sys
# import requests
from datetime import datetime
from decouple import config #use this to install package: pip install python-decouple
# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.


# SESSION = ${{ secrets.AOC_SESSION }} # for github actions '<FILL_ME_IN>'

try:
    SESSION = config('SESSION')  #import from env
except:
    SESSION ='<FILL_ME_IN>'

useragent = 'https://github.com/MuhammadSaadSiddique/AdventOfCode/blob/main/get_input.py by muhammadsaad2387@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
time =datetime.now()
parser.add_argument('--year', type=int, default=2023)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}"'

output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)