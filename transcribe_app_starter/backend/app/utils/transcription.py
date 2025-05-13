import whisperx, os, subprocess, json

async def transcribe_audio(path: str, job_id: str):
    model = whisperx.load_model("medium")
    result = model.transcribe(path)
    # Save outputs
    out_dir = f"/tmp/{job_id}"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "transcript.txt"), "w") as f:
        f.write(result["text"])
    model.write_srt(result, os.path.join(out_dir, "transcript.srt"))
    model.write_vtt(result, os.path.join(out_dir, "transcript.vtt"))
    # TODO: upload to S3 & update DB
