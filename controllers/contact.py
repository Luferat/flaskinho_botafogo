import html
import sqlite3
from flask import render_template, request
from pathlib import Path

# Localização do banco de dados
DB_PATH = Path("data/app.db")


def contact_controller():
    """
    Controlador para a rota /contacts.

    Processa o formulário de contato:
    - Recebe dados via POST.
    - Sanitiza os campos.
    - Salva no banco de dados SQLite.
    - Retorna a página de contato com mensagem de sucesso.

    Returns:
        Response: Página HTML renderizada.
    """
    # Inicializa variáveis de controle
    success = False
    # Primeiro nome do remetente
    fname = ""

    # Se o formulário foi enviado via POST
    if request.method == "POST":
        # Sanitiza os dados recebidos do formulário
        name = html.escape(request.form.get("name", "").strip())
        email = html.escape(request.form.get("email", "").strip())
        subject = html.escape(request.form.get("subject", "").strip())
        message = html.escape(request.form.get("message", "").strip())

        # Insere os dados no banco de dados SQLite
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)",
            (name, email, subject, message)
        )
        conn.commit()
        conn.close()

        # Extrai o primeiro nome para exibir na mensagem de sucesso
        fname = name.split()[0] if name else ""
        success = True

    # Renderiza a página de contatos, passando variáveis de status
    return render_template("contact.html", success=success, fname=fname if success else "")
