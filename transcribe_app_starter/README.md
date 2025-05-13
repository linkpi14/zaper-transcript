# Video Transcription Service

Starter repository for a self‑hosted API that downloads videos from **YouTube**, **Instagram** or direct upload,
extracts the audio and returns a **Whisper** transcription in `txt`, `srt` or `vtt`.

Powered by **FastAPI**, **RQ** workers and Docker. Deployable on **Render** in one click.

## Features

* `/transcribe/url` – pass a YouTube/Instagram URL and get back a job ID  
* `/transcribe/upload` – multipart file upload (up to 500 MB by default)  
* `/jobs/{id}` – polling endpoint for job status  
* `/transcript/{id}?fmt=srt` – download the transcript

### Supported sources

| Source      | How it’s fetched                           |
|-------------|-------------------------------------------|
| YouTube     | `yt‑dlp` best‑audio stream                |
| Instagram   | `instagrapi` (requires session cookie)    |

## Local development

```bash
docker compose up --build
```

## Render deployment

1. **Create a new Web Service** ➜ “Deploy from a Git repository”.  
2. Point to this repo, leave the Docker command as default.  
3. Add the environment variables shown below.  
4. (Optional) add a second *Background Worker* service running `python -m app.worker`.

## Environment variables

| Name | Description |
|------|-------------|
| `POSTGRES_URL` | e.g. `postgresql://user:password@host:5432/db` |
| `REDIS_URL`    | e.g. `redis://default:password@host:6379` |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | S3/Wasabi credentials |
| `S3_BUCKET` | bucket name for storing transcripts |
| `INSTAGRAM_SESSIONID` | value of your `sessionid` cookie |

## License

MIT
