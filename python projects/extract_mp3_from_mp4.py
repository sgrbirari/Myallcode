import moviepy
import moviepy.editor
vedio=moviepy.editor.VideoFileClip("D:\python\Practice_files\python projects\20211004_104655.mp4")
audio=vedio.audio
audio.write_audiofile('new_audio.mp3')

# program not running properly_07/12/22
