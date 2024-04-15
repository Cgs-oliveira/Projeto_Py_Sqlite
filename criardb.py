#importando sqlite
import sqlite3 as lite

#criando conexão
con = lite.connect('inventario_dados.db')

#ciando tabelas|cur serve para apontar o banco de dados
with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
    
