import sys
import os
import subprocess
import pickle
import math

if len(sys.argv) != 2:
  print("python3 get_non_crash.py tclist.txt")
  exit(1)

f1 = open(sys.argv[1], "r")
o1 = open("non_crash.out", "w")

for ln in f1:
  runcmd = ["/home/cheong/install/pin-3.7/pin", "-t", "/home/cheong/vuzzer64/fuzzer-code/obj-intel64/bbcounts2.so",
              "-o", "/home/cheong/lava_corpus/LAVA-M/bin/bb.out", "-libc", "0", "--"] + ln.strip().split(" ")
  out2 = subprocess.run(runcmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE).stdout
  nc = True
  for l in out2.split(b"\n"):
    if l[0:3] == b'Suc':
      nc = False
      break
  if nc:
    o1.write(ln.strip().split(" ")[-1] + "\n")

f1.close()
o1.close()
