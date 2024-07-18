import tkinter as tk
from tkinter import filedialog, ttk
from collections import Counter
import os

# Funciones de backend

def fibonacci_sequence_up_to(n):
    sequence = [1, 2]
    while sequence[-1] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    if sequence[-1] > n:
        sequence.pop()
    return sequence

def encode_fibonacci(n):
    if n == 0:
        return '11'
    fibonacci = fibonacci_sequence_up_to(n)[::-1]
    result = []
    for f in fibonacci:
        if f <= n:
            result.append('1')
            n -= f
        else:
            result.append('0')
    result = result[::-1]
    result.append('1')
    return ''.join(result)

def decode_string(cadena, probabilidades_ordenadas):
    buscador = ""
    cadena_auxiliar = []
    for i in cadena:
        buscador += i
        for simbolo, (_, codificacion_fibonacci, _) in probabilidades_ordenadas.items():
            if buscador == codificacion_fibonacci:
                buscador = ""
                cadena_auxiliar.append(simbolo)
    return "".join(cadena_auxiliar)

def encode_string(cadena, probabilidades_ordenadas):
    resultado = ""
    for i in cadena:
        for simbolo, (_, codificacion_fibonacci, _) in probabilidades_ordenadas.items():
            if i == simbolo:
                resultado += codificacion_fibonacci
    return resultado

def contar_simbolos(cadena):
    return Counter(cadena)

def preparar_probabilidades(cadena):
    resultado = contar_simbolos(cadena)
    probabilidades = {}
    longitud_cadena = len(cadena)
    for simbolo, cuenta in resultado.items():
        probabilidad = cuenta / longitud_cadena
        probabilidades[simbolo] = probabilidad
    probabilidades_ordenadas = dict(sorted(probabilidades.items(), key=lambda item: item[1], reverse=True))
    cont = 1
    for simbolo in probabilidades_ordenadas:
        probabilidad = probabilidades_ordenadas[simbolo]
        codificacion_fibonacci = encode_fibonacci(cont)
        probabilidades_ordenadas[simbolo] = (probabilidad, codificacion_fibonacci, cont)
        cont += 1
    return probabilidades_ordenadas

# Clase de la interfaz

class TextCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Compressor")
        
        # Estilos
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12))
        
        # Title
        self.title_frame = ttk.Frame(self.root)
        self.title_frame.pack(pady=10)
        
        self.title_label = ttk.Label(self.title_frame, text="Comprimir-Python-proyecto", font=("Helvetica", 16))
        self.title_label.pack()
        
        self.subtitle_label = ttk.Label(self.title_frame, text="Proyecto de compresión de texto usando codificación Fibonacci", font=("Helvetica", 12))
        self.subtitle_label.pack()
        
        # Context
        self.context_frame = ttk.Frame(self.root)
        self.context_frame.pack(pady=10)
        
        self.context_label = ttk.Label(self.context_frame, text="Esta aplicación permite comprimir y descomprimir textos utilizando la codificación Fibonacci.", font=("Helvetica", 12))
        self.context_label.pack()
        
        # File upload section
        self.file_frame = ttk.Frame(self.root)
        self.file_frame.pack(pady=10)
        
        self.upload_label = ttk.Label(self.file_frame, text="Cargue su archivo txt", font=("Helvetica", 12))
        self.upload_label.grid(row=0, column=0, columnspan=2)
        
        self.browse_button = ttk.Button(self.file_frame, text="Examinar directorio", command=self.browse_file)
        self.browse_button.grid(row=1, column=0, padx=5)
        
        self.file_size_label = ttk.Label(self.file_frame, text="Peso del archivo", font=("Helvetica", 12))
        self.file_size_label.grid(row=1, column=1, padx=5)
        
        # Horizontal compression and decompression section
        self.horizontal_frame = ttk.Frame(self.root)
        self.horizontal_frame.pack(pady=10)
        
        self.before_frame = ttk.Frame(self.horizontal_frame)
        self.before_frame.grid(row=0, column=0, padx=5)
        
        self.before_label = ttk.Label(self.before_frame, text="Antes de comprimir", font=("Helvetica", 12))
        self.before_label.pack()
        
        self.before_text = tk.Text(self.before_frame, height=20, width=40, font=('Helvetica', 10))
        self.before_text.pack(pady=5)
        
        self.compress_button = ttk.Button(self.before_frame, text="Comprimir", command=self.compress_text)
        self.compress_button.pack(pady=5)
        
        self.after_frame = ttk.Frame(self.horizontal_frame)
        self.after_frame.grid(row=0, column=1, padx=5)
        
        self.after_label = ttk.Label(self.after_frame, text="Después de comprimir", font=("Helvetica", 12))
        self.after_label.pack()
        
        self.after_text = tk.Text(self.after_frame, height=20, width=40, font=('Helvetica', 10))
        self.after_text.pack(pady=5)
        
        self.decompress_button = ttk.Button(self.after_frame, text="Descomprimir", command=self.decompress_text)
        self.decompress_button.pack(pady=5)
        
        self.decompressed_frame = ttk.Frame(self.horizontal_frame)
        self.decompressed_frame.grid(row=0, column=2, padx=5)
        
        self.decompressed_label = ttk.Label(self.decompressed_frame, text="Texto descomprimido", font=("Helvetica", 12))
        self.decompressed_label.pack()
        
        self.decompressed_text = tk.Text(self.decompressed_frame, height=20, width=40, font=('Helvetica', 10))
        self.decompressed_text.pack(pady=5)
        
        # File size labels with scrollbars
        self.compressed_file_size_frame = ttk.Frame(self.root)
        self.compressed_file_size_frame.pack(pady=10, fill=tk.X, expand=True)
        
        self.compressed_file_size_label = ttk.Label(self.compressed_file_size_frame, text="Peso del archivo comprimido", font=("Helvetica", 12))
        self.compressed_file_size_label.pack(side=tk.LEFT)
        
        self.compressed_file_size_text = tk.Text(self.compressed_file_size_frame, height=2, font=('Helvetica', 10), wrap=tk.WORD)
        self.compressed_file_size_text.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        
        self.decompressed_file_size_frame = ttk.Frame(self.root)
        self.decompressed_file_size_frame.pack(pady=10, fill=tk.X, expand=True)
        
        self.decompressed_file_size_label = ttk.Label(self.decompressed_file_size_frame, text="Peso del archivo descomprimido", font=("Helvetica", 12))
        self.decompressed_file_size_label.pack(side=tk.LEFT)
        
        self.decompressed_file_size_text = tk.Text(self.decompressed_file_size_frame, height=2, font=('Helvetica', 10), wrap=tk.WORD)
        self.decompressed_file_size_text.pack(side=tk.RIGHT, fill=tk.X, expand=True)
    
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_size = os.path.getsize(file_path)
            self.file_size_label.config(text=f"Peso del archivo: {file_size} bytes")
            with open(file_path, 'r') as file:
                content = file.read()
                content_fixed = content.replace("\n", "\\n")
                self.before_text.delete(1.0, tk.END)
                self.before_text.insert(tk.END, content_fixed)
    
    def compress_text(self):
        text = self.before_text.get(1.0, tk.END).strip()
        probabilidades_ordenadas = preparar_probabilidades(text)
        encoded_text = encode_string(text, probabilidades_ordenadas)
        self.after_text.delete(1.0, tk.END)
        self.after_text.insert(tk.END, encoded_text)
        
        # Calcular el peso comprimido en bytes
        bits_count = len(encoded_text)
        bytes_count = (bits_count + 7) // 8  # Redondea hacia arriba
        self.compressed_file_size_text.delete(1.0, tk.END)
        self.compressed_file_size_text.insert(tk.END, f"Peso del archivo comprimido: {bytes_count} bytes")
    
    def decompress_text(self):
        encoded_text = self.after_text.get(1.0, tk.END).strip()
        probabilidades_ordenadas = preparar_probabilidades(self.before_text.get(1.0, tk.END).strip())
        decoded_text = decode_string(encoded_text, probabilidades_ordenadas)
        self.decompressed_text.delete(1.0, tk.END)
        self.decompressed_text.insert(tk.END, decoded_text)
        
        # Calcular el peso descomprimido en bytes
        decompressed_size = len(decoded_text.encode('utf-8'))
        self.decompressed_file_size_text.delete(1.0, tk.END)
        self.decompressed_file_size_text.insert(tk.END, f"Peso del archivo descomprimido: {decompressed_size} bytes")

# Main loop
root = tk.Tk()
app = TextCompressorApp(root)
root.mainloop()
