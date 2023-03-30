
set logging enabled

set $gdb_py_dir = "/home/bach/gdb/python"
set $sys_prefix = "/usr"

# let gdb find our python script
python

import sys
import gdb

# kdevelop needs this?
print("GNU gdb (GDB) 13.1\n")

print("\n*********gdb init**************")

value_obj = gdb.convenience_variable("gdb_py_dir")
val_str = gdb.Value.string(value_obj)
print("convenience variable gdb_py_dir: " + val_str)
sys.path.insert(0, val_str)
from GdbFindAddSourceDirs import GdbFindAddSourceDirs

end


# gdb step command decorator
# processing before step
define hook-step

python

obj = GdbFindAddSourceDirs('step')
value_obj = gdb.convenience_variable("sys_prefix")
val_str = gdb.Value.string(value_obj)
print("convenience variable sys_prefix: " + val_str)
obj.dirs_add(val_str)

end

end


# gdb list command decorator
# processing before list
define hook-list

python

obj = GdbFindAddSourceDirs('list')
value_obj = gdb.convenience_variable("sys_prefix")
val_str = gdb.Value.string(value_obj)
obj.dirs_add(val_str)

end

end

