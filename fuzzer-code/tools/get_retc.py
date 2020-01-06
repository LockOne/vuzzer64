import sys
import os
import subprocess
import pickle
import math

if len(sys.argv) != 2:
  print("python3 get_non_crash.py tclist.txt")

f1 = open(sys.argv[1], "r")
o1 = open("retc.out", "w")
o1.write("tc, pin, non-pin\n")

progress = 0
prog = 9

for ln in f1:
  if prog < progress:
    print ("\r handled " + str(progress) + " files")
    prog += 10

  runcmd = ["/home/cheong/install/pin-3.7/pin", "-t", "/home/cheong/vuzzer64/fuzzer-code/obj-intel64/bbcounts2.so",
              "-o", "/home/cheong/lava_corpus/LAVA-M/bin/bb.out", "-libc", "0", "--"] + ln.strip().split(" ")
  proc = subprocess.Popen(" ".join(runcmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  stdout, stderr = proc.communicate()
  o1.write(ln.strip().split(" ")[-1] + "," + str(proc.returncode))
  runcmd = ln.strip().split(" ")

  proc = subprocess.Popen(" ".join(runcmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  stdout, stderr = proc.communicate()

  o1.write("," + str(proc.returncode) + "\n")
  progress += 1
  

f1.close()
o1.close()
