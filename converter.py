from pytube import YouTube
import os
from moviepy.editor import *
import time
failed=0
def download(link):
    try: 
        yt= YouTube(link)
        print(link+" "+"is downloading")
        download = yt.streams.get_lowest_resolution()
        title = yt.title
        path=download.get_file_path()
        download.download()
        print(title+" "+'downloaded')
        convert(path)
    except:
        global failed
        failed+=1
        faileds.writelines(link)
        print(link+" "+'An error  occurred   while downloading')
def convert(path):
    try:
        FILETOCONVERT = AudioFileClip(path)
        FILETOCONVERT.write_audiofile(path+'.mp3')
        FILETOCONVERT.close()
        time.sleep(1)
        os.remove(path)
    except:
        global failed
        failed+=1
        faileds.writelines(link)
        print('An error occurred  while  converting') 
faileds=open('failed.txt','w')
songs =open('songs.txt','r')
for i in songs.readlines():
    print("************************************************************")
    download(i)
    print("************************************************************")
print(str(failed)+" "+"download failed go `faileds.txt`")

                

