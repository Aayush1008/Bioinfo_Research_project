#!/usr/bin/python

hagap={}
hagap1=[]

with open("ary") as test_file:
 lines = test_file.readlines()
with open("list") as test_filea:
 linesa = test_filea.readlines()
for i in range(len(lines)):
 hagap1=lines[i].split(',')
 hagap[str(hagap1[0])]=hagap1[1]
 hagap1=[]
for i in range(len(linesa)):
 print str(linesa[i].strip())+','+hagap[linesa[i].strip()]
