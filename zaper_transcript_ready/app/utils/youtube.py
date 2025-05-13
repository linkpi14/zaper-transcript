import asyncio, subprocess, os

async def fetch_youtube_audio(url: str, job_id: str) -> str:
    dest = f"/tmp/{job_id}.m4a"
    cmd = ["yt-dlp", "-f", "bestaudio", "-o", dest, url]
    process = await asyncio.create_subprocess_exec(*cmd)
    await process.communicate()
    return dest
