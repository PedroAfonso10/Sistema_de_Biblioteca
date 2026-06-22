# Sistema de Biblioteca Universitária

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-brightgreen)](https://flask.palletsprojects.com/)

## 📌 Sobre o Projeto

Sistema de Biblioteca Universitária criado como API REST em Python com Flask para suportar gestão de acervo, usuários e empréstimos sem depender de um banco de dados tradicional.

A solução foi projetada para uso acadêmico, com indexação baseada em estruturas de dados puras. O projeto abrange cadastro, consulta e exclusão de usuários e livros, registro de empréstimos, devoluções, gerenciamento de filas de espera e suporte a desfazer operações. Esse modelo valida conceitos de performance, integridade e ordenação em tempo real, utilizando um padrão de projeto Singleton para garantir instâncias únicas dos repositórios.

### Diferenciais técnicos

- Indexação e busca otimizadas sem banco relacional
- Estruturas de dados customizadas para cada necessidade de domínio
- Fluxo completo de empréstimos com fila de espera e undo

## 🛠️ Arquitetura e Estruturas de Dados Utilizadas

A arquitetura do projeto segue uma separação clara entre rotas, controllers, services e repositories. A persistência é implementada em memória simples, com uso de objetos singleton globais para unificar o estado da aplicação.

### Estruturas de dados

| Estrutura | Uso no sistema | Benefício técnico |
|---|---|---|
| Árvore Binária de Busca (ABB) | Repositório de livros, ordenação por título | Listagens ordenadas em ordem crescente via percurso Em-Ordem (In-Order) |
| Tabela Hash (HashTable) | Indexação de empréstimos por ID e filas de espera por ISBN | Busca rápida O(1) para operações de leitura e remoção |
| Fila (Queue) | Controle cronológico de espera para exemplares esgotados | Gerencia ordem FIFO de usuários aguardando títulos indisponíveis |
| Pilha (Stack) | Histórico de reversão de empréstimos | Suporte ao comando de desfazer último empréstimo via LIFO |
| Lista Encadeada (LinkedList) | Armazenamento sequencial de registros e transações | Inserção dinâmica e navegação linear de dados em memória |

### Papel de cada estrutura

- **ABB**: mantém o acervo ordenado internamente por título. Ideal para listar livros em ordem alfabética sem depender de ordenação adicional.
- **HashTable**: usada para localizar imediatamente empréstimos ativos e filas associadas ao ISBN do livro.
- **Queue**: registra a ordem de chegada dos usuários que ficam em fila de espera para um livro esgotado.
- **Stack**: armazena o histórico de empréstimos recentes para permitir desfazer a última operação sem reprocessar toda a fila.
- **LinkedList**: base para coleções de transações e entidades que crescem dinamicamente sem alocação fixa.

## 🏗️ Arquitetura de Pastas

A organização do projeto separa responsabilidades em camadas claras, facilitando manutenção, testes e evolução. Cada pasta tem um propósito específico e representa um componente da aplicação.
### Visão Geral da Arquitetura

A arquitetura do sistema é orientada por camadas de responsabilidade, com foco em clareza, modularidade e separação entre interface, negócio e persistência.

#### Entrada da aplicação
- `app.py` — inicializa a aplicação Flask, configura os blueprints e define o ponto de partida do sistema. (Inicialização)

#### API e controle
- `api/routes` — mapeia rotas HTTP para os controllers. (Definição de rotas)
- `api/controller` — processa requisições, valida dados de entrada e converte resultados em respostas JSON. (Controladores)

#### Regras de negócio
- `service` — encapsula a lógica de domínio, orquestra operações entre API e repositórios e aplica validações de negócio. (Regras de negócio)

#### Persistência e dados
- `repository` — gerencia o armazenamento em memória e expõe operações de CRUD para as entidades. (Persistência)
- `models` — define as entidades do domínio (Livro, Usuário, Empréstimo) e suas estruturas de dados. (Modelos)

#### Infraestrutura
- `exceptions` — centraliza exceções customizadas e regras de validação. (Tratamento de erros)
- `structures` — implementa as estruturas de dados internas (ABB, HashTable, Queue, Stack, LinkedList) utilizadas pelos repositórios. (Biblioteca de estruturas)

Essa organização mantém a lógica de apresentação, negócio e dados desacoplada e facilita a evolução do sistema.

```text
Sistema_de_Biblioteca/
├─ app.py                             — Inicialização: configura Flask e blueprints
├─ api/                                — Interface HTTP
│  ├─ controller/                      — Controladores: lógica de conversão entre request/response
│  │  ├─ emprestimo_controller.py
│  │  ├─ livro_controller.py
│  │  └─ usuario_controller.py
│  └─ routes/                          — Roteamento: endpoints e blueprints
│     ├─ emprestimo_routes.py
│     ├─ livro_routes.py
│     └─ usuario_routes.py
├─ exceptions/                         — Tratamento de erros e validações
│  ├─ exceptions.py
│  └─ validator.py
├─ models/                             — Modelos de domínio: entidades e atributos
│  ├─ emprestimo.py
│  ├─ livro.py
│  └─ usuario.py
├─ repository/                         — Persistência em memória: acesso a dados
│  ├─ emprestimo_repository.py
│  ├─ livros_repository.py
│  └─ usuario_repository.py
├─ service/                            — Regras de negócio e orquestração
│  ├─ emprestimo_service.py
│  ├─ livros_service.py
│  └─ usuario_service.py
└─ structures/                         — Implementações de estruturas de dados
   ├─ binary_search_tree/
   │  ├─ abb.py
   │  └─ node.py
   ├─ hash_table/
   │  └─ hashtable.py
   ├─ linked_list/
   │  ├─ linkedlist.py
   │  └─ node.py
   ├─ queue/
   │  └─ queue.py
   └─ stack/
      └─ stack.py
```

## 🔌 Endpoints da API (Visão Geral)

### Usuários

| Método | Rota | Descrição |
|---|---|---|
| GET | `/usuarios` | Lista todos os usuários cadastrados |
| GET | `/usuarios/<matricula>` | Recupera um usuário pela matrícula |
| POST | `/usuarios` | Cadastra um novo usuário |
| DELETE | `/usuarios/<matricula>` | Remove um usuário pela matrícula |

### Livros

| Método | Rota | Descrição |
|---|---|---|
| GET | `/livros` | Lista todos os livros cadastrados |
| GET | `/livros/<isbn>` | Recupera um livro pelo ISBN |
| POST | `/livros` | Cadastra um novo livro no acervo |
| DELETE | `/livros/<isbn>` | Remove um livro pelo ISBN |

### Empréstimos

| Método | Rota | Descrição |
|---|---|---|
| GET | `/emprestimos` | Lista todos os empréstimos realizados |
| POST | `/emprestimos` | Registra um novo empréstimo |
| PUT | `/emprestimos/<id_emprestimo>/devolucao` | Registra devolução de empréstimo |
| POST | `/emprestimos/desfazer` | Desfaz o último empréstimo realizado |
| GET | `/emprestimos/relatorio` | Gera relatório do acervo com disponibilidade e fila |

## 🚀 Como Executar o Projeto

Siga os comandos abaixo conforme seu ambiente de execução.

Bash (Linux / macOS):

```bash
git clone <URL_DO_REPOSITORIO>
cd Sistema_de_Biblioteca/Sistema_de_Biblioteca
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

PowerShell (Windows):

```powershell
git clone <URL_DO_REPOSITORIO>
Set-Location -Path 'Sistema_de_Biblioteca\Sistema_de_Biblioteca'
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Command Prompt (Windows - cmd.exe):

```cmd
git clone <URL_DO_REPOSITORIO>
cd Sistema_de_Biblioteca\Sistema_de_Biblioteca
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python app.py
```

A API será inicializada em:

```text
http://localhost:5000
```

## 🧪 Roteiro de Testes

1. **Cadastrar um livro**
   - Envie `POST /livros` com payload válido.
   - Verifique retorno `201` e exibição dos dados do livro.

2. **Cadastrar um usuário**
   - Envie `POST /usuarios` com matrícula válida.
   - Aguarde retorno `201`.

3. **Realizar empréstimos até esgotar o título**
   - Envie múltiplos `POST /emprestimos` para o mesmo ISBN.
   - Observe decremento de `qtd_exemplares` a cada empréstimo.

4. **Tentar emprestar livro indisponível**
   - Quando o título estiver esgotado, envie `POST /emprestimos` novamente.
   - Valide retorno `202` e entrada do usuário na fila de espera.

5. **Gerar relatório do acervo**
   - Envie `GET /emprestimos/relatorio`.
   - Confirme que o relatório inclui `total_na_fila` e `matriculas_na_fila` para o ISBN em espera.

6. **Realizar devolução**
   - Envie `PUT /emprestimos/<id_emprestimo>/devolucao` para um empréstimo ativo.
   - Verifique que o livro retornou para o acervo ou foi repassado ao próximo da fila.

7. **Verificar repasse automático**
   - Caso exista fila de espera, confirme que o próximo usuário recebe o livro automaticamente após devolução.

8. **Desfazer o último empréstimo**
   - Envie `POST /emprestimos/desfazer`.
   - Verifique retorno `200` e restauração do estado anterior do estoque.

## Observações finais

Este sistema foi desenvolvido para demonstrar uma abordagem acadêmica de persistência em memória, enfatizando controle manual de estruturas de dados e operações determinísticas.
