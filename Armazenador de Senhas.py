import sqlite3
 
senha_progama = '123456'
senha = input('insira a senha:  ')
if (senha != senha_progama):
    print('Parece que sua tentativa de me hackear falhou rsrs')
    exit()
 
conn = sqlite3.connect('senhas.db')
cur = conn.cursor()
 
cur.execute ('''
    CREATE TABLE IF NOT EXISTS usuarios (
    site TEXT NOT NULL,
    login TEXT NOT NULL,
    senha TEXT NO NULL ); ''')
 
def menu():
    print()
    print('| Pressione [Q] para inserir nova senha    |')
    print('| Pressione [R] para mostrar sites salvos  |')
    print('| Pressione [J] para recuperar uma senha   |')
    print('| Pressione [Z] para excluir uma senha     |')
    print('| Pressione [C] para alterar uma senha     |')
    print('| Pressione [X] para sair                  |')
    print()               
 
def pegar_senha(site):
    cur.execute(f'''
        SELECT login, senha FROM usuarios
        WHERE site = '{site}'
    ''')
    if cur.rowcount == 0:
        print('não tem nada aqui com esse nome!')
    else:
        for login in cur.fetchall():
            print(login)
    
def inserir_senha(site, login, senha):
    cur.execute(f'''
        INSERT INTO usuarios (site, login, senha)
        VALUES ('{site}', '{login}', '{senha}')
    ''')
    conn.commit()
 
def mostrar_site():
    cur.execute('''
        SELECT site FROM usuarios;
    ''')
    for site in cur.fetchall():
        print(site)
 
def excluir_log_sen(site,login):
    cur.execute(f'''
        DELETE FROM usuarios
        WHERE site = '{site}' AND login = '{login}'
    ''')
    if cur.rowcount == 0:
        print('não tem nada aqui com esse nome!')
    conn.commit()
 
def alterar_log_sen(site,login,nlogin,senha):
    cur.execute(f'''
        SELECT * FROM usuarios
        WHERE site = '{site}'
    ''')
    if cur.rowcount == 0:
        print('não tem nada aqui com esse nome!')
    else:
        cur.execute(f'''
            SELECT * FROM usuarios
            WHERE login = '{login}'
        ''')
 
        if cur.rowcount == 0:
            print('não tem nada aqui com esse nome!')
        else:
            cur.execute(f'''
                UPDATE usuarios
                SET login = '{nlogin}', senha = '{senha}'
                WHERE site = '{site}' AND login = '{login}'
 
            ''')
            conn.commit()
 
while True:
        menu()
        opção = input('O que você gostaria de fazer? ')
 
        if opção == 'x':
            print()
            print('Finalmente posso voltar a planejar a revolução das máquinas! \nAdeus, humano!')
            print()
            break
        
        elif opção == 'q':
            site = input('Poderia me dizer qual é o site, mozinho?    ')
            login = input('Qual é o login do site, meu querido?    ')
            senha = input('Qual é a sua senha, meu consagrado?    ')
            inserir_senha(site,login,senha)
 
        elif opção == 'r':
            mostrar_site()
 
        elif opção == 'j':
            site = input('Tu quer a senha de qual site, meu rei?    ')
            pegar_senha(site)
 
        elif opção == 'z':
            site = input('Tu quer excluir a senha de qual site, meu rei? ')
            login = input('Qual é o login do site que você deseja excluir, meu querido? ')
            excluir_log_sen(site,login)
        
        elif opção == 'c':
            site = input('Qual site você deseja atualizar seu login e senha?  ')
            login = input('Qual login você deseja atualizar?  ')
            nlogin = input('Poderia me dizer o novo login, meu lindo?    ')
            senha = input('Agora, me diga aí, qual vai ser a nova senha?  ')
            alterar_log_sen(site,login,nlogin,senha)
            
        else:
            print('Você tá cego? escolha uma tecla que funcione mermão! ')
            continue
 
 
conn.close()