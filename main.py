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

IDUSUARIOLOGADO = None
USUARIOLOGADO = None
SETORLOGADO = None

'''
===================================================
FUNCOES AUXILIARES
===================================================
'''
#conectar ao banco
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

#executa procecure login no banco
def FazerLogin(conn, login, password):
    sql=conn.cursor()
    sql.execute("CALL PROC_LOGIN(%s, %s, NULL, NULL, NULL ,NULL)",(login, password))

    rs = sql.fetchone()
    return rs

#se login ok fecha o frame e abre menu
def FecharLogin(fraLogin, principal, entryUsuario, entrySenha):
    fraLogin.place_forget()
    fraLogin.grab_release()
    fraLogin.after(500,lambda: AbrirMenu(principal, fraLogin, entryUsuario, entrySenha))

#deslogar e voltar fra login
def Logout(fraMenu, fraLogin, entryUsuario, entrySenha):
    global IDUSUARIOLOGADO, USUARIOLOGADO, SETORLOGADO

    IDUSUARIOLOGADO = USUARIOLOGADO = SETORLOGADO = None
    fraMenu.destroy()

    entryUsuario.delete(0, "end")
    entrySenha.delete(0, "end")

    def reabrirlogin():
        fraLogin.place(relx = 0.5, rely = 0.5, anchor = 'center')
        fraLogin.grab_set()

    fraLogin.after(1000, reabrirlogin)

'''
===================================================
FUNCOES PRINCIPAIS
===================================================
'''


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
    lblstatusbanco.pack(side="left", padx=20, pady=2)

    lblVersao = ctk.CTkLabel(fraRodape, text="Versão: Desenvolvimento")
    lblVersao.pack(side='right', padx=20, pady=2)

    lblIdUsuarioLogado = ctk.CTkLabel(fraRodape, text=None)
    lblIdUsuarioLogado.pack(side='left', padx=20, pady=2)

    lblUsuarioLogado = ctk.CTkLabel(fraRodape, text=None)
    lblUsuarioLogado.pack(side='left', padx=20, pady=2)

    #FRAME LOGIN
    fraLogin = ctk.CTkFrame(principal, width=300, height=600)
    fraLogin.place(relx = 0.5, rely = 0.5, anchor = 'center')
    fraLogin.grab_set()

    titLogin = ctk.CTkLabel(fraLogin, text= "FLAME GESTOR", )
    titLogin.place(relx=0.5, rely= 0.01, anchor='n')

    lblUsuario = ctk.CTkLabel(fraLogin, text="USUARIO")
    entryUsuario = ctk.CTkEntry(fraLogin)

    lblUsuario.place(relx= 0.3, rely= 0.42, anchor = 'e')
    entryUsuario.place(relx= 0.4, rely= 0.42, anchor ='w', x=4)

    lblSenha = ctk.CTkLabel(fraLogin, text= "SENHA")
    entrySenha = ctk.CTkEntry(fraLogin, show="*")

    lblSenha.place(relx= 0.3, rely= 0.5, anchor= 'e')
    entrySenha.place(relx= 0.4, rely= 0.5, anchor ='w', x=4)

    btnEntrar = ctk.CTkButton(fraLogin, text="ENTRAR")
    btnEntrar.place(relx= 0.4, rely= 0.7)

    lblMsg = ctk.CTkLabel(fraLogin, text= None)
    lblMsg.place(relx=0.5, rely= 0.6, anchor = 'center')

    #validar entrys e chamar login
    def ChamarLogin():

        global IDUSUARIOLOGADO, USUARIOLOGADO, SETORLOGADO

        login = entryUsuario.get().strip()
        password = entrySenha.get()

        if not login or not password:
            lblMsg.configure(text='Insira usuario e senha validos')
            entryUsuario.focus_force()
            return

        status, idusuario, usuario, setor = FazerLogin(Conn, login, password)

        if status != 'OK':
            if status =='USUARIO_INVALIDO':
                lblMsg.configure(text="Usuario Invalido")
                entryUsuario.focus_force()
            else: lblMsg.configure(text="Usuario ou senha invalidos")
        else:
            lblMsg.configure(text='Logado com Sucesso!')

            IDUSUARIOLOGADO = idusuario
            USUARIOLOGADO = usuario
            SETORLOGADO = setor

            lblIdUsuarioLogado.configure(text=f"ID : {IDUSUARIOLOGADO}")
            lblUsuarioLogado.configure(text=f"USUARIO: {USUARIOLOGADO}")

            fraLogin.after(1000,lambda: FecharLogin(fraLogin, principal, entryUsuario, entrySenha))

    principal.after(100,entryUsuario.focus_force)

    btnEntrar.configure(command= ChamarLogin)

    entryUsuario.bind("<Return>", lambda event: ChamarLogin())

    entrySenha.bind("<Return>", lambda event: ChamarLogin())

    #Mantem a janela
    principal.mainloop()

#config menu na janela
def AbrirMenu(principal, fraLogin, entryUsuario, entrySenha):

    fraMenu = ctk.CTkFrame(principal, width=200)
    fraMenu.pack(side= 'left', fill ="y", padx= 20, pady=20)

    btnLogout = ctk.CTkButton(fraMenu, text='Logout',
    command= lambda:Logout(fraMenu, fraLogin, entryUsuario, entrySenha)
    )
    btnLogout.pack()

IniciarSistema()
