import pandas as pd

#  Ler a planilha
df = pd.read_excel("vendas.xlsx")

#  Calcular total vendido
total_vendido = df["valor"].sum()

#  Produto mais vendido (em valor total)
produto_mais_vendido = df.groupby("produto")["valor"].sum().idxmax()

#  Total por vendedor
vendas_por_vendedor = df.groupby("vendedor")["valor"].sum()

#  Criar resumo
resumo = pd.DataFrame({
    "Métrica": ["Total Vendido", "Produto Mais Vendido"],
    "Resultado": [total_vendido, produto_mais_vendido]
})

#  Salvar relatório
with pd.ExcelWriter("relatorio_final.xlsx") as writer:
    resumo.to_excel(writer, sheet_name="Resumo", index=False)
    vendas_por_vendedor.to_excel(writer, sheet_name="Vendas por Vendedor")

print("Relatório criado com sucesso!")
