import customtkinter as ctk
from tkinter import messagebox

#-------- função --------
taxa = 5.0

def converter_para_dolares ():
    reais = float (valor_reais.get())
    dolares = reais / taxa
    messagebox.showinfo('conversão', f'{reais:.2f} R$ = {dolares:.2f} US$')
    
def converter_para_reais ():
    reais = float (valor_dolares.get())
    dolares = reais * taxa
    messagebox.showinfo('conversão', f'{dolares:.2f} US$ = {reais:.2f} R$')

#-------------------------

ctk.set_appearance_mode ('dark')

janela = ctk.CTk ()
janela.geometry ('800x600')
janela.resizable (False,False)
janela.title ('Conversor de moedas')

ctk.CTkLabel(janela,
             text='Sistema de Conversão',
             font= ('Arial',45,'bold'),
             text_color='white'
).pack(pady=20),

valor_reais = ctk.CTkEntry(janela,
                           width= 500,
                           height= 40,
                           placeholder_text= 'Digite o valor em R$:'   
)

valor_reais.pack(pady=20)

valor_dolares = ctk.CTkEntry(janela,
                           width= 500,
                           height= 40,
                           placeholder_text= 'Digite o valor em US$:'   
)
valor_dolares.pack(pady=20)

botao_con_dolares = ctk.CTkButton(janela,
                                  width= 100,
                                  height= 30,
                                  text= 'Converter para US$',
                                  command = converter_para_dolares
)
botao_con_dolares.place(x=480, y=400)

botao_con_reais = ctk.CTkButton(janela,
                                  width= 100,
                                  height= 30,
                                  text= 'Converter para R$',
                                  command = converter_para_reais    
)
botao_con_reais.place(x=350, y=400)


janela.mainloop()


