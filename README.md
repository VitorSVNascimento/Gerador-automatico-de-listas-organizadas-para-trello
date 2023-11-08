# Gerador-automatico-de-listas-organizadas-para-trello
 Gerador automático de listas organizadas para trello, a partir de um prompt fornecido pelo cliente

# Requerimentos básicos
- python 3.10.10
- chave de api trello
- token de api trello
- chave de api galaxyAI (ou outra api que consulte a api openAI com modelo gpt-3.5 turbo)

# Como utilizar o projeto
## Supondo que todos os requisitos básicos tenham sido atendidos 
1. Clone ou faça download do projeto
2. Vá até a pasta raiz do projeto
3. Crie o ambiente virtual de sua preferencia. Exemplo

        python -m venv venv
4. Execute o ambiente virtual. Exemplo

        .\venv\Scripts\activate
5. Após entrar no ambiente virtual instale as bibliotecas necessárias a partir do arquivo requirements.txt
        
        pip install -r requirements.txt

6. Altere o nome do arquivo ".env_editable" para ".env"
7. Edite o arquivo fornecendo suas chaves de API


