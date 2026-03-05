import pandas as pd

dados = {
    "data": ["01/03/2024", "01/03/2024", "02/03/2024", "02/03/2024", "03/03/2024"],
    "vendedor": ["Ana", "Carlos", "Ana", "João", "Carlos"],
    "produto": ["Notebook", "Mouse", "Teclado", "Notebook", "Monitor"],
    "valor": [3500, 80, 150, 3500, 900]
}

df = pd.DataFrame(dados)
df.to_excel("vendas.xlsx", index=False)

print("Planilha criada com sucesso!")

