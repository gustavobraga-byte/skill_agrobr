#!/usr/bin/env python3
"""
Exemplo: Desmatamento PRODES + Queimadas.
Requer: pip install agrobr
"""
from agrobr.sync import desmatamento, queimadas


def main():
    print("=" * 60)
    print("MONITORAMENTO AMBIENTAL — AMAZÔNIA")
    print("=" * 60)

    # 1. Desmatamento PRODES
    print("\n[1] PRODES — Desmatamento no Pará (2022)")
    df_prodes = desmatamento.prodes(
        bioma='Amazônia',
        ano=2022,
        uf='PA'
    )
    print(df_prodes.to_string(index=False))

    # 2. Focos de queimadas
    print("\n[2] Focos de Queimadas — Amazônia (set/2024)")
    df_focos = queimadas.focos(
        ano=2024,
        mes=9,
        uf='PA',
        bioma='Amazonia'
    )
    print(f"  Total de focos: {len(df_focos)}")
    if len(df_focos) > 0:
        print(df_focos.head(10).to_string(index=False))

    # 3. Resumo
    print("\n[3] Resumo")
    print(f"  PRODES (PA, 2022): {len(df_prodes)} registros")
    print(f"  Queimadas (PA, set/2024): {len(df_focos)} focos")


if __name__ == "__main__":
    main()
