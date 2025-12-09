#!/usr/bin/python3
import argparse
import subprocess
import sys
# import requests
# from decouple import config #use this to install package: pip install python-decouple
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2025/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.


# SESSION = ${{ secrets.AOC_SESSION }} # for github actions '<FILL_ME_IN>'
# Set up session variable
SESSION = os.getenv("SESSION")  # import from env
if not SESSION or SESSION == '<FILL_ME_IN>':
    print("Error: SESSION environment variable not set. Please set it in your .env file.", file=sys.stderr)
    sys.exit(1)

useragent = 'https://github.com/Saqlain143/Advent-of-Code/blob/main/get_input.py by saqlainabid143@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2025)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

# Include user-agent header as recommended by Advent of Code
# Use subprocess with list to avoid shell injection and handle special characters properly
url = f'https://adventofcode.com/{args.year}/day/{args.day}/input'
cmd = [
    'curl',
    '-s',  # Silent mode
    '-A', useragent,  # User-agent header
    '--cookie', f'session={SESSION}',  # Session cookie
    url
]

try:
    output = subprocess.check_output(cmd, stderr=subprocess.PIPE)
    output = output.decode('utf-8')
    
    # Check if we got an error page (Advent of Code returns HTML error pages for invalid requests)
    # Common error messages from Advent of Code
    if (output.startswith('<!DOCTYPE html>') or 
        'Puzzle inputs differ by user' in output or
        "Please don't repeatedly request this endpoint" in output or
        "404 Not Found" in output):
        print(f"Error: Failed to fetch input. Check your SESSION cookie and ensure day {args.day} is available.", file=sys.stderr)
        sys.exit(1)
    
    # Print the input to stdout
    print(output, end='')
    # Print first 10 lines to stderr for preview
    lines = output.split('\n')
    preview = '\n'.join(lines[:10])
    if len(lines) > 10:
        preview += f'\n... ({len(lines) - 10} more lines)'
    print(f"Fetched {len(lines)} lines. Preview:", file=sys.stderr)
    print(preview, file=sys.stderr)
except subprocess.CalledProcessError as e:
    print(f"Error: Failed to fetch input. curl returned error code {e.returncode}", file=sys.stderr)
    if e.stderr:
        print(e.stderr.decode('utf-8'), file=sys.stderr)
    sys.exit(1)
except FileNotFoundError:
    print("Error: curl command not found. Please install curl.", file=sys.stderr)
    sys.exit(1)


# To get the input, run:

# python3 get_input.py --day 10 > input.txt