import os
import subprocess

names =os.popen('cd bank && ls').read()

print(len(names))


cmd = "ls"

# returns output as byte string
returned_output = subprocess.check_output(cmd)

# using decode() function to convert byte string to string
print(returned_output.decode("utf-8"))
