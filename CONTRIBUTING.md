# Contribuindo para agrobr-skill

Obrigado por interesse em contribuir! Este guia explica como participar do desenvolvimento desta skill.

## Tipos de Contribuição

### 1. Melhorias na Documentação
- Corrigir erros de digitação
- Adicionar exemplos de uso
- Traduzir documentação
- Melhorar explicações

### 2. Novos Evals (Cenários de Avaliação)
- Criar novos cenários de teste
- Melhorar asserts existentes
- Adicionar edge cases

### 3. Correções de Bug
- Reportar bugs via Issues
- Propor correções via Pull Request

### 4. Nova Funcionalidade
- Sugerir novas fontes de dados
- Propor novas funções de normalização

## Processo

1. **Abra uma Issue** descrevendo o que pretende fazer
2. **Fork** o repositório
3. **Crie uma branch** para sua feature (`git checkout -b feature/nome-da-feature`)
4. **Faça suas alterações**
5. **Execute os testes** (`python tests/test_skill_structure.py`)
6. **Abra um Pull Request**

## Regras

- **Não invente dados**: toda afirmação deve ter fonte rastreável
- **Mantenha o formato SKILL.md**: siga o padrão YAML frontmatter + Markdown
- **Adicione evals**: nova funcionalidade deve ter pelo menos 1 eval
- **Documente mudanças**: atualize o CHANGELOG.md

## Estrutura de um Eval

```json
{
  "id": 4,
  "name": "nome-do-cenario",
  "prompt": "descrição da tarefa em linguagem natural",
  "expected_output": "descrição da saída esperada",
  "files": [],
  "assertions": [
    {
      "name": "nome_da_assert",
      "description": "O que esta assert verifica",
      "expectation": "critério objetivo de sucesso"
    }
  ]
}
```

## Formato das Asserts

| Tipo | Exemplo |
|------|---------|
| Import | `import from agrobr.sync import cepea` |
| Chamada de função | `chama cepea.indicador()` |
| Parâmetros | `chama desmatamento.prodes(bioma=..., ano=..., uf=...)` |
| Saída | `saída contém valor do boi gordo em R$` |
| Comportamento | `código sem async def main()` |

## Padrões de Código

- Use `agrobr.sync` em vez de `agrobr` async para exemplos
- Prefira `datasets` quando a fonte não importa
- Sempre documente tokens necessários
- Inclua `return_meta=True` quando relevante para proveniência

## Perguntas?

Abra uma Issue com a标签 `pergunta` ou `question`.
