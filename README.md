# 🎬 Conversor de Vídeos MKV para MP4

Um script Python simples e eficiente para converter vídeos em formato MKV para MP4 em lote.

## 📋 Pré-requisitos

- **Python 3.7+**
- **MoviePy** - biblioteca para manipulação de vídeos
- **FFmpeg** - necessário pelo MoviePy para processar vídeos

## 🚀 Instalação

### 1. Clonar ou baixar o repositório
```bash
git clone <seu-repositorio>
cd Convert_Videos
```

### 2. Instalar dependências Python
```bash
pip install -r requirements.txt
```

### 3. Instalar FFmpeg (se necessário)

**Windows (com Chocolatey):**
```bash
choco install ffmpeg
```

**Windows (manual):**
Baixar de [ffmpeg.org](https://ffmpeg.org/download.html)

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

## 💡 Como Usar

### 1. Preparar os vídeos
Crie uma pasta chamada `videos` no mesmo diretório do script:
```
Convert_Videos/
├── convert_mkv_to_mp4.py
├── README.md
├── requirements.txt
└── videos/
    ├── video1.mkv
    ├── video2.mkv
    └── ...
```

### 2. Executar o script
```bash
python convert_mkv_to_mp4.py
```

### 3. Resultado
Os arquivos convertidos serão salvos na mesma pasta `videos/` com a extensão `.mp4`:
```
videos/
├── video1.mkv
├── video1.mp4
├── video2.mkv
├── video2.mp4
└── ...
```

## 🔧 Funcionalidades

- ✅ **Conversão em lote**: Processa todos os arquivos `.mkv` da pasta automaticamente
- ✅ **Verificação de pasta**: Valida se a pasta `videos/` existe antes de processar
- ✅ **Tratamento de erros**: Continua processando mesmo se um arquivo falhar
- ✅ **Feedback visual**: Mostra progresso com símbolos emoji
- ✅ **Preserva áudio**: Utiliza codec AAC para melhor compatibilidade

## 📊 Codecs Utilizados

- **Vídeo**: H.264 (libx264)
- **Áudio**: AAC
- **Resolução**: Mantém a original do arquivo de entrada

## ⚙️ Personalização

Para modificar os codecs, abra `convert_mkv_to_mp4.py` e altere a linha:

```python
video.write_videofile(destino, codec="libx264", audio_codec="aac")
```

Opções comuns:
- `codec="libx265"` - H.265 (melhor compressão, mais lento)
- `codec="mpeg4"` - MPEG-4
- `audio_codec="libmp3lame"` - MP3

## ⚠️ Limitações e Notas Importantes

- **Tempo de processamento**: Depends da qualidade e tamanho dos vídeos
- **Espaço em disco**: Certifique-se de ter espaço suficiente para os arquivos convertidos
- **Codec H.264**: Pode não estar disponível em alguns ambientes (verifique a licença para uso comercial)

## 🐛 Troubleshooting

### "Pasta 'videos' não encontrada"
Crie a pasta `videos` no mesmo diretório do script.

### "Nenhum arquivo .mkv encontrado"
Certifique-se de que seus arquivos estão na pasta `videos` e têm a extensão `.mkv`.

### Erro de FFmpeg
Instale o FFmpeg seguindo as instruções na seção de instalação.

### Conversão muito lenta
Use `codec="libx265"` para melhor compressão ou reduza a bitrate.

## 📄 Licença

Este projeto está sob a licença incluída no arquivo LICENSE.

## 👨‍💻 Contribuições

Sugestões e melhorias são bem-vindas!

---

**Criado com ❤️ para automação de conversão de vídeos**