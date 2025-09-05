# Flaskinho

Criando um aplicativo Web fullstack experimental com Python e Flask.

## Estrutura do Aplicativo

- [ ] No VSCode, crie a estrutura conforme o modelo.
- [ ] Abra `app.py`.
- [ ] Verifique se o VSCode reconhece o versão do Python correta (rodapé à direita).


## Ambiente virtual

- [ ] Criando o ambiente virtual (venv) usando `Python 3.12`
```cmd
python3.12 -m venv .venv
```

> _Troque `python3.12` pela versão mais recente do Python, obtida da loja da Microsoft ou baixada da Internet._

- [ ] Ativando o venv
```cmd
.venv/Scripts/activate
```

- [ ] Se precisar desativar o venv
```cmd
.venv/Scripts/deactivate.tab
```

- [ ] Ao ativar o `venv`, certifique-se que o VSCode está no contexto dele (rodapé à direita).

## Dependências

- [ ] Instale o Flask
```cmd
pip install Flask
```

- [ ] Crie/atualize a lista de dependências
```cmd
pip freeze > requirements.txt
```

- [ ] Quando clonar e reinstalar este aplicativo, para baixar todas as dependências
```cmd
pip install -r requirements.txt
```

## Rodando o aplicativo

- [ ] Defina o aplicativo de entrada, o modo "debug" e execute
```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
Ou
```cmd
python app.py
```
O prompt deve ficar aberto e ativo porque está rodando o serviço do Flask.

Também é possível rodar pelo próprio VSCode, abrindo `app.py` e clicando no triângulo (Play).

Ao rodar, observe o endereço de entrada, normalmente `http://127.0.0.1:5000` e abra-o no navegador.

