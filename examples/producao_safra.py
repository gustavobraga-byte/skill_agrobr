#!/usr/bin/env python3
"""
Exemplo: Produção de milho — datasets + CONAB.
Requer: pip install agrobr
"""
from agrobr.sync import datasets, conab


def main():
    print("=" * 60)
    print("PRODUÇÃO DE MILHO — BRASIL")
    print("=" * 60)

    # 1. Produção anual via camada semântica (fallback automático)
    print("\n[1] Produção anual consolidada (datasets)")
    df_producao = datasets.producao_anual('milho', ano=2023)
    print(df_producao.to_string(index=False))

    # 2. Série histórica CONAB
    print("\n[2] Série histórica CONAB (2010-2024)")
    df_serie = conab.serie_historica('milho', inicio=2010, fim=2024)
    print(df_serie.to_string(index=False))

    # 3. Comparação entre fontes
    print("\n[3] Comparação")
    if df_producao is not None and df_serie is not None:
        print("  Dados obtidos de duas fontes diferentes.")
        print("  Compare os valores para verificar consistência.")
    else:
        print("  Uma ou mais fontes indisponíveis.")


if __name__ == "__main__":
    main()
