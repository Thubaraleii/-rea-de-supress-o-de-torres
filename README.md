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
