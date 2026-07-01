# Chatbot com IA Generativa
### João Vitor Andrade da Silva

## Introdução

Este projeto foi desenvolvido como parte de uma atividade acadêmica com foco na criação, implantação e documentação de uma aplicação baseada em Inteligência Artificial Generativa.

A proposta consiste no desenvolvimento de um chatbot acessível via navegador web, utilizando Python, Streamlit e um modelo open source disponibilizado pela NVIDIA por meio da plataforma NVIDIA NIM. A aplicação permite que usuários façam perguntas em linguagem natural e recebam respostas geradas por um modelo de linguagem.

---

## Objetivo da Atividade

O objetivo principal da atividade é desenvolver e implantar um chatbot baseado em Inteligência Artificial Generativa utilizando um modelo open source disponibilizado pela NVIDIA.

Ao final do projeto, a aplicação deve estar disponível por meio de um endereço IP público, permitindo que usuários acessem o chatbot diretamente pelo navegador.

Os principais objetivos são:

* Desenvolver uma aplicação web em Python;
* Utilizar Streamlit para criação da interface;
* Integrar a aplicação a um modelo de IA Generativa da NVIDIA;
* Organizar o projeto em um repositório GitHub;
* Publicar a aplicação em uma máquina virtual na Oracle Cloud ou serviço similar;
* Documentar o processo de desenvolvimento e implantação.

---

## Visão Geral da Solução Desenvolvida

A solução desenvolvida é um chatbot web simples, funcional e acessível pelo navegador.

O usuário digita uma pergunta na interface da aplicação, desenvolvida com Streamlit. Em seguida, essa pergunta é enviada para um modelo de linguagem disponibilizado pela NVIDIA. O modelo processa a entrada e retorna uma resposta em linguagem natural, que é exibida na tela do usuário.

A aplicação foi estruturada com separação entre interface, configurações, prompts e serviço de comunicação com o modelo, facilitando manutenção e futuras melhorias.

Fluxo geral da aplicação:

```text
Usuário
   ↓
Interface Streamlit
   ↓
Serviço de comunicação com a NVIDIA
   ↓
Modelo de IA Generativa
   ↓
Resposta exibida no navegador
```

---

## Infraestrutura

### Ambiente de Desenvolvimento Local

O desenvolvimento inicial foi realizado em ambiente local, permitindo testar a aplicação antes da publicação em nuvem.

Configuração utilizada no ambiente local:

* Linguagem: Python
* Framework web: Streamlit
* Gerenciador de dependências: pip
* Ambiente virtual: venv
* Controle de versão: Git e GitHub

### Máquina Virtual em Nuvem

A aplicação foi preparada para ser implantada em uma máquina virtual na Oracle Cloud ou serviço similar.

Configuração prevista para a VM:

* Provedor: Oracle Cloud Infrastructure
* Sistema operacional: Ubuntu Server
* Acesso remoto: SSH
* Porta da aplicação: 8501
* Execução da aplicação: Streamlit

### Recursos Computacionais Disponíveis

A aplicação não executa o modelo diretamente na máquina virtual. O processamento de IA é realizado pela API da NVIDIA, o que reduz a necessidade de GPU local ou recursos computacionais avançados na VM.

Dessa forma, a máquina virtual precisa principalmente executar a aplicação web, lidar com requisições HTTP e se comunicar com a API externa da NVIDIA.

Recursos mínimos recomendados:

* 1 ou mais CPUs virtuais;
* 1 GB ou mais de memória RAM;
* Sistema operacional Linux;
* Acesso à internet;
* Porta pública liberada para acesso via navegador.

---

## Modelo Escolhido

### Nome do Modelo

O modelo utilizado no projeto é:

```text
meta/llama-3.1-8b-instruct
```

### Justificativa da Escolha

O modelo foi escolhido por ser adequado para aplicações conversacionais e por estar disponível para uso por meio da plataforma NVIDIA NIM.

Além disso, trata-se de um modelo instruído, ou seja, treinado para responder comandos, perguntas e interações em linguagem natural. Isso o torna apropriado para a construção de chatbots, assistentes virtuais e aplicações de atendimento automatizado.

### Principais Características

As principais características do modelo escolhido são:

* Modelo de linguagem de grande porte;
* Adequado para conversas e respostas instrucionais;
* Boa capacidade de compreensão de contexto;
* Integração via API;
* Uso simplificado por meio de endpoint compatível com clientes OpenAI;
* Não exige execução local do modelo na máquina do desenvolvedor ou na VM.

---

## Desenvolvimento

### Arquitetura da Aplicação

A aplicação foi organizada de forma modular, separando responsabilidades em diferentes arquivos e pastas.

Estrutura principal do projeto:

```text
chatbot-nvidia/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── config/
│   └── settings.py
│
├── services/
│   └── llm.py
│
└── utils/
    └── prompts.py
```

Descrição dos principais arquivos:

* `app.py`: arquivo principal da aplicação Streamlit;
* `services/llm.py`: responsável pela comunicação com o modelo da NVIDIA;
* `config/settings.py`: centraliza configurações e variáveis de ambiente;
* `utils/prompts.py`: armazena o prompt de sistema utilizado pelo chatbot;
* `.env.example`: exemplo das variáveis necessárias para execução;
* `.gitignore`: impede o envio de arquivos sensíveis ou desnecessários ao GitHub;
* `requirements.txt`: lista as dependências do projeto;
* `README.md`: documentação e relatório do projeto.

---

## Bibliotecas Utilizadas

As principais bibliotecas utilizadas foram:

### Streamlit

Utilizada para desenvolver a interface web do chatbot de forma simples e rápida.

### OpenAI

Utilizada como cliente para comunicação com a API da NVIDIA, já que o endpoint da NVIDIA NIM é compatível com o padrão de chamadas da OpenAI.

### python-dotenv

Utilizada para carregar variáveis de ambiente a partir de um arquivo `.env`, permitindo que credenciais sensíveis sejam mantidas fora do código-fonte.

---

## Estratégia de Gerenciamento de Credenciais

Para proteger a chave da API da NVIDIA, foi utilizada uma estratégia baseada em variáveis de ambiente.

A chave real da API fica armazenada em um arquivo chamado `.env`, que não deve ser enviado para o GitHub.

Exemplo de arquivo `.env`:

```env
NVIDIA_API_KEY=sua_chave_real_aqui
NVIDIA_MODEL=meta/llama-3.1-8b-instruct
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
```

O arquivo `.gitignore` contém a entrada:

```gitignore
.env
```

Dessa forma, a chave de API permanece protegida no ambiente local ou na máquina virtual.

Para orientar outros usuários, foi criado o arquivo `.env.example`, contendo apenas um exemplo da configuração necessária, sem expor a chave real.

---

## Instalação e Execução Local

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd chatbot-nvidia
```

### 2. Criar o ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o arquivo `.env`

Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:

```env
NVIDIA_API_KEY=sua_chave_real_aqui
NVIDIA_MODEL=meta/llama-3.1-8b-instruct
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
```

### 5. Executar a aplicação

```bash
streamlit run app.py
```

A aplicação será aberta no navegador em:

```text
http://localhost:8501
```

---

## Implantação

A implantação da aplicação foi planejada para uma máquina virtual na Oracle Cloud.

O processo geral de publicação consiste nas seguintes etapas:

1. Criar uma máquina virtual na Oracle Cloud;
2. Configurar acesso via SSH;
3. Instalar Python, pip, venv e Git;
4. Clonar o repositório do GitHub na VM;
5. Criar e ativar um ambiente virtual;
6. Instalar as dependências do projeto;
7. Criar o arquivo `.env` com a chave da NVIDIA;
8. Executar a aplicação Streamlit;
9. Liberar a porta `8501` nas regras de rede da Oracle Cloud;
10. Acessar a aplicação pelo IP público da VM.

Comando básico para execução na VM:

```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Após a execução, a aplicação poderá ser acessada pelo navegador utilizando o IP público da máquina virtual:

```text
http://IP_PUBLICO_DA_VM:8501
```

---

## Principais Desafios Encontrados

Durante o desenvolvimento, alguns desafios importantes foram considerados:

* Organização correta da estrutura do projeto;
* Proteção da chave da API;
* Configuração das variáveis de ambiente;
* Integração entre Streamlit e o modelo da NVIDIA;
* Tratamento de erros na comunicação com a API;
* Preparação da aplicação para execução em ambiente local e em nuvem;
* Configuração da máquina virtual para permitir acesso externo pelo navegador.

Esses desafios fazem parte do processo real de desenvolvimento de aplicações baseadas em IA Generativa e ajudam a compreender melhor a relação entre código, infraestrutura e segurança.

---

## Discussão

### Lições Aprendidas

O desenvolvimento deste projeto permitiu compreender melhor como aplicações modernas de IA Generativa podem ser criadas e publicadas.

Entre as principais lições aprendidas, destacam-se:

* A importância de separar o código em módulos;
* A necessidade de proteger credenciais sensíveis;
* O uso de APIs para consumir modelos de IA sem precisar executá-los localmente;
* A facilidade do Streamlit para criar interfaces web em Python;
* A importância da documentação para facilitar instalação, execução e manutenção;
* O processo de publicação de uma aplicação em uma máquina virtual na nuvem.

### Possíveis Melhorias Futuras

Algumas melhorias podem ser implementadas em versões futuras do projeto:

* Adicionar autenticação de usuários;
* Salvar histórico de conversas em banco de dados;
* Criar opção para escolher diferentes modelos;
* Adicionar streaming de respostas;
* Melhorar o layout visual da aplicação;
* Criar logs de uso e monitoramento;
* Configurar execução contínua com systemd na VM;
* Utilizar HTTPS com domínio próprio;
* Adicionar testes automatizados;
* Criar uma arquitetura com Docker para facilitar o deploy.

---

## Conclusão

Este projeto demonstrou o desenvolvimento de um chatbot baseado em Inteligência Artificial Generativa utilizando Python, Streamlit e um modelo open source disponibilizado pela NVIDIA.

A aplicação foi estruturada de forma simples, segura e organizada, permitindo execução local e posterior implantação em uma máquina virtual na nuvem.

Além de atender aos requisitos da atividade, o projeto representa uma base inicial para aplicações mais completas envolvendo assistentes virtuais, automação de atendimento e integração com modelos de linguagem.
