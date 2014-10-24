#!/usr/bin/python

import os
import json

def dirFileDetails(direc = ".", limit = 12):
  """
  This function walks a directory and returns
  a list containing objects with the details of
  each file.
  
  *Ex: 
    A directory with two files ('main.js', styles.css') would return:
  [
    {
      'fileName': 'main.js',
      'fileExtension': '.js',
      'fileSize': '347 bytes'
    },
    {
      'fileName': 'styles.css',
      'fileExtension': '.css',
      'fileSize': '1,863 bytes'
    },
  ]
  """
  
  fmt = lambda x: "{:,}".format(x)
  
  details = []
  for root, dirs, files in os.walk(direc):
    for f in files:
      absFile = os.path.abspath(os.path.join(root, f))
      n = {}
      n["fileName"] = f
      ##n["AbsfileName"] = absFile
      n["fileSize"] = fmt(os.path.getsize(absFile)) + " bytes"
      n["fileExtension"] = os.path.splitext(absFile)[-1]
      details.append(n)
  # Return a limited amount of the results.
  return details[:limit]
