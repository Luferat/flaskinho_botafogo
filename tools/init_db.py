import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
import random

# Localização do banco de dados
DB_PATH = Path("data/app.db")

# Função para gerar datas aleatórias no último ano
def random_date():
    now = datetime.now()
    days_ago = random.randint(0, 365)
    dt = now - timedelta(days=days_ago, hours=random.randint(0,23), minutes=random.randint(0,59))
    return dt.strftime("%Y-%m-%d %H:%M:%S")

# Cria as tabelas e insere dados iniciais "fake"
schema_sql = """
CREATE TABLE peoples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(63) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('on','off')) DEFAULT 'on'
);

INSERT INTO peoples (name, email, password) VALUES
('Joca da Silva', 'joca@email.com', 'Senha@123'),
('Maria de Souza', 'maria@email.com', 'Senha@123'),
('Pedro Oliveira', 'pedro@email.com', 'Senha@123'),
('Ana Pereira', 'ana@email.com', 'Senha@123'),
('Lucas Fernandes', 'lucas@email.com', 'Senha@123');

CREATE TABLE things (
    tid INTEGER PRIMARY KEY AUTOINCREMENT,
    tname VARCHAR(100) NOT NULL,
    tdescription TEXT,
    tstatus TEXT CHECK(tstatus IN ('on','off')) DEFAULT 'on',
    tlocation VARCHAR(255),
    timage VARCHAR(255),
    tcreated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    towner_id INT,
    FOREIGN KEY (towner_id) REFERENCES peoples(id) ON DELETE CASCADE
);

CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    subject VARCHAR(20),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT CHECK(status IN ('on','off')) DEFAULT 'on'
);
"""

# Lista de coisas divertidas e sem noção
things_data = [
    ("Chinelo Voador", "Ideal para resolver discussões à distância.", "Sala de Aula"),
    ("Cacto Falante", "Conta piadas ruins quando alguém passa perto.", "Recepção"),
    ("Geladeira de Bolso", "Cabe um picolé e dois sonhos de valsa.", "Bolsa da Tia"),
    ("Drone de Pipoca", "Entrega pipoca direto na sua boca durante o filme.", "Cinema"),
    ("Relógio que Atrasado", "Sempre marca 5 minutos depois do horário real.", "Parede da Cozinha"),
    ("Guarda-chuva Invertido", "Te deixa molhado e mantém a chuva seca.", "Porta de Entrada"),
    ("Caneta que Apaga Provas", "Só funciona em dias de chuva.", "Mesa do Professor"),
    ("Sapato com Wi-Fi", "Conecta à internet quando você está correndo.", "Pista de Atletismo"),
    ("Cadeira que Dança", "Se mexe ao som de qualquer música.", "Auditório"),
    ("Livro de Piadas Invisíveis", "Só quem tem imaginação consegue ler.", "Biblioteca"),
    ("Luminária que Conta Histórias", "Apaga a luz e começa a narrar contos.", "Quarto"),
    ("Mouse que Foge", "Sai correndo quando você tenta clicar.", "Laboratório de Informática"),
    ("Espelho que Elogia", "Sempre diz que você está incrível.", "Banheiro"),
    ("Copo que Ri", "Solta gargalhadas quando você toma água.", "Cozinha"),
    ("Boné que Toca Funk", "Começa a tocar música quando está no sol.", "Quadra"),
]

def init_db():
    # Cria o banco de dados e as tabelas executando o script SQL acima
    DB_PATH.parent.mkdir(exist_ok=True)  # cria pasta data/ se não existir
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript(schema_sql)

    # Insere coisas divertidas e sem noção com datas aleatórias
    for i, (tname, tdescription, tlocation) in enumerate(things_data, start=1):
        timage = f'https://picsum.photos/400?random={i}'
        tcreated_at = random_date()
        towner_id = ((i - 1) % 5) + 1  # Garante valores de 1 a 5  # Associa cada coisa a um usuário diferente
        cursor.execute(
            "INSERT INTO things (tname, tdescription, tlocation, timage, tcreated_at, towner_id) VALUES (?, ?, ?, ?, ?, ?)",
            (tname, tdescription, tlocation, timage, tcreated_at, towner_id)
        )

    conn.commit()
    conn.close()
    print(" - Banco de dados criado em", DB_PATH)

# Se precisar rodar este script diretamente comante `python init_db.py`
if __name__ == "__main__":
    init_db()