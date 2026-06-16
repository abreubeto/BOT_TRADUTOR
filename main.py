import os
import asyncio
from hydrogram import Client, filters
from whisper import load_model
from deep_translator import GoogleTranslator
import ffmpeg

# =====================================================================
# CONFIGURAÇÕES OBRIGATÓRIAS (Substitua com os seus dados)
# =====================================================================
API_ID = 36373217                     # Seu App api_id do my.telegram.org (sem aspas)
API_HASH = ""  # Seu App api_hash do my.telegram.org (com aspas)
BOT_TOKEN = ""     # Token do @BotFather (com aspas)
# =====================================================================

# Carrega o modelo Whisper (o modelo 'base' funciona bem para inglês)
print("Carregando modelo de Inteligência Artificial...")
model = load_model("base")

def format_time(seconds):
    """Formata o tempo para o padrão SRT de legendas (00:00:00,000)"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    msecs = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{msecs:03d}"

# Criamos a função que processará o vídeo fora para manter o escopo limpo
async def setup_handlers(app):
    @app.on_message(filters.video & filters.private)
    async def process_video(client, message):
        msg_status = await message.reply_text("📥 Baixando o vídeo enviado...")
        video_path = await message.download()
        
        await msg_status.edit_text("🤖 Transcrevendo o áudio em inglês e traduzindo para o português...")
        
        # 1. Transcreve o vídeo definindo o idioma original como inglês
        result = model.transcribe(str(video_path), language="en")
        
        # 2. Cria o arquivo SRT traduzido para português
        srt_path = "legendas_pt.srt"
        translator = GoogleTranslator(source='en', target='pt')
        
        with open(srt_path, "w", encoding="utf-8") as f:
            for i, segment in enumerate(result['segments'], start=1):
                start = format_time(segment['start'])
                end = format_time(segment['end'])
                text_en = segment['text']
                
                # Traduz o texto linha por linha
                text_pt = translator.translate(text_en)
                
                f.write(f"{i}\n{start} --> {end}\n{text_pt}\n\n")

        await msg_status.edit_text("🎬 Renderizando novas legendas em português no vídeo...")
        output_video = "video_legendado.mp4"
        
        # 3. Usa o FFmpeg para queimar a legenda traduzida no vídeo
        try:
            video_input = ffmpeg.input(str(video_path))
            audio_input = video_input.audio
            video_output = video_input.filter('subtitles', srt_path)
            
            ffmpeg.output(video_output, audio_input, output_video).run(overwrite_output=True)
            
            await msg_status.edit_text("📤 Enviando o vídeo legendado...")
            await message.reply_video(output_video)
            await msg_status.delete()
            
        except Exception as e:
            await msg_status.edit_text(f"❌ Erro ao processar o vídeo: {e}")
        
        # Limpeza de arquivos temporários criados
        for file in [video_path, srt_path, output_video]:
            if os.path.exists(file):
                os.remove(file)

async def main():
    print("Iniciando ambiente assíncrono...")
    
    # IMPORTANTE: Criamos o Client AQUI DENTRO para o Python 3.14 não quebrar.
    app = Client("tradutor_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    
    # Registra a função de receber mensagens no bot recém-criado
    await setup_handlers(app)
    
    print("Iniciando conexão com os servidores do Telegram...")
    async with app:
        print("\n==================================================")
        print("🎉 Bot online e aguardando vídeos no Telegram!")
        print("==================================================")
        # Mantém o loop ativo infinitamente
        await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        # Executa o loop assíncrono compatível com o Python 3.14+
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot desligado manualmente pelo usuário.")
