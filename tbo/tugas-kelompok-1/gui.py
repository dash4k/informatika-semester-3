import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import mysql.connector


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Arsip dan Validasi Berkas Syarat Kelulusan")
        self.geometry("1000x500")
        self.frames = {}

        # for Page in (q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17):
        for Page in (q0,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10):
            frame = Page(parent=self, controller=self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(q0)
    
    

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

        if isinstance(frame, q5) or isinstance(frame, q7) or isinstance(frame, q9):
            frame.refresh_data()

class q0(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Welcome!")
        label.pack(pady=60)

        username_label = tk.Label(self, text="Username:")
        username_label.pack(pady=5, padx=400)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5, padx=400)

        password_label = tk.Label(self, text="Password:")
        password_label.pack(pady=5, padx=400)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5, padx=400)

        login_button = tk.Button(self, text="Login", command=self.perform_login)
        login_button.pack(pady=10, padx=400)

    def perform_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.login(username, password):
            self.controller.show_frame(q1)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

    @staticmethod
    def login(username: str, password: str) -> bool:
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = "SELECT id FROM akun WHERE username = %s AND pw = %s;"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            return True if result else False
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()

class q1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Dashboard", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 20

        button1 = tk.Button(self, text="KEMAHASISWAAN",
                            command=lambda: controller.show_frame(q2),
                            pady=5,
                            width=button_width)
        button1.pack()
        label = tk.Label(self, text="")
        label.pack(pady=5)

        button2 = tk.Button(self, text="UMUM",
                            command=lambda: controller.show_frame(q3),
                            pady=5,
                            width=button_width)
        button2.pack()
        label1 = tk.Label(self, text="")
        label1.pack(pady=5)
        
        button3 = tk.Button(self, text="INTERNAL",
                            command=lambda: controller.show_frame(q4),
                            pady=5,
                            width=button_width)
        button3.pack()
        label2 = tk.Label(self, text="")
        label2.pack(pady=5)
        
        button4 = tk.Button(self, text="EXIT",
                            command=self.quit,
                            pady=5,
                            width=button_width)
        button4.pack()

class q2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Butir Kemahasiswaan", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 30

        button1 = tk.Button(self, text="View Butir Kemahasiswaan",
                            command=lambda: controller.show_frame(q5),
                            pady=5,
                            width=button_width)
        button1.pack()
        label = tk.Label(self, text="")
        label.pack(pady=5)

        button2 = tk.Button(self, text="Tambah Butir Kemahasiswaan",
                            command=lambda: controller.show_frame(q6),
                            pady=5,
                            width=button_width)
        button2.pack()

class q3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Butir Umum", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 30

        button1 = tk.Button(self, text="View Butir Umum",
                            command=lambda: controller.show_frame(q7),
                            pady=5,
                            width=button_width)
        button1.pack()
        label = tk.Label(self, text="")
        label.pack(pady=5)

        button2 = tk.Button(self, text="Tambah Butir Umum",
                            command=lambda: controller.show_frame(q8),
                            pady=5,
                            width=button_width)
        button2.pack()

class q4(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Butir Internal", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 30

        button1 = tk.Button(self, text="View Butir Internal",
                            command=lambda: controller.show_frame(q9),
                            pady=5,
                            width=button_width)
        button1.pack()
        label = tk.Label(self, text="")
        label.pack(pady=5)

        button2 = tk.Button(self, text="Tambah Butir Internal",
                            command=lambda: controller.show_frame(q10),
                            pady=5,
                            width=button_width)
        button2.pack()

class q5(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.choice = ''

        columns = ("NIM", "Nama", "Angkatan")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        data = self.fetch()
        for row in data:
            self.tree.insert("", tk.END, values=row)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        button1 = tk.Button(button_frame, text="Lihat Data", command=self.perform_action)
        button1.pack(side=tk.LEFT, padx=5)

        button2 = tk.Button(button_frame, text="Kembali ke Dashboard", command=lambda: controller.show_frame(q1))
        button2.pack(side=tk.LEFT, padx=5)

    def refresh_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = "SELECT nim, nama_mahasiswa, angkatan_mahasiswa FROM kemahasiswaan"
            cursor.execute(query)
            result = cursor.fetchall()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in result:
            self.tree.insert("", tk.END, values=row)

    def fetch(self) -> bool:
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = "SELECT nim, nama_mahasiswa, angkatan_mahasiswa FROM kemahasiswaan"
            cursor.execute(query)
            result = cursor.fetchall()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()
        return result

    def perform_action(self):
        selected_mahasiswa = self.tree.selection()
        if selected_mahasiswa:
            row_values = self.tree.item(selected_mahasiswa, "values")
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="tbo_kelompok_kelulusan"
                )
                cursor = connection.cursor()
                query = "SELECT ktm_mahasiswa, uktku_mahasiswa, univ_mahasiswa, fakultas_mahasiswa FROM kemahasiswaan WHERE nim = %s"
                cursor.execute(query, (row_values[0],))
                result = cursor.fetchall()
                if not result:
                    messagebox.showwarning("No Files", "No files found in the database.")
                    return
                
                new_window = tk.Toplevel()
                new_window.title("Pilih Butir Kemahasiswaan")
                new_window.geometry("500x250")

                button_width = 25
                
                button0 = tk.Button(new_window,
                             text="ktm_mahasiswa", 
                             command=lambda: self.download("ktm_mahasiswa", row_values[0]), 
                             width=button_width)
                button0.pack(pady=10, padx=100)

                button1 = tk.Button(new_window,
                             text="UKTKu", 
                             command=lambda: self.download("uktku_mahasiswa", row_values[0]), 
                             width=button_width)
                button1.pack(pady=10, padx=100)

                button2 = tk.Button(new_window,
                             text="Sertifikat PKKMB Universitas",
                             command=lambda: self.download("univ_mahasiswa", row_values[0]),
                             width=button_width)
                button2.pack(pady=10, padx=100)

                button3 = tk.Button(new_window,
                             text="Sertifikat PKKMB Fakultas",
                             command=lambda: self.download("fakultas_mahasiswa", row_values[0]),
                             width=button_width)
                button3.pack(pady=10, padx=100)

            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
                return False
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            tk.messagebox.showwarning("No Selection", "Please select a row first!")
    
    def download(self, item: str, nim: str):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = f"SELECT {item}, {item.split('_')[0]}_ext FROM kemahasiswaan WHERE nim = %s"
            cursor.execute(query, (nim,))
            result = cursor.fetchone()
            
            if result and result[0]:
                file_content, file_extension = result
                save_path = filedialog.asksaveasfilename(
                    initialfile=f"{nim}_{item}.{file_extension}",
                    title="Save File As",
                    defaultextension=f".{file_extension}"
                )
                if save_path:
                    with open(save_path, "wb") as file:
                        file.write(file_content)
                    messagebox.showinfo("Success", "File has been downloaded successfully.")
                else:
                    messagebox.showinfo("Cancelled", "Download cancelled.")
            else:
                messagebox.showerror("Error", "File not found in the database.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

class q6(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.ktm = None
        self.uktku = None
        self.univ = None
        self.fakultas = None

        label_width = 25
        button_width = 30
        entry_width = 33

        label = tk.Label(self, text="Tambah Butir Kemahasiswaan", font=("Arial", 10))
        label.pack(pady=5)

        nama_mahasiswa = tk.Frame(self)
        nama_mahasiswa.pack(pady=10)
        
        nim_mahasiswa = tk.Frame(self)
        nim_mahasiswa.pack(pady=10)
        
        angkatan_mahasiswa = tk.Frame(self)
        angkatan_mahasiswa.pack(pady=10)
        
        ktm_mahasiswa = tk.Frame(self)
        ktm_mahasiswa.pack(pady=10)

        uktku_mahasiswa = tk.Frame(self)
        uktku_mahasiswa.pack(pady=10)
        
        univ_mahasiswa = tk.Frame(self)
        univ_mahasiswa.pack(pady=10)
        
        fakultas_mahasiswa = tk.Frame(self)
        fakultas_mahasiswa.pack(pady=10)
        
        option = tk.Frame(self)
        option.pack(pady=10)

        label1 = tk.Label(nama_mahasiswa,
                          text="Nama Mahasiswa",
                          width=label_width,
                          anchor='w')
        label1.pack(side=tk.LEFT, padx=10)

        self.entry1 = tk.Entry(nama_mahasiswa, 
                               width=entry_width)
        self.entry1.pack(side=tk.LEFT, padx=10)
        
        label2 = tk.Label(nim_mahasiswa, 
                          text="Nim Mahasiswa",
                          width=label_width,
                          anchor='w')
        label2.pack(side=tk.LEFT, padx=10)

        self.entry2 = tk.Entry(nim_mahasiswa,
                               width=entry_width)
        self.entry2.pack(side=tk.LEFT, padx=10)
        
        label3 = tk.Label(angkatan_mahasiswa,
                          text="Angkatan Mahasiswa",
                          width=label_width,
                          anchor='w')
        label3.pack(side=tk.LEFT, padx=10)

        self.entry3 = tk.Entry(angkatan_mahasiswa,
                               width=entry_width)
        self.entry3.pack(side=tk.LEFT, padx=10)

        label4 = tk.Label(ktm_mahasiswa,
                          text="Berkas KTM",
                          width=label_width,
                          anchor='w')
        label4.pack(side=tk.LEFT, padx=10)

        button1 = tk.Button(ktm_mahasiswa,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(1),
                            width=button_width)
        button1.pack(side=tk.LEFT, padx=10)
        
        label5 = tk.Label(uktku_mahasiswa,
                          text="Berkas UKTKu",
                          width=label_width,
                          anchor='w')
        label5.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(uktku_mahasiswa,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(2),
                            width=button_width)
        button2.pack(side=tk.LEFT, padx=10)
        
        label6 = tk.Label(univ_mahasiswa,
                          text="Berkas PKKMB Universitas",
                          width=label_width,
                          anchor='w')
        label6.pack(side=tk.LEFT, padx=10)

        button3 = tk.Button(univ_mahasiswa,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(3),
                            width=button_width)
        button3.pack(side=tk.LEFT, padx=10)
        
        label7 = tk.Label(fakultas_mahasiswa,
                          text="Berkas PKKMB Fakultas",
                          width=label_width,
                          anchor='w')
        label7.pack(side=tk.LEFT, padx=10)

        button4 = tk.Button(fakultas_mahasiswa,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(4),
                            width=button_width)
        button4.pack(side=tk.LEFT, padx=10)

        label0 = tk.Label(self, text="")
        label0.pack(pady=2)
        
        button5 = tk.Button(option,
                            text="Verifikasi Berkas", 
                            command=lambda: self.upload(-1),
                            width=20)
        button5.pack(side=tk.LEFT, padx=10)
        
        button6 = tk.Button(option,
                            text="Back to Dashboard", 
                            command=lambda: controller.show_frame(q1),
                            width=20)
        button6.pack(side=tk.LEFT, padx=10)
    
    def upload(self, item: int):
        if item == -1:
            if not all([self.ktm, self.uktku, self.univ, self.fakultas]):
                messagebox.showerror("Caution", "Please fill out everything before continuing!")
                return
            elif self.ktm[1] != 'pdf' or self.uktku[1] != 'pdf' or self.univ[1] != 'pdf' or self.fakultas[1] != 'pdf':
                messagebox.showerror("Caution", "Please select a valid file type!")
                return
            elif not self.entry2.get().isdigit() or not self.entry3.get().isdigit() or len(self.entry2.get()) != 10 or len(self.entry3.get()) != 4:
                messagebox.showerror("Caution", "Please enter a valid student data!")
                return
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="tbo_kelompok_kelulusan"
                )
                cursor = connection.cursor()
                query = "SELECT 1 FROM kemahasiswaan WHERE nim = %s"
                cursor.execute(query, (self.entry2.get(), ))
                result = cursor.fetchall()
                if result:  # If the NIM exists, update the row
                    query = """UPDATE kemahasiswaan
                            SET ktm_mahasiswa = %s, uktku_mahasiswa = %s, univ_mahasiswa = %s, fakultas_mahasiswa = %s,
                                ktm_ext = %s, uktku_ext = %s, univ_ext = %s, fakultas_ext = %s
                            WHERE nim = %s"""
                    cursor.execute(query, (
                        self.ktm[0], self.uktku[0], self.univ[0], self.fakultas[0],
                        self.ktm[1], self.uktku[1], self.univ[1], self.fakultas[1], self.entry2.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Data has been saved.")
                else:
                    query = """INSERT INTO kemahasiswaan (nim, nama_mahasiswa, angkatan_mahasiswa,
                                                        ktm_mahasiswa, uktku_mahasiswa, univ_mahasiswa, fakultas_mahasiswa,
                                                        ktm_ext, uktku_ext, univ_ext, fakultas_ext)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(query, (
                        self.entry2.get(), self.entry1.get(), self.entry3.get(),
                        self.ktm[0], self.uktku[0], self.univ[0], self.fakultas[0],  # Binary content
                        self.ktm[1], self.uktku[1], self.univ[1], self.fakultas[1]   # File extensions
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Data has been saved.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            file_path = filedialog.askopenfilename(title="Select a File")
            if file_path:
                with open(file_path, "rb") as file:
                    file_content = file.read()
                if item == 1:
                    self.ktm = (file_content, file_path.split('.')[-1])  # Store content and extension
                elif item == 2:
                    self.uktku = (file_content, file_path.split('.')[-1])
                elif item == 3:
                    self.univ = (file_content, file_path.split('.')[-1])
                elif item == 4:
                    self.fakultas = (file_content, file_path.split('.')[-1])

class q7(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.choice = ''

        columns = ("NIM", "Nama", "Angkatan")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        data = self.fetch()
        for row in data:
            self.tree.insert("", tk.END, values=row)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        button1 = tk.Button(button_frame, text="Lihat Data", command=self.perform_action)
        button1.pack(side=tk.LEFT, padx=5)

        button2 = tk.Button(button_frame, text="Kembali ke Dashboard", command=lambda: controller.show_frame(q1))
        button2.pack(side=tk.LEFT, padx=5)

    def refresh_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = "SELECT nim, nama_mahasiswa, angkatan_mahasiswa FROM kemahasiswaan"
            cursor.execute(query)
            result = cursor.fetchall()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in result:
            self.tree.insert("", tk.END, values=row)

    def fetch(self) -> bool:
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = "SELECT nim, nama_mahasiswa, angkatan_mahasiswa FROM kemahasiswaan"
            cursor.execute(query)
            result = cursor.fetchall()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()
        return result

    def perform_action(self):
        selected_mahasiswa = self.tree.selection()
        if selected_mahasiswa:
            row_values = self.tree.item(selected_mahasiswa, "values")
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="tbo_kelompok_kelulusan"
                )
                cursor = connection.cursor()
                query = "SELECT ta_mahasiswa, pernyataan_lulus_ta_mahasiswa, transkrip_nilai_mahasiswa FROM kemahasiswaan WHERE nim = %s"
                cursor.execute(query, (row_values[0],))
                result = cursor.fetchall()
                if not result:
                    messagebox.showwarning("No Files", "No files found in the database.")
                    return
                
                new_window = tk.Toplevel()
                new_window.title("Pilih Butir Umum")
                new_window.geometry("500x250")

                button_width = 25
                
                button0 = tk.Button(new_window,
                             text="Tugas Akhr", 
                             command=lambda: self.download("ta_mahasiswa", row_values[0]), 
                             width=button_width)
                button0.pack(pady=10, padx=100)

                button1 = tk.Button(new_window,
                             text="Pernyataan Lulus TA", 
                             command=lambda: self.download("pernyataan_lulus_ta_mahasiswa", row_values[0]), 
                             width=button_width)
                button1.pack(pady=10, padx=100)

                button2 = tk.Button(new_window,
                             text="Transkrip Mahasiswa",
                             command=lambda: self.download("transkrip_nilai_mahasiswa", row_values[0]),
                             width=button_width)
                button2.pack(pady=10, padx=100)


            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
                return False
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            tk.messagebox.showwarning("No Selection", "Please select a row first!")
    
    def download(self, item: str, nim: str):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = f"SELECT {item}, {item.split('_')[0]}_ext FROM kemahasiswaan WHERE nim = %s"
            cursor.execute(query, (nim,))
            result = cursor.fetchone()
            
            if result and result[0]:
                file_content, file_extension = result
                save_path = filedialog.asksaveasfilename(
                    initialfile=f"{nim}_{item}.{file_extension}",
                    title="Save File As",
                    defaultextension=f".{file_extension}"
                )
                if save_path:
                    with open(save_path, "wb") as file:
                        file.write(file_content)
                    messagebox.showinfo("Success", "File has been downloaded successfully.")
                else:
                    messagebox.showinfo("Cancelled", "Download cancelled.")
            else:
                messagebox.showerror("Error", "File not found in the database.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

class q8(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.ta = None
        self.pernyataan = None
        self.transkrip = None

        label_width = 25
        button_width = 30
        entry_width = 33

        label = tk.Label(self, text="Tambah Butir Umum", font=("Arial", 10))
        label.pack(pady=5)

        nama_mahasiswa = tk.Frame(self)
        nama_mahasiswa.pack(pady=10)
        
        nim_mahasiswa = tk.Frame(self)
        nim_mahasiswa.pack(pady=10)
        
        angkatan_mahasiswa = tk.Frame(self)
        angkatan_mahasiswa.pack(pady=10)
        
        ta_mahasiswa = tk.Frame(self)
        ta_mahasiswa.pack(pady=10)

        pernyataan_lulus = tk.Frame(self)
        pernyataan_lulus.pack(pady=10)
        
        transkrip_mahasiswa = tk.Frame(self)
        transkrip_mahasiswa.pack(pady=10)
        
        option = tk.Frame(self)
        option.pack(pady=10)

        label1 = tk.Label(nama_mahasiswa,
                          text="Nama Mahasiswa",
                          width=label_width,
                          anchor='w')
        label1.pack(side=tk.LEFT, padx=10)

        self.entry1 = tk.Entry(nama_mahasiswa, 
                               width=entry_width)
        self.entry1.pack(side=tk.LEFT, padx=10)
        
        label2 = tk.Label(nim_mahasiswa, 
                          text="Nim Mahasiswa",
                          width=label_width,
                          anchor='w')
        label2.pack(side=tk.LEFT, padx=10)

        self.entry2 = tk.Entry(nim_mahasiswa,
                               width=entry_width)
        self.entry2.pack(side=tk.LEFT, padx=10)
        
        label3 = tk.Label(angkatan_mahasiswa,
                          text="Angkatan Mahasiswa",
                          width=label_width,
                          anchor='w')
        label3.pack(side=tk.LEFT, padx=10)

        self.entry3 = tk.Entry(angkatan_mahasiswa,
                               width=entry_width)
        self.entry3.pack(side=tk.LEFT, padx=10)

        label4 = tk.Label(ta_mahasiswa,
                          text="Berkas TA",
                          width=label_width,
                          anchor='w')
        label4.pack(side=tk.LEFT, padx=10)

        button1 = tk.Button(ta_mahasiswa,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(1),
                            width=button_width)
        button1.pack(side=tk.LEFT, padx=10)
        
        label5 = tk.Label(pernyataan_lulus,
                          text="Berkas Pernyataan TA",
                          width=label_width,
                          anchor='w')
        label5.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(pernyataan_lulus,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(2),
                            width=button_width)
        button2.pack(side=tk.LEFT, padx=10)
        
        label6 = tk.Label(transkrip_mahasiswa,
                          text="Berkas Transkrip",
                          width=label_width,
                          anchor='w')
        label6.pack(side=tk.LEFT, padx=10)

        button3 = tk.Button(transkrip_mahasiswa,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(3),
                            width=button_width)
        button3.pack(side=tk.LEFT, padx=10)

        label0 = tk.Label(self, text="")
        label0.pack(pady=2)
        
        button5 = tk.Button(option,
                            text="Verifikasi Berkas", 
                            command=lambda: self.upload(-1),
                            width=20)
        button5.pack(side=tk.LEFT, padx=10)
        
        button6 = tk.Button(option,
                            text="Back to Dashboard", 
                            command=lambda: controller.show_frame(q1),
                            width=20)
        button6.pack(side=tk.LEFT, padx=10)
    
    def upload(self, item: int):
        if item == -1:
            if not all([self.ta, self.pernyataan, self.transkrip]):
                messagebox.showerror("Caution", "Please fill out everything before continuing!")
                return
            elif self.ta[1] != 'pdf' or self.pernyataan[1] != 'pdf' or self.transkrip[1] != 'pdf':
                messagebox.showerror("Caution", "Please select a valid file type!")
                return
            elif not self.entry2.get().isdigit() or not self.entry3.get().isdigit() or len(self.entry2.get()) != 10 or len(self.entry3.get()) != 4:
                messagebox.showerror("Caution", "Please enter a valid student data!")
                return
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="tbo_kelompok_kelulusan"
                )
                cursor = connection.cursor()
                query = "SELECT 1 FROM kemahasiswaan WHERE nim = %s"
                cursor.execute(query, (self.entry2.get(), ))
                result = cursor.fetchall()
                if result:
                    query = """UPDATE kemahasiswaan
                            SET ta_mahasiswa = %s, pernyataan_lulus_ta_mahasiswa = %s, transkrip_nilai_mahasiswa = %s,
                                ta_ext = %s, pernyataan_ext = %s, transkrip_ext = %s
                            WHERE nim = %s"""
                    cursor.execute(query, (
                        self.ta[0], self.pernyataan[0], self.transkrip[0],
                        self.ta[1], self.pernyataan[1], self.transkrip[1], self.entry2.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Data has been saved.")
                else:
                    query = """INSERT INTO kemahasiswaan (nim, nama_mahasiswa, angkatan_mahasiswa,
                                                        ta_mahasiswa, pernyataan_lulus_ta_mahasiswa, transkrip_nilai_mahasiswa,
                                                        ta_ext, pernyataan_ext, transkrip_ext)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(query, (
                        self.entry2.get(), self.entry1.get(), self.entry3.get(),
                        self.ta[0], self.pernyataan[0], self.transkrip[0],
                        self.ta[1], self.pernyataan[1], self.transkrip[1]
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Data has been saved.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            file_path = filedialog.askopenfilename(title="Select a File")
            if file_path:
                with open(file_path, "rb") as file:
                    file_content = file.read()
                if item == 1:
                    self.ta = (file_content, file_path.split('.')[-1])  # Store content and extension
                elif item == 2:
                    self.pernyataan = (file_content, file_path.split('.')[-1])
                elif item == 3:
                    self.transkrip = (file_content, file_path.split('.')[-1])

class q9(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.choice = ''

        columns = ("NIM", "Nama", "Angkatan")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        data = self.fetch()
        for row in data:
            self.tree.insert("", tk.END, values=row)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        button1 = tk.Button(button_frame, text="Lihat Data", command=self.perform_action)
        button1.pack(side=tk.LEFT, padx=5)

        button2 = tk.Button(button_frame, text="Kembali ke Dashboard", command=lambda: controller.show_frame(q1))
        button2.pack(side=tk.LEFT, padx=5)

    def refresh_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = "SELECT nim, nama_mahasiswa, angkatan_mahasiswa FROM kemahasiswaan"
            cursor.execute(query)
            result = cursor.fetchall()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in result:
            self.tree.insert("", tk.END, values=row)

    def fetch(self) -> bool:
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = "SELECT nim, nama_mahasiswa, angkatan_mahasiswa FROM kemahasiswaan"
            cursor.execute(query)
            result = cursor.fetchall()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            return False
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals() and connection.is_connected():
                connection.close()
        return result

    def perform_action(self):
        selected_mahasiswa = self.tree.selection()
        if selected_mahasiswa:
            row_values = self.tree.item(selected_mahasiswa, "values")
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="tbo_kelompok_kelulusan"
                )
                cursor = connection.cursor()
                query = "SELECT wta_mahasiswa, supremasi_mahasiswa, snatia_mahasiswa FROM kemahasiswaan WHERE nim = %s"
                cursor.execute(query, (row_values[0],))
                result = cursor.fetchall()
                if not result:
                    messagebox.showwarning("No Files", "No files found in the database.")
                    return
                
                new_window = tk.Toplevel()
                new_window.title("Pilih Butir Internal")
                new_window.geometry("500x250")

                button_width = 25
                
                button0 = tk.Button(new_window,
                             text="Workshop TA", 
                             command=lambda: self.download("wta_mahasiswa", row_values[0]), 
                             width=button_width)
                button0.pack(pady=10, padx=100)

                button1 = tk.Button(new_window,
                             text="Sertifikat Supremasi", 
                             command=lambda: self.download("supremasi_mahasiswa", row_values[0]), 
                             width=button_width)
                button1.pack(pady=10, padx=100)

                button2 = tk.Button(new_window,
                             text="Sertifikat Snatia",
                             command=lambda: self.download("snatia_mahasiswa", row_values[0]),
                             width=button_width)
                button2.pack(pady=10, padx=100)


            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
                return False
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            tk.messagebox.showwarning("No Selection", "Please select a row first!")
    
    def download(self, item: str, nim: str):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="tbo_kelompok_kelulusan"
            )
            cursor = connection.cursor()
            query = f"SELECT {item}, {item.split('_')[0]}_ext FROM kemahasiswaan WHERE nim = %s"
            cursor.execute(query, (nim,))
            result = cursor.fetchone()
            
            if result and result[0]:
                file_content, file_extension = result
                save_path = filedialog.asksaveasfilename(
                    initialfile=f"{nim}_{item}.{file_extension}",
                    title="Save File As",
                    defaultextension=f".{file_extension}"
                )
                if save_path:
                    with open(save_path, "wb") as file:
                        file.write(file_content)
                    messagebox.showinfo("Success", "File has been downloaded successfully.")
                else:
                    messagebox.showinfo("Cancelled", "Download cancelled.")
            else:
                messagebox.showerror("Error", "File not found in the database.")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

class q10(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.wta = None
        self.supremasi = None
        self.snatia = None

        label_width = 25
        button_width = 30
        entry_width = 33

        label = tk.Label(self, text="Tambah Butir Internal", font=("Arial", 10))
        label.pack(pady=5)

        nama_mahasiswa = tk.Frame(self)
        nama_mahasiswa.pack(pady=10)
        
        nim_mahasiswa = tk.Frame(self)
        nim_mahasiswa.pack(pady=10)
        
        angkatan_mahasiswa = tk.Frame(self)
        angkatan_mahasiswa.pack(pady=10)
        
        wta_mahasiswa = tk.Frame(self)
        wta_mahasiswa.pack(pady=10)

        supremasi = tk.Frame(self)
        supremasi.pack(pady=10)
        
        snatia = tk.Frame(self)
        snatia.pack(pady=10)
        
        option = tk.Frame(self)
        option.pack(pady=10)

        label1 = tk.Label(nama_mahasiswa,
                          text="Nama Mahasiswa",
                          width=label_width,
                          anchor='w')
        label1.pack(side=tk.LEFT, padx=10)

        self.entry1 = tk.Entry(nama_mahasiswa, 
                               width=entry_width)
        self.entry1.pack(side=tk.LEFT, padx=10)
        
        label2 = tk.Label(nim_mahasiswa, 
                          text="Nim Mahasiswa",
                          width=label_width,
                          anchor='w')
        label2.pack(side=tk.LEFT, padx=10)

        self.entry2 = tk.Entry(nim_mahasiswa,
                               width=entry_width)
        self.entry2.pack(side=tk.LEFT, padx=10)
        
        label3 = tk.Label(angkatan_mahasiswa,
                          text="Angkatan Mahasiswa",
                          width=label_width,
                          anchor='w')
        label3.pack(side=tk.LEFT, padx=10)

        self.entry3 = tk.Entry(angkatan_mahasiswa,
                               width=entry_width)
        self.entry3.pack(side=tk.LEFT, padx=10)

        label4 = tk.Label(wta_mahasiswa,
                          text="Berkas WTA",
                          width=label_width,
                          anchor='w')
        label4.pack(side=tk.LEFT, padx=10)

        button1 = tk.Button(wta_mahasiswa,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(1),
                            width=button_width)
        button1.pack(side=tk.LEFT, padx=10)
        
        label5 = tk.Label(supremasi,
                          text="Berkas Sertifikat Supremasi",
                          width=label_width,
                          anchor='w')
        label5.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(supremasi,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(2),
                            width=button_width)
        button2.pack(side=tk.LEFT, padx=10)
        
        label6 = tk.Label(snatia,
                          text="Berkas Sertifikat Snatia",
                          width=label_width,
                          anchor='w')
        label6.pack(side=tk.LEFT, padx=10)

        button3 = tk.Button(snatia,
                            text="Pilih Dokumen", 
                            command=lambda: self.upload(3),
                            width=button_width)
        button3.pack(side=tk.LEFT, padx=10)

        label0 = tk.Label(self, text="")
        label0.pack(pady=2)
        
        button5 = tk.Button(option,
                            text="Verifikasi Berkas", 
                            command=lambda: self.upload(-1),
                            width=20)
        button5.pack(side=tk.LEFT, padx=10)
        
        button6 = tk.Button(option,
                            text="Back to Dashboard", 
                            command=lambda: controller.show_frame(q1),
                            width=20)
        button6.pack(side=tk.LEFT, padx=10)
    
    def upload(self, item: int):
        if item == -1:
            if not all([self.wta, self.supremasi, self.snatia]):
                messagebox.showerror("Caution", "Please fill out everything before continuing!")
                return
            elif self.wta[1] != 'pdf' or self.supremasi[1] != 'pdf' or self.snatia[1] != 'pdf':
                messagebox.showerror("Caution", "Please select a valid file type!")
                return
            elif not self.entry2.get().isdigit() or not self.entry3.get().isdigit() or len(self.entry2.get()) != 10 or len(self.entry3.get()) != 4:
                messagebox.showerror("Caution", "Please enter a valid student data!")
                return
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="tbo_kelompok_kelulusan"
                )
                cursor = connection.cursor()
                query = "SELECT 1 FROM kemahasiswaan WHERE nim = %s"
                cursor.execute(query, (self.entry2.get(), ))
                result = cursor.fetchall()
                if result:
                    query = """UPDATE kemahasiswaan
                            SET wta_mahasiswa = %s, supremasi_mahasiswa = %s, snatia_mahasiswa = %s,
                               wta_ext = %s, supremasi_ext = %s, snatia_ext = %s
                            WHERE nim = %s"""
                    cursor.execute(query, (
                        self.wta[0], self.supremasi[0], self.snatia[0],
                        self.wta[1], self.supremasi[1], self.snatia[1], self.entry2.get()
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Data has been saved.")
                else:
                    query = """INSERT INTO kemahasiswaan (nim, nama_mahasiswa, angkatan_mahasiswa,
                                                        wta_mahasiswa, supremasi_mahasiswa, snatia_mahasiswa,
                                                        wta_ext, supremasi_ext, snatia_ext)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(query, (
                        self.entry2.get(), self.entry1.get(), self.entry3.get(),
                        self.wta[0], self.supremasi[0], self.snatia[0],
                        self.wta[1], self.supremasi[1], self.snatia[1]
                    ))
                    connection.commit()
                    messagebox.showinfo("Success", "Data has been saved.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Error: {e}")
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'connection' in locals() and connection.is_connected():
                    connection.close()
        else:
            file_path = filedialog.askopenfilename(title="Select a File")
            if file_path:
                with open(file_path, "rb") as file:
                    file_content = file.read()
                if item == 1:
                    self.wta = (file_content, file_path.split('.')[-1])  # Store content and extension
                elif item == 2:
                    self.supremasi = (file_content, file_path.split('.')[-1])
                elif item == 3:
                    self.snatia = (file_content, file_path.split('.')[-1])

if __name__ == "__main__":
    app = App()
    app.mainloop()
