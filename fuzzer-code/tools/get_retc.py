import sys
import os
import subprocess
import pickle
import math

if len(sys.argv) != 3:
  print("python3 get_non_crash.py TC_path execute_command")
  exit()

o1 = open("retc.out", "w")
o1.write("tc, ret code, stdout\n")

for fi in os.listdir(sys.argv[1]):
  runcmd = sys.argv[2] % (sys.argv[1] + fi)
  proc = subprocess.Popen(runcmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
 
  stdout, stderr = proc.communicate()
  o1.write(fi + ", " + str(proc.returncode) +", " +  stderr.decode() + "\n")
  
o1.close()
