import pandas as pd
import numpy as np

# Definição dos parâmetros
faixa_servico_largura = 5  # metros

# Lista de torres com coordenadas e tipos
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

# Convertendo para array NumPy para otimizar cálculos
torres_array = np.array(torres, dtype=object)

# Cálculo das áreas de supressão
larguras = np.array([dimensoes_torres[tipo][0] for tipo in torres_array[:, 2]])
comprimentos = np.array([dimensoes_torres[tipo][1] for tipo in torres_array[:, 2]])
areas_torres = larguras * comprimentos

# Criando DataFrame
df = pd.DataFrame({
    "X": torres_array[:, 0],
    "Y": torres_array[:, 1],
    "Tipo": torres_array[:, 2],
    "Largura (m)": larguras,
    "Comprimento (m)": comprimentos,
    "Área (m²)": areas_torres
})

# Cálculo da área total de supressão
area_total_torres = np.sum(areas_torres)

# Comprimento total da faixa de serviço (exemplo: soma das distâncias entre torres)
comprimento_faixa_servico = 1000  # Valor fictício para exemplo
area_faixa_servico = faixa_servico_largura * comprimento_faixa_servico

# Área total de supressão
area_total_supressao = area_total_torres + area_faixa_servico

# Adicionando ao DataFrame
df.loc[len(df)] = ["Faixa de Serviço", "-", "-", faixa_servico_largura, comprimento_faixa_servico, area_faixa_servico]
df.loc[len(df)] = ["Total", "-", "-", "-", "-", area_total_supressao]

# Exportar para Excel
df.to_excel("area_supressao_alternativa.xlsx", index=False)

print("Cálculo concluído. Arquivo 'area_supressao_alternativa.xlsx' gerado com sucesso.")
