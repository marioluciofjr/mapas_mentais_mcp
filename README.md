[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/marioluciofjr-mapas-mentais-mcp-badge.png)](https://mseep.ai/app/marioluciofjr-mapas-mentais-mcp)

# MCP-Server de Mapas Mentais

[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")
![license - MIT](https://img.shields.io/badge/license-MIT-green)
![site - prazocerto.me](https://img.shields.io/badge/site-prazocerto.me-230023)
![linkedin - @marioluciofjr](https://img.shields.io/badge/linkedin-marioluciofjr-blue)
[![smithery badge](https://smithery.ai/badge/@marioluciofjr/mapas_mentais_mcp)](https://smithery.ai/server/@marioluciofjr/mapas_mentais_mcp)

A dynamic MCP server management service that creates, runs, and manages Model Context Protocol (MCP) servers dynamically. This service itself functions as an MCP server and launches/manages other MCP servers as child processes, enabling a flexible MCP ecosystem.

<a href="https://glama.ai/mcp/servers/@marioluciofjr/mapas_mentais_mcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@marioluciofjr/mapas_mentais_mcp/badge" alt="MCP-Server de Mapas Mentais MCP server" />
</a>

## Índice

* [Introdução](#introdução)
* [Estrutura do projeto](#estrutura-do-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Requisitos](#requisitos)
* [Como instalar no Claude Desktop](#como-instalar-no-claude-desktop)
* [Links úteis](#links-úteis)
* [Contribuições](#contribuições)
* [Licença](#licença)
* [Contato](#contato)

## Introdução

O projeto mapas_mentais é uma aplicação Python que gera mapas mentais automatizados para facilitar o estudo, revisão, comparação e apresentação de temas diversos. 
Utilizando a ideia de MCP-server, o sistema oferece insights ao interagir diretamente com o Claude Desktop por meio dos modelos Claude.
Ideal para estudantes, professores e profissionais que desejam organizar ideias de forma visual e eficiente, o projeto é facilmente extensível e pode ser integrado a outros sistemas de automação ou assistentes virtuais.

## Estrutura do projeto

A ideia desse projeto surgiu a partir das explicações do professor Sandeco Macedo, da UFG (Universidade Federal de Goiás), sobre MCPs por meio do livro [MCP e A2A para Leigos
](https://physia.com.br/mcp/). É um MCP-Server simples que utiliza somente o pacote FastMCP, seguindo também as orientações do repositório oficial do [Model Context Protol](https://github.com/modelcontextprotocol/python-sdk), da Anthropic.

Os seis tipos de mapas mentais utilizados neste MCP-Server são: 

* apresenta - Gera um mapa mental para apresentações sobre um tema;
* compara - Gera um mapa mental comparando dois temas;
* inicial - Gera um mapa mental de conhecimentos iniciais sobre o tema;
* intermediario - Gera um mapa mental de conhecimentos intermediários sobre o tema;
* problemas - Gera um mapa mental de análise de problemas relacionados ao tema;
* revisa - Gera um mapa mental para revisão de conteúdo sobre um tema.

## Tecnologias utilizadas

<div>
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/c0604008-f730-413f-9c4e-9b06c0912692" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/76e7aca0-5321-4238-9742-164c20af5b4a" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/57ffab5c-81a9-4821-8301-67391854789b" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/cf957637-962d-4548-87d4-bbde91fadc22" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/775a6ce6-3474-436b-b6f6-7f1f9192a878" />&nbsp;&nbsp;&nbsp
  <img align="center" height="60" width="80" src="https://github.com/user-attachments/assets/abafaea5-eb57-4965-9130-7816280a8d84" />&nbsp;&nbsp;&nbsp; 
</div>

## Requisitos

* Python instalado (versão 3.10 ou superior);
* Pacote `uv` instalado;
* Claude Desktop instalado.

## Como instalar no Claude Desktop

### Installing via Smithery

To install Mapas Mentais Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@marioluciofjr/mapas_mentais_mcp):

```bash
npx -y @smithery/cli install @marioluciofjr/mapas_mentais_mcp --client claude
```

Agora vou detalhar como foi o meu passo a passo no Windows 11, utilizando o terminal (atalho `CTRL` + `SHIFT` + `'`) no VSCode: 

1. Instalei a [versão mais atualizada do Python](https://www.python.org/downloads/)
2. Já no VSCode, eu utizei o terminal para verificiar a versão do python com o comando
   ```powershell
   python --version
   ```
3. Depois eu instalei o `uv` com o comando
   ```powershell
   pip install uv
   ```
4. Para conferir se estava tudo certo, eu utilizei o comando
   ```powershell
   uv
   ```
5. Para criar a pasta do projeto, eu utilizei este comando
   ```powershell
   mkdir “C:\Users\meu_usuario\OneDrive\area_de_trabalho\mapas_mentais”
   ```

  > [!IMPORTANT]
  > Não necessariamente quer dizer que você utilizará o mesmo caminho, pode ser que você queira utilizar outro caminho, como este abaixo
  > ```powershell
  >   mkdir "C:\Users\seu_usuario\mapas_mentais"
  >   ```
  >   Ou você pode simplesmente fazer o download do zip desse projeto para a sua máquina pelo caminho `Code` > `Download ZIP` aqui mesmo no GitHub
  > 
  > ![Image](https://github.com/user-attachments/assets/e9d57d6f-0303-4c94-98b3-8812edce235e)

6. Chamei a pasta que eu tinha acabado de criar
   ```powershell
   cd “C:\Users\meu_usuario\OneDrive\area_de_trabalho\mapas_mentais”
   ```
7. Utilizei o comando abaixo para abrir outra janela do VSCode e continuar com os demais comandos direto na pasta
   ```
   code .
   ```

  > [!IMPORTANT]
  > Se não quiser criar a pasta via terminal, você pode criar uma nova pasta na sua área de trabalho ou outro local que se lembre facilmente, a fim de utilizar o atalho no VSCode
  > `CTRL` + `O`
  > Depois é só procurar a pasta que acabou de criar, clicar nela e abrir no VSCode. Ou somente importar a pasta completa desse repositório no seu VSCode.

8. Voltando ao terminal, utilizei o comando abaixo para inicializar um novo projeto Python, criando arquivos de configuração e dependências automaticamente
   ```powershell
   uv init
   ```
9. Utilizei em seguida o comando abaixo para criar um ambiente virtual Python isolado para instalar dependências do projeto
    ```powershell
    uv venv
    ```
10. Para ativar o .venv, utilizei o comando abaixo
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
11. Adicionei a dependência MCP, necessária para o projeto
    ```powershell
    uv add mcp[cli]
    ```
12. Verifiquei se estava tudo ok, com o comando abaixo
    ```powershell
    uv run mcp
    ```

> [!IMPORTANT]
> Se aparecer esta informação abaixo no seu terminal é porque está tudo certo
> 
> ![Image](https://github.com/user-attachments/assets/7c692a88-929e-4b8c-84df-b8ce0f004139)

13. Para criar o arquivo `server.py`, eu utilizei esse comando
    ```powershell
    uv init --script server.py
    ```

> [!TIP]
> Como você pode já ter baixado a pasta desse repositório, então o arquivo `server.py`já estará lá no seu VSCode nessa altura do campeonato.

14. Instalei o json abaixo do MCP-Server diretamente no arquivo `claude_desktop_config.json`
    ```json
    "mapas_mentais": {
      "command": "uv",
      "args": [
        "--directory",
        "C://Users//meu_usuario//OneDrive//area_de_trabalho//mapas_mentais",
        "run",
        "server.py"
      ]
    }
    ```

> [!IMPORTANT]
> Se você já instalou o Claude Desktop corretamente, siga o caminho para acessar o arquivo `claude_desktop_config.json` no seu computador\
> 14a. Com o Claude Desktop aberto, utilize o atalho `CTRL` + `,`\
> 14b. Clique na aba `Desenvolvedor` e depois em `Editar configuração`\
> 14c. Procure o arquivo `claude_desktop_config.json` e edite no VSCode corretamente\
> 14d. Salve o arquivo com `CTRL` + `S`\
> 14e. Feche o Claude Desktop e abra novamente depois de alguns segundos\
> 14f. Confira no ícone de configuração se as ferramentas do MCP "mapas_mentais" estão instaladas corretamente
>
> ![Image](https://github.com/user-attachments/assets/6553bcd2-1f3c-4963-9d6a-15b0dc614edd)
>
> As ferramentas foram nomeadas como `"apresenta", "compara", "inicial", "intermediario", "problemas" e "revisa".

## Links úteis

* [Documentação oficial do Model Context Protocol](https://modelcontextprotocol.io/introduction) - Você saberá todos os detalhes dessa inovação da Anthropic
* [Site oficial da Anthropic](https://www.anthropic.com/) - Para ficar por dentro das novidaddes e estudos dos modelos Claude
* [Como baixar o Claude Desktop](https://claude.ai/download) - Link direto para download
* [Como instalar o VSCode](https://code.visualstudio.com/download)- Link direto para download
* [Documentação oficial do pacote uv](https://docs.astral.sh/uv/) - Você saberá todos os detalhes sobre o `uv` e como ele é importante no python
* [venv — Criação de ambientes virtuais](https://docs.python.org/pt-br/3/library/venv.html) - Explicação completa de como funcionam os venvs
* [Conjunto de ícones de modelos de IA/LLM](https://lobehub.com/pt-BR/icons) - site muito bom para conseguir ícones do ecossistema de IA
* [Devicon](https://devicon.dev/) - site bem completo também com ícones gerais sobre tecnologia

## Contribuições

Contribuições são bem-vindas! Se você tem ideias para melhorar este projeto, sinta-se à vontade para fazer um fork do repositório.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marioluciofjr/mapas_mentais_mcp/blob/main/LICENSE) para detalhes.

## Contato
    
Mário Lúcio - Prazo Certo®
<div>  	
  <a href="https://www.linkedin.com/in/marioluciofjr" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
  <a href = "mailto:marioluciofjr@gmail.com" target="_blank"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <a href="https://prazocerto.me/contato" target="_blank"><img src="https://img.shields.io/badge/prazocerto.me/contato-230023?style=for-the-badge&logo=wordpress&logoColor=white"></a>
</div> 
