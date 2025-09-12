from pathlib import Path
from flask import render_template
import sqlite3

# Caminho do banco de dados SQLite utilizado pelo aplicativo
DB_PATH = Path("data/app.db")

def home_controller():
    """
    Renderiza a página inicial com os registros ativos da tabela 'things'.

    Executa:
        - Conexão com o banco de dados SQLite.
        - Seleção dos registros onde tstatus='on', ordenados pela data mais recente.
        - Retorno do template 'home.html' com os dados filtrados.

    Returns:
        Response: Página HTML renderizada com os dados filtrados.
    """
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Seleciona os campos necessários dos registros ativos, ordenados por data (mais recentes primeiro)
    cur.execute("""
        SELECT t.tid, t.tname, t.timage, p.name as owner_name
        FROM things t
        JOIN peoples p ON t.towner_id = p.id
        WHERE t.tstatus = 'on'
        ORDER BY t.tcreated_at DESC
    """)
    things = cur.fetchall()

    # Encerra a conexão com o banco de dados
    conn.close()

    # Renderiza o template passando os dados dos itens ativos
    return render_template("home.html", things=things)