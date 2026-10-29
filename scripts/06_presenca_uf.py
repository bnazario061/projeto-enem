from pathlib import Path
import pandas as pd

raiz = Path(__file__).resolve().parent.parent
arq = raiz / "dados" / "microdados_enem_2022" / "DADOS" / "MICRODADOS_ENEM_2022.csv"
pasta = raiz / "dados" / "tratados"

cols = ["SG_UF_PROVA", "TP_PRESENCA_CN", "TP_PRESENCA_CH",
        "TP_PRESENCA_LC", "TP_PRESENCA_MT"]

df = pd.read_csv(arq, sep=";", encoding="latin-1", usecols=cols)

df["PRESENTE"] = (
    (df["TP_PRESENCA_CN"] == 1) & (df["TP_PRESENCA_CH"] == 1)
    & (df["TP_PRESENCA_LC"] == 1) & (df["TP_PRESENCA_MT"] == 1)
).astype(int)

presenca = df.groupby("SG_UF_PROVA").agg(
    INSCRITOS=("PRESENTE", "size"),
    PRESENTES=("PRESENTE", "sum"),
).reset_index()

print(presenca)
print("Total de inscritos:", presenca["INSCRITOS"].sum())
print("Total de presentes:", presenca["PRESENTES"].sum())

presenca.to_csv(pasta / "fPresencaUF.csv", index=False, encoding="utf-8-sig")
print("Salvo em:", pasta / "fPresencaUF.csv")