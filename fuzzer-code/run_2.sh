#!/bin/sh
#$1 : "SUT %s", $2 : TC file name (%s), $3 : a number?

cwd=$PWD
cd ../libdft64/tools
$PIN_ROOT/pin -t libdft-dta.so -filename $2 -x $3 -- $1
cd $cwd
cp ../libdft64/tools/cmp.out .
cp ../libdft64/tools/lea.out .
cp ../libdft64/tools/func.out .
