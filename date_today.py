#!/usr/bin/env python3
"""
Date Today - A simple script that gets and prints today's date
"""
from datetime import datetime

def main():
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    print(f"Date Today: {date_str}")

if __name__ == "__main__":
    main()

