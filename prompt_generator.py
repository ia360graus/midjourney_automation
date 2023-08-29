import openai

# Inserir sua chave API aqui
openai.api_key = ''

# Função para ler o system prompt do arquivo
def ler_system_prompt(arquivo):
    with open(arquivo, "r") as file:
        return file.read()

# Perguntando ao usuário sobre a quantidade de prompts e o tema das imagens
quantidade_prompts = int(input("Quantos prompts você gostaria de gerar? "))
tema_imagem = input("Qual é o tema da imagem que você gostaria de usar? ")

# Lendo o system prompt do arquivo
system_prompt = ler_system_prompt("midjourney_system_prompt.txt")

# Texto base para o prompt do usuário
user_prompt_text = f"Gere {quantidade_prompts} prompts para imagens com o tema de {tema_imagem} de tirar o fôlego, certifique de sempre gerar imagens diferentes, seja criativo. Gere uma lista com um comando em baixo do outro. Gere imagens que gerem interesse nas pessoas. Certifique-se de ser detalhista nos prompts. Certifique-se de sempre gerar prompts diferentes. Certifique de não gerar imagens com crianças. Todos os prompts devem começar com /imagine prompt:"

# Criando a conversa com a API
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  max_tokens=2000,
  messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_text}
    ]
)

# Extraindo os prompts
prompts = response.choices[0].message['content'].split("\n")
prompts = [prompt for prompt in prompts if prompt.startswith("/imagine prompt:")]

# Salvando os prompts no arquivo
with open("prompts_midjourney.txt", "a") as file:
    file.write("\n".join(prompts))

print("Prompts salvos com sucesso no arquivo prompts_midjourney.txt!")
