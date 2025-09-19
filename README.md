Assistente de Voz (Python) – STT + TTS + Ações

Projeto bem básico de assistente virtual por voz usando Python.
Ele entende comandos falados (Speech-to-Text), fala as respostas (Text-to-Speech) e executa ações simples no navegador:

“pesquisar <termo>” → abre a Wikipédia do termo

“youtube <termo>” → pesquisa o termo no YouTube

“farmácia” → abre o mapa com farmácias próximas

“sair / fechar / encerrar” → termina o programa

Código principal: assistant.py
Bibliotecas: SpeechRecognition, PyAudio, pyttsx3, webbrowser
