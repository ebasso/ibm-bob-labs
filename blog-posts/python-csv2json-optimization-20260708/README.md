# Projeto CSV para JSON com Baixa Performance

Este projeto lê um arquivo `.csv` e gera um arquivo `.json` em Python de forma intencionalmente ineficiente.

## Como usar

Versão original, com baixa performance:

```bash
python3 main-low.py entrada.csv saida.json
```

Versão otimizada, com alta performance:

```bash
python3 main-high.py entrada.csv saida.json
```

## Observações

- O arquivo `main.py` foi escrito para ter baixa performance de propósito.
- O arquivo `main-high.py` aplica uma versão otimizada da mesma conversão CSV para JSON.
- A versão otimizada registra início, fim e tempo total de execução no terminal.
