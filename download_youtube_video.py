from pytube import YouTube

# where to save
SAVE_PATH = "D:\\Learning_videos\\"  # to_do

# link of the video to be downloaded
# opening the file

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=7t2alSnE2-I"
from pytube import YouTube

yt = YouTube(link)

# Showing details
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
# Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
