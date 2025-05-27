import random

class Chatbot:
    def __init__(self):
        self.produtos = [
            {
                "codigo": "1.1",
                "nome": "Notebook Dell Inspiron 15",
                "descricao": "Ideal para estudos e trabalho, com processador Intel i5, 8GB RAM, SSD 256GB",
                "preco": "R$ 3.000",
                "qualidade": "Alta performance para atividades diárias, construção resistente, tela Full HD.",
                "compatibilidade": "Compatível com impressoras Wi-Fi, mouses USB, monitores HDMI."
            },
            {
                "codigo": "1.2",
                "nome": "Fone de Ouvido JBL Tune 510BT",
                "descricao": "Fone Bluetooth com som potente e até 40h de bateria",
                "preco": "R$ 250",
                "qualidade": "Som limpo e com graves reforçados, ideal para uso diário.",
                "compatibilidade": "Compatível com celulares, tablets e notebooks com Bluetooth."
            },
            {
                "codigo": "1.3",
                "nome": "Tablet Samsung Galaxy Tab A8",
                "descricao": "Tela de 10.5'', ótimo para vídeos, leitura e apps educativos.",
                "preco": "R$ 1.800",
                "qualidade": "Boa performance para multimídia e apps simples.",
                "compatibilidade": "Compatível com fones Bluetooth, canetas capacitivas e capas magnéticas."
            },
            {
                "codigo": "1.4",
                "nome": "Smartphone Motorola G73 5G",
                "descricao": "Celular com câmera de 50MP, 5G, 128GB de memória e 8GB RAM",
                "preco": "R$ 1.950",
                "qualidade": "Excelente desempenho para jogos e multitarefa, ótima câmera.",
                "compatibilidade": "Compatível com fones Bluetooth, capinhas magnéticas, carregadores tipo C."
            },
            {
                "codigo": "1.5",
                "nome": "Smartwatch Amazfit Bip U Pro",
                "descricao": "Relógio inteligente com monitoramento de saúde, GPS e 9 dias de bateria",
                "preco": "R$ 350",
                "qualidade": "Boa construção, bateria duradoura, recursos avançados de saúde.",
                "compatibilidade": "Compatível com Android e iOS via app Zepp."
            }
        ]
        self.estado = "menu"
        self.produto_atual = None
        self.estado_recomendacao = None

    def menu_opcoes(self):
        return (
            "\n📋 Menu de Opções:\n"
            "1 - Ver produtos disponíveis\n"
            "2 - Obter recomendação de produto\n"
            "3 - Falar com um atendente\n"
            "4 - Encerrar atendimento\n"
            "Digite o número da opção desejada:"
        )

    def responder(self, entrada):
        entrada = entrada.strip().lower()

        if self.estado_recomendacao:
            return self.processar_resposta_recomendacao(entrada)

        if self.estado == "produto":
            return self.dialogo_sobre_produto(entrada)

        if entrada == "1":
            return self.listar_produtos()

        elif entrada == "2":
            self.estado_recomendacao = "esperando_escolha"
            return self.perguntar_recomendacao()

        elif entrada == "3":
            return "Encaminhando para um atendente disponivel... Envie Mensagem com sua duvida,problema ou  questão para o número (81983685500)"

        elif entrada == "4":
            return "Até mais! Foi um prazer te ajudar. 😊"

        else:
            return "Desculpe, não entendi. Escolha uma opção válida do menu."

    def listar_produtos(self):
        resposta = "🛍️ Produtos disponíveis:\n\n"
        for produto in self.produtos:
            resposta += (
                f"{produto['codigo']} - {produto['nome']}\n"
                f"    📄 {produto['descricao']}\n"
                f"    💰 {produto['preco']}\n\n"
            )
        resposta += "Digite o código (ex: 1.1) para saber mais ou 'voltar' para retornar ao menu."
        self.estado = "produto"
        return resposta

    def dialogo_sobre_produto(self, entrada):
        if entrada == "voltar":
            self.estado = "menu"
            self.produto_atual = None
            return self.menu_opcoes()

        for p in self.produtos:
            if entrada == p["codigo"].lower():
                self.produto_atual = p
                return (
                    f"🧾 {p['nome']} selecionado.\n"
                    "Você pode perguntar:\n"
                    "- Qual a qualidade do produto?\n"
                    "- Ele é compatível com outro item?\n"
                    "- Ou digite 'voltar' para retornar ao menu."
                )

        if self.produto_atual:
            if "qualidade" in entrada:
                return f"📈 Qualidade: {self.produto_atual['qualidade']}"
            elif "compatível" in entrada or "compatibilidade" in entrada:
                return f"🔌 Compatibilidade: {self.produto_atual['compatibilidade']}"
            else:
                return (
                    "Desculpe, não entendi a pergunta. "
                    "Tente perguntar sobre a qualidade ou compatibilidade, ou digite 'voltar'."
                )

        return "Código inválido. Digite um código como '1.1' ou 'voltar' para retornar."

    def perguntar_recomendacao(self):
        return (
            "🔍 Para qual finalidade você está procurando um produto?\n"
            "a - Estudo e trabalho\n"
            "b - Música e entretenimento\n"
            "c - Mobilidade e comunicação\n"
            "d - Monitoramento de saúde\n"
            "Digite a letra correspondente (a, b, c ou d):"
        )

    def processar_resposta_recomendacao(self, entrada):
        self.estado_recomendacao = None

        if entrada == "a":
            produto = next((p for p in self.produtos if "notebook" in p["nome"].lower()), None)
        elif entrada == "b":
            produto = next((p for p in self.produtos if "fone" in p["nome"].lower()), None)
        elif entrada == "c":
            produto = next((p for p in self.produtos if "smartphone" in p["nome"].lower()), None)
        elif entrada == "d":
            produto = next((p for p in self.produtos if "smartwatch" in p["nome"].lower()), None)
        else:
            return "Opção inválida. Tente digitar a, b, c ou d."

        if produto:
            return (
                f"🎯 Recomendação baseada na sua escolha:\n"
                f"🔸 {produto['nome']}\n"
                f"📄 {produto['descricao']}\n"
                f"💰 {produto['preco']}"
            )
        else:
            return "Desculpe, não encontrei um produto adequado para essa finalidade."
