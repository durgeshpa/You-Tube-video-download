"""using python gui application create you tube video downloade ..."""
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
# from    urllib import urlopen
from pytube import YouTube
# from functools import partial


# txt = tk.StringVar()
# txt ='please wait ........'
class GUI(tk.Tk):
    """'Python GUI .."""

    def __init__(self):
        """Intilize all resources.."""
        super().__init__()
        self.title('python downloader')
        self.geometry('400x400')

    def guisetup(self):
        """GUI configration .."""
        root.grid_columnconfigure(0, weight=1)
        youtubelinklabel = tk.Label(self, text="enter you tube link please",
                                    fg='green', font='bold 15', bg='black')
        youtubelinklabel.grid()
        # input url
        self.youtube_video_url = tk.StringVar()
        input_box = tk.Entry(self, width=40,
                             textvariable=self.youtube_video_url,
                             font='bold 12')
        input_box.grid(pady=(4, 10), ipady=3)
        # user not set url then error will show
        self.youtube_video_url_error = tk.Label(self, text='', fg='red',
                                                font='bold 24', bg='black')
        self.youtube_video_url_error.grid(pady=(0, 10))
        # download video path label
        path = tk.Label(self, text='please select file path',
                        fg='blue', font='bold 15', bg='black')
        path.grid(pady=(0, 3))

        path_directory = tk.Button(self, width=20, text=" chose folder",
                                   bg='green', fg='red',
                                   command=self.open_file_path,
                                   font='lucida 17')
        path_directory.grid(pady=(20, 7))

        self.file_path_label = tk.Label(self, text='', bg='black')
        self.file_path_label.grid(pady=(5, 5))

        txt = 'please select video download option'
        video_option_label = tk.Label(self, text=txt, bg='black')
        video_option_label.grid(pady=(5, 5))

        self.download_video_option = ["MP4_720p",
                                      "Mp4_360p",
                                      "Video_3gp",
                                      "Song_MP3"]
        self.youtube_option = ttk.Combobox(self,
                                           values=self.download_video_option,
                                           width=30,)
        self.youtube_option.current(0)

        self.youtube_option.grid(ipady=10)

        download_button = tk.Button(self, text='download', fg='blue',
                                    bg='red', command=self.download_video)
        download_button.grid(pady=(15, 10))

        '''self.progressbar = ttk.Progressbar(root, orient="horizontal",
                                           length=300, mode='determinate',
                                           bg='black')
        self.progressbar.grid(pady=(2, 3))
        self.progressbar['maximum'] = 100'''

        self.download_label = tk.Label(self,
                                       text='Delvoped By DURGESH PATEL',
                                       fg='green', bg='black', font='bold 17')
        self.download_label.grid()

    def progress(self, stream=None, chunk=None, file_handle=0,
                 bytes_remaining=0):
        """How much video are dowmloaded .."""
        percent = int(100 * (self.file_size_in_bytes - file_handle) / self.file_size_in_bytes)
        print("down load" + str(percent) + "%")
        self.progressbar['value'] = percent
        self.progressbar.update()

    def complete(self):
            """After down load compltion video ..."""
            self.download_label.config(text='downloading complete')
            self.progressbar['value'] = 0
            self.progressbar.update()


class GuiPython(GUI):
    """Python gui class .."""

    def __init__(self):
        """Class variable for intialization .."""
        super().__init__()
        self.folder = ""
        self.file_size_in_bytes = 0
        self.max_file_size = 0

    def open_file_path(self):
        """File path where video will download .."""
        self.folder = filedialog.askdirectory()
        if len(self.folder) > 1:
            self.file_path_label.config(text=self.folder, fg='blue',
                                        font='lucida 12')
        else:
            self.file_path_label.config(text='select folder name', fg='blue')

    def download_video(self):
        """Download video logic .."""
        option = self.youtube_option.get()
        video_url = self.youtube_video_url.get()
        if len(video_url) > 1:
            self.youtube_video_url_error.config(text="")
            print(self.folder)
            video = YouTube(video_url, on_progress_callback=self.progress)
            print("Video Name is:\n\n", video.title)
            if option == self.download_video_option[0]:
                self.download_label.config(text='downloading video in 720p ..')
                video_download = video.streams.get_by_itag(22)
            elif option == self.download_video_option[1]:
                self.download_label.config(text='downloading video in mp4')
                video_download = video.streams.get_by_itag(18)
            elif option == self.download_video_option[2]:
                self.download_label.config(text='downloading video in 3gp')
                video_download = video.streams.get_by_itag(36)
            elif option == self.download_video_option[3]:
                self.download_label.config(text='downloading audio')
                video_download = video.streams.filter(only_audio=True).first()
            # Calculating file size
            self.file_size_in_bytes = video_download.filesize
            self.max_file_size = self.file_size_in_bytes / 1024000
            print("File Size = {:00.00f} MB".format(self.max_file_size))

            self.progressbar = ttk.Progressbar(root, orient="horizontal",
                                               length=300, mode='determinate',
                                               )
            self.progressbar.grid(pady=(2, 3))
            self.progressbar['maximum'] = 100

            video_download.download(self.folder)
            self.complete()
        else:
            txt = "enter youtube link please."
            self.youtube_video_url_error.config(text=txt,
                                                fg='red')


if __name__ == '__main__':
    root = GuiPython()
    root.configure(background='black')
    root.guisetup()

    root.mainloop()
