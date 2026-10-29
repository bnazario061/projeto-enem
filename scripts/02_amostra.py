from pathlib import Path
import pandas as pd

raiz = Path(__file__).resolve().parent.parent
arq = raiz / "dados" / "microdados_enem_2022" / "DADOS" / "MICRODADOS_ENEM_2022.csv"
print("Procurando em:", arq)

cols = [
    "NU_INSCRICAO", "TP_COR_RACA", "TP_ST_CONCLUSAO", "TP_FAIXA_ETARIA",
    "IN_TREINEIRO", "SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_MT",
    "NU_NOTA_CN", "NU_NOTA_MT", "NU_NOTA_REDACAO", "Q006", "TP_PRESENCA_LC",
]

df = pd.read_csv(arq, sep=";", encoding="latin-1", usecols=cols, nrows=100000)

print(df.shape)
print(df.head())
print(df.isna().sum())
print(df["TP_PRESENCA_CN"].value_counts(dropna=False))
print(pd.crosstab(df["TP_PRESENCA_LC"], df["NU_NOTA_REDACAO"].isna()))
print(df["IN_TREINEIRO"].value_counts())
print(df["Q006"].value_counts().sort_index())
print(df["TP_ST_CONCLUSAO"].value_counts().sort_index())