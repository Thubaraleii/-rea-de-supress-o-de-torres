import pandas as pd

# Definição dos parâmetros
faixa_servico_largura = 5  # metros

# Lista de torres com seus respectivos tipos e coordenadas
# Exemplo: [(x, y, tipo), ...]
torres = [
    (100, 200, "Estaiada"),
    (300, 400, "Autoportante"),
    (500, 600, "Estaiada"),
    (700, 800, "Autoportante"),
]

# Dicionário com dimensões das torres
dimensoes_torres = {
    "Estaiada": (60, 40),  # largura x comprimento
    "Autoportante": (40, 40),
}

# Cálculo das áreas de supressão
dados = []

for x, y, tipo in torres:
    largura, comprimento = dimensoes_torres[tipo]
    area_torre = largura * comprimento
    dados.append([x, y, tipo, largura, comprimento, area_torre])

# Criação do DataFrame
df = pd.DataFrame(dados, columns=["X", "Y", "Tipo", "Largura (m)", "Comprimento (m)", "Área (m²)"])

# Cálculo da área total de supressão
area_total_torres = df["Área (m²)"].sum()

# Supondo um comprimento total da faixa de serviço baseado na distância entre as torres
comprimento_faixa_servico = 1000  # Exemplo de comprimento total da faixa de serviço
area_faixa_servico = faixa_servico_largura * comprimento_faixa_servico

# Área total de supressão
area_total_supressao = area_total_torres + area_faixa_servico

# Adiciona ao DataFrame
df.loc[len(df)] = ["Faixa de Serviço", "-", "-", faixa_servico_largura, comprimento_faixa_servico, area_faixa_servico]
df.loc[len(df)] = ["Total", "-", "-", "-", "-", area_total_supressao]

# Exportar para Excel
df.to_excel("area_supressao.xlsx", index=False)

print("Cálculo concluído. Arquivo 'area_supressao.xlsx' gerado com sucesso.")

# Criando um README.md
readme_content = """
# Cálculo de Área de Supressão

Este projeto em Python calcula a área de supressão de torres e faixa de serviço.

## Como Usar
1. Instale as dependências com `pip install pandas openpyxl`.
2. Execute `python script.py`.
3. O resultado será salvo em `area_supressao.xlsx`.

## Estrutura do Código
- Define dimensões das torres.
- Calcula a área de supressão de cada torre.
- Considera a faixa de serviço.
- Exporta os resultados para um arquivo Excel.

"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Arquivo 'README.md' gerado com sucesso.")
