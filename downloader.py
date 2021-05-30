from tkinter import *
from tkinter import ttk
from tkinter import  filedialog
from pytube import YouTube

folder_name="."
file_size_in_bytes=0
max_file_size=0

def open_directory(event=None):
    global folder_name
    folder_name=filedialog.askdirectory()y
    print(folder_name)
    if len(folder_name)>1: file_location_error.config(text=f'[output] {folder_name}',font=('Arial',12),fg='green')
    else: file_location_error.config(fg='red',font=('Agency FB',18),text='Select any folder to save the file')

def download_file(event=None):
    global max_file_size,file_size_in_bytes
    choices=youtube_choices.get()
    video_url =edt_url_input.get()
    selectVideo=None
    if len(video_url)>1:
        labl_error.config(text=f'[output]/{video_url}')
        yt =YouTube(video_url, on_progress_callback=progress_functio,
                     )
        print("[Title ] {yt.title}" )
        
        if(choices == download_choises[0]):
            print("720p Video is downloading..")
            loading_label.config(text="720p Formato a baixar")
            selectVideo = yt.streams.filter(progressive=True).first() # escolhe do primeiro formato de video
            file_size_in_bytes = selectVideo.filesize
            max_file_size = file_size_in_bytes/1024000
            MB = str(max_file_size)+"MB"
            print("File size = :{max_file_size:00.00f}")
        elif(choices ==download_choises[1]):
            print("144p foi escolhido pra o download")
            loading_label.config(text="144p formato escohido")
            selectVideo = yt.streams.filter(progressive=True).last() # escolhe do primeiro formato de video
            file_size_in_bytes = selectVideo.filesize
            max_file_size = file_size_in_bytes/1024000
            MB = str(max_file_size)+"MB"
            print(f"File size = :{max_file_size:00.00f}")
        elif(choices ==download_choises[2]):
            print('3gp video is downloading..')
            selectVideo =yt.streams.filter(file_extension="3gp").first()
            file_size_in_bytes = selectVideo.filesize
            max_file_size = file_size_in_bytes/1024000
            MB = str(max_file_size)+"MB"
            print(f"File size = :{max_file_size:00.00f}")
        elif(choices ==download_choises[3]):
            print("Voce escolheu o formato de audio")
            selectVideo =yt.streams.filter(only_audio=True).first()
            file_size_in_bytes = selectVideo.filesize
            max_file_size = file_size_in_bytes/1024000
            MB = str(max_file_size)+"MB"
            print(f"File size = :{max_file_size:00.00f}")
        else:
            print('sect first inputs')
    else:
        print("past best url")
    
    # now download file selected
    selectVideo.download(folder_name)
    print('Download on :{ }')
    progress_bar.config(max=max_file_size)
    complete_download()
c=1
# este metodo sera chamdo quando o progresso do download esta sendo exceutado
def progress_functio(streams=None, chunk =None, file_handler=None, remaining_file_size=None):
    global c
    print(file_handler)
    c+=0.12
    percentagem =(100 * (file_size_in_bytes - remaining_file_size))/file_size_in_bytes
    print(f" {percentagem:00.0f}% downloade")
    progress_bar.config(value=percentagem)

# quando terminar o download
def complete_download():
    loading_label.config(text="Downloaded complete...")
    ...

root=Tk()
root.title("Youtube Video downloader")
root.grid_columnconfigure(0, weight=1)
youtubeLinkLabel=Label(root, text="Please past your Link hel", fg="blue", font=('Agency FB',16))
youtubeLinkLabel.grid(padx=20)

edt_url_var=StringVar()
edt_url_input=ttk.Entry(root, width=50, textvariable=edt_url_var)
edt_url_input.grid(pady=(0,20), padx=(20,20))

labl_error=Label(root, fg='red', text='select file please', font=('Helvetica',30))
labl_error.grid(pady=(0,10))
saveLabel =Label(root, text="Where to download file? ", fg='blue',font=('Agency FB',20,'bold'))
saveLabel.grid()

saveEntry =Button(root, width=20, bg='green', fg='white',text='Choose folder', font=('Arial',15),command=open_directory)
saveEntry.grid()

file_location_error=Label(root,text="",font=('Agency FB',20))
file_location_error.grid(pady=(5,5),padx=20)

chooselabel=Label(root, text='Please choose what to download', font=('Agency FB',20))
chooselabel.grid()

download_choises=['p 720p  ',
                  'Mp4 144p',
                  'Video 3gp',
                  'song mp3 ']

youtube_choices =ttk.Combobox(root,values=download_choises)
youtube_choices.grid(ipadx=50)

download_btn=ttk.Button(root, text="Download",command=download_file)
download_btn.grid(ipadx=60,pady=20,padx=20)
progress_bar =ttk.Progressbar(root,orient=HORIZONTAL,value=10) #orient, length, mode, maximum, value, variable, phase
progress_bar.grid(ipadx=40)
loading_label=ttk.Label(root,text="app developed by | @tylorGuy")
loading_label.grid(ipadx=10,padx=10)

root.mainloop()