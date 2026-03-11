from moviepy import VideoFileClip
import os

def converter_mkv_para_mp4(arquivo_mkv, destino=None):
    """
    Converte um vídeo .mkv para .mp4.

    :param arquivo_mkv: Caminho do arquivo MKV de entrada.
    :param destino: Caminho de saída (opcional). Se não for informado, salva no mesmo diretório.
    :return: Caminho do arquivo convertido (.mp4)
    """
    if not arquivo_mkv.lower().endswith(".mkv"):
        raise ValueError("O arquivo de entrada deve ter a extensão .mkv")

    # Define nome de saída
    if destino is None:
        destino = os.path.splitext(arquivo_mkv)[0] + ".mp4"

    print(f"🔄 Convertendo '{arquivo_mkv}' para '{destino}'...")

    # Carrega e converte
    with VideoFileClip(arquivo_mkv) as video:
        video.write_videofile(destino, codec="libx264", audio_codec="aac")

    print("✅ Conversão concluída com sucesso!")
    return destino

# Exemplo de uso:
if __name__ == "__main__":
    # Define pasta de vídeos
    pasta_videos = "videos"
    
    # Verifica se a pasta existe
    if not os.path.exists(pasta_videos):
        print(f"❌ Pasta '{pasta_videos}' não encontrada!")
        print(f"📁 Por favor, crie a pasta '{pasta_videos}' e adicione seus arquivos .mkv nela.")
    else:
        # Lista todos os arquivos .mkv na pasta
        arquivos_mkv = [f for f in os.listdir(pasta_videos) if f.lower().endswith(".mkv")]
        
        if not arquivos_mkv:
            print(f"⚠️ Nenhum arquivo .mkv encontrado na pasta '{pasta_videos}'")
        else:
            print(f"📁 Encontrados {len(arquivos_mkv)} arquivo(s) .mkv para converter:\n")
            
            # Converte cada arquivo
            for arquivo in arquivos_mkv:
                caminho_entrada = os.path.join(pasta_videos, arquivo)
                try:
                    converter_mkv_para_mp4(caminho_entrada)
                    print()
                except Exception as e:
                    print(f"❌ Erro ao converter '{arquivo}': {str(e)}\n")
