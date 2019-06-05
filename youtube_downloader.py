from tkinter import *
from tkinter import filedialog
import os
import youtube_dl

windows=Tk()
windows.title('Youtube Video Downloader')
windows.configure(background='khaki')
windows.geometry('1280x720')

def clear():
    entry1.delete(first=0,last=100)

def sel_folder():
    global filename
    global folder_path
    filename=filedialog.askdirectory()
    folder_path.set(filename)

def download():
    URL=entry1.get()
    PATH=entry2.get()
    ydl_opts={}
    os.chdir(PATH)
    with youtube_dl.YoutubeDL(ydl_opts)as ydl:
        windows.title('Downloading... ' + URL)
        ydl.download([URL])
    print(ydl_opts)
    noty = 'Your video Downloaded'
    windows.title(noty)

folder_path = StringVar()

lbl5=Label(windows,text='Youtube Video Downloader', width='25',fg='red',bg='khaki',font=('times',25,'bold'))
lbl5.place(x=400,y=80)
lbl1=Label(windows,text='Enter URL', width='15',fg='black',bg='orange',font=('times',15,'bold'))
lbl1.place(x=100,y=200)
lbl3=Label(windows,text='Select PATH', width='15',fg='black',bg='orange',font=('times',15,'bold'))
lbl3.place(x=100,y=300)
lbl6=Label(windows,text='©Kanha Janwa', width='130',fg='black',bg='chocolate1',font=('times',13,'bold'))
lbl6.place(x=0,y=650)

entry1=Entry(windows,width='50',fg='black',bg='papaya whip',font=('times',15,'italic'))
entry1.place(x=400,y=200)
entry2=Entry(windows,width='50',textvariable = folder_path,fg='black',bg='papaya whip',font=('times',15,'italic'))
entry2.place(x=400,y=300)

btn1=Button(windows,text='Clear',command=clear,width='15',fg='black',bg='sky blue',activebackground='snow')
btn1.place(x=1000,y=200)
btn3=Button(windows,text='Browse',width='15',fg='black',bg='sky blue',command = sel_folder,activebackground='snow')
btn3.place(x=1000,y=300)
btn2=Button(windows,text='Download',width='25',fg='black',bg='sky blue',activebackground='snow',command  = download)
btn2.place(x=550,y=450)


windows.mainloop()
