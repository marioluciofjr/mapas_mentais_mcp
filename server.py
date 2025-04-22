# server.py
from mcp.server.fastmcp import FastMCP

# Inicializa o servidor FastMCP com o nome "mapas_mentais"
mcp = FastMCP("mapas_mentais")

# Tool: compara
@mcp.tool(name="compara")
def compara(tema1: str, tema2: str) -> str:
    """Gera um mapa mental comparando dois temas."""
    return (
        f"Comparação entre {tema1} e {tema2}, focando somente nos tópicos abaixo:\n"
        f"- Definições de {tema1} e {tema2}\n"
        f"- Características principais\n"
        f"- Vantagens e desvantagens\n"
        f"- Aplicações práticas\n"
        f"- Diferenças e semelhanças"
    )

# Tool: revisa
@mcp.tool(name="revisa")
def revisa(tema: str) -> str:
    """Gera um mapa mental para revisão de conteúdo sobre um tema."""
    return (
        f"Revisão de {tema}, focando somente nos tópicos abaixo:\n"
        f"- Tópico principal: {tema}\n"
        f"- Subtópicos como ramos principais\n"
        f"- Detalhes e exemplos como ramos secundários"
    )

# Tool: problemas
@mcp.tool(name="problemas")
def problemas(tema: str) -> str:
    """Gera um mapa mental de análise de problemas relacionados ao tema."""
    return (
        f"Análise de problemas sobre {tema}, focando somente nos tópicos abaixo:\n"
        f"- Definição do problema\n"
        f"- Possíveis causas\n"
        f"- Soluções propostas\n"
        f"- Recursos necessários\n"
        f"- Etapas de implementação de possíveis soluções"
    )

# Tool: apresenta
@mcp.tool(name="apresenta")
def apresenta(tema: str) -> str:
    """Gera um mapa mental para apresentações sobre um tema."""
    return (
        f"Apresentação sobre {tema}, focando somente nos tópicos abaixo:\n"
        f"- O que é\n"
        f"- Diferenças entre o {tema} e um conceito similar\n"
        f"- Exemplos de ferramentas\n"
        f"- Vantagens e desafios\n"
        f"- Casos de uso"
    )

# Tool: inicial
@mcp.tool(name="inicial")
def inicial(tema: str) -> str:
    """Gera um mapa mental de conhecimentos iniciais sobre o tema."""
    return (
        f"Conhecimentos iniciais sobre {tema}, focando somente nos tópicos abaixo:\n"
        f"- Lembrar: liste definições, fatos e informações básicas.\n"
        f"- Compreender: explique conceitos, forneça exemplos e traduza ideias.\n"
        f"- Aplicar: descreva como o conhecimento pode ser usado na prática."
    )

# Tool: intermediario
@mcp.tool(name="intermediario")
def intermediario(tema: str) -> str:
    """Gera um mapa mental de conhecimentos intermediários sobre o tema."""
    return (
        f"Conhecimentos intermediários sobre {tema}, focando somente nos tópicos abaixo:\n"
        f"- Analisar: identifica padrões, relacione ideias e compare conceitos.\n"
        f"- Avaliar: julga a eficácia, valide argumentos e critique resultados.\n"
        f"- Criar: propõe novas soluções, crie projetos ou sugira melhorias."
    )

# Executa o servidor via protocolo stdio
if __name__ == "__main__":
    mcp.run(transport="stdio")
