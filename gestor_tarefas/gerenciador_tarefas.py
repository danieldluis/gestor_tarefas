# gestor_tarefas.py
# fiz este programa pra praticar tkinter
# basicamente é um to-do list com prioridades

import tkinter as tk
from tkinter import messagebox

tarefas = []

root = tk.Tk()
root.title("📋 Gestor de Tarefas")
root.geometry("480x420")
root.resizable(False, False)

frame_topo = tk.Frame(root, padx=10, pady=5)
frame_topo.pack(fill="x")

tk.Label(frame_topo, text="Tarefa:").pack(side="left")
entry_nome = tk.Entry(frame_topo, width=25)
entry_nome.pack(side="left", padx=5)

tk.Label(frame_topo, text="Prior. (1-10):").pack(side="left", padx=(10, 0))
entry_prio = tk.Entry(frame_topo, width=4)
entry_prio.pack(side="left", padx=5)


def adicionar():
    nome = entry_nome.get().strip()
    prio = entry_prio.get().strip()

    if nome == "":
        messagebox.showwarning("Ops", "Põe o nome da tarefa!")
        return
    if not prio.isdigit() or int(prio) < 1 or int(prio) > 10:
        messagebox.showwarning("Ops", "Prioridade tem que ser 1 a 10")
        return

    tarefas.append({"nome": nome, "prioridade": int(prio)})
    tarefas.sort(key=lambda x: x["prioridade"])

    entry_nome.delete(0, tk.END)
    entry_prio.delete(0, tk.END)
    entry_nome.focus()
    atualizar()


def remover():
    sel = lista.curselection()
    if not sel:
        messagebox.showwarning("Ops", "Seleciona uma tarefa primeiro")
        return
    del tarefas[sel[0]]
    atualizar()


def limpar_tudo():
    if not tarefas:
        return
    if messagebox.askyesno("Confirmar", "Tirar tudo?"):
        tarefas.clear()
        atualizar()


def atualizar():
    lista.delete(0, tk.END)
    for t in tarefas:
        lista.insert(tk.END, f"[{t['prioridade']}] {t['nome']}")
    lbl_status.config(text=f"{len(tarefas)} tarefa(s)")


frame_botao = tk.Frame(root, padx=10)
frame_botao.pack(pady=5)

tk.Button(frame_botao, text="Adicionar", command=adicionar, bg="#4CAF50", fg="white", width=11).pack(side="left", padx=3)
tk.Button(frame_botao, text="Remover", command=remover, bg="#f44336", fg="white", width=11).pack(side="left", padx=3)
tk.Button(frame_botao, text="Limpar", command=limpar_tudo, bg="#FF9800", fg="white", width=11).pack(side="left", padx=3)

frame_lista = tk.Frame(root, padx=10)
frame_lista.pack(fill="both", expand=True)

lista = tk.Listbox(frame_lista, height=10)
lista.pack(fill="both", expand=True)

lbl_status = tk.Label(root, text="0 tarefa(s)", anchor="w")
lbl_status.pack(fill="x", padx=10, pady=(0, 8))

root.mainloop()   
