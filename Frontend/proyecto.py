import tkinter as tk
from tkinter import filedialog

class TextCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Compressor")
        
        # Title
        self.title_frame = tk.Frame(self.root)
        self.title_frame.pack(pady=100, padx= 200)
        
        self.title_label = tk.Label(self.title_frame, text="Comprimir-Python-proyecto", font=("Helvetica", 16))
        self.title_label.pack()
        
        self.subtitle_label = tk.Label(self.title_frame, text="Subtítulo", font=("Helvetica", 12))
        self.subtitle_label.pack()
        
        # Context
        self.context_frame = tk.Frame(self.root)
        self.context_frame.pack(pady=10)
        
        self.context_label = tk.Label(self.context_frame, text="Contexto breve", font=("Helvetica", 12))
        self.context_label.pack()
        
        # File upload section
        self.file_frame = tk.Frame(self.root)
        self.file_frame.pack(pady=10)
        
        self.upload_label = tk.Label(self.file_frame, text="Cargue su archivo txt", font=("Helvetica", 12))
        self.upload_label.grid(row=0, column=0, columnspan=2)
        
        self.browse_button = tk.Button(self.file_frame, text="Examinar directorio", command=self.browse_file)
        self.browse_button.grid(row=1, column=0)
        
        self.file_size_label = tk.Label(self.file_frame, text="Peso del archivo", font=("Helvetica", 12))
        self.file_size_label.grid(row=1, column=1)
        
        # Compression section
        self.compression_frame = tk.Frame(self.root)
        self.compression_frame.pack(pady=10)
        
        self.before_label = tk.Label(self.compression_frame, text="Antes de comprimir", font=("Helvetica", 12))
        self.before_label.grid(row=0, column=0)
        
        self.before_text = tk.Text(self.compression_frame, height=10, width=40)
        self.before_text.grid(row=1, column=0)
        
        self.after_label = tk.Label(self.compression_frame, text="Después de comprimir", font=("Helvetica", 12))
        self.after_label.grid(row=2, column=0)
        
        self.after_text = tk.Entry(self.compression_frame)
        self.after_text.grid(row=3, column=0)

    def centra(self,win,ancho,alto): 
        """ centra las ventanas en la pantalla """ 
        x = win.winfo_screenwidth() // 2 - ancho // 2 
        y = win.winfo_screenheight() // 2 - alto // 2 
        win.geometry(f'{ancho}x{alto}+{x}+{y}') 
        
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Display file size
            file_size = os.path.getsize(file_path)
            self.file_size_label.config(text=f"Peso del archivo: {file_size} bytes")
            # Load file content into before_text widget
            with open(file_path, 'r') as file:
                content = file.read()
                self.before_text.delete(1.0, tk.END)
                self.before_text.insert(tk.END, content)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextCompressorApp(root)
    root.mainloop()
