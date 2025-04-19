import mysql.connector as mysql

def inserir_usuario():
    try:
        conexao = mysql.connect(
            host="localhost",
            user="root",
            password="milho@1234",
            database="sakila"
        )

        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM customer")
        result = cursor.fetchall()
        for linha in result:
            print(linha)

        dados_usuario = {
            "nome_usuario": input("Nome usuario: "),
            "senha": input("Senha: "),
            "customer_id": input("Customer_id: ")
        }
        if dados_usuario == "":
            print("Dado não preenchido, verifique novamente")
        else:
            print("Dados válidos")
        comando = """INSERT INTO usuario (nome_usuario, senha, customer_id) VALUES (%(nome_usuario)s, %(senha)s, %(customer_id)s)"""
        cursor.execute(comando, dados_usuario)
        conexao.commit()

    except mysql.Error as e:
        print(f"Deu erro {e}")

    finally:
        conexao.close()

inserir_usuario()