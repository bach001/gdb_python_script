import re
import os

class ReverseTextBlock:

    def __init__(self, path):
        self.prefix = os.path.dirname(path)
        self.path = path

    def reverse(self):
        p = re.compile(r'^\s*[0-9]+\s*\n$')
        with open(self.path) as f:
            keys = []
            vals = []
            blank_lines = ''
            lines = ''
            matched = False
            for line in f:
                if p.fullmatch(line):
                    keys.append(line)
                    if not matched:
                        blank_lines = lines
                    else:
                        vals.append(lines)
                    matched = True
                    lines = ''
                else:
                    lines += line
            vals.append(lines)

        print(len(keys))
        print(len(vals))
        #keys.reverse()
        #vals.reverse()
        
        output_path = os.path.join(self.prefix, 'output.txt')
        with open(output_path, 'w') as f:
            f.write(blank_lines)
            for i in reversed(range(len(keys))):
                f.write(keys[i])
                f.write(vals[i])


if __name__ == '__main__':
    obj = ReverseTextBlock('/home/bach/Documents/1111.txt')
    obj.reverse()
