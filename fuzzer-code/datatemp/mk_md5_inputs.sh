#!/bin/bash
rm md5/*
../../subjects/md5sum ./b64/* > md5/md5_1.txt
../../subjects/md5sum ./cflow/* >> md5/md5_1.txt
../../subjects/md5sum ./bmp2/* > md5/md5_2.txt
../../subjects/md5sum ./mp3/* > md5/md5_3.txt
