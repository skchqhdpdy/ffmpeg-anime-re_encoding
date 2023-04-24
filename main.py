import os
#pip install natsort
import natsort

path = input("dir : ")
file_list = natsort.natsorted(os.listdir(path))

num = 1
for fileName in file_list:
    #change file name to 1.mp4, 2.mp4, 3.mp4 ...
    os.rename(f'{path}\{fileName}', f'{path}\{num}.mp4')
    #use ffmpeg (re_encoding)
    os.system(f'ffmpeg -i "{path}\{num}.mp4" -vcodec copy -acodec copy "{path}\{fileName}".mp4')
    num += 1
num -= 1
print("\n\n")
for i in range(num):
    #delete 1.mp4, 2.mp4, 3.mp4 ...
    os.remove(f'{path}\{i + 1}.mp4')
    print(f'Delete | {path}\{i + 1}.mp4')