CREATE TABLE obra(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT NOT NULL,
autor TEXT NOT NULL,
genero TEXT NOT NULL
);

CREATE TABLE funcionario(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
senha TEXT NOT NULL
);

CREATE TABLE cliente(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
senha TEXT NOT NULL
);

CREATE TABLE copia(
id INTEGER PRIMARY KEY AUTOINCREMENT,
edicao INTEGER NOT NULL,
obra_id INTEGER,
FOREIGN KEY(obra_id) REFERENCES obra(id)
);

CREATE TABLE emprestimo(
id INTEGER PRIMARY KEY AUTOINCREMENT,
cliente_id INTEGER,
data_emprestimo date,
ata_devolucao date,
copia_id INTEGER,
funcionario_id INTEGER,
FOREIGN KEY(cliente_id) REFERENCES cliente(id),
FOREIGN KEY(copia_id) REFERENCES copia(id),
FOREIGN KEY(funcionario_id) REFERENCES funcionario(id)
);

CREATE TABLE multa(
id INTEGER PRIMARY KEY AUTOINCREMENT,
emprestimo_id INTEGER,
valor REAL,
FOREIGN KEY(emprestimo_id) REFERENCES emprestimo(id)
);
