# CRUD de Produtos em Flask

Este projeto é uma aplicação simples de CRUD (Create, Read, Update, Delete) de produtos utilizando Flask, uma biblioteca leve para desenvolvimento web em Python. Os produtos são armazenados em memória usando um array, permitindo fácil manipulação e teste.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação.
- **Flask**: Framework web para Python.
- **JSON**: Formato de troca de dados.

## Funcionalidades

- **Criar um novo produto**: Adiciona um produto à lista.
- **Obter todos os produtos**: Retorna uma lista de todos os produtos.
- **Obter um produto específico**: Retorna os detalhes de um produto com base em seu ID.
- **Atualizar um produto**: Modifica as informações de um produto existente.
- **Deletar um produto**: Remove um produto da lista.

## Endpoints

A API possui os seguintes endpoints:

### 1. Criar um Novo Produto

- **URL**: `/produtos`
- **Método**: `POST`
- **Body** (JSON):
  ```json
  {
      "NomeDoProduto": "Nome do Produto",
      "descricao": "Descrição do Produto",
      "preco": "Preço do Produto",
      "QuantidadeDeProdutos": "Quantidade em Estoque"
  }
  
### 2. Obter Todos os Produtos

- **URL**: `/produtos`
- **Método**: `GET`
- **Resposta** (JSON):
  ```json
  [
      {
          "NomeDoProduto": "Produto A",
          "descricao": "Descrição do Produto A",
          "preco": "10.00",
          "QuantidadeDeProdutos": "100"
      },
      {
          "NomeDoProduto": "Produto B",
          "descricao": "Descrição do Produto B",
          "preco": "20.00",
          "QuantidadeDeProdutos": "200"
      }
  ]

