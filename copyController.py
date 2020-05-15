# !/usr/bin/python

import os
from shutil import copyfile

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
        if "art/controller.svg" in os.path.join(root, name) :
            src = os.path.join(root, name)
            filename, file_extension = os.path.splitext(src)
            dst = filename+"_black"+file_extension
            copyfile(src, dst)