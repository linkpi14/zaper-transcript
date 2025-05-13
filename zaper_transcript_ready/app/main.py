from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from pydantic import BaseModel
import uuid, os, asyncio

from .utils.youtube import fetch_youtube_audio
from .utils.instagram import fetch_instagram_audio
from .utils.transcription import transcribe_audio

app = FastAPI(title="Zaper Transcript API")

class URLPayload(BaseModel):
    url: str

@app.post("/transcribe/url")
async def transcribe_url(payload: URLPayload, background_tasks: BackgroundTasks):
    job_id = uuid.uuid4().hex
    background_tasks.add_task(process_url, payload.url, job_id)
    return {"job_id": job_id, "status": "queued"}

async def process_url(url: str, job_id: str):
    if "youtube.com" in url or "youtu.be" in url:
        audio_path = await fetch_youtube_audio(url, job_id)
    elif "instagram.com" in url:
        audio_path = await fetch_instagram_audio(url, job_id)
    else:
        raise ValueError("Unsupported URL")
    await transcribe_audio(audio_path, job_id)

@app.post("/transcribe/upload")
async def transcribe_upload(file: UploadFile = File(...)):
    job_id = uuid.uuid4().hex
    dest = f"/tmp/{job_id}_{file.filename}"
    with open(dest, "wb") as f:
        f.write(await file.read())
    await transcribe_audio(dest, job_id)
    return {"job_id": job_id, "status": "processing"}
