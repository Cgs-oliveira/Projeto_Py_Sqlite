# importando sqlite
import sqlite3 as lite

# conexão
con = lite.connect('inventario_dados.db')


dados = ['sofa','sala de estar','magalu','ortobom','01/08/2024','1500','xxxxy','F:\BANCO DE DADOS\Projeto_Py_Sqlite\img']

#CRUD
#podemos usar o DB BROWSER para editar a tabela adicionar dados e remover tambem
# CRIAR dados
def inserir_from(i):
    with con:
        cur=con.cursor() 
        query= "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra,valor_da_compra,serie, imagem)VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query,i)


#atualiza dados de inventario
def atualizar(i):
    with con:
        cur=con.cursor() 
        query= "UPDATE invetario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?,valor_da_compra=?,serie=?, imagem=? WHERE id="
        cur.execute(query,i)
    

#podemos usar o DB BROWSER para editar a tabela adicionar dados e remover tambem
# DELETAR dados
def deletar_from(i):
    with con:
        cur=con.cursor() 
        query= "DELETE FROM inventario where id=? "
        cur.execute(query,i)

#vizualizar tabela
def ver_from(i):
    ver_dados = []
    with con:
        cur=con.cursor() 
        query= "select * from inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return (ver_dados)

#ver dados separados
def ver_item(id):
    ver_item_individual = []
    with con:
            cur=con.cursor() 
            query= "SELECT * from inventario WHERE id = ?"
            cur.execute(query,id)

            rows = cur.fetchall()
            for row in rows:
                ver_item_individual.append(row)
        




