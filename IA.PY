import json
import os
import random


# ============================================================
# CONFIGURAÇÕES
# ============================================================

NOME_DA_IA = "Luna"
ARQUIVO_MEMORIA = "memoria.json"


# ============================================================
# MEMÓRIA
# ============================================================

def carregar_memoria():
    if os.path.exists(ARQUIVO_MEMORIA):
        try:
            with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except:
            return {}

    return {}


def salvar_memoria():
    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as arquivo:
        json.dump(memoria, arquivo, ensure_ascii=False, indent=4)


memoria = carregar_memoria()


# ============================================================
# RESPOSTAS PRONTAS
# ============================================================

respostas = {
    "oi": [
        "Olá! Tudo bem?",
        "Oi! Como você está?",
        "Olá! O que vamos fazer hoje?"
    ],

    "olá": [
        "Olá!",
        "Oi! Tudo certo?",
        "Olá! Como posso ajudar?"
    ],

    "tudo bem": [
        "Tudo certo por aqui!",
        "Estou funcionando normalmente."
    ],

    "quem é você": [
        "Eu sou uma pequena IA feita em Python.",
        "Meu nome é Luna e fui criada usando Python."
    ],

    "qual seu nome": [
        "Meu nome é Luna."
    ],

    "o que você faz": [
        "Eu converso, respondo perguntas simples e posso aprender novas respostas."
    ],

    "tchau": [
        "Até mais!",
        "Tchau! Volte quando quiser.",
        "Até a próxima!"
    ]
}


# ============================================================
# FUNÇÃO PARA ENCONTRAR UMA RESPOSTA
# ============================================================

def responder(pergunta):

    pergunta = pergunta.lower().strip()

    # Primeiro procura na memória que a IA aprendeu
    if pergunta in memoria:
        return memoria[pergunta]

    # Depois procura nas respostas prontas
    if pergunta in respostas:
        return random.choice(respostas[pergunta])

    # Procura palavras dentro da pergunta
    if "seu nome" in pergunta:
        return "Meu nome é Luna."

    if "python" in pergunta:
        return "Python é uma linguagem de programação."

    if "idade" in pergunta:
        return "Eu não tenho idade como uma pessoa."

    return None


# ============================================================
# INÍCIO DA IA
# ============================================================

print("=" * 50)
print("                 LUNA IA")
print("=" * 50)

print()
print("Olá! Eu sou a Luna.")
print("Digite 'sair' para fechar a IA.")
print()


# ============================================================
# CONVERSA
# ============================================================

while True:

    pergunta = input("Você: ").strip()

    if pergunta == "":
        print("Luna: Você não escreveu nada.")
        continue

    if pergunta.lower() == "sair":
        print("Luna: Até mais!")
        salvar_memoria()
        break

    resposta = responder(pergunta)

    if resposta is not None:
        print("Luna:", resposta)

    else:
        print("Luna: Ainda não sei responder isso.")

        ensinar = input("Você quer me ensinar uma resposta? (sim/não): ")

        if ensinar.lower() == "sim":

            nova_resposta = input("Digite a resposta que eu devo aprender: ")

            if nova_resposta.strip() != "":
                memoria[pergunta.lower()] = nova_resposta

                salvar_memoria()

                print("Luna: Aprendi!")

        else:
            print("Luna: Tudo bem.")