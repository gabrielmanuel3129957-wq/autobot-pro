# interface.py
import config

def iniciar_menu():
    print("=== AutoBot Pro - Assistente de Automação ===")
    
    # Pede a chave do utilizador
    chave_inserida = input("Insira a sua Chave API do 2Captcha: ").strip()
    
    if len(chave_inserida) > 10:
        config.USER_CAPTCHA_KEY = chave_inserida
        print("\nStatus: Software Ativado com Sucesso!")
    else:
        print("\nStatus: Chave API Inválida! Tente novamente.")
        return

    # Inicia a automação
    iniciar_tarefa()

def iniciar_tarefa():
    if not config.USER_CAPTCHA_KEY:
        print("Status: Erro! Insira a Chave API primeiro.")
        return
    
    print("\nStatus: A executar automação web...")
    
    import automacao
    sucesso = automacao.executar_tarefa_scraping()
    
    if sucesso:
        print("Status: Automação Concluída com Sucesso!")
    else:
        print("Status: Falha na execução ou saldo insuficiente.")

if __name__ == "__main__":
    iniciar_menu()
