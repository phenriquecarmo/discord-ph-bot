# discord-ph-bot
Discord Bot for Channel

## Controlar versões do python

### Instalar o `pyenv`:

```bash
curl https://pyenv.run | bash
```

### Adicionar pyenv ao seu shell: Adicione as seguintes linhas ao seu arquivo de inicialização do shell (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Reiniciar o shell:

```bash
exec "$SHELL"
```

### Instalar e utilizar versão utilizada no projeto:

```bash
pyenv install
pyenv local
```

## Inicializar ambiente:

```bash
python -m venv ./.venv
source .venv/bin/activate
```

## Instalação de dependências

```bash
pip install -r requirements.txt
```

## Remover as saídas das execuções no commit dos notebooks

```bash
nbstripout --install
```

## Atualizar arquivo requirements.txt

```bash
pip freeze > requirements.txt
```
