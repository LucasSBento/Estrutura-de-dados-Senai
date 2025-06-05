# 📋 Sistema de RH (Recrutamento de Vagas)

Este é um **Sistema de Recrutamento de Vagas** simples e funcional, desenvolvido em **Python**, que simula um processo básico de recrutamento com foco em ensino de **estruturas de dados**. O sistema permite que usuários se cadastrem, visualizem vagas, se candidatem e finalizem o processo de forma organizada e interativa.

---

## 🚀 Funcionalidades

### 🔐 Login e Cadastro

* Cadastro de usuários (nome, idade, email, senha).
* Login com verificação de credenciais.
* Usuário administrador pré-cadastrado:

  * **Usuário:** `admin`
  * **Senha:** `admin`

### 🧑‍💼 Painel do Administrador

* Adição e listagem de vagas.
* Listagem de todos os candidatos cadastrados.

### 🧾 Visualização de Vagas

* Usuários autenticados podem visualizar todas as vagas disponíveis.

### 🛒 Candidatura a Vagas

* Os usuários podem:

  * Se candidatar a vagas (empilhando no carrinho).
  * Remover a última candidatura (modelo **Pilha - LIFO**).
  * Visualizar suas candidaturas.
  * Finalizar candidatura (simulando envio com métodos de pagamento).

### 💳 Processamento de Inscrição

* Os métodos de "pagamento" (simbolizando envio de currículo) seguem ordem **FIFO (Fila)**:

  * Dinheiro → Pix → Cartão

### 📬 Resumo Final

* Mostra:

  * Nome do candidato
  * Email
  * Vagas selecionadas

---

## 🧠 Estruturas de Dados Utilizadas

| Estrutura           | Implementação em Python | Finalidade no Sistema                                    |
| ------------------- | ----------------------- | -------------------------------------------------------- |
| **Matriz**          | `list[list]`            | Armazena os usuários: nome, idade, email, senha, admin   |
| **Vetor**           | `list`                  | Armazena as vagas disponíveis (`produtos`)               |
| **Lista (Simples)** | `list`                  | Itens de menu, iteração de candidatos, exibição de dados |
| **Pilha (LIFO)**    | `list`                  | Gerencia o carrinho de candidaturas (`carrinho`)         |
| **Fila (FIFO)**     | `collections.deque`     | Métodos de pagamento processados sequencialmente         |

Essas estruturas foram escolhidas para reforçar o entendimento conceitual e prático de como diferentes formas de armazenamento e acesso a dados funcionam na programação.

---

## 🧪 Como Executar

1. Certifique-se de que o **Python 3.x** está instalado.
2. Salve o arquivo com o nome `sistema_rh.py`.
3. Execute o programa pelo terminal:

```bash
python sistema_rh.py
```

---

## 🧾 Exemplo de Fluxo de Uso

1. Inicie o sistema e cadastre-se ou entre como `admin`.
2. Admin pode criar vagas.
3. Usuário visualiza e se candidata a vagas.
4. Finaliza candidatura com método de "pagamento".
5. Sistema exibe resumo e limpa o carrinho.

---

## 🏗️ Estrutura do Projeto

```
📁 sistema-rh
├── sistema_rh.py        # Código-fonte principal
└── README.md            # Documentação do projeto
```

---

## 💡 Melhorias Futuras

* Armazenamento em arquivo ou banco de dados.
* Validação de dados (emails, senhas fortes).
* Interface gráfica com Tkinter ou web com Flask/Django.
* Relatórios de candidatura por usuário.
* Reutilização de métodos de pagamento.

---

## 📝 Licença

Este projeto é livre para fins **educacionais** e pode ser utilizado como base para **ensino de estruturas de dados e lógica de programação**.

---

Se quiser, posso gerar esse conteúdo como um arquivo `README.md` para download. Deseja?
