import platform
import psutil

sysinfo = platform.uname()
meminfo = psutil.virtual_memory()
print(sysinfo)
print(meminfo)
