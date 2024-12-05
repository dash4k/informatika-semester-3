import tkinter as tk
from algo import merge_sort, quick_sort, count_sort, bucket_sort


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Desain Analisis Algoritma")
        self.geometry("675x500")
        self.frames = {}

        for Page in (Main, Merge, Quick, Count, Bucket):
            frame = Page(parent=self, controller=self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class Main(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Dashboard", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 20

        button1 = tk.Button(self, text="MERGE SORT",
                            command=lambda: controller.show_frame(Merge),
                            pady=5,
                            width=button_width)
        button1.pack()
        label = tk.Label(self, text="")
        label.pack(pady=5)

        button2 = tk.Button(self, text="QUICK SORT",
                            command=lambda: controller.show_frame(Quick),
                            pady=5,
                            width=button_width)
        button2.pack()
        label1 = tk.Label(self, text="")
        label1.pack(pady=5)

        button3 = tk.Button(self, text="COUNT SORT",
                            command=lambda: controller.show_frame(Count),
                            pady=5,
                            width=button_width)
        button3.pack()
        label2 = tk.Label(self, text="")
        label2.pack(pady=5)

        button4 = tk.Button(self, text="BUCKET SORT",
                            command=lambda: controller.show_frame(Bucket),
                            pady=5,
                            width=button_width)
        button4.pack()


class Merge(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Merge Sort", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 20

        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        output_frame = tk.Frame(self)
        output_frame.pack(pady=40)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        entry_label = tk.Label(entry_frame, text="Enter an array of numbers (comma-separated):")
        entry_label.pack(side=tk.LEFT, padx=5)

        self.entry_field = tk.Entry(entry_frame)
        self.entry_field.pack(side=tk.LEFT, padx=5)

        sort_button = tk.Button(button_frame, text="Back to Dashboard",
                                command=lambda: controller.show_frame(Main),
                                pady=5,
                                width=button_width)
        sort_button.pack(side=tk.LEFT, padx=5)

        sort_button = tk.Button(button_frame, text="Sort",
                                command=self.perform_sort,
                                pady=5,
                                width=button_width)
        sort_button.pack(side=tk.LEFT, padx=5)

        output_label = tk.Label(output_frame, text="Output:")
        output_label.pack(side=tk.LEFT, padx=5)

        self.output = tk.Label(output_frame, text="", anchor="w", width=50)  
        self.output.pack(side=tk.LEFT, padx=5)

    def perform_sort(self):
        user_input = self.entry_field.get()
        try:
            array = list(map(float, user_input.split(',')))
            merge_sort(array)
            self.output.config(text=", ".join(map(str, array)))
        except ValueError:
            self.output.config(text="Invalid input! Please enter integers separated by commas.")


class Quick(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Quick Sort", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 20

        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        output_frame = tk.Frame(self)
        output_frame.pack(pady=40)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        entry_label = tk.Label(entry_frame, text="Enter an array of numbers (comma-separated):")
        entry_label.pack(side=tk.LEFT, padx=5)

        self.entry_field = tk.Entry(entry_frame)
        self.entry_field.pack(side=tk.LEFT, padx=5)

        sort_button = tk.Button(button_frame, text="Back to Dashboard",
                                command=lambda: controller.show_frame(Main),
                                pady=5,
                                width=button_width)
        sort_button.pack(side=tk.LEFT, padx=5)
        
        sort_button = tk.Button(button_frame, text="Sort",
                                command=self.perform_sort,
                                pady=5,
                                width=button_width)
        sort_button.pack(side=tk.LEFT, padx=5)

        output_label = tk.Label(output_frame, text="Output:")
        output_label.pack(side=tk.LEFT, padx=5)

        self.output = tk.Label(output_frame, text="", anchor="w", width=50)  
        self.output.pack(side=tk.LEFT, padx=5)

    def perform_sort(self):
        user_input = self.entry_field.get()
        try:
            array = list(map(float, user_input.split(',')))
            quick_sort(array)
            self.output.config(text=", ".join(map(str, array)))
        except ValueError:
            self.output.config(text="Invalid input! Please enter integers separated by commas.")


class Count(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Count Sort", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 20

        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        output_frame = tk.Frame(self)
        output_frame.pack(pady=40)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        entry_label = tk.Label(entry_frame, text="Enter an array of numbers (comma-separated):")
        entry_label.pack(side=tk.LEFT, padx=5)

        self.entry_field = tk.Entry(entry_frame)
        self.entry_field.pack(side=tk.LEFT, padx=5)

        sort_button = tk.Button(button_frame, text="Back to Dashboard",
                                command=lambda: controller.show_frame(Main),
                                pady=5,
                                width=button_width)
        sort_button.pack(side=tk.LEFT, padx=5)
        
        sort_button = tk.Button(button_frame, text="Sort",
                                command=self.perform_sort,
                                pady=5,
                                width=button_width)
        sort_button.pack(side=tk.LEFT, padx=5)

        output_label = tk.Label(output_frame, text="Output:")
        output_label.pack(side=tk.LEFT, padx=5)

        self.output = tk.Label(output_frame, text="", anchor="w", width=50)  
        self.output.pack(side=tk.LEFT, padx=5)

    def perform_sort(self):
        user_input = self.entry_field.get()
        try:
            array = list(map(float, user_input.split(',')))
            array = count_sort(array)
            self.output.config(text=", ".join(map(str, array)))
        except ValueError:
            self.output.config(text="Invalid input! Please enter integers separated by commas.")


class Bucket(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Bucket Sort", font=("Arial", 15))
        label.pack(pady=50)

        button_width = 20

        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        output_frame = tk.Frame(self)
        output_frame.pack(pady=40)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        entry_label = tk.Label(entry_frame, text="Enter an array of numbers (comma-separated):")
        entry_label.pack(side=tk.LEFT, padx=5)

        self.entry_field = tk.Entry(entry_frame)
        self.entry_field.pack(side=tk.LEFT, padx=5)

        sort_button = tk.Button(button_frame, text="Back to Dashboard",
                                command=lambda: controller.show_frame(Main),
                                pady=5,
                                width=button_width)
        sort_button.pack(side=tk.LEFT, padx=5)
        
        sort_button = tk.Button(button_frame, text="Sort",
                                command=self.perform_sort,
                                pady=5,
                                width=button_width)
        sort_button.pack(side=tk.LEFT, padx=5)

        output_label = tk.Label(output_frame, text="Output:")
        output_label.pack(side=tk.LEFT, padx=5)

        self.output = tk.Label(output_frame, text="", anchor="w", width=50)  
        self.output.pack(side=tk.LEFT, padx=5)

    def perform_sort(self):
        user_input = self.entry_field.get()
        try:
            array = list(map(float, user_input.split(',')))
            array = bucket_sort(array)
            self.output.config(text=", ".join(map(str, array)))
        except ValueError:
            self.output.config(text="Invalid input! Please enter integers separated by commas.")


if __name__ == "__main__":
    app = App()
    app.mainloop()
