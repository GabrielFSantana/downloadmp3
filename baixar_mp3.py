import subprocess
import sys
from pathlib import Path

PASTA = Path(__file__).parent / "downloads"


def main():
    try:
        import yt_dlp  # noqa: F401
    except ImportError:
        print("Instalando yt-dlp...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "yt-dlp"])

    from yt_dlp import YoutubeDL

    PASTA.mkdir(exist_ok=True)
    opcoes = {
        "format": "bestaudio/best",
        "outtmpl": str(PASTA / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "postprocessors": [
            {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}
        ],
    }

    while True:
        link = input("\nCole o link do YouTube (ou Enter para sair): ").strip()
        if not link:
            break
        try:
            with YoutubeDL(opcoes) as ydl:
                ydl.download([link])
            print(f"Pronto! Salvo em: {PASTA}")
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
