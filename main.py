import os
import psycopg
import customtkinter as ctk

'''
===================================================
VARIAVEIS / CONSTANTES
===================================================
'''

HOST = os.environ["FLAME_DB_HOST"]
PORTA = os.environ.get("FLAME_DB_PORT", "5432")
BANCO = os.environ.get("FLAME_DB_NAME", "postgres")
USUARIO = os.environ["FLAME_DB_USER"]

STATUS = None

'''
===================================================
FUNCOES AUXILIARES
===================================================
'''

def ConectarBanco():
    global STATUS

    conexao = psycopg.connect(
    host= HOST,
    port= PORTA,
    dbname= BANCO,
    user= USUARIO,
    password= os.environ["FLAME_DB_PASSWORD"]
    )

    STATUS = "Banco Conectado"
    return conexao

Conn = ConectarBanco()

'''
===================================================
FUNCOES PRINCIPAIS
===================================================
'''
def FazerLogin():
    pass

'''
===================================================
INTERFACE CTK
===================================================
'''

def IniciarSistema():

    #CONFIG JANELA
    principal = ctk.CTk()

    principal.title("ERP - Flame")

    principal.geometry("1280x720")

    #RODAPE JANELA
    fraRodape = ctk.CTkFrame(principal, width=10, height=10)
    fraRodape.pack(side='bottom', fill='x')

    lblstatusbanco = ctk.CTkLabel(fraRodape, text=STATUS)
    lblstatusbanco.pack(side="left", padx=12, pady=2)

    lblVersao = ctk.CTkLabel(fraRodape, text="Versão: Desenvolvimento")
    lblVersao.pack(side='left', padx=12, pady=2)

    #FRAME LOGIN
    fraLogin = ctk.CTkFrame(principal, width=300, height=600)
    fraLogin.place(relx = 0.5, rely = 0.5, anchor = 'center')

    titLogin = ctk.CTkLabel(fraLogin, text= "FLAME GESTOR", )
    titLogin.place(relx=0.5, rely= 0.01, anchor='n')

    lblUsuario = ctk.CTkLabel(fraLogin, text="USUARIO")
    entryUsuario = ctk.CTkEntry(fraLogin)

    lblUsuario.place(relx= 0.3, rely= 0.42, anchor = 'e')
    entryUsuario.place(relx= 0.4, rely= 0.42, anchor ='w', x=4)

    lblSenha = ctk.CTkLabel(fraLogin, text= "SENHA")
    entrySenha = ctk.CTkEntry(fraLogin)

    lblSenha.place(relx= 0.3, rely= 0.5, anchor= 'e')
    entrySenha.place(relx= 0.4, rely= 0.5, anchor ='w', x=4)

    btnEntrar = ctk.CTkButton(fraLogin, text="ENTRAR")
    btnEntrar.place(relx= 0.4, rely= 0.7)

    lblMsg = ctk.CTkLabel(fraLogin, text= None)
    lblMsg.place(relx=0.5, rely= 0.75)

    def ChamarLogin():
            pass

    #MAINLOOP
    principal.mainloop()

IniciarSistema()
