# 🎬 Bot Tradutor de Legendas para Telegram

Olá! Seja muito bem-vindo(a) ao projeto **Bot Tradutor de Legendas - Telegram**! 🚀

Este é um bot automatizado para o Telegram que resolve um problema muito comum: traduzir e legendar vídeos automaticamente. Se você recebeu ou tem um vídeo com áudio em **inglês**, basta enviá-lo para este bot no chat privado. Ele vai baixar a mídia, transcrever o áudio com Inteligência Artificial, traduzir tudo para o **português** e te devolver o vídeo pronto com as legendas embutidas ("queimadas") na tela.

---

## ✨ Funcionalidades

* 📥 **Download Automático:** Monitora o chat e baixa vídeos enviados diretamente a ele.
* 🤖 **Transcrição Inteligente:** Utiliza o modelo **Whisper da OpenAI** para reconhecer o áudio em inglês com altíssima precisão.
* 🌐 **Tradução Automática:** Traduz as linhas de diálogo para o português de forma fluida.
* 🎬 **Legendas Fixas (Hardsub):** Usa o poder do **FFmpeg** para embutir as legendas diretamente no arquivo de vídeo final.

---

## 🛠️ Pré-requisitos do Sistema

Antes de começar, você precisará ter instalado no seu computador:

1. **Python:** Versão 3.9 ou superior (Totalmente compatível com Python 3.14+).
2. **FFmpeg:** Essencial para que o script consiga colar as legendas no vídeo.
   * **Windows:** Baixe no site oficial e adicione a pasta `bin` às Variáveis de Ambiente do seu sistema.
   * **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install ffmpeg -y`
   * **Mac:** `brew install ffmpeg`

---

## 📥 Instalação

Siga o passo a passo abaixo para colocar o projeto para rodar na sua máquina:

### 1. Clonar o repositório
```bash
git clone https://github.com
cd NOME_DO_REPOSITORIO
```

### 2. Instalar as dependências do Python
Abra o seu terminal na pasta do projeto e instale as bibliotecas necessárias executando o comando abaixo:
```bash
pip install hydrogram tgcrypto openai-whisper deep-translator ffmpeg-python torch
```

### 3. Configurar as suas Credenciais
Abra o arquivo `main.py` em seu editor de código e substitua as variáveis no topo com os seus dados reais obtidos no [my.telegram.org](https://telegram.org) e com o [@BotFather](https://t.me):

```python
API_ID = 1234567                     # Seu App api_id (apenas números, sem aspas)
API_HASH = "seu_api_hash_real_aqui"  # Seu App api_hash (com aspas)
BOT_TOKEN = "seu_bot_token_aqui"     # Token do seu Bot no BotFather (com aspas)
```

---

## 🚀 Como Executar

Com tudo configurado e o FFmpeg devidamente instalado no sistema, basta iniciar o script pelo terminal:

```bash
python main.py
```

Quando você visualizar a mensagem abaixo no terminal, o seu bot estará pronto para a ação:
```text
==================================================
🎉 Bot online e aguardando vídeos no Telegram!
==================================================
```

### 📱 Como usar no Telegram:
1. Vá até o chat do bot que você criou.
2. Clique em **/start** (ou Começar).
3. Envie qualquer vídeo que possua diálogos ou falas em **inglês**.
4. Aguarde o bot processar e receba o seu vídeo traduzido e legendado em **português**! 🍿

---

## 💡 Dicas de Desempenho

* **Primeira Execução:** Na primeira vez que você enviar um vídeo, o script fará o download do modelo da IA Whisper (cerca de 139MB). Isso acontece apenas uma vez automaticamente.
* **Placa de Vídeo (Opcional):** Se o seu computador possuir uma placa de vídeo dedicada da NVIDIA configurada com suporte a CUDA, a transcrição dos vídeos será feita em poucos segundos de forma extremamente rápida! Caso use apenas o processador (CPU), o processo funcionará perfeitamente, mas levará um pouco mais de tempo.

---

Feito com 💙 para facilitar a acessibilidade e tradução de conteúdos de vídeo! Sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request* caso queira contribuir com melhorias para o projeto.
