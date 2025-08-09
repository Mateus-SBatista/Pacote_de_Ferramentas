import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

# Configurações de estilo
COR_PRIMARIA = "#2c3e50"
COR_SECUNDARIA = "#3498db"
COR_TERCIARIA = "#e74c3c"
COR_FUNDO = "#ecf0f1"
COR_TEXTO = "#2c3e50"
FONTE_TITULO = ("Verdana", 16, "bold")
FONTE_TEXTO = ("Verdana", 10)
FONTE_BOTOES = ("Verdana", 10, "bold")

# =====================
# 1 - Gerador de Senhas
# =====================
def abrir_gerador_senhas():
    janela_senha = tk.Toplevel(root)
    janela_senha.title("🔒 Gerador de Senhas Seguras")
    janela_senha.geometry("450x350")
    janela_senha.configure(bg=COR_FUNDO)
    janela_senha.resizable(False, False)
    
    # Frame principal
    frame_principal = tk.Frame(janela_senha, bg=COR_FUNDO)
    frame_principal.pack(pady=20, padx=20, fill="both", expand=True)
    
    tk.Label(frame_principal, text="🔐 Gerador de Senhas Seguras", font=FONTE_TITULO, 
             bg=COR_FUNDO, fg=COR_PRIMARIA).pack(pady=(0, 20))
    
    # Frame de configuração
    frame_config = tk.LabelFrame(frame_principal, text=" Configurações ", font=FONTE_BOTOES, 
                                bg=COR_FUNDO, fg=COR_PRIMARIA, padx=10, pady=10)
    frame_config.pack(fill="x", pady=(0, 15))
    
    tk.Label(frame_config, text="Tamanho da senha:", font=FONTE_TEXTO, bg=COR_FUNDO).grid(row=0, column=0, sticky="w", pady=5)
    spin_tamanho = tk.Spinbox(frame_config, from_=8, to=50, width=5, font=FONTE_TEXTO)
    spin_tamanho.grid(row=0, column=1, sticky="w", padx=5)
    spin_tamanho.delete(0, "end")
    spin_tamanho.insert(0, "12")
    
    # Checkboxes para tipos de caracteres
    var_maiusculas = tk.IntVar(value=1)
    var_minusculas = tk.IntVar(value=1)
    var_numeros = tk.IntVar(value=1)
    var_especiais = tk.IntVar(value=1)
    
    tk.Checkbutton(frame_config, text="Letras maiúsculas", variable=var_maiusculas, 
                   font=FONTE_TEXTO, bg=COR_FUNDO).grid(row=1, column=0, sticky="w", pady=2)
    tk.Checkbutton(frame_config, text="Letras minúsculas", variable=var_minusculas, 
                   font=FONTE_TEXTO, bg=COR_FUNDO).grid(row=2, column=0, sticky="w", pady=2)
    tk.Checkbutton(frame_config, text="Números", variable=var_numeros, 
                   font=FONTE_TEXTO, bg=COR_FUNDO).grid(row=1, column=1, sticky="w", pady=2, padx=10)
    tk.Checkbutton(frame_config, text="Caracteres especiais", variable=var_especiais, 
                   font=FONTE_TEXTO, bg=COR_FUNDO).grid(row=2, column=1, sticky="w", pady=2, padx=10)
    
    # Frame da senha gerada
    frame_senha = tk.LabelFrame(frame_principal, text=" Senha Gerada ", font=FONTE_BOTOES, 
                               bg=COR_FUNDO, fg=COR_PRIMARIA, padx=10, pady=10)
    frame_senha.pack(fill="x", pady=(0, 15))
    
    entry_senha = tk.Entry(frame_senha, font=("Courier", 14), bd=0, bg="white", 
                          fg=COR_PRIMARIA, justify="center", width=30)
    entry_senha.pack(pady=5)
    
    # Frame de botões
    frame_botoes = tk.Frame(frame_principal, bg=COR_FUNDO)
    frame_botoes.pack(fill="x")
    
    def gerar_senha():
        try:
            tamanho = int(spin_tamanho.get())
            if tamanho <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido para o tamanho.")
            return
        
        caracteres = ""
        if var_maiusculas.get(): caracteres += string.ascii_uppercase
        if var_minusculas.get(): caracteres += string.ascii_lowercase
        if var_numeros.get(): caracteres += string.digits
        if var_especiais.get(): caracteres += string.punctuation
            
        if not caracteres:
            messagebox.showerror("Erro", "Selecione pelo menos um tipo de caractere.")
            return
            
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
        entry_senha.config(fg=COR_PRIMARIA)

    def copiar_senha():
        senha = entry_senha.get()
        if senha:
            janela_senha.clipboard_clear()
            janela_senha.clipboard_append(senha)
            entry_senha.config(fg="green")
            janela_senha.after(1000, lambda: entry_senha.config(fg=COR_PRIMARIA))
            messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
        else:
            messagebox.showwarning("Atenção", "Nenhuma senha para copiar.")

    btn_gerar = tk.Button(frame_botoes, text="Gerar Senha", font=FONTE_BOTOES, 
                          bg=COR_SECUNDARIA, fg="white", command=gerar_senha)
    btn_gerar.pack(side="left", padx=5, expand=True, fill="x")
    
    btn_copiar = tk.Button(frame_botoes, text="Copiar Senha", font=FONTE_BOTOES, 
                           bg="#2ecc71", fg="white", command=copiar_senha)
    btn_copiar.pack(side="left", padx=5, expand=True, fill="x")

# =====================
# 2 - Jogo de Adivinhação
# =====================
def abrir_jogo_adivinhacao():
    janela_jogo = tk.Toplevel(root)
    janela_jogo.title("🎯 Jogo de Adivinhação")
    janela_jogo.geometry("500x500")
    janela_jogo.configure(bg=COR_FUNDO)
    janela_jogo.resizable(False, False)

    # Variáveis do jogo
    numero_secreto = None
    tentativas = 0
    limite_tentativas = 5
    inicio = 0
    fim = 100

    # Frame principal
    frame_principal = tk.Frame(janela_jogo, bg=COR_FUNDO)
    frame_principal.pack(pady=20, padx=20, fill="both", expand=True)
    
    tk.Label(frame_principal, text="🎯 Jogo de Adivinhação", font=FONTE_TITULO, 
             bg=COR_FUNDO, fg=COR_PRIMARIA).pack(pady=(0, 20))
    
    # Frame de configuração
    frame_config = tk.LabelFrame(frame_principal, text=" Configuração do Jogo ", 
                                font=FONTE_BOTOES, bg=COR_FUNDO, fg=COR_PRIMARIA, padx=10, pady=10)
    frame_config.pack(fill="x", pady=(0, 15))
    
    tk.Label(frame_config, text="Intervalo de números:", font=FONTE_TEXTO, bg=COR_FUNDO).pack(anchor="w")
    
    frame_intervalo = tk.Frame(frame_config, bg=COR_FUNDO)
    frame_intervalo.pack(pady=5)
    
    tk.Label(frame_intervalo, text="De:", font=FONTE_TEXTO, bg=COR_FUNDO).grid(row=0, column=0, padx=5)
    entry_inicio = tk.Entry(frame_intervalo, font=FONTE_TEXTO, width=5, justify="center")
    entry_inicio.grid(row=0, column=1, padx=5)
    entry_inicio.insert(0, "1")
    
    tk.Label(frame_intervalo, text="Até:", font=FONTE_TEXTO, bg=COR_FUNDO).grid(row=0, column=2, padx=5)
    entry_fim = tk.Entry(frame_intervalo, font=FONTE_TEXTO, width=5, justify="center")
    entry_fim.grid(row=0, column=3, padx=5)
    entry_fim.insert(0, "100")
    
    # Frame do jogo
    frame_jogo = tk.LabelFrame(frame_principal, text=" Jogar ", font=FONTE_BOTOES, 
                              bg=COR_FUNDO, fg=COR_PRIMARIA, padx=10, pady=10)
    frame_jogo.pack(fill="x", pady=(0, 15))
    
    label_status = tk.Label(frame_jogo, text="Configure o intervalo e clique em 'Iniciar Jogo'.", 
                           font=FONTE_TEXTO, bg=COR_FUNDO, wraplength=400)
    label_status.pack(pady=5)
    
    label_tentativas = tk.Label(frame_jogo, text="", font=FONTE_TEXTO, bg=COR_FUNDO)
    label_tentativas.pack(pady=5)
    
    frame_palpite = tk.Frame(frame_jogo, bg=COR_FUNDO)
    frame_palpite.pack(pady=10)
    
    tk.Label(frame_palpite, text="Seu palpite:", font=FONTE_TEXTO, bg=COR_FUNDO).grid(row=0, column=0, padx=5)
    entry_palpite = tk.Entry(frame_palpite, font=FONTE_TEXTO, width=8, justify="center")
    entry_palpite.grid(row=0, column=1, padx=5)
    
    # Barra de progresso
    progresso = ttk.Progressbar(frame_jogo, orient="horizontal", length=400, mode="determinate")
    progresso.pack(pady=10)
    
    # Funções do jogo
    def iniciar_jogo(primeira_vez=False):
        nonlocal numero_secreto, tentativas, inicio, fim
        try:
            inicio = int(entry_inicio.get())
            fim = int(entry_fim.get())
            if inicio >= fim:
                messagebox.showerror("Erro", "O início deve ser menor que o fim.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")
            return

        numero_secreto = random.randint(inicio, fim)
        tentativas = 0
        progresso["value"] = 0
        progresso["maximum"] = limite_tentativas
        label_status.config(text=f"Tente adivinhar o número entre {inicio} e {fim}.", fg=COR_TEXTO)
        label_tentativas.config(text=f"Tentativas restantes: {limite_tentativas}", fg=COR_SECUNDARIA)
        btn_palpite.config(state="normal")
        entry_palpite.focus()
        
        if primeira_vez:
            btn_iniciar.config(text="Reiniciar Jogo", command=lambda: iniciar_jogo(False))

    def verificar_palpite():
        nonlocal tentativas
        try:
            palpite = int(entry_palpite.get())
            if palpite < inicio or palpite > fim:
                messagebox.showwarning("Atenção", f"Digite um número entre {inicio} e {fim}.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")
            return

        tentativas += 1
        progresso["value"] = tentativas
        tentativas_restantes = limite_tentativas - tentativas

        if palpite == numero_secreto:
            if tentativas == 1:
                messagebox.showinfo("Parabéns!", "Incrível! Você acertou de primeira! 🎉")
            else:
                messagebox.showinfo("Parabéns!", f"Você acertou em {tentativas} tentativa(s)!")
            resetar_jogo()
        elif tentativas >= limite_tentativas:
            messagebox.showinfo("Fim de Jogo", f"O número secreto era {numero_secreto}.")
            resetar_jogo()
        elif palpite < numero_secreto:
            label_status.config(text="Tente um número maior! ⬆️", fg=COR_SECUNDARIA)
        else:
            label_status.config(text="Tente um número menor! ⬇️", fg=COR_TERCIARIA)

        label_tentativas.config(text=f"Tentativas restantes: {tentativas_restantes}")
        entry_palpite.delete(0, tk.END)

    def resetar_jogo():
        entry_palpite.delete(0, tk.END)
        label_status.config(text="Configure o intervalo e clique em 'Iniciar Jogo'.", fg=COR_TEXTO)
        label_tentativas.config(text="")
        btn_palpite.config(state="disabled")
        progresso["value"] = 0

    # Botões do jogo
    btn_iniciar = tk.Button(frame_config, text="Iniciar Jogo", font=FONTE_BOTOES, 
                           bg=COR_SECUNDARIA, fg="white", command=lambda: iniciar_jogo(True))
    btn_iniciar.pack(pady=5)

    btn_palpite = tk.Button(frame_palpite, text="Verificar", font=FONTE_BOTOES, 
                           bg="#2ecc71", fg="white", command=verificar_palpite, state="disabled")
    btn_palpite.grid(row=0, column=2, padx=5)

    # Rodapé
    tk.Label(frame_principal, text="Dica: Comece com um palpite no meio do intervalo!", 
             font=("Verdana", 8), bg=COR_FUNDO, fg="#7f8c8d").pack(side="bottom", pady=10)

# =====================
# 3 - Calculadora Simples
# =====================
def abrir_calculadora():
    janela_calc = tk.Toplevel(root)
    janela_calc.title("🧮 Calculadora")
    janela_calc.geometry("350x450")
    janela_calc.configure(bg=COR_FUNDO)
    janela_calc.resizable(False, False)
    
    # Estilo dos botões
    estilo_botoes = {
        "font": ("Arial", 18),
        "width": 5,
        "height": 1,
        "bd": 0,
        "relief": "flat",
        "bg": "#f8f9fa",
        "activebackground": "#e9ecef"
    }
    
    estilo_botoes_operacoes = {
        "font": ("Arial", 18),
        "width": 5,
        "height": 1,
        "bd": 0,
        "relief": "flat",
        "bg": "#dee2e6",
        "activebackground": "#ced4da"
    }
    
    estilo_botoes_especiais = {
        "font": ("Arial", 18),
        "width": 5,
        "height": 1,
        "bd": 0,
        "relief": "flat",
        "bg": COR_SECUNDARIA,
        "fg": "white",
        "activebackground": "#2980b9"
    }
    
    # Display
    frame_display = tk.Frame(janela_calc, bg=COR_FUNDO)
    frame_display.pack(pady=10)
    
    entry = tk.Entry(frame_display, width=15, font=("Arial", 28), bd=0, bg="white", 
                     fg=COR_PRIMARIA, justify="right", relief="solid", highlightthickness=1, 
                     highlightbackground="#ced4da", highlightcolor=COR_SECUNDARIA)
    entry.pack(pady=5, padx=10, ipady=10)
    
    # Funções
    def click(num):
        entry.insert(tk.END, num)
    
    def limpar():
        entry.delete(0, tk.END)
    
    def calcular():
        try:
            resultado = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(resultado))
        except:
            messagebox.showerror("Erro", "Expressão inválida.")
    
    def backspace():
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])
    
    # Teclado
    frame_teclado = tk.Frame(janela_calc, bg=COR_FUNDO)
    frame_teclado.pack()
    
    # Linha 1
    tk.Button(frame_teclado, text="C", command=limpar, **estilo_botoes_especiais).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame_teclado, text="⌫", command=backspace, **estilo_botoes_especiais).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame_teclado, text="%", command=lambda: click("%"), **estilo_botoes_operacoes).grid(row=0, column=2, padx=5, pady=5)
    tk.Button(frame_teclado, text="/", command=lambda: click("/"), **estilo_botoes_operacoes).grid(row=0, column=3, padx=5, pady=5)
    
    # Linha 2
    tk.Button(frame_teclado, text="7", command=lambda: click("7"), **estilo_botoes).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame_teclado, text="8", command=lambda: click("8"), **estilo_botoes).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(frame_teclado, text="9", command=lambda: click("9"), **estilo_botoes).grid(row=1, column=2, padx=5, pady=5)
    tk.Button(frame_teclado, text="*", command=lambda: click("*"), **estilo_botoes_operacoes).grid(row=1, column=3, padx=5, pady=5)
    
    # Linha 3
    tk.Button(frame_teclado, text="4", command=lambda: click("4"), **estilo_botoes).grid(row=2, column=0, padx=5, pady=5)
    tk.Button(frame_teclado, text="5", command=lambda: click("5"), **estilo_botoes).grid(row=2, column=1, padx=5, pady=5)
    tk.Button(frame_teclado, text="6", command=lambda: click("6"), **estilo_botoes).grid(row=2, column=2, padx=5, pady=5)
    tk.Button(frame_teclado, text="-", command=lambda: click("-"), **estilo_botoes_operacoes).grid(row=2, column=3, padx=5, pady=5)
    
    # Linha 4
    tk.Button(frame_teclado, text="1", command=lambda: click("1"), **estilo_botoes).grid(row=3, column=0, padx=5, pady=5)
    tk.Button(frame_teclado, text="2", command=lambda: click("2"), **estilo_botoes).grid(row=3, column=1, padx=5, pady=5)
    tk.Button(frame_teclado, text="3", command=lambda: click("3"), **estilo_botoes).grid(row=3, column=2, padx=5, pady=5)
    tk.Button(frame_teclado, text="+", command=lambda: click("+"), **estilo_botoes_operacoes).grid(row=3, column=3, padx=5, pady=5)
    
    # Linha 5
    tk.Button(frame_teclado, text="0", command=lambda: click("0"), **estilo_botoes).grid(row=4, column=0, padx=5, pady=5)
    tk.Button(frame_teclado, text=".", command=lambda: click("."), **estilo_botoes).grid(row=4, column=1, padx=5, pady=5)
    tk.Button(frame_teclado, text="=", command=calcular, **estilo_botoes_especiais).grid(row=4, column=2, columnspan=2, sticky="we", padx=5, pady=5)
    
    # Configuração de teclado
    def tecla_pressionada(event):
        key = event.char
        if key in '0123456789':
            click(key)
        elif key in '+-*/':
            click(key)
        elif event.keysym == 'Return':
            calcular()
        elif event.keysym == 'Escape':
            limpar()
        elif event.keysym == 'BackSpace':
            backspace()
    
    janela_calc.bind('<Key>', tecla_pressionada)

# =====================
# 4 - Cronômetro / Timer
# =====================
def abrir_cronometro():
    janela_timer = tk.Toplevel(root)
    janela_timer.title("⏱️ Cronômetro")
    janela_timer.geometry("450x250")
    janela_timer.configure(bg=COR_FUNDO)
    janela_timer.resizable(False, False)
    
    # Variáveis
    tempo = tk.IntVar(value=0)
    rodando = [False]
    formato_tempo = tk.StringVar(value="00:00:00")
    
    # Frame principal
    frame_principal = tk.Frame(janela_timer, bg=COR_FUNDO)
    frame_principal.pack(pady=20, padx=20, fill="both", expand=True)
    
    tk.Label(frame_principal, text="⏱️ Cronômetro", font=FONTE_TITULO, 
             bg=COR_FUNDO, fg=COR_PRIMARIA).pack(pady=(0, 20))
    
    # Display do tempo
    frame_display = tk.Frame(frame_principal, bg=COR_FUNDO)
    frame_display.pack(pady=10)
    
    label_tempo = tk.Label(frame_display, textvariable=formato_tempo, 
                          font=("Courier New", 36, "bold"), bg=COR_FUNDO, fg=COR_PRIMARIA)
    label_tempo.pack()
    
    # Frame de botões
    frame_botoes = tk.Frame(frame_principal, bg=COR_FUNDO)
    frame_botoes.pack(pady=20)
    
    def atualizar_tempo():
        if rodando[0]:
            tempo.set(tempo.get() + 1)
            horas = tempo.get() // 3600
            minutos = (tempo.get() % 3600) // 60
            segundos = tempo.get() % 60
            formato_tempo.set(f"{horas:02d}:{minutos:02d}:{segundos:02d}")
            janela_timer.after(1000, atualizar_tempo)
    
    def iniciar():
        if not rodando[0]:
            rodando[0] = True
            atualizar_tempo()
    
    def parar():
        rodando[0] = False
    
    def resetar():
        rodando[0] = False
        tempo.set(0)
        formato_tempo.set("00:00:00")
    
    btn_iniciar = tk.Button(frame_botoes, text="▶ Iniciar", font=FONTE_BOTOES, 
                           bg="#2ecc71", fg="white", width=10, command=iniciar)
    btn_iniciar.grid(row=0, column=0, padx=5)
    
    btn_parar = tk.Button(frame_botoes, text="⏸ Parar", font=FONTE_BOTOES, 
                         bg="#e74c3c", fg="white", width=10, command=parar)
    btn_parar.grid(row=0, column=1, padx=5)
    
    btn_resetar = tk.Button(frame_botoes, text="⏹ Resetar", font=FONTE_BOTOES, 
                           bg="#95a5a6", fg="white", width=10, command=resetar)
    btn_resetar.grid(row=0, column=2, padx=5)
    
    # Voltas
    frame_voltas = tk.LabelFrame(frame_principal, text=" Voltas ", font=FONTE_BOTOES, 
                               bg=COR_FUNDO, fg=COR_PRIMARIA, padx=10, pady=10)
    frame_voltas.pack(fill="x", pady=(10, 0))
    
    lista_voltas = tk.Listbox(frame_voltas, height=3, font=("Courier New", 10), bd=0)
    lista_voltas.pack(fill="x")
    
    def registrar_volta():
        if tempo.get() > 0:
            lista_voltas.insert(tk.END, formato_tempo.get())
    
    btn_volta = tk.Button(frame_voltas, text="⏱ Registrar Volta", font=FONTE_BOTOES, 
                         bg=COR_SECUNDARIA, fg="white", command=registrar_volta)
    btn_volta.pack(pady=5)

# =====================
# Menu Principal
# =====================
root = tk.Tk()
root.title("🛠️ Pacote de Ferramentas")
root.geometry("450x550")
root.configure(bg=COR_FUNDO)
root.resizable(False, False)

# Frame principal
frame_principal = tk.Frame(root, bg=COR_FUNDO)
frame_principal.pack(pady=30, padx=30, fill="both", expand=True)

tk.Label(frame_principal, text="🛠️ Pacote de Ferramentas", font=("Verdana", 18, "bold"), 
        bg=COR_FUNDO, fg=COR_PRIMARIA).pack(pady=(0, 30))

# Estilo dos botões principais
estilo_botoes_principais = {
    "font": ("Verdana", 12),
    "width": 25,
    "height": 2,
    "bd": 0,
    "relief": "flat",
    "bg": COR_SECUNDARIA,
    "fg": "white",
    "activebackground": "#2980b9"
}

# Botões do menu
tk.Button(frame_principal, text="🔒 Gerador de Senhas", command=abrir_gerador_senhas, 
          **estilo_botoes_principais).pack(pady=10)

tk.Button(frame_principal, text="🎯 Jogo de Adivinhação", command=abrir_jogo_adivinhacao, 
          **estilo_botoes_principais).pack(pady=10)

tk.Button(frame_principal, text="🧮 Calculadora", command=abrir_calculadora, 
          **estilo_botoes_principais).pack(pady=10)

tk.Button(frame_principal, text="⏱️ Cronômetro", command=abrir_cronometro, 
          **estilo_botoes_principais).pack(pady=10)

# Botão de sair
tk.Button(frame_principal, text="🚪 Sair", command=root.destroy, 
          font=("Verdana", 12), width=25, height=2, bd=0, relief="flat", 
          bg=COR_TERCIARIA, fg="white", activebackground="#c0392b").pack(pady=20)

# Rodapé
tk.Label(frame_principal, text="© 2025 Pacote de Ferramentas", 
         font=("Verdana", 8), bg=COR_FUNDO, fg="#7f8c8d").pack(side="bottom", pady=10)
tk.Label(frame_principal, text="By Mateus Batista", 
         font=("Verdana", 8), bg=COR_FUNDO, fg="#7f8c8d").pack(side="bottom", pady=10)
root.mainloop()