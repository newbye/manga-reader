#!/usr/bin/python
print("Content-Type: text/html\n")

import sys,os
from commands import getoutput as g

try:    arg = int(sys.argv[1])
except: arg = 1

files=g("ls | grep -i -e png -e jpg -e gif -e jpeg -e bmp").splitlines()
files.sort()

if(arg>len(files)):arg=len(files)
if(arg<1):arg=1

if(arg>1):print("<a href='?{0}'>< BACK</a> | ".format(arg-1))
if(arg<len(files)):print("<a href='?{0}'> FORWARD ></a> | ".format(arg+1))
print("<a href='..'>^ UP ^</a><br/>{0} / {1}<br/><a href='?{3}'><img src='{2}'></a>".format(arg,len(files),files[arg-1],arg+1))

