# flaskinho
Experimentos com Python / Flask para criação de um aplicativo Web.

Python 3.13

## Ambiente Virtual
```
python -m venv .venv
```
Para uma versão específica do Python:
```
python3.13 -m venv .venv
```

Para ativar o `venv`:
```
.venv\Scrits\activate
```

Caso precisa desativar:
```
.venv\Scripts\deactivate.bat
```

> _OBS: Verifique se o VSCode está usando o mesmo "venv"._

## Dependências

Instalando o Flask:
```
pip install flask
```

Criando a lista de dependências:
```
pip freeze > dependencies.txt
```

Caso precise baixar as dependências novamente:
```
pip install -r dependencies.txt
```

> _Dica: sempre que instalar uma nova dependência gere o 'dependencies.txt' novamente._

## Rodando o Aplicativo

```
flask run
```
ou
```
python app.py
```

ou ainda, clicar no botão "Play" do VSCode quando `app.py` estiver aberto.