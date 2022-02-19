from time import time, strftime, struct_time, mktime, strptime
from datetime import *
from os import name, listdir, walk, getenv
from sys import argv, builtin_module_names, executable, hash_info, platform

# Number of seconds that have passed since the epoch
print(time())

# Current time
print(strftime('%c'))

# Another way of displaying time
time_tuple = (2022, 2, 20, 19, 20, 0, 6, 51, 0)
time_struct = struct_time(time_tuple)
print(time_struct)

# Converting a local time into seconds
print(mktime(time_struct))

# Converting a Python time string to an object
print(strptime('Sun Feb 20 19:32:31 2022'))

# Getting the current local date by creating a date instance
print(date.today())
print(type(date.today()))

# Getting the current local date and time by creating a datatime instance
now = datetime.now()
print(now)
print(type(now))

# Addition with timedelta()
tomorrow = timedelta(days=+1)
print(f'The time in 24 hours is  {now + tomorrow}')

# Subtraction with timedelta()
yesterday = timedelta(days=-1)
print(f'Let\'s travel back in time! Yesterday at this moment the time was {now + yesterday}')

# Name of the OS
print(f'The name of my OS is {name}')

# Generation of file names in a directory
my_data = walk('/home/sasha/python-education/python/basics/world')
for content in my_data:
    print(content)

# List of files and directories in a path
print(f" My world folder contains {listdir('/home/sasha/python-education/python/basics/world')}")

# Getting an environmental variable if it exists
print(getenv('PATH'))

# Getting a name of the module
print(f'Module\'s name is {argv[0]}')

# Getting a tuple with all available modules
print(builtin_module_names)

# Getting a path to a python interpreter
print(f'Lovely python is here {executable}')

# Information about hash parameters
print(hash_info)

# Information about the operating system
print(platform)

