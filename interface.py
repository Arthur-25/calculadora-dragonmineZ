import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        texto_peso = entry_peso.get().replace(',', '.')
        if not texto_peso:
            messagebox.showerror("Erro", "Por favor, insira um valor para o peso ideal.")
            return
        
        peso_ideal = float(texto_peso)
        
        # Lógica original do main.py
        peso_ideal = peso_ideal / 0.75
        
        if var_dimensao.get():
            peso_ideal = peso_ideal / 10
            
        label_resultado.config(text=f"Resultado: {peso_ideal:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Configuração da Janela Principal
root = tk.Tk()
root.title("Calculadora Dragon MineZ - Peso")
root.geometry("380x300")
root.config(bg="#1e1e2e")
root.resizable(False, False)

# Estilos de cores (Tema Escuro / Moderno)
BG_COLOR = "#1e1e2e"
TEXT_COLOR = "#cdd6f4"
ACCENT_COLOR = "#89b4fa"
BTN_BG = "#313244"
BTN_FG = "#cdd6f4"

# Título
title_label = tk.Label(root, text="Calculadora Dragon MineZ", font=("Arial", 16, "bold"), bg=BG_COLOR, fg=ACCENT_COLOR)
title_label.pack(pady=20)

# Frame para Entrada de Peso
frame_peso = tk.Frame(root, bg=BG_COLOR)
frame_peso.pack(pady=10)

label_peso = tk.Label(frame_peso, text="Peso Ideal:", font=("Arial", 11), bg=BG_COLOR, fg=TEXT_COLOR)
label_peso.pack(side=tk.LEFT, padx=5)

entry_peso = tk.Entry(frame_peso, font=("Arial", 11), width=12, justify="center")
entry_peso.pack(side=tk.LEFT, padx=5)

# Checkbox para Dimensão Alternativa
var_dimensao = tk.BooleanVar()
check_dimensao = tk.Checkbutton(root, text="Dimensão alternativa (Gravidade alterada)", variable=var_dimensao,
                                font=("Arial", 10), bg=BG_COLOR, fg=TEXT_COLOR, selectcolor="#313244", activebackground=BG_COLOR, activeforeground=TEXT_COLOR)
check_dimensao.pack(pady=15)

# Botão de Calcular
btn_calcular = tk.Button(root, text="Calcular", font=("Arial", 11, "bold"), bg=ACCENT_COLOR, fg="#11111b", 
                         activebackground="#b4befe", activeforeground="#11111b", relief=tk.FLAT, width=15, command=calcular)
btn_calcular.pack(pady=10)

# Label de Resultado
label_resultado = tk.Label(root, text="Resultado: -", font=("Arial", 13, "bold"), bg=BG_COLOR, fg="#a6e3a1")
label_resultado.pack(pady=15)

root.mainloop()
