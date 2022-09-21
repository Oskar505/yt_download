import pafy
import youtube_dl


def downloadFromYt(urls, mp4=True):

    if type(urls) == str:
        video = pafy.new(urls)
        title = video.title


        if mp4 == True:
            try:
                best = video.getbest()
                best.download(filepath=f'/downloads/{title}.mp4')
            
            except:
                print('download error')
                print(title)
                print(url)
                print('')
        
        else:
            try:
                best = video.getbestaudio()
                best.download(filepath=f'/downloads/{title}.aac')

            except:
                print('download error')
                print(title)
                print(url)
                print('')
            
    
    elif type(urls) == list:

        for url in urls:
            video = pafy.new(url)
            title = video.title

            print(title)

            if mp4 == True:
                try:
                    best = video.getbest()
                    best.download(filepath=f'/downloads/{title}.mp4')
                
                except:
                    print('download error')
                    print(title)
                    print(url)
                    print('')

            
            else:
                try:
                    best = video.getbestaudio()
                    best.download(filepath=f'/downloads/{title}.aac')
                
                except:
                    print('download error')
                    print(title)
                    print(url)
                    print('')
    
    else:
        print('urls must be string or list')

#downloadFromYt('https://youtu.be/3N8m9vsAwds')