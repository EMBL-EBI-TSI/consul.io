#!/usr/bin/python

import os
import psutil
import sys

memoryUse = psutil.virtual_memory()
cpuUse = psutil.cpu_percent(interval=5)
storageUse = psutil.disk_usage('/')
print('memory use:', memoryUse[2])
print('cpu use:', cpuUse)
print('storage use:', storageUse[3])

if cpuUse >= 50:
   print('CPU use:',cpuUse , "%"  )
   sys.exit(1)
else:
   print('CPU use:',cpuUse , "%"  )
   print("service available")
   sys.exit(0)
