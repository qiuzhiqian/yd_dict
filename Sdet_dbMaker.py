#!/usr/bin/env python
# -*- coding: utf-8 -*-

#------------------------
#Author:qiuzhiqian
#Email:xia_mengliang@163.com
#------------------------

import re
import os

import Sdet_core

print("1-数据库制作")
print("2-数据库恢复")
op=input("请选择操作:")



sdh=Sdet_core.Sdet_handle()

if(op=='1'):
    db_file=os.path.split(os.path.realpath(__file__))[0]+'/script/Sdet_dbIndex.txt'
    file_obj=open(db_file,mode='r',encoding='UTF-8')
    fileLine=file_obj.readlines()
    
    reg_cmd=r'[a-zA-Z]+'
    
    lineLen=len(fileLine)
    for index in range(lineLen):
        #print(line)
        words=re.search(reg_cmd,fileLine[index]).group(0)
        
        res=sdh.GetWordLocalInfo(words)
        if(res<0):          #本地查询无结果
            sdh.GetWordWebInfo(sdh.GetWebString(words))
            sdh.SaveLocalInfo()     #更新数据库

elif(op=='2'):
    sdh.DB_Reset(1997)

