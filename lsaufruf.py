#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:41:36 2022

@author: rene
"""

import subprocess
process = subprocess.run(["ls", "-l", "noexist"], check=False,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          universal_newlines=True)
output = process.stdout
print(output)

error = process.stderr
print(error)