import json
import os
import subprocess

current_folder = os.getcwd()
ffmpeg = current_folder + "/ffmpeg.exe"
main_folder = input("缓存主目录：")
max_episode = int(input("集数："))
output_dir = current_folder + "/output/"
if os.access(output_dir, os.F_OK):
    print("Start")
else:
    os.mkdir(output_dir)

def title(episode_folder):
	episode_json = episode_folder + "/entry.json"
	file = open(episode_json,encoding='utf-8')
	load = json.loads(file.read())
	episode_title = load["page_data"]["part"]
	return episode_title

for i in range(1,max_episode):
	episode_folder = main_folder + "/" + str(i)
	episode_title = title(episode_folder)
	episode_video = episode_folder + "/16/video.m4s"
	episode_audio = episode_folder + "/16/audio.m4s"
	episode_video_new = episode_video.replace("m4s","mp4")
	episode_audio_new = episode_audio.replace("m4s","aac")
	if os.access(episode_video, os.F_OK):
		os.rename(episode_video,episode_video_new)
	if os.access(episode_audio, os.F_OK):
		os.rename(episode_audio,episode_audio_new)
	
	output_dir = current_folder + "/output/" + str(i) + "-" + episode_title + ".mp4"
	output_dir = output_dir.replace(" ","-")
	command = " -i " + episode_video_new + " -i " + episode_audio_new + " -c copy " + output_dir
	subprocess.call(ffmpeg + command)
	i = i + 1