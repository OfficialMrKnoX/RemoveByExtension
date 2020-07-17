import os

path = input('Folder Path: ')
fType= input('File Extension: ')
files = []

# r=root, d=directories, f=files
for r, d, f in os.walk(path):
    for file in f:
        if fType in file:
            files. append(os.path.join(r, file))

for f in files:
    print(f)

print('\n')
conf = input("Do you want to delete all files(y/n): ")

if conf == 'y':
    for f in files:
        try:
            print('Deleting', f)
            os.remove(f)
        except OSError as e:
            print('\n', e, '\n')
            pass

if conf == 'n':
    print('Thanks for using Knox Extension Cleaner')
