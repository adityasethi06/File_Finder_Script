import glob
import sys


file_to_be_searched = sys.argv[1]

print(f'Searching for {file_to_be_searched}......')
print("Finding file can take some time.........")
files = glob.glob('/Users/test/Desktop/**/' + file_to_be_searched, recursive=True)


if files:
    for file in files:
        print(file)
else:
    print('File not there is the file system')

