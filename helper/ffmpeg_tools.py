import subprocess
import os

def add_watermark(input_path, output_path, watermark_path):
    cmd = ["ffmpeg", "-i", input_path, "-i", watermark_path, "-filter_complex", "overlay=10:10", output_path]
    subprocess.run(cmd)

def extract_demo(input_path, output_path):
    cmd = ["ffmpeg", "-ss", "00:00:05", "-t", "15", "-i", input_path, "-c", "copy", output_path]
    subprocess.run(cmd)