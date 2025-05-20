from chatbot import Chatbot

def main():
    bot = Chatbot()
    print("Olá! Sou o assistente virtual da TechStore.")
    print(bot.menu_opcoes())  # Exibe menu ao iniciar

    while True:
        entrada = input("\nVocê: ")
        resposta = bot.responder(entrada)
        print("\nBot:", resposta)

        if "até mais" in resposta.lower():
            break
        else:
            print(bot.menu_opcoes())  # Exibe o menu novamente após cada resposta

if __name__ == "__main__":
    main()
