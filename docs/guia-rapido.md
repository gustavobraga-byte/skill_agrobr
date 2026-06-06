# Guia Rápido

## Início Rápido

```bash
# Instalar a biblioteca
pip install agrobr

# Importar no modo síncrono (recomendado)
from agrobr.sync import cepea, conab, datasets
```

## Receitas Comuns

### Preço de uma commodity

```python
from agrobr.sync import cepea

# Série histórica
df = cepea.indicador('soja', inicio='2024-01-01')

# Último preço disponível
ultimo = cepea.ultimo('soja')
print(f"{ultimo.produto}: R$ {ultimo.valor}/{ultimo.unidade} em {ultimo.data}")
```

### Produção agrícola

```python
from agrobr.sync import datasets

# Produção anual consolidada (fallback automático)
df = datasets.producao_anual('soja', ano=2023)

# Estimativa da safra corrente
df = datasets.estimativa_safra('soja', safra='2024/25')
```

### Crédito rural

```python
from agrobr.sync import bcb

# Crédito por cultura e programa
df = bcb.credito_rural('soja', safra='2024/25', programa='Pronamp')
```

### Clima para agricultura

```python
from agrobr.sync import datasets

# Clima com fallback INMET → NASA POWER
df = datasets.clima(uf='MT', ano=2024)
```

### Monitoramento ambiental

```python
from agrobr.sync import queimadas, desmatamento

# Focos de queimadas
focos = queimadas.focos(ano=2024, mes=9, uf='MT', bioma='Amazonia')

# Desmatamento PRODES
desmat = desmatamento.prodes(bioma='Cerrado', ano=2022, uf='MT')
```

### Comércio exterior

```python
from agrobr.sync import comexstat

# Exportações
df = comexstat.exportacao('soja', ano=2024, agregacao='mensal')

# Importações
df = comexstat.importacao('fertilizante', ano=2024)
```

## Dicas

1. **Use `agrobr.sync`** em vez de `agrobr` async para scripts diretos
2. **Use `datasets`** quando não precisa de uma fonte específica
3. **Adicione `return_meta=True`** para proveniência rastreada
4. **Use `as_polars=True`** para performance com dados grandes
5. **Execute `agrobr health`** no terminal para verificar fontes
