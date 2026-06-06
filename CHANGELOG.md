# Changelog

Todas as mudanças notáveis nesta skill serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2025-01-01

### Adicionado
- Skill completa com 38+ fontes de dados agrícolas brasileiros
- SKILL.md com documentação abrangente de todas as funções
- 3 cenários de avaliação (evals): CEPEA, produção de milho, desmatamento/queimadas
- Referência rápida por 8 categorias de dados:
  - Preços e Mercado (CEPEA, B3, IMEA, CONAB CEASA, ANP)
  - Produção e Safras (CONAB, IBGE PAM/LSPA/PPM/Abate/PEVS, DERAL, USDA, ABIOVE, ANEC)
  - Comércio e Logística (ComexStat, UN Comtrade, ANTAQ, ANTT)
  - Crédito e Finanças (BCB/SICOR, BCB SGS/PTAX/Focus, MAPA PSR)
  - Clima e Água (NASA POWER, INMET, ANA/SNIRH)
  - Ambiental (Queimadas, PRODES/DETER, MapBiomas, IBAMA, ICMBio, SFB)
  - Cadastros Territoriais (SICAR/CAR, FUNAI, INCRA, EMBRAPA Solos)
  - Insumos e Regulatório (ANDA, Defensivos, RNC, Lista Suja, ZARC)
- Camada semântica `datasets` com 35 datasets e fallback automático
- Suporte a Polars via `as_polars=True`
- Modo determinístico para reprodutibilidade
- Sistema de snapshots para auditorias
- Documentação de configuração (tokens de ambiente)
- Guia de uso síncrono vs assíncrono
