#!/usr/bin/python3
import sys

codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0

try:
    while sys.stdin:
        input_line = sys.stdin.readline()
        section = input_line.split()

        status_code = section[-2]
        size = section[-1]

        if status_code:
            if status_code in codes.keys():
                codes[status_code] += 1
     
        file_size += int(size)
        
        for _ in range(10):
            print("File size: {}".format(file_size))
            for key, value in sorted(codes.items()):
                if value > 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(file_size))
    for key, value in sorted(codes.items()):
        if value > 0:
            print('{}: {}'.format(key, value))
