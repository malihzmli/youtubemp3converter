from pytube import YouTube
import os
from moviepy.editor import *
import time
def videoindirme(link):
    try:
        yt= YouTube(link)
        print(1)
        download = yt.streams.get_lowest_resolution()
        print(2)
        path=download.get_file_path()
        print(3)
        download.download()
        print(4)
        print(path+" "+'indirildi')
        
        
        try:
            FILETOCONVERT = AudioFileClip(path)
            FILETOCONVERT.write_audiofile(path+'.mp3')
            FILETOCONVERT.close()
            time.sleep(1)
            print(title+" "+'donusturuldu')
            
        except:
            os.remove(path)
            print(path+" "+' donusurken bir hata ile karsilasildi')
    except:
        print(link+" "+'indirilirken  hata ile karsilasildi')
    
   
    
file =open('songs.txt','r')
for i in file.readlines():
    videoindirme(i)

                

