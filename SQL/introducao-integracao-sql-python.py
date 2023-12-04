import sqlite3 as sql

con = sql.connect('banco.db')   #conecta ao banco de dados
cur = con.cursor()  #cria o cursor, que é o que usaremos para dar os comandos do sqlite
res = cur.execute('select * from conta')
#SELECT
for id,numero, agencia, cliente_id in res.fetchall():
    print(id, numero, agencia, cliente_id)

#INSERT INTO com input
numero = input('Numero')
agencia = input('agencia')
cur.execute(f"""
            insert into conta (numero, agencia, cliente_id)
            values ('{numero}'), '{agencia}', 1)
        """)
con.commit()    #salva as informações/alterações no banco

