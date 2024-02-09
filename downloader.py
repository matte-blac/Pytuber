# import required modules
from tkinter import *

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
download_start = Button(root, text='Download Start', state=DISABLED)
download_start.pack(pady=10)

# execute tkinter
root.mainloop()