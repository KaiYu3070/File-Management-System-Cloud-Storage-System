import os
import subprocess
import yt_dlp


def download_video_and_audio(url, output_dir):
    # 使用 yt-dlp 下载视频和音频
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # 下载最佳视频和音频
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # 保存路径
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def merge_video_audio_ffmpeg(video_file, audio_file, output_file):
    print("开始合并视频和音频...")

    # 检查音频文件是否存在
    if not os.path.exists(audio_file):
        print(f"音频文件不存在: {audio_file}")
        download_progress['error'] = True
        download_progress['error_message'] = f"音频文件未找到: {audio_file}"
        return

    # 使用绝对路径
    video_file = os.path.abspath(video_file)
    audio_file = os.path.abspath(audio_file)
    output_file = os.path.abspath(output_file)

    # 构造 FFmpeg 命令
    ffmpeg_command = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-y',
        output_file
    ]

    # 执行命令
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

    # 实时读取输出并显示进度
    for line in iter(process.stdout.readline, ''):
        line = line.strip()
        if line.startswith('out_time='):
            print(line)  # 输出 FFmpeg 的进度信息

    # 等待进程结束并获取返回码
    stdout, stderr = process.communicate()
    print(stdout)  # 打印标准输出
    print(stderr)  # 打印错误输出

    if process.returncode == 0:
        print(f"合并完成，保存为: {output_file}")
        download_progress['merging'] = False
        download_progress['complete'] = True
    else:
        print(f"合并失败，返回码：{process.returncode}")
        download_progress['merging'] = False
        download_progress['error'] = True
        download_progress['error_message'] = f"合并失败，返回码：{process.returncode}，错误信息：{stderr}"


# 示例调用
url = "https://youtu.be/BE9pTVhUOvg?si=8juG4gLXdC4shtBT"
output_dir = "/Users/kawsar/PycharmProjects/dj_data"
download_video_and_audio(url, output_dir)

# 生成音频和视频文件路径
video_file = os.path.join(output_dir, "Custom Bikes and Models： Full Throttle, Leesburg, Fl  Bike Expo 2024.mp4")
audio_file = os.path.join(output_dir, "Custom Bikes and Models： Full Throttle, Leesburg, Fl  Bike Expo 2024.m4a")
output_file = os.path.join(output_dir, "Merged_Custom_Bikes_and_Models.mp4")

# 调用合并函数
merge_video_audio_ffmpeg(video_file, audio_file, output_file)


def progress_hook(d):
    global download_progress
    if d['status'] == 'downloading':
        download_progress["percent"] = float(d.get('_percent_str', '0.00%').replace('%', ''))
        download_progress["eta"] = format_eta(d.get('eta'))
        print(f"下载进度: {download_progress['percent']}%, ETA: {download_progress['eta']}")
    elif d['status'] == 'finished':
        download_progress["downloading"] = False
        download_progress["merging"] = True
        print("下载完成，开始合并...")

def format_eta(eta):
    # 这里可以格式化 ETA 输出，比如转换为分钟/秒等格式
    return f"{eta:.2f}秒" if eta is not None else "未知"
