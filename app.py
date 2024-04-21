import requests
import os
import time
import threading
import shutil

multiThreading = False if input("1. 순차적으로 다운로드 \n2. 랜덤 다운로드 (멀티스레딩, 파일로 저장) \n개인적으로 2번 추천함 : ") == "1" else True
VLE = input("Video (.aaa file) Link End : ") #https://edge-01.gcdn.app/st/___210_Moozzi2_Mushoku_Tensei___Mushoku_Tensei01___/1080/bf2640c14dce4746b16b1abad6774e180355.aaa
title = input("Title : ")

try:
    num = str(int(VLE[-8:].replace(".aaa", "")))
except Exception as e:
    print(e)
    print("4자리 실패! 3자리로 시도해봄")
    try:
        num = str(int(VLE[-7:].replace(".aaa", "")))
    except Exception as e:
        print(e)
        print("3자리 실패! 2자리로 시도해봄")
        num = str(int(VLE[-6:].replace(".aaa", "")))

if len(num) == 4:
    format_str = "{:04d}"  # 4자리 숫자일 때 형식
elif len(num) == 3:
    format_str = "{:03d}"  # 3자리 숫자일 때 형식
elif len(num) == 2:
    format_str = "{:02d}"  # 2자리 숫자일 때 형식
else:
    print("num의 자릿구 구하기에서 자릿수 감지 못함!")
    exit()

st = time.time()

if not multiThreading:
    with open(f"{title}.ts", "wb+") as f:
        for i in range(int(num) + 1):
            link = f"{VLE[:-(len(num) + 4)]}{format_str.format(i)}.aaa"
            print(format_str.format(i) + ".aaa")

            aaa = requests.get(link, headers={"Referer": "https://anilife.app"})
            if aaa.status_code == 200:
                f.write(aaa.content)
            else:
                print("오류 발생!")
                exit()
else:
    if not os.path.isdir("data"):
        os.mkdir("data")
    def download_file(url, filename):
        aaa = requests.get(url, headers={"Referer": "https://anilife.app"})
        if aaa.status_code == 200:
            with open(f"data/{filename}.aaa", 'wb') as f:
                f.write(aaa.content)
        else:
            print("오류 발생!")
            exit()
    threads = []
    for i in range(int(num) + 1):
        link = f"{VLE[:-(len(num) + 4)]}{format_str.format(i)}.aaa"
        print(format_str.format(i) + ".aaa")
        thread = threading.Thread(target=download_file, args=(link, format_str.format(i)))
        threads.append(thread)
        thread.start()
    # 모든 스레드의 작업이 완료될 때까지 대기
    for thread in threads:
        thread.join()
    os.system(f'copy /b data\\*.aaa {title}.ts')
    shutil.rmtree("data")
print(f"{time.time() - st} Sec")

os.system(f'ffmpeg -i "{title}.ts" -vcodec copy -acodec copy "{title}.mp4"')
os.remove(f"{title}.ts")
print(f"{time.time() - st} Sec")