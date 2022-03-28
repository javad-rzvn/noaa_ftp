import os
import time
from ftplib import FTP
from tqdm import tqdm
# pip install progressbar2
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, UnknownLength


class NOAA:
    def __init__(self, url):
        self.url = url


    def dir(self):
        download_url = self.url
        with urllib.request.urlopen(download_url) as r:
            data = r.read().splitlines()

        for l in data:
            print (l)


    def download(self, folder_path, filename):
        global pbar, i
        ftp = FTP(self.url)
        ftp.login()
        ftp.cwd(folder_path)
        # ftp.retrlines('LIST')
        
        def file_write(data):
            global pbar
            localfile.write(data)
            pbar += len(data)

        localfile = open(filename, 'wb')
        remote_file = filename
        ftp.voidcmd('TYPE I')
        file_size = ftp.size(remote_file)
        widgets = ['Downloading: ', Percentage(), ' ', Bar(marker='#', \
            left='[',right=']'), ' ', ETA(), ' ', FileTransferSpeed()]
        pbar = ProgressBar(widgets=widgets, maxval=file_size)
        pbar.start()
        
        ftp.retrbinary("RETR " + remote_file, file_write)