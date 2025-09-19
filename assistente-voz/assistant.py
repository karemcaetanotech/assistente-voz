import webbrowser
import pyttsx3
import speech_recognition as sr

# --- TTS ---
tts = pyttsx3.init()
def speak(text: str):
    tts.say(text)
    tts.runAndWait()

# --- STT ---
rec = sr.Recognizer()
def listen() -> str:
    with sr.Microphone() as mic:
        speak("Pode falar.")
        audio = rec.listen(mic)
    try:
        text = rec.recognize_google(audio, language="pt-BR")
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Falha no serviço de reconhecimento.")
        return ""

# --- Ações ---
def abrir_wikipedia(termo: str):
    url = f"https://pt.wikipedia.org/wiki/{termo.replace(' ', '_')}"
    webbrowser.open(url)

def abrir_youtube(termo: str):
    url = f"https://www.youtube.com/results?search_query={termo.replace(' ', '+')}"
    webbrowser.open(url)

def abrir_farmacia_perto():
    webbrowser.open("https://www.google.com/maps/search/farmacia/")

if __name__ == "__main__":
    speak("Assistente iniciado. Diga: pesquisar <termo>, youtube <termo> ou farmácia.")
    while True:
        comando = listen()
        if not comando:
            speak("Não entendi. Repita, por favor.")
            continue

        if comando.startswith("pesquisar") or comando.startswith("pesquisa"):
            termo = comando.replace("pesquisar", "").replace("pesquisa", "").strip()
            if termo:
                speak(f"Abrindo Wikipédia para {termo}.")
                abrir_wikipedia(termo)
            else:
                speak("Diga o que deseja pesquisar.")

        elif comando.startswith("youtube"):
            termo = comando.replace("youtube", "").strip()
            if termo:
                speak(f"Abrindo YouTube para {termo}.")
                abrir_youtube(termo)
            else:
                speak("Diga o que deseja assistir no YouTube.")

        elif "farmácia" in comando:
            speak("Abrindo mapa com farmácias próximas.")
            abrir_farmacia_perto()

        elif comando in ("sair", "fechar", "encerrar"):
            speak("Até mais!")
            break
        else:
            speak("Comando não reconhecido. Tente: pesquisar, youtube ou farmácia.")
