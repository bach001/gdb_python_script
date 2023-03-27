# 
# add system installed library directories
# to enable gdb to find them
#

import gdb
import re
import sys
import os


class GdbFindAddSourceDirs:

    errmsgs = ["No such file", "Bad file", "Directory is not"]

    def __init__(self, cmd):
        print(f"\n********** hook {cmd} ************")
        self.cmd = cmd

    def dirs_add(self, prefix):
        captured = gdb.execute(self.cmd, to_string=True)
        print('*********** captured command output ***********')
        print('|' + captured + '|')

        err = False
        for msg in self.errmsgs:
            if msg in captured: err = True; break
        if not err: print('**** fine, just return ****'); return

        print("**** try adding source directories ********")

        try:
            s = re.split(r'/|:', captured)
            print('************************')
            print(s)
            fname = s[-2]
            info = s[-1]
            print('************************')
            print(f"file name: {fname}$\nerr info: {info}@@")
            print('************************')
            print(info)
            paths = self.find_all(fname, prefix)
            print('************************')
            print(paths)
            for path in paths:
                cmd = f'dir {path}'
                print(f"***** execute dir add command '{cmd}' *******")
                gdb.execute(f'dir {path}', to_string=True)
        except Exception as e:
            print(f'++++ caught exception: {type(e)} +++++')

    @staticmethod
    def find_all(name, path):
        res = []
        for root, dirs, files in os.walk(path):
            if name in files:
                res.append(root)
        return res
