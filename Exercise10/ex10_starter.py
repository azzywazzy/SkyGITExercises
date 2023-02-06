import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames

filename = glob.glob(pattern)

# print(filename)

# for files in filename:
#     print(files)

# for i in range (len(filename)):
#     print(filename[i])

# TODO: use os.path.getsize to find each file's size

# for i in range (len(filename)):
#     print(str(filename[i]) + " - " + str(os.path.getsize(filename[i])) + " bytes")


# other example code to only look for files, not directories
# for i in range (len(filename)):
#     if not os.path.isdir(filename[i]):
#         continue
#         print(filename[i])
#         print(os.path.getsize(filename[i]))
#         # print(os.path.isdir(filename[i]))

# TODO: Add a test to only display files that are not zero length

# for i in range (len(filename)):
#     if os.path.getsize(filename[i]) == 0:
#         continue
#     else:
#         print(str(filename[i]) + " - " + str(os.path.getsize(filename[i])) + " bytes")

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

# print(os.path.basename(filename[0]))

for i in range(len(filename)):
    if os.path.getsize(filename[i]) != 0:
        print(str(os.path.basename(filename[i])) + " - " + str(os.path.getsize(filename[i])) + " bytes")
