---
name: "agrobr"
description: "Access Brazilian agricultural data from 38+ public sources using the agrobr Python library. Use this skill whenever the user needs agricultural data from Brazil — including commodity prices (soja, milho, café, boi, trigo, algodão, arroz), crop production and forecasts (CONAB, IBGE PAM/LSPA), livestock, trade exports/imports (ComexStat, UN Comtrade), rural credit (BCB/SICOR), climate/weather (NASA POWER, INMET), environmental monitoring (Queimadas, PRODES/DETER, MapBiomas), land registry (SICAR/CAR, SIGEF, FUNAI, INCRA), fertilizers (ANDA), pesticides (Agrofit), cultivars (RNC), agricultural zoning (ZARC), port logistics (ANTAQ), and more. Activate this skill when the user explicitly mentions 'agrobr', 'dados agrícolas Brasil', 'preço da soja', 'safra', 'produção agrícola', 'desmatamento', 'queimadas', 'crédito rural', 'zoneamento agrícola', 'cadastro ambiental rural', 'CAR', 'conab', 'cepea', 'ibge pam', 'mapbiomas', 'prodes', 'deter', 'sicor', 'comexstat', or any Brazilian agriculture-related data query. This is the primary and ONLY skill for agrobr — prefer it over the ibge-br skill for agricultural data since agrobr already wraps IBGE PAM/LSPA/PPM/Abate/PEVS/Censo Agro with cleaner APIs and fallback chains."
---

# agrobr — Dados Agrícolas Brasileiros

Biblioteca Python que unifica **38+ fontes públicas** de dados agropecuários brasileiros. Retorna DataFrames pandas padronizados, validados e documentados.

## Instalação

```bash
pip install agrobr
```

Para recursos geoespaciais:
```bash
pip install agrobr[geo]      # variantes _geo (PRODES, SICAR, FUNAI, etc.)
pip install agrobr[pdf]      # para fontes com PDF (ANDA, Lista Suja, Rio Verde)
pip install agrobr[all]      # tudo
```

## Modo Síncrono (recomendado para scripts)

A API nativa é async, mas o módulo `agrobr.sync` expõe **todas as fontes** com a mesma assinatura sem `async/await`:

```python
from agrobr.sync import cepea, conab, ibge, datasets, alt
```

## Referência Rápida por Categoria

### 1. Preços e Mercado

| Fonte | Import | Funções principais |
|-------|--------|-------------------|
| **CEPEA** | `from agrobr.sync import cepea` | `cepea.indicador('soja', inicio='2024-01-01')`, `cepea.ultimo('soja')`, `cepea.produtos()`, `cepea.pracas('soja')` |
| **B3 Futuros** | `from agrobr.sync import b3` | `b3.ajustes(data="13/02/2025")`, `b3.posicoes_abertas(data=...)`, `b3.historico(contrato="boi", inicio=..., fim=...)` |
| **IMEA** (MT) | `from agrobr.sync import imea` | `imea.cotacoes("soja", safra="24/25")` |
| **CONAB CEASA** | `from agrobr.sync import conab` | `conab.ceasa_precos(produto="tomate", ceasa="SAO PAULO")` |
| **ANP Diesel** | `from agrobr.sync import alt` | `alt.anp_diesel.precos_diesel(uf="MT")`, `alt.anp_diesel.vendas_diesel(uf="MT")` |

**Exemplo CEPEA — preço diário da soja:**
```python
from agrobr.sync import cepea

df = cepea.indicador('soja', inicio='2024-01-01')
print(df.head())

ultimo = cepea.ultimo('soja')
print(f"Soja: R$ {ultimo.valor}/sc em {ultimo.data}")

# Listar produtos e praças
print(cepea.produtos())      # 21 produtos
print(cepea.pracas('soja'))  # praças de comercialização
```

**Produtos CEPEA:** soja, milho, cafe, boi, trigo, algodao, arroz, frango, suino, etanol, acucar, leite, ovos, batata, cebola, tomate, feijao, mandioca, cacau, madeira (+1 — ver `cepea.produtos()`; total 21 na v1.1.0).

### 2. Produção e Safras

| Fonte | Import | Funções principais |
|-------|--------|-------------------|
| **CONAB** | `from agrobr.sync import conab` | `conab.safras('soja', safra='2024/25')`, `conab.balanco('soja')`, `conab.serie_historica('soja', inicio=2010, fim=2024)`, `conab.progresso_safra(cultura='Soja', estado='MT', operacao='Colheita')`, `conab.custo_producao(cultura='soja', uf='MT', safra='2024/25')` |
| **IBGE PAM** | `from agrobr.sync import ibge` | `ibge.pam('soja', ano=2023, nivel='uf')`, `ibge.pam('cafe', ano=2023, nivel='municipio', uf='MG')` |
| **IBGE LSPA** | `from agrobr.sync import ibge` | `ibge.lspa('soja', ano=2024, mes=6)` |
| **IBGE PPM** | `from agrobr.sync import ibge` | `ibge.ppm('bovino', ano=2023)` |
| **IBGE Abate** | `from agrobr.sync import ibge` | `ibge.abate('frango', trimestre='202303', uf='PR')` |
| **IBGE PEVS** | `from agrobr.sync import ibge` | `ibge.silvicultura('madeira_tora', ano=2023)`, `ibge.extracao_vegetal('acai', ano=2023)` |
| **IBGE Leite** | `from agrobr.sync import ibge` | `ibge.leite_trimestral(trimestre='202303', uf='MG')` |
| **IBGE PIB Agro** | `from agrobr.sync import ibge` | `ibge.pib_agro(trimestre='202501', setor='agropecuaria')` |
| **IBGE Censo Agro** | `from agrobr.sync import ibge` | `ibge.censo_agro('efetivo_rebanho')`, `ibge.censo_agro_historico('estabelecimentos_area')`, `ibge.censo_agro_municipal_1985('bovinos', uf='SP')` |
| **DERAL** (PR) | `from agrobr.sync import deral` | `deral.condicao_lavouras('soja')` |
| **USDA PSD** | `from agrobr.sync import usda` | `usda.psd('soja', country='BR', market_year=2024)` (requer `AGROBR_USDA_API_KEY`) |
| **ABIOVE** | `from agrobr.sync import abiove` | `abiove.exportacao(ano=2024, produto='grao')` |
| **ANEC** | `from agrobr import anec` (async — ausente no `agrobr.sync` da v1.1.0) | `await anec.embarques(ano=2026)`, `await anec.destinos(ano=2026)` (requer `agrobr[pdf]`; só anos 2026+) |
| **CFTC** | `from agrobr.sync import cftc` | `cftc.cot(commodity='soybeans')` (posições CFTC EUA) |
| **UNICA** | `from agrobr.sync import unica` | `unica.moagem_quinzenal()`, `unica.safra_resumo()`, `unica.producao_historica()` (cana-de-açúcar) |
| **Rio Verde** | `from agrobr.sync import rio_verde` | `rio_verde.ensaio_soja(safra='2023/24')` |

### 3. Comércio e Logística

| Fonte | Import | Funções principais |
|-------|--------|-------------------|
| **ComexStat** | `from agrobr.sync import comexstat` | `comexstat.exportacao('soja', ano=2024, agregacao='mensal')`, `comexstat.importacao('fertilizante', ano=2024)` |
| **UN Comtrade** | `from agrobr.sync import comtrade` | `comtrade.comercio('soja', reporter='BR')`, `comtrade.trade_mirror('soja', reporter='BR')` |
| **ANTAQ** | `from agrobr.sync import antaq` | `antaq.movimentacao(ano=2024)` |
| **ANTT Pedágio** | `from agrobr.sync import alt` | `alt.antt_pedagio.fluxo_pedagio(ano=2024)`, `alt.antt_pedagio.pracas_pedagio(uf='SP')` |

### 4. Crédito, Câmbio e Seguro

| Fonte | Import | Funções principais |
|-------|--------|-------------------|
| **BCB SICOR** | `from agrobr.sync import bcb` | `bcb.credito_rural('soja', safra='2024/25')`, `bcb.credito_rural('soja', safra='2024/25', programa='Pronamp')` |
| **BCB SGS** | `from agrobr.sync import bcb` | `bcb.sgs('selic', ultimos=12)`, `bcb.sgs('ipa_agropecuario', data_inicial='2020-01-01')` |
| **BCB PTAX** | `from agrobr.sync import bcb` | `bcb.ptax(data_inicial='2024-01-01', data_final='2024-12-31')` |
| **BCB Focus** | `from agrobr.sync import bcb` | `bcb.focus('PIB Agropecuário')` |
| **MAPA PSR** | `from agrobr.sync import alt` | `alt.mapa_psr.apolices(cultura='soja', ano=2023)`, `alt.mapa_psr.sinistros(cultura='soja', uf='MT')` |

**Séries SGS disponíveis:** `selic`, `ipca`, `igpm`, `cdi`, `tjlp`, `dolar_ptax_venda`, `ipa_agropecuario`, `pib_agropecuaria`, `cambio_efetivo_real`, e dezenas de outras séries temporais do BCB.

### 5. Clima e Água

| Fonte | Import | Funções principais |
|-------|--------|-------------------|
| **NASA POWER** | `from agrobr.sync import nasa_power` | `nasa_power.clima_uf('MT', ano=2024)`, `nasa_power.clima_ponto(-12.6, -56.1, '2024-01-01', '2024-12-31')` |
| **INMET** | `from agrobr.sync import inmet` | `inmet.estacao('A001', '2024-01-01', '2024-01-31')`, `inmet.clima_uf('SP', ano=2024)` (requer `AGROBR_INMET_TOKEN`) |
| **ANA/SNIRH** | `from agrobr.sync import ana` | `ana.pivos_irrigacao(uf='MT')`, `ana.pivos_irrigacao_geo(uf='MT')` (requer `agrobr[geo]`) |

> INMET retorna `SourceUnavailableError` sem token. Para clima sem token, use NASA POWER.

### 6. Ambiental

| Fonte | Import | Funções principais |
|-------|--------|-------------------|
| **Queimadas** | `from agrobr.sync import queimadas` | `queimadas.focos(ano=2024, mes=9, uf='MT', bioma='Amazonia')`, `queimadas.focos_geo(...)` |
| **PRODES/DETER** | `from agrobr.sync import desmatamento` | `desmatamento.prodes(bioma='Cerrado', ano=2022, uf='MT')`, `desmatamento.deter(bioma='Amazônia', uf='PA', data_inicio='2024-01-01', data_fim='2024-06-30')`, `desmatamento.prodes_geo(...)` |
| **MapBiomas** | `from agrobr.sync import mapbiomas` | `mapbiomas.cobertura(estado='MT', ano=2022)`, `mapbiomas.transicao(estado='PA')` |
| **MapBiomas Alerta** | `from agrobr.sync import mapbiomas_alerta` | `mapbiomas_alerta.alertas(start_date='2024-01-01')` (requer `AGROBR_MAPBIOMAS_ALERTA_TOKEN`) |
| **IBAMA** | `from agrobr.sync import ibama` | `ibama.embargos(uf='PA')`, `ibama.embargos_geo(uf='PA')` |
| **ICMBio** | `from agrobr.sync import icmbio` | `icmbio.ucs(uf='AM', grupo='PI')`, `icmbio.ucs_geo(uf='AM', grupo='PI')` |
| **SFB** | `from agrobr.sync import sfb` | `sfb.cnfp(uf='AM')`, `sfb.concessoes(uf='AM')`, `sfb.ifn_conglomerados(uf='MT')` |

**Biomas disponíveis:** `Amazonia`, `Cerrado`, `Mata_Atlantica`, `Caatinga`, `Pampa`, `Pantanal`.

**Satélites Queimadas:** AQUA, AQUA_M-T, ABI_GOES16, VIIRS_SNPP, VIIRS_NOAA20, e outros (13 satélites).

### 7. Cadastros Territoriais

| Fonte | Import | Funções principais |
|-------|--------|-------------------|
| **SICAR/CAR** | `from agrobr.sync import alt` | `alt.sicar.imoveis('DF')`, `alt.sicar.resumo('MT', municipio='Sorriso')`, `alt.sicar.imoveis_geo('DF')` |
| **Acervo Fundiário** | `from agrobr.sync import acervo_fundiario` | `acervo_fundiario.sigef('MT')`, `acervo_fundiario.snci('PA')`, `acervo_fundiario.assentamentos(uf='PA')` |
| **FUNAI** | `from agrobr.sync import funai` | `funai.terras_indigenas(uf='AM', fase='Regularizada')`, `funai.terras_indigenas_geo(uf='AM')` |
| **INCRA** | `from agrobr.sync import incra` | `incra.quilombolas(uf='BA')` |
| **EMBRAPA Solos** | `from agrobr.sync import embrapa_solos` | `embrapa_solos.perfis(uf='SP')`, `embrapa_solos.mapa_solos(ordem='LATOSSOLO')`, `embrapa_solos.mapa_solos_geo(ordem='LATOSSOLO')` |

### 8. Insumos e Regulatório

| Fonte | Import | Funções principais |
|-------|--------|-------------------|
| **ANDA** | `from agrobr.sync import anda` | `anda.entregas(ano=2024, uf='MT')` (requer `agrobr[pdf]`) |
| **Defensivos** | `from agrobr.sync import defensivos` | `defensivos.formulados(ingrediente_ativo='glifosato')`, `defensivos.tecnicos(titular='Bayer')`, `defensivos.autorizacoes(cultura='soja')` |
| **RNC/CultivarWeb** | `from agrobr.sync import rnc` | `rnc.registradas(especie='Soja')`, `rnc.protegidas(titular='Embrapa')` |
| **Lista Suja** | `from agrobr.sync import lista_suja` | `lista_suja.empregadores(uf='PA')` |
| **ZARC** | `from agrobr.sync import zarc` | `zarc.zoneamento(cultura='soja', uf='MT')`, `zarc.culturas()` |

## Camada Semântica — datasets (recomendado)

A camada `datasets` é o jeito mais simples de obter dados: você não precisa saber qual fonte específica usar, ela orquestra fallback automático e retorna proveniência rastreada.

```python
from agrobr.sync import datasets

# Preço diário (CEPEA → fallback)
df = datasets.preco_diario('soja')

# Produção anual (IBGE PAM → CONAB)
df = datasets.producao_anual('soja', ano=2023)

# Estimativa safra corrente (CONAB → IBGE LSPA)
df = datasets.estimativa_safra('soja', safra='2024/25')

# Crédito rural (BCB SICOR → BigQuery via basedosdados)
df = datasets.credito_rural('soja', safra='2024/25')

# Clima (INMET → NASA POWER)
df = datasets.clima(uf='SP', ano=2024)

# Com proveniência rastreada
df, meta = datasets.preco_diario('soja', return_meta=True)
print(meta.selected_source, meta.attempted_sources)

# Listar todos os datasets disponíveis
print(datasets.list_datasets())

# Polars
df = datasets.preco_diario('soja', as_polars=True)
```

### Datasets Disponíveis (36 na v1.1.0 — ver `datasets.list_datasets()`)

| Dataset | Descrição | Fontes (fallback) |
|---------|-----------|-------------------|
| `preco_diario` | Preços diários spot | CEPEA → cache |
| `preco_atacado` | Preços atacado hortifrúti CEASA | CONAB CEASA/PROHORT |
| `producao_anual` | Produção consolidada | IBGE PAM → CONAB |
| `estimativa_safra` | Estimativa safra corrente | CONAB → IBGE LSPA |
| `serie_historica_safra` | Série histórica 1976+ | CONAB |
| `balanco` | Oferta/demanda | CONAB |
| `custo_producao` | Custos de produção | CONAB |
| `progresso_safra` | Progresso semanal semeadura/colheita | CONAB |
| `condicao_lavouras` | Condição lavouras PR | DERAL |
| `censo_agropecuario` | Censo Agro 1995/2006/2017 | IBGE Censo Agro |
| `censo_agropecuario_historico` | Série histórica 1920-2006 | IBGE SIDRA |
| `censo_agropecuario_legado` | Censo 1995/96 legado | IBGE FTP |
| `censo_agropecuario_municipal_1985` | Censo 1985 municipal | IBGE PDFs |
| `pecuaria_municipal` | Pecuária municipal | IBGE PPM |
| `abate_trimestral` | Abate bovinos/suínos/frangos | IBGE Abate |
| `silvicultura` | Produção silvicultural | IBGE PEVS |
| `extrativismo_vegetal` | Extrativismo (açaí, castanha, erva-mate) | IBGE PEVS |
| `leite_industrial` | Aquisição/industrialização leite | IBGE Leite |
| `pib_agro` | PIB agropecuário trimestral | IBGE SIDRA |
| `exportacao` | Exportações agrícolas | ComexStat → ABIOVE |
| `importacao` | Importações agrícolas | ComexStat |
| `comercio_internacional` | Comércio bilateral HS | UN Comtrade |
| `embarques_anec` | Embarques semanais por porto | ANEC |
| `movimentacao_portuaria` | Movimentação portuária | ANTAQ |
| `futuros_agricolas` | Futuros B3 | B3 |
| `credito_rural` | Crédito rural por cultura | BCB/SICOR → BigQuery |
| `seguro_rural` | Apólices e sinistros | MAPA PSR |
| `fertilizante` | Entregas fertilizantes | ANDA |
| `clima` | Clima mensal/diário | INMET → NASA POWER |
| `desmatamento` | Desmatamento PRODES/DETER | INPE TerraBrasilis |
| `queimadas` | Focos de calor | INPE |
| `uso_do_solo` | Cobertura/uso da terra | MapBiomas |
| `cadastro_rural` | CAR — imóveis rurais | SICAR WFS |
| `zoneamento_agricola` | ZARC — risco climático | MAPA/Embrapa |
| `oferta_demanda_global` | Oferta/demanda global | USDA PSD |

## Utilitários de Normalização

```python
from agrobr.normalize import (
    normalizar_cultura, municipio_para_ibge, coordenada_para_municipio,
    normalizar_uf, normalizar_safra,
)

normalizar_cultura("Soja em Grão")     # "soja"
normalizar_cultura("milho 2ª safra")   # "milho_2"
normalizar_cultura("coffee")           # "cafe"

municipio_para_ibge("Sorriso", "MT")   # 5107925
coordenada_para_municipio(-12.74, -55.68)
# {'codigo_ibge': 5107925, 'nome': 'Sorriso', 'uf': 'MT'}

normalizar_uf("São Paulo")             # "SP"
normalizar_safra("24/25")              # "2024/25"
```

## Contratos e Schemas

Cada dataset tem contrato formal com validação automática:

```python
from agrobr.contracts import get_contract, list_contracts, validate_dataset

contracts = list_contracts()
contract = get_contract("preco_diario")
print(contract.primary_key)   # ['data', 'produto']
validate_dataset(df, "preco_diario")  # levanta ContractViolationError se falhar
```

## Snapshots e Modo Determinístico

Para reprodutibilidade (papers, auditorias, pipelines CI):

```python
from agrobr.snapshots import create_snapshot, list_snapshots, delete_snapshot

info = create_snapshot("2025-Q4")          # captura dados atuais
create_snapshot(sources=["cepea", "conab"]) # fontes específicas

# Modo determinístico — consultas sem rede
from agrobr.sync import datasets
with datasets.deterministic("2025-12-31"):
    df = datasets.preco_diario("soja")
```

## Configuração

Tokens de ambiente necessários para fontes que exigem autenticação:

```bash
export AGROBR_INMET_TOKEN=seu_token          # INMET (estações meteorológicas)
export AGROBR_USDA_API_KEY=sua_key           # USDA PSD (dados internacionais)
export AGROBR_MAPBIOMAS_ALERTA_TOKEN=token   # MapBiomas Alerta
```

Configure o módulo via código:

```python
from agrobr import configure
configure(inmet_token="...", usda_api_key="...")
```

## Dicas Importantes

- **Todas as funções aceitam** `as_polars=True` para retornar Polars DataFrame e `return_meta=True` para metadados de proveniência
- **Sempre use `agrobr.sync`** em vez do módulo async para scripts diretos (evita problemas de event loop)
- **CEPEA** tem cache local DuckDB com TTL inteligente (expira às 18h hora oficial)
- **Licenças**: várias fontes têm licença restritiva (CEPEA NC, IMEA restrito). Consulte `agrobr config show` e as warnings na primeira chamada
- **Health check**: execute `agrobr health` no terminal para verificar disponibilidade das fontes
- **Fallback automático**: a camada `datasets` tenta múltiplas fontes em ordem — se a principal falha, usa a segunda opção
