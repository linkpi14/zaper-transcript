# Zaper Transcript – Video Transcription API

Repositório pronto para fazer deploy no **Render**.

* **FastAPI** expõe endpoints `/transcribe/url`, `/transcribe/upload`, `/jobs/{id}`, `/transcript/{id}`  
* Suporta YouTube (yt-dlp), Instagram (instagrapi) e upload direto  
* Transcreve com **WhisperX** e devolve TXT/SRT/VTT  
* Dockerfile já está na raiz ➜ não precisa configuração de monorepo

## Como testar localmente

```bash
docker compose up --build
```

Abra <http://localhost:8000/docs> para a UI Swagger.

## Deploy no Render

1. Crie um novo **Web Service** → ‘Deploy from a Git repository’.  
2. Deixe *Environment = Docker* (o Dockerfile já está na raiz).  
3. Adicione as variáveis de ambiente abaixo.  
4. Crie um **Background Worker** com o mesmo repo e comando `python -m app.worker`.

| Variável             | Descrição                                   |
|----------------------|---------------------------------------------|
| `POSTGRES_URL`       | URL de conexão do Postgres                  |
| `REDIS_URL`          | URL do Redis (ex.: `redis://default:...`)   |
| `INSTAGRAM_SESSIONID`| Cookie `sessionid` da sua conta Instagram   |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | credenciais S3     |
| `S3_BUCKET`          | Nome do bucket S3/Wasabi                    |

---

MIT License
