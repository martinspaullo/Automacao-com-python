from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sys
import os

# Importa funções auxiliares de módulos personalizados
import funcoes_so
import funcoes_noticias
import funcoes_moedas


# Converte texto em áudio, reproduz o som e remove o arquivo temporário
def criar_audio(nome_arquivo, texto):
    tts = gTTS(texto, lang='pt-br')
    tts.save(nome_arquivo)
    playsound(nome_arquivo)
    os.remove(nome_arquivo)

# Captura áudio do microfone e transforma em texto usando reconhecimento de voz
def escutar_microfone():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga alguma coisa...")
        while True:
            audio = reconhecedor.listen(source)
            try:
                comando = reconhecedor.recognize_google(audio, language='pt-br').lower()
                print(f"Você disse: {comando}")
                executar_comando(comando)
                return comando
            except sr.UnknownValueError:
                # Ignora se não entender o que foi dito
                print("Não entendi. Tente novamente.")
            except sr.RequestError:
                # Ignora falha de conexão com o serviço de reconhecimento
                print("Erro de conexão com o serviço de reconhecimento.")

# Executa ações com base no comando de voz reconhecido
def executar_comando(comando):
    if 'fechar assistente' in comando:
        sys.exit()

    elif 'horas' in comando:
        hora_atual = funcoes_so.verifica_hora()
        criar_audio('mensagem.mp3', hora_atual)

    elif 'desligar computador' in comando:
        if 'uma hora' in comando:
            funcoes_so.desliga_computador_uma_hora()
        elif 'meia hora' in comando:
            funcoes_so.desliga_computador_meia_hora()

    elif 'cancelar desligamento' in comando:
        funcoes_so.cancela_desligamento()

    elif 'notícias' in comando:
        noticias = funcoes_noticias.ultima_noticias()
        criar_audio('mensagem.mp3', noticias)

    elif 'cotação' in comando:
        if 'dólar' in comando:
            cotacao = funcoes_moedas.cotacao_moeda('Dólar')
            criar_audio('mensagem.mp3', cotacao)
        elif 'euro' in comando:
            cotacao = funcoes_moedas.cotacao_moeda('Euro')
            criar_audio('mensagem.mp3', cotacao)
        elif 'bitcoin' in comando:
            cotacao = funcoes_moedas.cotacao_moeda('Bitcoin')
            criar_audio('mensagem.mp3', cotacao)

# Função principal que inicia o assistente virtual
def main():
    criar_audio("welcome.mp3", "Olá, sou a Paulete. Em que posso lhe ajudar?")
    while True:
        escutar_microfone()

# Inicia o programa
if __name__ == "__main__":
    main()