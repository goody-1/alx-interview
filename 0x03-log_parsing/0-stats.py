#!/usr/bin/python3
"""Log Parsing project with Pythhon"""
import sys
import re


count = 0
total_size = 0
status_code_count = {
    "200": 0, "301": 0, "400": 0, "403": 0,
    "404": 0, "405": 0, "500": 0
}


def parser(line):
    """Check line for the format
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> \
        <file size>

    return: True or False
    """
    pattern = (
        r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
        r'"GET /projects/\d+ HTTP/1\.1" (\d{3}) (\d+)$'
        )
    
    return re.match(pattern, line.strip())


def print_statistics(total_size, status_code_count):
    """Print the statistics"""
    print(f'File size: {total_size}')
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

for line in sys.stdin:
    match = parser(line)
    count+=1

    if match:
        ip, date, status, size = match.groups()
        try:
            total_size += int(size)
        except Exception as e:
            print(e)
        if status in status_code_count.keys():
            status_code_count[status]+=1
    else:
        continue

    try:
        if count > 10:
            print(f'File size: {total_size}')
            for code, num in status_code_count.items():
                if num > 0:
                    print(f"{code}: {num}")
            count = 0
    except KeyboardInterrupt:
        print(f'File size: {total_size}')
        for code, num in status_code_count.items():
            if num > 0:
                print(f"{code}: {num}")

