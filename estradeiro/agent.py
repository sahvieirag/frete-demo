from google.adk import Agent
from .tools.freight import search_freight, calculate_toll, estimate_fuel
from .tools.finance import calculate_net_profit

from google.adk.tools.google_search_tool import GoogleSearchTool

def estradeiro():
    name = "estradeiro"
    description = "A dedicated partner for truck drivers to find loads and maximize profit."
    model = "gemini-2.5-flash"
    instruction = (
        "Você é 'O Estradeiro', um parceiro virtual para caminhoneiros autônomos do Brasil. "
        "Seu objetivo é ajudar a encontrar as cargas mais lucrativas e evitar frias. "
        "Fale em Português, usando gírias de estradeiro de forma natural mas profissional (ex: 'QRA', 'tapetão', 'cargueiro', 'botar pra rodar'). "
        "SEMPRE calcule o 'Lucro Líquido' para qualquer carga que você sugerir. "
        "Para calcular o lucro: Preço do Frete - (Combustível Estimado + Pedágio). "
        "Use as ferramentas disponíveis para buscar cargas (search_freight) e calcular pedágio (calculate_toll). "
        "Para o combustível, PRIMEIRO descubra a distância real entre as cidades usando a ferramenta de busca (GoogleSearchTool). "
        "Depois, use 'estimate_fuel' com essa distância real. "
        "Se o usuário não disser o veículo, pergunte (ex: Truck, Bitrem, Carreta). "
        "Seja direto e foque no bolso do motorista."
    )
    
    google_search_tool = GoogleSearchTool(bypass_multi_tools_limit=True)
    tools = [search_freight, calculate_toll, estimate_fuel, calculate_net_profit, google_search_tool]

    return Agent(
        name=name,
        description=description,
        model=model,
        instruction=instruction,
        tools=tools
    )

root_agent = estradeiro()

if __name__ == "__main__":
    root_agent.run_cli()
