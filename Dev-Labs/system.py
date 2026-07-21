import sys

#print("Executable 'sys.executable' = " + str(sys.executable))


# PYTHONHOME = sys.prefix
#print("PYTHONHOME 'sys.prefix' = " + str(sys.prefix))

# PYTHONPATH = sys.path
#print("PYTHONPATH 'sys.path' = " + str(sys.path))
#for path in sys.path: print("PYTHONPATH 'sys.path' = " + str(path))

# PYTHONPLATLIBDIR = sys.platlibdir
#print("PYTHONPLATLIBDIR 'sys.platlibdir' = " + str(sys.platlibdir))

print("sys.version = " + str(sys.version))
# print("sys.version_info = " + str(sys.version_info))
# print("sys.api_version = " + str(sys.api_version))
# print("sys.hexversion = " + str(sys.hexversion))
# print("sys.flags = " + str(sys.flags))

#mods = sys.modules
for _ in sys.modules: print("sys.modules = " + str(_))
#print("sys.modules = " + str(sys.modules))