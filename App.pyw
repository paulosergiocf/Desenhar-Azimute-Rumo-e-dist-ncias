# -*- coding: UTF-8 -*-

import tkinter as tk
import os
from tkinter import filedialog
import re
#---------------- Manipular Arquivos------------------
class ScriptCad:
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def criar(self):
        arq = open(r''+self.arquivo+'.scr', 'w')
        arq.writelines(f'_PLINE\n0,0\n')
        arq.close()


    def editar(self, msg):
        arq = open(r''+self.arquivo+'.scr', 'r+')
        conteudo = arq.readlines()
        conteudo.append(f'{msg}\n')
        arq= open(r''+self.arquivo+'.scr', 'w')
        arq.writelines(conteudo)
        arq.close()


    def concluir(self):
        with open(r''+self.arquivo+'.scr', 'r+') as fd:
            txt = fd.read()
            txt = txt.replace(r"´´´´",r'"')

        with open(r''+self.arquivo+'.scr','w') as fd:
            fd.write(txt)


#---------------- Manipular Rumos e Distâncias------------------
class Orientacoes:
    def __init__(self, grau, minuto, segundo, distancia):
        self.grau = grau
        self.minuto = minuto
        self.segundo = segundo
        self.distancia = distancia


class Azimutes(Orientacoes):
    def __init__(self, grau, minuto, segundo, distancia):
        super().__init__(grau, minuto, segundo, distancia)

    def __str__(self):
        return f"@{self.distancia:.2f}<{self.grau}d{self.minuto}'{self.segundo:.2f}´´´´"


class Rumos(Orientacoes):
    def __init__(self, grau, minuto, segundo, distancia, rumo):
        super().__init__(grau, minuto, segundo, distancia)
        self.rumo = rumo.upper()

    def __str__(self):
        return f"@{self.distancia:.2f}<{self.rumo[0]}{self.grau}d{self.minuto}'{self.segundo:.2f}´´´´{self.rumo[1]}"

#---------------- Interface------------------
class Aplicacao(tk.Frame):

    def __init__(self, janela=None):
        super().__init__(janela)
        self.cor = {'Fundo':'#111526','Fonte':'#aed1e8','bom':'#055902', 'ruim':'#B24448'}
        self.janela = janela
        self.janela.title('Digitar Script')
        self.janela.geometry('500x500')
        self.janela["bg"]=self.cor['Fundo']
        photo = tk.PhotoImage(file ='logo.png')#icone_do_programa
        janela.iconphoto(False, photo)
        self.pack()
        self.inicio()

    # ------- Aparencia --------
    def inicio(self):
        self.container = tk.Frame(janela, bg=self.cor["Fundo"],  padx=40, pady=20)
        self.container.pack()
        self.container01 = tk.Frame(self.container, bg=self.cor["Fundo"],  padx=40, pady=20)
        self.container01.pack()
        bt_lb = tk.Label(self.container01, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='ESCOLHA UMA OPÇÃO', width=20, height=3)
        bt_lb.pack()

        self.container02 = tk.Frame(self.container, bg=self.cor["Fundo"],  padx=40, pady=20)
        self.container02.pack()

        bt_rumo = tk.Button(self.container02, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='RUMO', width=20, height=3, command=self.rumo)
        bt_rumo.pack(side='left')
        bt_azimute = tk.Button(self.container02, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='AZIMUTE', width=20, height=3, command=self.azimute)
        bt_azimute.pack(side='left')

        self.container03 = tk.Frame(self.container, bg=self.cor["Fundo"],  padx=40)
        self.container03.pack()

        bt_sair = tk.Button(self.container03, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='SAIR', width=41, height=3, command=self.quit)
        bt_sair.pack()


    def escolher_diretorio(self):
        self.container00 = tk.Frame(self.container, bg=self.cor["Fundo"])
        self.container00.pack()
        bt_lb = tk.Label(self.container00, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='Selecione o Diretório', width=20, height=3)
        bt_lb.pack(side='left')
        self.bt_sel_dir = tk.Button(self.container00, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='SELECIONAR', width=25, height=1, command=self.dir)
        self.bt_sel_dir.pack(side='left')
        self.nome_do_arquivo()


    def nome_do_arquivo(self):
        self.container01 = tk.Frame(self.container, bg=self.cor["Fundo"], pady=10)
        self.container01.pack()
        bt_lb = tk.Label(self.container01, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='Nome do Arquivo:', width=20, height=3)
        bt_lb.pack(side='left')
        self.bt_en = tk.Entry(self.container01, bg=self.cor["Fonte"], foreground=self.cor["Fundo"], width=15)
        self.bt_en.pack(side='left')
        self.bt_sel_arq = tk.Button(self.container01, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='CRIAR', width=25, height=1, command=self.criar_arquivo)
        self.bt_sel_arq.pack(side='left')
        self.programa()


    def programa(self):
        self.container02 = tk.Frame(self.container, bg=self.cor["Fundo"])
        self.container02.pack()
        bt_lb = tk.Label(self.container02, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='GRAU', width=15, height=3)
        bt_lb.pack(side='left')
        bt_lb = tk.Label(self.container02, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='MINUTO', width=15, height=3)
        bt_lb.pack(side='left')
        bt_lb = tk.Label(self.container02, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='SEGUNDO', width=15, height=3)
        bt_lb.pack(side='left')
        if self.escolha == 'rumo':
            bt_lb = tk.Label(self.container02, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='RUMO', width=15, height=3)
            bt_lb.pack(side='left')

        self.container03 = tk.Frame(self.container, bg=self.cor["Fundo"])
        self.container03.pack()
        self.engrau = tk.Entry(self.container03, bg=self.cor["Fonte"], border=2, foreground=self.cor["Fundo"], width=15)
        self.engrau.pack(side='left')
        self.enminuto = tk.Entry(self.container03, bg=self.cor["Fonte"], border=2, foreground=self.cor["Fundo"], width=15)
        self.enminuto.pack(side='left')
        self.ensegundo = tk.Entry(self.container03, bg=self.cor["Fonte"], border=2, foreground=self.cor["Fundo"], width=15)
        self.ensegundo.pack(side='left')
        if self.escolha == 'rumo':
            self.enrumo = tk.Entry(self.container03, bg=self.cor["Fonte"], border=2, foreground=self.cor["Fundo"], width=15)
            self.enrumo.pack(side='left')

        self.container04 = tk.Frame(self.container, bg=self.cor["Fundo"])
        self.container04.pack()
        bt_lbdis = tk.Label(self.container04, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='Distância', width=15, height=3)
        bt_lbdis.pack(side='left')
        self.endistancia = tk.Entry(self.container04, bg=self.cor["Fonte"], border=2, foreground=self.cor["Fundo"], width=15)
        self.endistancia.pack(side='left')

        self.container05 = tk.Frame(self.container, bg=self.cor["Fundo"])
        self.container05.pack()
        bt_next = tk.Button(self.container05, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='PRÓXIMO', width=20, height=1, command=self.proximo)
        bt_next.pack(side='left')
        bt_conc = tk.Button(self.container05, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='CONCLUÍR', width=20, height=1, command=self.encerrar)
        bt_conc.pack(side='left')

        self.container06 = tk.Frame(self.container, bg=self.cor["Fundo"])
        self.container06.pack()
        self.bt_lblog = tk.Label(self.container06, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='>_', width=50, height=3)
        self.bt_lblog.pack()
        self.voltar_bt()


    def voltar_bt(self):
        self.container07 = tk.Frame(self.container, bg=self.cor["Fundo"], pady=10)
        self.container07.pack()
        self.bt_voltar = tk.Button(self.container07, bg=self.cor["Fundo"], foreground=self.cor["Fonte"], text='VOLTAR', width=25, height=1, command=self.voltar)
        self.bt_voltar.pack(side='left')



    # ------- Escolha --------
    def azimute(self):
        self.container.forget()
        self.container = tk.Frame(janela, bg=self.cor["Fundo"],  padx=40, pady=20)
        self.container.pack()
        self.escolha = 'azimute'
        self.escolher_diretorio()


    def rumo(self):
        self.container.forget()
        self.container = tk.Frame(janela, bg=self.cor["Fundo"],  padx=40, pady=20)
        self.container.pack()
        self.escolha = 'rumo'
        self.escolher_diretorio()


    # ------- Funcionalidades --------
    def voltar(self):
        self.container.forget()
        self.inicio()

    def isnumber(self, value):
        try:
             float(value)
        except ValueError:
             return False
        return True

    def proximo(self):
        teste_orientacoes = 'bad'
        # -- entradas---
        test_grau = self.engrau.get().strip()
        if test_grau.isnumeric():
            grau = test_grau
            self.engrau['bg']=self.cor['Fonte']
        else:
            self.engrau['bg']=self.cor['ruim']

        teste_minuto = self.enminuto.get().strip()
        if teste_minuto.isnumeric():
            minuto = teste_minuto
            self.enminuto['bg']=self.cor['Fonte']
        else:
            self.enminuto['bg']=self.cor['ruim']

        teste_segundo = self.ensegundo.get().strip()
        teste_segundo = teste_segundo.replace(",",".")

        if self.isnumber(teste_segundo) == True:
            segundo = float(teste_segundo)
            self.ensegundo['bg']=self.cor['Fonte']
        else:
            self.ensegundo['bg']=self.cor['ruim']

        teste_distancia = self.endistancia.get().strip()
        teste_distancia = teste_distancia.replace(",",".")

        if self.isnumber(teste_distancia)== True:
            distancia = float(teste_distancia)
            self.endistancia['bg']=self.cor['Fonte']
        else:
            self.endistancia['bg']=self.cor['ruim']


        # --- arquivo-----
        try:
            a = ScriptCad(self.caminho)
        except AttributeError:
            self.criar_arquivo()
            a = ScriptCad(self.caminho)

        # -----se é rumo ou azimute
        if self.escolha == 'rumo':
            rm = self.enrumo.get().strip()
            rm = rm.upper()

            if len(rm) !=2:
                self.enrumo['bg']=self.cor['ruim']

            else:
                if 'S' in rm[0] or 'N' in rm[0]:
                    if 'W' in rm[1] or 'O' in rm[1] or 'L' in rm[1] or 'E' in rm[1]:
                        if rm[1] == 'W':
                            rm = f'{rm[0]}O'
                        elif rm[1] =='E':
                            rm = f'{rm[0]}L'
                        try:
                            rumo = Rumos(grau, minuto, segundo, distancia, rm)
                            a.editar(rumo)
                            self.bt_lblog['text'] = f'Anterior: {rumo}'
                            teste_orientacoes = 'ok'
                            self.enrumo.delete(0, tk.END)
                            self.enrumo['bg']=self.cor['Fonte']

                        except:
                            teste_orientacoes = 'bad'

                    else:
                        self.enrumo['bg']=self.cor['ruim']
                else:
                    self.enrumo['bg']=self.cor['ruim']
        else:
            try:
                azimute = Azimutes(grau, minuto, segundo, distancia)
                a.editar(azimute)
                self.bt_lblog['text'] = f'Anterior: {azimute}'

            except:
                teste_orientacoes = 'bad'

            else:
                teste_orientacoes = 'ok'

        #------limpar dados------
        if teste_orientacoes == 'ok':
            self.engrau.delete(0, tk.END)
            self.enminuto.delete(0, tk.END)
            self.ensegundo.delete(0, tk.END)
            self.endistancia.delete(0, tk.END)


    def encerrar(self):
        a = ScriptCad(self.caminho)
        a.concluir()
        quit()


    def criar_arquivo(self):
        arquivo = self.bt_en.get()
        if arquivo == '':
            arquivo = 'arquivo_sem_nome'
        try:
            self.caminho = f'{self.path}/{arquivo}'
        except AttributeError:
            self.caminho = f'{arquivo}'
        a = ScriptCad(self.caminho)
        a.criar()
        self.bt_sel_arq['bg']=self.cor["bom"]


    def dir(self):
        application_window = tk.Frame(self.container00)
        my_filetypes = [('all files', '.*'), ('text files', '.txt')]
        self.path = filedialog.askdirectory(parent=application_window, initialdir=os.getcwd(), title="Selecione a Pasta:")
        if self.path =='':
            self.bt_sel_dir['bg']=self.cor["ruim"]
            self.path = os.getcwd()
        else:
            self.bt_sel_dir['bg']=self.cor["bom"]


#---------------- Inicar Aplicação------------------
if __name__ == '__main__':
    janela = tk.Tk()
    app = Aplicacao(janela=janela)
    app.mainloop()
