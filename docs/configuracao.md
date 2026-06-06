# Configuração

Guia completo de configuração da skill agrobr.

## Variáveis de Ambiente

A maioria das fontes não requer autenticação. As exceções:

| Variável | Fonte | Descrição | Como obter |
|----------|-------|-----------|------------|
| `AGROBR_INMET_TOKEN` | INMET | Token de acesso às estações meteorológicas | [INMET Portal](https://portal.inmet.gov.br/) |
| `AGROBR_USDA_API_KEY` | USDA PSD | Chave de API do USDA | [USDA API](https://api.data.gov/signup/) |
| `AGROBR_MAPBIOMAS_ALERTA_TOKEN` | MapBiomas Alerta | Token de acesso | [MapBiomas Alerta](https://alerta.mapbiomas.org/) |

## Configuração via Código

```python
from agrobr import configure

configure(
    inmet_token="seu_token_aqui",
    usda_api_key="sua_chave_aqui",
    mapbiomas_alerta_token="seu_token_aqui",
)
```

## Configuração via Terminal

```bash
# Ver configuração atual
agrobr config show

# Definir token
agrobr config set inmet_token seutoken

# Health check — verifica disponibilidade das fontes
agrobr health
```

## Modo Síncrono vs Assíncrono

### Síncrono (recomendado)

```python
from agrobr.sync import cepea, conab, datasets

# Funciona diretamente em scripts
df = cepea.indicador('soja')
```

### Assíncrono

```python
import asyncio
from agrobr import cepea, conab, datasets

async def main():
    df = await cepea.indicador('soja')

asyncio.run(main())
```

## Polars

Todas as funções suportam Polars via `as_polars=True`:

```python
from agrobr.sync import datasets

# pandas (padrão)
df_pandas = datasets.producao_anual('soja', ano=2023)

# Polars
df_polars = datasets.producao_anual('soja', ano=2023, as_polars=True)
```

## Proveniência

Para rastrear de qual fonte os dados vieram:

```python
from agrobr.sync import datasets

df, meta = datasets.preco_diario('soja', return_meta=True)
print(f"Fonte selecionada: {meta.selected_source}")
print(f"Fontes tentadas: {meta.attempted_sources}")
```

## Snapshots (Modo Determinístico)

Para reprodutibilidade em papers e auditorias:

```python
from agrobr.snapshots import create_snapshot
from agrobr.sync import datasets

# Criar snapshot dos dados atuais
create_snapshot("2025-Q4")

# Usar snapshot para consultas sem rede
with datasets.deterministic("2025-12-31"):
    df = datasets.preco_diario("soja")
```

## Solução de Problemas

### Erro: `SourceUnavailableError`

A fonte está indisponível. Tente:
1. Verificar `agrobr health`
2. Usar a camada `datasets` (fallback automático)
3. Configurar token se necessário

### Erro: `TokenRequired`

Token não configurado. Veja seção "Variáveis de Ambiente".

### Erro: `RateLimitError`

Muitas requisições. Aguarde ou use cache/snapshots.
