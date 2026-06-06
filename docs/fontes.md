# Fontes de Dados

Referência completa das 38+ fontes de dados suportadas pela skill agrobr.

## Fontes por Categoria

### 1. Preços e Mercado

| Fonte | Descrição | Acesso | Token |
|-------|-----------|--------|-------|
| **CEPEA** | Centro de Estudos Avançados em Economia Aplicada | Público | Não |
| **B3** | Bolsa de Valores — dados de futuros | Público | Não |
| **IMEA** | Instituto Mato-Grossense de Economia Agropecuária | Restrito | Sim |
| **CONAB CEASA** | Companhia Nacional de Abastecimento — preços CEASA | Público | Não |
| **ANP** | Agência Nacional do Petróleo — diesel | Público | Não |

### 2. Produção e Safras

| Fonte | Descrição | Acesso | Token |
|-------|-----------|--------|-------|
| **CONAB** | Acompanhamento da Safra Brasileira de Grãos | Público | Não |
| **IBGE PAM** | Pesquisa Agrícola Municipal | Público | Não |
| **IBGE LSPA** | Levantamento Sistemático da Produção Agrícola | Público | Não |
| **IBGE PPM** | Pesquisa Pecuária Municipal | Público | Não |
| **IBGE Abate** | Abate de animais | Público | Não |
| **IBGE PEVS** | Produção Extrativa e Silvicultura | Público | Não |
| **IBGE Leite** | Aquisição de Leite | Público | Não |
| **IBGE Censo Agro** | Censo Agropecuário | Público | Não |
| **DERAL** | Departamento de Economia Rural (PR) | Público | Não |
| **USDA PSD** | Production, Supply and Distribution | Público | API Key |
| **ABIOVE** | Associação Brasileira das Indústrias de Óleos Vegetais | Público | Não |
| **ANEC** | Associação Nacional dos Exportadores de Cereais | Público | Não |
| **Rio Verde** | Fundação Municipal de Educação e Cultura | Público | Não |

### 3. Comércio e Logística

| Fonte | Descrição | Acesso | Token |
|-------|-----------|--------|-------|
| **ComexStat** | Ministério da Economia — comércio exterior | Público | Não |
| **UN Comtrade** | Comércio internacional da ONU | Público | Não |
| **ANTAQ** | Agência Nacional de Transportes Aquaviários | Público | Não |
| **ANTT** | Agência Nacional de Transportes Terrestres | Público | Não |

### 4. Crédito, Câmbio e Seguro

| Fonte | Descrição | Acesso | Token |
|-------|-----------|--------|-------|
| **BCB SICOR** | Sistema de Informações do Crédito Rural | Público | Não |
| **BCB SGS** | Sistema Gerenciador de Séries Temporais | Público | Não |
| **BCB PTAX** | Taxas de câmbio | Público | Não |
| **BCB Focus** | Boletim de Expectativas | Público | Não |
| **MAPA PSR** | Programa de Seguro Rural | Público | Não |

### 5. Clima e Água

| Fonte | Descrição | Acesso | Token |
|-------|-----------|--------|-------|
| **NASA POWER** | Prediction Of Worldwide Energy Resources | Público | Não |
| **INMET** | Instituto Nacional de Meteorologia | Público | Token |
| **ANA/SNIRH** | Agência Nacional de Águas | Público | Não |

### 6. Ambiental

| Fonte | Descrição | Acesso | Token |
|-------|-----------|--------|-------|
| **Queimadas** | INPE — focos de calor | Público | Não |
| **PRODES** | INPE — desmatamento anual | Público | Não |
| **DETER** | INPE — alertas de desmatamento | Público | Não |
| **MapBiomas** | Mapa anual de uso do solo | Público | Não |
| **MapBiomas Alerta** | Alertas de desmatamento | Público | Token |
| **IBAMA** | Lista suja, embargos | Público | Não |
| **ICMBio** | Unidades de Conservação | Público | Não |
| **SFB** | Serviço Florestal Brasileiro | Público | Não |

### 7. Cadastros Territoriais

| Fonte | Descrição | Acesso | Token |
|-------|-----------|--------|-------|
| **SICAR/CAR** | Sistema Nacional de Cadastro Ambiental Rural | Público | Não |
| **FUNAI** | Fundação Nacional dos Povos Indígenas | Público | Não |
| **INCRA** | Instituto Nacional de Colonização e Reforma Agrária | Público | Não |
| **EMBRAPA Solos** | Dados de solos | Público | Não |

### 8. Insumos e Regulatório

| Fonte | Descrição | Acesso | Token |
|-------|-----------|--------|-------|
| **ANDA** | Associação Nacional para Difusão de Adubos | Restrito | Não |
| **Defensivos** | Agrofit — defensivos agrícolas | Público | Não |
| **RNC** | Registro Nacional de Cultivares | Público | Não |
| **Lista Suja** | Lista suja do trabalho escravo | Público | Não |
| **ZARC** | Zoneamento Agrícola de Risco Climático | Público | Não |

## Tokens Necessários

```bash
# INMET (estações meteorológicas)
export AGROBR_INMET_TOKEN=seu_token

# USDA PSD (dados internacionais)
export AGROBR_USDA_API_KEY=sua_key

# MapBiomas Alerta
export AGROBR_MAPBIOMAS_ALERTA_TOKEN=token
```

## Acesso via Camada Semântica

A camada `datasets` orquestra fallback automático entre fontes:

```python
from agrobr.sync import datasets

# Tenta: IBGE PAM → CONAB
df = datasets.producao_anual('soja', ano=2023)

# Tenta: INMET → NASA POWER
df = datasets.clima(uf='SP', ano=2024)

# Tenta: BCB SICOR → BigQuery (basedosdados)
df = datasets.credito_rural('soja', safra='2024/25')
```
