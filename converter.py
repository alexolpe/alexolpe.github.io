from moviepy.editor import VideoFileClip

def convert_avi_to_mp4(input_path, output_path):
    video = VideoFileClip(input_path)
    video.write_videofile(output_path, codec='libx264', audio_codec="aac")

# Example usage
input_file = '/data/aolivepe/web/resrgan/125.1_out.avi'
output_file = '/data/aolivepe/web/resrgan/125.1_out.mp4'
convert_avi_to_mp4(input_file, output_file)