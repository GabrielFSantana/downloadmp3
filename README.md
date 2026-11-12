# downloadmp3

Script simples em Python para baixar o áudio de vídeos do YouTube em MP3, usando [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Requisitos

- [Python 3](https://www.python.org/downloads/) (no Windows, marque "Add Python to PATH" na instalação)
- [FFmpeg](https://ffmpeg.org/download.html) disponível no PATH, usado para converter o áudio em MP3

O `yt-dlp` é instalado automaticamente na primeira execução, caso ainda não esteja.

## Como usar

No Windows, dê dois cliques em `baixar_mp3.bat`. Em qualquer sistema, também dá para rodar pelo terminal:

```bash
python baixar_mp3.py
```

Depois:

1. Cole o link do vídeo e aperte Enter.
2. Aguarde o download e a conversão.
3. Cole outro link, ou aperte Enter com o campo vazio para sair.

Os arquivos são salvos na pasta `downloads/`, ao lado do script, em MP3 a 192 kbps, com o título do vídeo como nome.

## Observações

- Se o link for de uma playlist, apenas o vídeo do link é baixado.
- Se aparecer erro de conversão, verifique se o FFmpeg está instalado: `ffmpeg -version`.
- Se o YouTube passar a recusar os downloads, atualize o yt-dlp: `python -m pip install -U yt-dlp`.

## Aviso

Use apenas com conteúdo que você tem direito de baixar, respeitando os direitos autorais e os termos de uso do YouTube.
