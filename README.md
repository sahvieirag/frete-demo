# 🚛 O Estradeiro - Parceiro Virtual do Caminhoneiro

Bem-vinda ao **Projeto Estradeiro**! Este é um agente inteligente desenvolvido com o **Google ADK** (Agent Development Kit) e alimentado pelo **Gemini 2.5 Flash**. 

O objetivo do Estradeiro é ser o "copiloto" ideal para caminhoneiros autônomos no Brasil, ajudando a encontrar cargas lucrativas, calcular custos de viagem (combustível e pedágio) e garantir que o frete realmente valha a pena ("evitar frias").

---

## 🛠️ Pré-requisitos

Antes de botar o cargueiro no tapetão, você vai precisar de:

*   **Python 3.10+** instalado.
*   Uma conta no **Google Cloud** com o **Vertex AI** habilitado.
*   O **ADK** (Agent Development Kit) instalado no seu ambiente.

---

## 🚀 Configuração Inicial

1.  **Instale as dependências:**
    No terminal, dentro da pasta do projeto, rode:
    ```bash
    pip install google-adk python-dotenv
    ```

2.  **Configure suas chaves:**
    Abra o arquivo `.env` na raiz do projeto e preencha as informações necessárias:
    *   `GOOGLE_API_KEY`: Sua chave de API do Vertex AI.
    *   `GOOGLE_CLOUD_PROJECT`: O ID do seu projeto no Google Cloud.
    *   `GOOGLE_CLOUD_LOCATION`: A região (ex: `us-central1`).

---

## 🕹️ Como Rodar - via ADK Web (Interface Visual) 🌐

O ADK oferece uma interface web incrível para você interagir com o agente de forma visual, ver o histórico de ferramentas sendo chamadas e testar o fluxo completo.

Para rodar a interface web, entre no diretório frete-demo e use o comando:
```bash
adk web .
```

---

## 🧩 Estrutura do Código

*   `estradeiro/agent.py`: O "cérebro" do projeto. Aqui definimos as instruções do Estradeiro e quais ferramentas ele pode usar.
*   `estradeiro/tools/`:
    *   `freight.py`: Ferramentas para buscar cargas, calcular pedágio e estimar combustível.
    *   `finance.py`: Lógica para cálculo de lucro líquido.

---

## 🛡️ Princípios de Segurança (Projeto Guardião)

Este código foi construído com foco em:
*   **Menor Privilégio:** As ferramentas acessam apenas o necessário para os cálculos.
*   **Segurança por Padrão:** Uso de variáveis de ambiente para segredos.
*   **Transparência:** O agente explica os cálculos de lucro líquido para evitar erros de interpretação financeira.

---

**Bora botar pra rodar!** Se tiver qualquer dúvida, é só chamar no QRA. 😉
