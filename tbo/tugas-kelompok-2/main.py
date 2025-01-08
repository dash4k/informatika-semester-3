import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from cyk import cykParse

anggota_kelompok = """
Anggota Kelompok:\n
1. I Nyoman Suryadana \t\t\t\t2308561032
2. Jesika Emiya Pepayosa Br Sembiring \t\t\t2308561038
3. I Gusti Bagus Rahajeng Danishwara Dipa Pracheta \t2308561050
4. Ni Made Anita Widyastini \t\t\t\t2308561130
"""

def display_results(text_accepted, text, data):
    if text_accepted:
        messagebox.showinfo("Hasil Validasi", "Kalimat diterima: {}".format(" ".join(text)))
    else:
        messagebox.showerror("Hasil Validasi", "Kalimat tidak diterima.")

    if data is not None:
        # Clear previous table
        for item in tree.get_children():
            tree.delete(item)
        for col in tree["columns"]:
            tree.heading(col, text="")
            tree.column(col, width=0)
        tree["columns"] = []  # Reset columns

        # Dynamically set the columns
        columns = [f"Column {i+1}" for i in range(len(data[0]))] if data else []
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        # Insert data into table
        for i, row in enumerate(data):
            tree.insert("", "end", text=str(i), values=row)

def validate_sentence():
    input_text = entry.get().strip()

    if not input_text:
        messagebox.showwarning("Warning", "Masukkan Kalimat untuk Divalidasi.")
        return

    text = input_text.lower().split(" ")
    text_accepted, result = cykParse(text)

    data = pd.DataFrame(result).fillna('')
    display_results(text_accepted, text, data.values.tolist())


root = tk.Tk()
root.title("Kelompok B2")

title = tk.Label(root, text="Memvalidasi Kalimat Sederhana Bahasa Bali dengan Predikat Frasa Adjektiva (AdjP)", font=("Helvetica", 14), wraplength=1000, justify="center")
title.pack(pady=40)

divider = tk.Frame(root, height=2, bd=1, relief="sunken", bg="grey")
divider.pack(fill="x", pady=0)

anggota_frame = tk.Frame(root, padx=100, pady=10)
anggota_frame.pack(fill="both", expand=False)

anggota = tk.Label(anggota_frame, text=anggota_kelompok, font=("Arial", 12), justify="left", anchor="w")
anggota.pack(pady=10, fill="x")

divider = tk.Frame(root, height=2, bd=1, relief="sunken", bg="grey")
divider.pack(fill="x", pady=40)

frame_input = tk.Frame(root, padx=100, pady= 10)
frame_input.pack(fill="both", expand=False)

label_input = tk.Label(frame_input, text="Input Kalimat dalam Bahasa Bali dengan Predikat Frasa Adjektiva:")
label_input.pack()

entry = tk.Entry(frame_input, width=50)
entry.pack()

button = tk.Button(root, text="Periksa", command=validate_sentence)
button.pack(pady=10)

# Table to display parsing result
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

tree = ttk.Treeview(frame_table, show="headings")
tree.pack(fill="both", expand=True)

root.mainloop()
