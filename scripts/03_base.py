from pathlib import Path
import pandas as pd

raiz = Path(__file__).resolve().parent.parent
arq = raiz / "dados" / "microdados_enem_2022" / "DADOS" / "MICRODADOS_ENEM_2022.csv"

notas = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]

cols = [
    "NU_INSCRICAO", "TP_COR_RACA", "TP_ST_CONCLUSAO", "TP_FAIXA_ETARIA",
    "IN_TREINEIRO", "SG_UF_PROVA", "Q006",
    "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT",
] + notas

df = pd.read_csv(arq, sep=";", encoding="latin-1", usecols=cols, nrows=100000)

print(pd.crosstab(df["IN_TREINEIRO"], df["TP_ST_CONCLUSAO"]))

presentes = (
    (df["TP_PRESENCA_CN"] == 1) & (df["TP_PRESENCA_CH"] == 1)
    & (df["TP_PRESENCA_LC"] == 1) & (df["TP_PRESENCA_MT"] == 1)
)
base = df[presentes].copy()
base["NOTA_MEDIA"] = base[notas].mean(axis=1)

print("Linhas de base:", len(base))
print(base[notas].isna().sum())
print("Redações com nota zero:", (base["NU_NOTA_REDACAO"] == 0).sum())
print(base["NOTA_MEDIA"].describe())
print((base[notas] == 0).sum())
print(base.nsmallest(5, "NOTA_MEDIA")[notas + ["NOTA_MEDIA"]])