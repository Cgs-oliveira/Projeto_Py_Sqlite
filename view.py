# importando sqlite
import sqlite3 as lite

# conexão
con = lite.connect('inventario_dados.db')


'''dados = ['sofa','sala de estar','magalu','ortobom','01/08/2024','1500','xxxxy','']'''

# inserir dados

with con:
    cur=con.cursor() 
    query= "DELETE FROM inventario where id= 3 "
    cur.execute(query)

'''ver_dados = []




#ver dados da tabela

with con:
    cur=con.cursor() 
    query= "select * from inventario"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)


print (ver_dados)'''