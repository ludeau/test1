# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import urllib.request
import zipfile

urllib.request.urlretrieve ("http://data.gdeltproject.org/events/20180613.export.CSV.zip", "ludo1.zip")
with zipfile.ZipFile("ludo1.zip","r") as zip_ref:
    zip_ref.extractall(".") 


