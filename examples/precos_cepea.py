#!/usr/bin/env python3
"""
Exemplo: Preços CEPEA da soja e boi gordo.
Requer: pip install agrobr
"""
from agrobr.sync import cepea


def main():
    print("=" * 60)
    print("PREÇOS CEPEA — ÚLTIMOS 30 DIAS")
    print("=" * 60)

    # Preço diário da soja
    print("\n[1] Preço da soja (últimos 30 dias)")
    df_soja = cepea.indicador('soja', inicio='2024-01-01')
    print(df_soja.tail(10).to_string(index=False))

    # Último preço do boi gordo
    print("\n[2] Último preço do boi gordo")
    ultimo_boi = cepea.ultimo('boi')
    print(f"  Produto:  {ultimo_boi.produto}")
    print(f"  Valor:    R$ {ultimo_boi.valor}/@")
    print(f"  Data:     {ultimo_boi.data}")

    # Listar produtos disponíveis
    print("\n[3] Produtos CEPEA disponíveis")
    produtos = cepea.produtos()
    print(f"  Total: {len(produtos)} produtos")
    print(f"  Lista: {', '.join(produtos[:10])}...")

    # Listar praças da soja
    print("\n[4] Praças de comercialização da soja")
    pracas = cepea.pracas('soja')
    print(f"  Praças: {', '.join(pracas)}")


if __name__ == "__main__":
    main()
