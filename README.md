# Meu Portfólio – Projetos com Django e IA

![Django logo](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python logo](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5 logo](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3 logo](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![AI logo](https://img.shields.io/badge/Artificial%20Intelligence-FF4500?style=for-the-badge&logo=openai&logoColor=white)

Este é o repositório do projeto **"Meu Portfólio – Portfólio de projetos com Django + IA"**, desenvolvido como parte do curso da Asimov Academy. O objetivo principal aqui é criar uma aplicação web funcional para exibir e organizar os meus projetos de forma simples e intuitiva, com um toque especial de inteligência artificial no desenvolvimento do *frontend*.

---

## 💡 Sobre o Projeto

O projeto "Meu Portfólio" é uma aplicação web construída com **Django (Python)** que me permite listar e detalhar os meus projetos. Foi concebido para ser uma ferramenta eficaz para apresentar as minhas habilidades e trabalhos, sem a necessidade de conhecimento prévio em desenvolvimento web para a sua construção inicial.

Durante o desenvolvimento, abordei os seguintes tópicos:

* **Estrutura Básica do Django:** Criei as primeiras *views*, organizei URLs e passei contexto para *templates*.
* **Gestão de Conteúdo:** Implementei a listagem e exibição detalhada das informações de cada projeto.
* **Templates e Reutilização:** Construí um *template* base para reaproveitar a estrutura visual em diferentes páginas.
* **Integração de Ficheiros Estáticos:** Gerei e incluí imagens, estilos CSS e *scripts* JavaScript.
* **Desenvolvimento Frontend com IA:** Utilizei *prompts* para gerar o *design* visual do *frontend* (HTML/CSS), demonstrando como a **Inteligência Artificial** pode acelerar o processo de criação de interfaces elegantes, mesmo sem experiência aprofundada em *design*.

Este portfólio é um exemplo prático de como o **Python** e o **Django** podem ser usados para criar aplicações web úteis e visualmente atraentes, integrando conceitos de IA para otimização do fluxo de trabalho.

---

## ✨ Funcionalidades

* **Listagem de Projetos:** Exibe todos os projetos de forma organizada.
* **Detalhes do Projeto:** Cada projeto possui uma página dedicada com descrição, tecnologias utilizadas e *links* para GitHub/Demo.
* **Design Responsivo:** O *layout* adapta-se a diferentes tamanhos de ecrã.
* **Tecnologias Dinâmicas:** As tecnologias de cada projeto são exibidas como *tags*, geradas dinamicamente a partir dos dados.

---

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Django:** *Framework* web para o *backend*.
* **HTML5:** Estrutura das páginas web.
* **CSS3:** Estilização e *design* das interfaces (auxiliado por IA).
* **Inteligência Artificial:** Ferramentas de IA utilizadas para a geração do *frontend*.

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e correr o projeto na sua máquina:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    # No macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install django
    ```
    *(Se tiver um `requirements.txt` com todas as dependências, use `pip install -r requirements.txt`)*

4.  **Execute as Migrações (se houver modelos de base de dados):**
    ```bash
    python manage.py migrate
    ```
    *Observação: Para este projeto inicial da Asimov, os dados estão em ficheiros Python (`.dados`), então talvez não seja necessário migrar.*

5.  **Execute o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

6.  **Aceda à Aplicação:**
    Abra o seu navegador e aceda a: `http://127.0.0.1:8000/`

---

## 📁 Estrutura do Projeto
meu_portifolio/
├── .venv/                     # Ambiente virtual
├── manage.py                  # Utilitário de linha de comando do Django
├── meu_portifolio/            # Configurações globais do projeto
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py            # Configurações do projeto
│   ├── urls.py                # URLs globais do projeto
│   └── wsgi.py
├── portifolio/                # Aplicação Django do portfólio
│   ├── migrations/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── dados.py               # Onde os dados dos projetos e habilidades estão armazenados
│   ├── static/                # Ficheiros estáticos (CSS, JS, 
│   │   ├── css/
│   │   ├── img/
│   ├── templates/             # Templates HTML
│   │   ├── base.html
│   │   ├── detalhes_projeto.html
│   │   ├── home.html
│   │   └── projetos.html
│   ├── tests.py
│   └── views.py               # Lógica das views (onde os dados são processados e enviados para o template)
└── README.md
└── requirements.txt


---

## 🤝 Contribuições

Sinta-se à vontade para explorar o código, sugerir melhorias ou abrir *issues*. Toda a contribuição é bem-vinda!

---

## 🎓 Agradecimentos

Este projeto foi desenvolvido com base no curso da Asimov Academy, sob a orientação de **Ana Maria Gomes**. Um agradecimento especial à Asimov Academy por fornecer este material de aprendizagem tão prático e eficaz.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o ficheiro `LICENSE` para mais detalhes.

---

**Desenvolvido por:** [Jobson Barbosa](https://github.com/jobsonbarbosa/)
