from pathlib import Path
import pandas as pd

raiz = Path(__file__).resolve().parent.parent
arq = raiz / "dados" / "microdados_enem_2022" / "DADOS" / "MICRODADOS_ENEM_2022.csv"

print("Procurando em:", arq)
print("Existe?", arq.exists())

cab = pd.read_csv(arq, sep=";", encoding="latin-1", nrows=0)
colunas = list(cab.columns)

print(len(colunas), "colunas")

with open(raiz / "colunas_2022.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(colunas))