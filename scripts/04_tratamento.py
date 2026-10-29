from pathlib import Path
import pandas as pd

raiz = Path(__file__).resolve().parent.parent
arq = raiz / "dados" / "microdados_enem_2022" / "DADOS" / "MICRODADOS_ENEM_2022.csv"
saida = raiz / "dados" / "tratados" / "enem_2022_base_parquet"

notas = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT", "NU_NOTA_REDACAO"]
objetivas = notas[:4]

cols = [
    "NU_INSCRICAO", "TP_COR_RACA", "TP_ST_CONCLUSAO", "TP_FAIXA_ETARIA",
    "IN_TREINEIRO", "SG_UF_PROVA", "Q006",
    "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT",
] + notas

df = pd.read_csv(arq, sep=";", encoding="latin-1", usecols=cols)
print("Linhas no arquivo:", len(df))

presentes = (
    (df["TP_PRESENCA_CN"] == 1) & (df["TP_PRESENCA_CH"] == 1)
    & (df["TP_PRESENCA_LC"]== 1) & (df["TP_PRESENCA_MT"] == 1)
)
df = df[presentes]
print("Após filtrar presença:", len(df))

df = df[df["IN_TREINEIRO"] == 0]
print("Após tirar treineiros:", len(df))

df = df[(df[objetivas] > 0).all(axis=1)].copy()
print("Após tirar zero nas objetivas:", len(df))

df["NOTA_MEDIA"] = df[notas].mean(axis=1)

saida.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(saida, index=False)
print("Salvo em:", saida)
