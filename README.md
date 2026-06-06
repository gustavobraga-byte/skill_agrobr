# agrobr — Skill para Dados Agrícolas Brasileiros

Skill do [PesquisAI](https://github.com/K-Dense-AI/scientific-agent-skills) que unifica **38+ fontes públicas** de dados agropecuários brasileiros em uma única interface Python.

## Visão Geral

| Aspecto | Detalhe |
|---------|---------|
| **Nome** | `agrobr` |
| **Descrição** | Acesso a dados agrícolas brasileiros de 38+ fontes públicas |
| **Categoria** | Dados Governamentais / Agricultura |
| **Compatível com** | PesquisAI, agentes K-Dense, scripts Python genéricos |
| **Formato** | SKILL.md + evals/ + documentação |

## O que esta skill cobre

- **Preços e Mercado**: CEPEA, B3, IMEA, CONAB CEASA, ANP Diesel
- **Produção e Safras**: CONAB, IBGE PAM/LSPA/PPM/Abate/PEVS, DERAL, USDA, ABIOVE, ANEC
- **Comércio e Logística**: ComexStat, UN Comtrade, ANTAQ, ANTT
- **Crédito e Finanças**: BCB/SICOR, BCB SGS/PTAX/Focus, MAPA PSR
- **Clima e Água**: NASA POWER, INMET, ANA/SNIRH
- **Ambiental**: Queimadas, PRODES/DETER, MapBiomas, IBAMA, ICMBio, SFB
- **Cadastros Territoriais**: SICAR/CAR, FUNAI, INCRA, EMBRAPA Solos
- **Insumos e Regulatório**: ANDA, Defensivos, RNC, Lista Suja, ZARC

## Estrutura da Skill

```
agrobr/
├── SKILL.md              # Instruções principais da skill
├── evals/
│   └── evals.json        # Avaliações de qualidade (3 cenários)
├── README.md             # Este arquivo
├── LICENSE               # Licença MIT
├── CHANGELOG.md          # Histórico de versões
├── CONTRIBUTING.md       # Guia de contribuição
├── .gitignore
├── .github/              # Templates e CI
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
├── docs/                 # Documentação adicional
│   ├── guia-rapido.md
│   ├── fontes.md
│   └── configuracao.md
├── examples/             # Exemplos de uso
│   ├── precos_cepea.py
│   ├── producao_safra.py
│   └── desmatamento.py
└── tests/                # Testes da skill
    └── test_skill_structure.py
```

## Instalação da Biblioteca

```bash
pip install agrobr
```

Para recursos geoespaciais:
```bash
pip install agrobr[geo]
pip install agrobr[pdf]
pip install agrobr[all]
```

## Uso Rápido

```python
from agrobr.sync import cepea, conab, datasets

# Preço da soja (CEPEA)
df = cepea.indicador('soja', inicio='2024-01-01')
print(df.head())

# Último preço do boi gordo
ultimo = cepea.ultimo('boi')
print(f"Boi: R$ {ultimo.valor}/@ em {ultimo.data}")

# Produção anual via camada semântica
df = datasets.producao_anual('soja', ano=2023)
print(df)
```

## Evals (Avaliações)

A skill inclui 3 cenários de avaliação:

| # | Nome | O que testa |
|---|------|-------------|
| 1 | `cepea-prices` | Preços CEPEA (soja + boi gordo) |
| 2 | `corn-production` | Produção milho (datasets + CONAB) |
| 3 | `deforestation-fires` | Desmatamento PRODES + queimadas |

### Rodar os evals

```bash
# Via PesquisAI
pesquisai eval run agrobr

# Ou manualmente (verifica estrutura)
python tests/test_skill_structure.py
```

## Categorias de Fontes

### 1. Preços e Mercado
| Fonte | Funções |
|-------|---------|
| CEPEA | `indicador()`, `ultimo()`, `produtos()`, `pracas()` |
| B3 | `ajustes()`, `posicoes_abertas()`, `historico()` |
| IMEA | `cotacoes()` |
| CONAB CEASA | `ceasa_precos()` |

### 2. Produção e Safras
| Fonte | Funções |
|-------|---------|
| CONAB | `safras()`, `balanco()`, `serie_historica()`, `custo_producao()` |
| IBGE PAM | `pam()` |
| IBGE LSPA | `lspa()` |
| IBGE PPM | `ppm()` |
| USDA PSD | `psd()` |

### 3. Ambiental
| Fonte | Funções |
|-------|---------|
| Queimadas | `focos()`, `focos_geo()` |
| PRODES/DETER | `prodes()`, `deter()` |
| MapBiomas | `cobertura()`, `transicao()` |

## Configuração

```bash
export AGROBR_INMET_TOKEN=seu_token
export AGROBR_USDA_API_KEY=sua_key
export AGROBR_MAPBIOMAS_ALERTA_TOKEN=token
```

Ou via código:
```python
from agrobr import configure
configure(inmet_token="...", usda_api_key="...")
```

## Licença

MIT License — veja [LICENSE](LICENSE) para detalhes.

## Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para guia completo de contribuição.

## Links Úteis

- [agrobr no PyPI](https://pypi.org/project/agrobr/)
- [Documentação agrobr](https://github.com/agrobr/agrobr)
- [PesquisAI Skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- [CEPEA](http://www.cepea.esalq.usp.br/)
- [CONAB](https://www.conab.gov.br/)
- [IBGE SIDRA](https://sidra.ibge.gov.br/)
