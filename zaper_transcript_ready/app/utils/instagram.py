import os, tempfile, subprocess
from instagrapi import Client

async def fetch_instagram_audio(url: str, job_id: str) -> str:
    cl = Client()
    cl.login_by_sessionid(os.getenv("INSTAGRAM_SESSIONID"))
    media_id = cl.media_pk_from_url(url)
    temp_dir = tempfile.mkdtemp()
    video_path = cl.video_download(media_id, folder=temp_dir)
    audio_path = os.path.join(temp_dir, f"{job_id}.m4a")
    subprocess.run(["ffmpeg","-i",video_path,"-vn","-acodec","aac", audio_path], check=True)
    return audio_path
