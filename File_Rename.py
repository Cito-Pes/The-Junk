#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, glob


import os
new_folder = "d:/현대투어존동의자료_모음/"

import shutil

def File_search(dir):
    err_file = []
    filenames = os.listdir(dir)
    i = 1
    for filename in filenames:
        full_path = os.path.join(dir, filename)

        print(full_path)
        if os.path.isdir(full_path):
            File_search(full_path)
        else:
            # print(f"파일명: {full_path}", filename)
            name, ext = os.path.splitext(filename)
            print('name',name, '              ext ::::', ext)

            print(name.find("-"))



        i +=1

    print(i)
    print(err_file)



# File_search('C:/Users/jino0/Cloudike/현대투어존동의자료')

File_search('z:/temp')