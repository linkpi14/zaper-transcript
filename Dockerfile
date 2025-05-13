# Estágio Final: Aplicação Python
FROM python:3.10-slim

# Definir variáveis de ambiente para evitar prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Instalar FFmpeg e git (git pode ser útil para algumas dependências pip ou para debug)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    # Limpar cache do apt para reduzir o tamanho da imagem
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho dentro do contentor
WORKDIR /app

# Copiar primeiro o requirements.txt para aproveitar o cache do Docker
COPY requirements.txt .

# Instalar as dependências Python
# --no-cache-dir para reduzir o tamanho da imagem
# --default-timeout=100 para evitar timeouts em redes lentas
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copiar todo o código da aplicação para o diretório de trabalho
# Certifique-se de que a pasta 'public' e 'app.py' estão no mesmo nível que o Dockerfile
COPY public ./public
COPY app.py .

# Variável de ambiente para a porta que o Gunicorn vai escutar.
# O Render irá definir a variável PORT, que o Gunicorn pode usar.
ENV PORT 8080
# Opcional: Definir PYTHONUNBUFFERED para que os prints apareçam nos logs do Docker/Render imediatamente
ENV PYTHONUNBUFFERED=1

# Expor a porta em que a aplicação vai correr dentro do contentor
EXPOSE 8080

# Comando para correr a aplicação usando Gunicorn (ALTERADO PARA FORMATO SHELL)
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 300 app:app
