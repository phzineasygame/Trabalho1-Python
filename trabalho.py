print("🎉 Bem-vindo ao Quiz de Conhecimentos Gerais! ")
nome = input("Digite seu nome: ")

while not nome:
    nome = input("Por favor, digite um nome válido: ")

print(f"\nOlá, {nome}! Vamos começar o quiz.\n")

perguntas = [
    {"pergunta": "Qual a capital do Brasil?", "resposta": "brasília"},
    {"pergunta": "Quanto é 5 x 3?", "resposta": "15"},
    {"pergunta": "Qual linguagem estamos usando agora?", "resposta": "python"},
    {"pergunta": "Quantos dias tem uma semana?", "resposta": "7"}
]

pontos = 0
tentativas = 0

for item in perguntas:
    while True:
        resposta = input(f"{item['pergunta']} ").strip().lower()

        if resposta == "":
            print(" Você precisa digitar uma resposta!")
            continue

        tentativas += 1

        if resposta == item['resposta']:
            print(" Resposta correta!\n")
            pontos += 1
            break
        else:
            print(" Resposta errada. Tente novamente ou digite 'sair' para pular.\n")
            if resposta == "sair":
                print(f"A resposta correta era: {item['resposta']}\n")
                break

print(f" Fim do quiz! Você acertou {pontos} de {len(perguntas)} perguntas.")
print(f"Número total de tentativas: {tentativas}")
print("Obrigado por jogar!")
