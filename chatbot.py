from openai import AzureOpenAI

conversa_completa = "conversa completa, para que você consiga entender melhor o que está sendo dito:\n"

# Configurações Azure
endpoint = "https://14798-max9hw08-eastus2.cognitiveservices.azure.com/"
model_name = "gpt-4.1"            # Nome do modelo que está vinculado ao seu deployment
deployment = "gpt-4.1"            # Nome exato do deployment criado no portal
subscription_key = "COLOQUE-SUA-CHAVE-AQUI"
api_version = "2024-12-01-preview"

# Cria o cliente AzureOpenAI
client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

# Função que responde perguntas
def responder(pergunta: str) -> str:
    global conversa_completa
    try:
        conversa_completa += f"eu: {pergunta}\n"
        response = client.chat.completions.create(
            model=deployment,
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": conversa_completa},
            ],
            max_tokens=800,
            temperature=1.0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )

        resposta = response.choices[0].message.content.strip()
        conversa_completa += f"voce: {resposta}\n"
        return resposta
    except Exception as e:
        print(f"[ERRO AZURE] {e}")
        return "Erro ao processar a pergunta com a IA."


