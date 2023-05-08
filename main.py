import os
import time
#pip install natsort
import natsort

path = input("dir : ")
file_list = natsort.natsorted(os.listdir(path))
file_list_ts = [file for file in file_list if file.endswith(".ts")]
#file_list_aaa = [file for file in file_list if file.endswith(".aaa")]

os.system(f'copy /b *.aaa result.ts')
time.sleep(3)

num = 1
for fileName in file_list_ts:
    #change file name to 1.ts, 2.ts, 3.ts ...
    os.rename(f'{path}\{fileName}', f'{path}\{num}.ts')
    #use ffmpeg (re_encoding)
    newfileName = fileName.replace(".ts", ".mp4")
    os.system(f'ffmpeg -i "{path}\{num}.ts" -vcodec copy -acodec copy "{path}\{newfileName}"')
    num += 1
num -= 1

print("\n\n")
for i in range(num):
    #delete 1.ts, 2.ts, 3.ts ...
    os.remove(f'{path}\{i + 1}.ts')
    print(f'Delete | {path}\{i + 1}.ts')
print("\n\n")