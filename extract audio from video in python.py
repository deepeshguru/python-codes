# -*- coding: utf-8 -*-
"""
@author: Deepesh Agrawal

"""
import sys
from moviepy.editor import *

videoclip = VideoFileClip(Filename)
audioclip = videoclip.audio
audioclip.write_audiofile("test_audio.wav")

