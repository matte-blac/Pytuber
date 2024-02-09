# import required modules
from tkinter import *
from pyyoutube import Api
from pytube import YouTube
from threading import Thread
from tkinter import messagebox

# it will give a list of all video links of a YouTube playlist
def get_list_videos():
    global playlist_item_by_id
    # clear ListBox
    list_box.delete(0, 'end')

    # create API object
    api = Api(api_key='AIzaSyBpW0EF6rb4fXFNBSXGfBKTGkPpVXkmy6E')

    if 'youtube' in playlistId.get():
        playlist_id = playlistId.get()[len(
            'https://www.youtube.com/playlist?list='
        ):]
    else:
        playlist_id = playlistId.get()

    # get list of video links
    playlist_item_by_id = api.get_playlist_items(
        playlist_id=playlist_id, count=None, return_json=True
        )
    
    # iterate through all video links and insert into listbox
    for index, videoid in enumerate(playlist_item_by_id['items']):
        list_box.insert(
            END, f' {str(index+1)}. {videoid['[contentDetails]']['videoId']}'
        )

    download_start.config(state=NORMAL)

# it is used for threading into tkinter
def threading():
    # call download_videos function
    t1 = Thread(target=download_videos)
    t1.start()

# it is used for downloading youtube videos
def download_videos():
    download_start.config(state='disabled')
    get_videos.config(state='disabled')

    # iterate through all seleced videos
    for i in list_box.curselection():
        videoid = playlist_item_by_id['items'][i]['contentDetails']['videoId']

        link = f'https://www.youtube.com/watch?v={videoid}'

        yt_obj = YouTube(link)

        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

        # download the highest quality video
        filters.get_highest_resolution().download()

    messagebox.showinfo('Success', 'Video Successfully Downloaded')
    download_start.config(state='normal')
    get_videos.config(state='normal')

# create object
root = Tk()

# set geometry
root.geometry('400x400')

# add label
Label(root, text='Youtube Playlist Downloader',
      font='italic 15 bold').pack(pady=10)
Label(root, text='Enter Playlist URL:', font='italic 10').pack()

# add entry box
playlistId = Entry(root, width=60)
playlistId.pack(pady=5)

# add video button
get_videos = Button(root, text='Get Videos')
get_videos.pack(pady=10)

# add scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=BOTH)
list_box = Listbox(root, selectmode='multiple')
list_box.pack(expand=YES, fill='both')
list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

# add download button
download_start = Button(root, text='Download Start', command=threading, state=DISABLED)
download_start.pack(pady=10)

# execute tkinter
root.mainloop()