# 🧾 Micro SaaS - Inserção de CPF em PDFs

Este é um micro SaaS construído com **Flask (Python)** que permite adicionar automaticamente o **CPF de uma pessoa em todas as páginas de um arquivo PDF**. Ideal para marcação de documentos digitais de forma segura e personalizada.

## 🚀 Funcionalidades

- Upload de PDF
- Inserção automática do CPF em cada página
- Download do novo PDF com marcação personalizada
- Interface web simples e intuitiva

## 🛠 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [PyPDF2](https://pythonhosted.org/PyPDF2/) ou outra lib de manipulação de PDFs
- [requirements.txt](./requirements.txt) com todas as dependências necessárias

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/LukianLeopoldo/micro-saas-python.git
   cd micro-saas-python
   ```

2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o servidor Flask:
   ```bash
   flask run
   ```

5. Acesse em: [http://localhost:5000](http://localhost:5000)

## 🧪 Exemplo de uso

1. Faça upload de um arquivo PDF.
2. Digite o CPF que deseja inserir.
3. Clique em "Gerar PDF".
4. Baixe o novo PDF com o CPF inserido em cada página.

## 📂 Estrutura básica do projeto

```
📁 seurepositorio/
├── app.py
├── templates/
│   └── index.html
├── static/
├── upload/
├── pdf_modifier.py
├── requirements.txt
└── README.md
```

## 📃 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
