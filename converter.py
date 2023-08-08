from pytube import YouTube
import os
from moviepy.editor import *
def videoindirme(link):
    try:
        yt= YouTube(link)
        download = yt.streams.get_lowest_resolution()
        path=download.get_file_path()
        download.download()
        print(path+'indirildi')
        try:
            FILETOCONVERT = AudioFileClip(path)
            FILETOCONVERT.write_audiofile(path+'.mp3')
            FILETOCONVERT.close()
            print(path+" "+'donusturuldu')
            os.remove(path)
        except:
            print('bir hata ile karsilasildi') 
    except:
        print('bir hata ile karsilasildi')
   
    
file =open('sarkilar.txt','r')
for i in file.readlines():
    print(i)
    videoindirme(i)
                


