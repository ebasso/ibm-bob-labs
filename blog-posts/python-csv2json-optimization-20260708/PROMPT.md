# Prompt para Rebuild com Alta Performance

Use o prompt abaixo para reconstruir o projeto da pasta `python-csv2json-optimization-20260708` mantendo a mesma finalidade, mas com alta performance em Python.

## Prompt

```text
Você é um engenheiro de software especialista em Python e otimização de desempenho.

Sua tarefa é reconstruir um projeto Python que lê um arquivo CSV e gera um arquivo JSON.
O projeto original funciona, mas foi escrito de forma intencionalmente ineficiente.

Objetivo:
- Recriar o projeto com alta performance.
- Continuar usando Python.
- Criar o arquivo `main-high.py` dentro da pasta `python-csv2json-optimization-20260708`.
- Manter a mesma interface de linha de comando, adaptada para o novo arquivo: `python3 main-high.py entrada.csv saida.json`.
- Preservar a lógica principal de conversão de CSV para JSON.

Requisitos técnicos:
- Ler o CSV de forma eficiente, sem trabalho redundante.
- Evitar loops e cópias desnecessárias de strings.
- Evitar serializações repetidas dentro do processamento.
- Escrever o JSON de forma eficiente em disco.
- Registrar o tempo de início, o tempo de fim e o tempo total de execução.
- Manter o código simples, legível e pronto para arquivos maiores.
- Usar apenas bibliotecas padrão do Python, se possível.

Entregáveis esperados:
1. Arquivo `python-csv2json-optimization-20260708/main-high.py` otimizado.
2. Atualização opcional do `README.md` da pasta `python-csv2json-optimization-20260708` com instruções de uso.
3. Registro do tempo de início, fim e duração da execução no terminal.
4. Explicação objetiva das mudanças que melhoram a performance.

Ao reconstruir:
- Remova atrasos artificiais.
- Evite `flush()` a cada caractere.
- Não reconstrua strings caractere por caractere sem necessidade.
- Não faça `json.dumps()` e `json.loads()` repetidamente dentro do loop.
- Prefira processamento direto com `csv.DictReader` e escrita única com `json.dump()`.

No final, apresente:
- O código completo.
- Uma lista curta comparando os gargalos do projeto antigo com as melhorias do novo.
```
