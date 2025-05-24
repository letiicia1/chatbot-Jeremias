# 🤖 Chatbot com Flask + OpenAI

Este projeto é um **chatbot simples** feito com **Python, Flask, OpenAI API**, e uma interface básica com **HTML e CSS**. Ele foi criado com o objetivo de praticar a linguagem Python e explorar a integração com inteligência artificial em uma aplicação web.

---

## 🚀 Objetivos

- Aprender a integrar Flask com front-end (HTML + CSS)
- Utilizar a API da OpenAI para gerar respostas com IA
- Praticar a construção de aplicações web simples
- Servir como base para projetos maiores e mais interativos

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- OpenAI API
- HTML5 + CSS3

---

## 📁 Estrutura do Projeto

```
chatbot/
├── app.py            # Inicializa o servidor Flask
├── chatbot.py        # Contém a função de integração com a API da OpenAI
├── static/
│   ├── style.css     # Estilos da interface
│   ├── fundo.png     # Imagem de fundo
│   └── robo.png      # Ícone do robô
├── templates/
│   └── index.html    # Página web principal
```

---

## ▶️ Como Executar Localmente

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/letiicia1/chatbot-Jeremias.git
   cd chatbot-Jeremias/chatbot
   ```

2. **Instale as dependências:**
   ```bash
   pip install flask openai
   ```

3. **Configure sua chave da OpenAI:**
   No arquivo `chatbot.py`, encontre a linha comentada com `"SUA-CHAVE-AQUI"` e insira sua chave da OpenAI.

4. **Execute a aplicação:**
   ```bash
   python app.py
   ```

5. **Abra no navegador:**
   ```
   http://127.0.0.1:5000/
   ```

---
