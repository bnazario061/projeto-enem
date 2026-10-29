from pathlib import Path
import pandas as pd

raiz = Path(__file__).resolve().parent.parent
pasta = raiz / "dados" / "tratados"

regioes = {
    "Norte": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
    "Nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "Centro-Oeste": ["DF", "GO", "MS", "MT"],
    "Sudeste": ["ES", "MG", "RJ", "SP"],
    "Sul": ["PR", "RS", "SC"],
}

linhas = []
for regiao, ufs in regioes.items():
    for uf in ufs:
        linhas.append({"SG_UF_PROVA": uf, "REGIAO": regiao})

d_uf = pd.DataFrame(linhas)
print(d_uf)
print("Total de UFs:", len(d_uf))

d_renda = pd.DataFrame({ "Q006": list("ABCDEFGHIJKLMNOPQ"),
    "FAIXA_RENDA": ["Sem renda", "Até 1 SM", "1 a 2 SM", "1 a 2 SM",
                    "2 a 3 SM", "2 a 3 SM", "3 a 5 SM", "3 a 5 SM"]
                   + ["5 a 10 SM"] * 5 + ["Mais de 10 SM"] * 4,
    "ORDEM_RENDA": [1, 2, 3, 3, 4, 4, 5, 5] + [6] * 5 + [7] * 4,
})
print(d_renda)

d_uf.to_csv(pasta / "dUF.csv", index=False, encoding="utf-8-sig")
d_renda.to_csv(pasta / "dRenda.csv", index=False, encoding="utf-8-sig")
print("Dimensões salvas em:", pasta)

d_cor = pd.DataFrame({
    "TP_COR_RACA": [0, 1, 2, 3, 4, 5, 6],
    "COR_RACA": ["Não informado", "Branca", "Preta", "Parda",
                 "Amarela", "Indígena", "Não informado"],
    "ORDEM_COR": [6, 1, 2, 3, 4, 5, 6],
})
print(d_cor)

d_conclusao = pd.DataFrame({
    "TP_ST_CONCLUSAO": [1, 2, 4],
    "SITUACAO_CONCLUSAO": ["Já concluiu", "Concluindo em 2022",
                           "Não concluiu e não está cursando"],
})
print(d_conclusao)

d_cor.to_csv(pasta / "dCorRaca.csv", index=False, encoding="utf-8-sig")
d_conclusao.to_csv(pasta / "dConclusao.csv", index=False, encoding="utf-8-sig")
print("Dimensões de cor e conclusão salva")

d_idade = pd.DataFrame({
    "TP_FAIXA_ETARIA": list(range(1, 21)),
    "FAIXA_ETARIA": ["Até 17 anos"] * 2 + ["18 a 19 anos"] * 2
                    + ["20 a 21 anos"] * 2 + ["22 a 25 anos"] * 4
                    + ["26 a 30 anos"] + ["31 a 40 anos"] * 2
                    + ["41 a 50 anos"] * 2 + ["Mais de 50 anos"] * 5,
    "ORDEM_IDADE": [1] * 2 + [2] * 2 + [3] * 2 + [4] * 4
                   + [5] + [6] * 2 + [7] * 2 + [8] * 5,
})
print(d_idade)

d_idade.to_csv(pasta / "dFaixaEtaria.csv", index=False, encoding="utf-8-sig")
print("Dimensão de faixa etária salva.")