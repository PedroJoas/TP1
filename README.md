# Técnicas de Programação para Ciência de Dados
Repositório destinado a disciplina de Técnicas de Programação para Ciência de Dados 2024.2


## Configurando o Ambiente Virtual  

Um ambiente virtual permite gerenciar dependências de projeto isoladamente.  

### Criando o ambiente virtual  

1. No diretório raiz do projeto, crie um ambiente virtual:  
   ```bash
   python -m venv env
   # ou, se o comando acima não funcionar
   python3 -m venv env
   ```

2. Isso criará um diretório chamado `env`, onde o ambiente virtual será armazenado.

---

### Ativando o ambiente virtual  

- **No Windows**:  
  ```bash
  .\env\Scripts\activate
  ```

- **No macOS/Linux**:  
  ```bash
  source env/bin/activate
  ```

Você saberá que o ambiente está ativo quando o nome do ambiente (`env`) aparecer antes do cursor no terminal, por exemplo:  
```bash
(env) user@machine:~$
```

---

### Instalando as dependências  

1. Após ativar o ambiente virtual, instale as dependências listadas no `requirements.txt`:  
   ```bash
   pip install -r requirements.txt
   ```

2. Aguarde enquanto as bibliotecas são instaladas. Quando o processo terminar, todas as dependências estarão configuradas no ambiente virtual.

---

## Executando o Projeto  

Certifique-se de que o ambiente virtual está ativado antes de executar qualquer script do projeto.  

- Ative o ambiente conforme mostrado acima.
- Execute o script desejado, por exemplo:  
  ```bash
  python main.py
  ```

---

## Desativando o Ambiente Virtual  

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual usando o comando:  
```bash
deactivate
```

Isso retornará você ao ambiente global do Python.

---

## Problemas Comuns  

1. **O comando `python` chama uma versão diferente do Python**  
   Use `python3` em vez de `python` nos comandos.

2. **Erro ao instalar dependências**  
   Certifique-se de estar no diretório correto e com o ambiente virtual ativado antes de executar `pip install`.

3. **Permissões negadas no Linux/macOS**  
   Use `python3 -m venv env` em vez de `python -m venv env` se você tem múltiplas versões do Python instaladas.

---  

Agora você está pronto para usar o projeto! 🎉

--- 

