# automacao.py
import time
import requests
import config

def enviar_captcha_para_resolver(site_key, url_da_pagina):
    print("[AutoBot] A preparar envio do captcha...")
    
    payload = {
        'key': config.USER_CAPTCHA_KEY,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': url_da_pagina,
        'soft_id': config.DEVELOPER_ID,
        'json': 1
    }
    
    try:
        resposta = requests.post("https://2captcha.com/in.php", data=payload).json()
        
        if resposta.get("status") == 1:
            captcha_id = resposta.get("request")
            print(f"[AutoBot] Captcha enviado com sucesso! ID: {captcha_id}. A aguardar resolução...")
            return captcha_id
        else:
            print(f"[AutoBot] Erro ao enviar captcha: {resposta.get('request')}")
            return None
    except Exception as e:
        print(f"[AutoBot] Erro de conexão: {e}")
        return None

def obter_resultado_captcha(captcha_id):
    url_verificacao = f"https://2captcha.com/res.php?key={config.USER_CAPTCHA_KEY}&action=get&id={captcha_id}&json=1"
    
    for tentativa in range(20):
        time.sleep(5)  
        try:
            resposta = requests.get(url_verificacao).json()
            if resposta.get("status") == 1:
                token_resolvido = resposta.get("request")
                print("[AutoBot] Captcha resolvido pelos servidores do 2Captcha!")
                return token_resolvido
            elif resposta.get("request") == "CAPCHA_NOT_READY":
                print("[AutoBot] O captcha ainda está a ser resolvido... a aguardar...")
            else:
                print(f"[AutoBot] Erro na resolução: {resposta.get('request')}")
                return None
        except Exception as e:
            print(f"[AutoBot] Erro ao verificar status: {e}")
            return None
            
    print("[AutoBot] Tempo limite esgotado para resolver o captcha.")
    return None

def executar_tarefa_scraping():
    site_alvo_url = "https://exemplo-loja-protegida.com/produtos"
    site_captcha_key = "6LeHx_gUAAAAAL7To..." 
    
    id_do_captcha = enviar_captcha_para_resolver(site_captcha_key, site_alvo_url)
    
    if id_do_captcha:
        token_final = obter_resultado_captcha(id_do_captcha)
        
        if token_final:
            print(f"[AutoBot] Token obtido: {token_final[:20]}...")
            print("[AutoBot] A injetar o token no navegador e a extrair os dados com sucesso!")
            return True
            
    return False
