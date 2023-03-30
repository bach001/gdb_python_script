"""
reversing file blocks tagged with number
"""

import re
import os


class ReverseTextBlock:

    def __init__(self, file_path):
        self.prefix = os.path.dirname(file_path)
        self.path = file_path

    def reverse(self):
        p = re.compile(r'^\s*[0-9]+\s*\n$')
        with open(self.path) as f:
            keys = []
            vals = []
            head_lines = ''
            lines = ''
            matched = False
            for line in f:
                if p.fullmatch(line):
                    keys.append(line)
                    if not matched:
                        head_lines = lines
                    else:
                        vals.append(lines)
                    matched = True
                    lines = ''
                else:
                    lines += line
            vals.append(lines)

        print(len(keys))
        print(len(vals))
        # keys.reverse()
        # vals.reverse()

        # output = 'output.txt'
        # output = os.path.join(self.prefix, 'output.txt')
        with open("./output.txt", 'w') as f:
            f.write(head_lines)
            for i in reversed(range(len(keys))):
                f.write(keys[i])
                f.write(vals[i])


if __name__ == '__main__':
    path = '/home/bach/Documents/test.txt'
    obj = ReverseTextBlock(path)
    obj.reverse()
