from pytube import YouTube
import os
from moviepy.editor import *
import time
def videoindirme(link):
    try:
        yt= YouTube(link)
        download = yt.streams.get_lowest_resolution()
        path=download.get_file_path()
        download.download()
        print(path+" "+'indirildi')
        
        
        try:
            FILETOCONVERT = AudioFileClip(path)
            FILETOCONVERT.write_audiofile(path+'.mp3')
            FILETOCONVERT.close()
            time.sleep(1)
            print(title+" "+'donusturuldu')
            
        except:
            os.remove(path)
        except:
            
            print(path+" "+' donusurken bir hata ile karsilasildi')
    except:
        print(link+" "+'indirilirken  hata ile karsilasildi')
file =open('songs.txt','r')
for i in file.readlines():
    videoindirme(i)

                

