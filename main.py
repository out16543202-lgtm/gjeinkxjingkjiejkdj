from moviepy.editor import *
from gtts import gTTS
import os

# Define paths
input_video_path = "input/your_long_movie.mp4"
output_video_path = "output/short_video.mp4"
voice_text = "你的中文配音文本在这里"
subtitle_text = "中文字幕在这里"

# Load the long video
video = VideoFileClip(input_video_path).subclip(0, 240)  # Get the first 4 minutes

# Resize video to 9:16
video_resized = video.resize(height=1080).crop(x_center=video.w/2, y_center=video.h/2, width=video.h*(9/16), height=video.h)

# Create voiceover
tts = gTTS(text=voice_text, lang='zh')
voiceover_path = "output/voiceover.mp3"
tts.save(voiceover_path)
voiceover = AudioFileClip(voiceover_path)

# Set voiceover audio to video
video_with_audio = video_resized.set_audio(voiceover)

# Add subtitles (you would add actual text and timing here)
subtitles = TextClip(subtitle_text, fontsize=24, color='white').set_position('bottom').set_duration(video_with_audio.duration)

# Combine everything
final_video = CompositeVideoClip([video_with_audio, subtitles])

# Write the result to a file
final_video.write_videofile(output_video_path, codec='libx264', audio=True)

# Clean up temporary voiceover file
os.remove(voiceover_path)
