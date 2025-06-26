from random import randint
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save(audio)
    playsound(audio)

# Fala a mensagem inicial
cria_audio('wellcome.mp3', 'Escolha um número entre 1 a 10')

recon = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga alguma coisa \n")
    audio = recon.listen(source)

try:
    numero_texto = recon.recognize_google(audio, language="pt-br").lower()
    print(f"Você disse: {numero_texto}")

    # Mapeamento de números por extenso e dígitos
    word_to_digit = {
        'um': 1, '1': 1,
        'dois': 2, '2': 2,
        'três': 3, '3': 3,
        'quatro': 4, '4': 4,
        'cinco': 5, '5': 5,
        'seis': 6, '6': 6,
        'sete': 7, '7': 7,
        'oito': 8, '8': 8,
        'nove': 9, '9': 9,
        'dez': 10, '10': 10
    }

    numero_digito = word_to_digit.get(numero_texto)

    if numero_digito is None:
        cria_audio("erro.mp3", f"Não entendi o número '{numero_texto}'. Tente novamente.")
    else:
        resultado = randint(1, 10)
        print(f"Número sorteado: {resultado}")

        if numero_digito == resultado:
            cria_audio("venceu.mp3", "Parabéns. Você acertou o número")
        else:
            cria_audio("perdeu.mp3", "Infelizmente você errou. Tente novamente")

except sr.UnknownValueError:
    cria_audio("erro_voz.mp3", "Não consegui entender o que você disse.")
except sr.RequestError as e:
    print(f"Erro ao acessar o serviço de reconhecimento: {e}")