import tkinter as tk

def calcular_tempo_animacao():
    try:
        fps = int(entry_fps.get())
        total_frames = int(entry_frames.get())
        
        if fps <= 0 or total_frames <= 0:
            resultado_label.config(text="FPS and Frames must be greater than zero.")
            return
        
        tempo_por_frame = 1 / fps
        duracao_total = total_frames * tempo_por_frame
        
        resultado_label.config(text=f"Time per Frame: {round(tempo_por_frame, 4)} seg\nTotal Animation Time: {round(duracao_total, 4)} seg")
    except ValueError:
        resultado_label.config(text="Enter a valid valor.")

# Configuração da interface
tk_root = tk.Tk()
tk_root.title("Spriteframe Time Calculator")
tk_root.geometry("400x250")
tk_root.iconbitmap("icon.ico")

tk.Label(tk_root, text="FPS:").pack(pady=5)
entry_fps = tk.Entry(tk_root)
entry_fps.pack(pady=5)

tk.Label(tk_root, text="Total Frames:").pack(pady=5)
entry_frames = tk.Entry(tk_root)
entry_frames.pack(pady=5)

botao_calcular = tk.Button(tk_root, text="Calculate", command=calcular_tempo_animacao)
botao_calcular.pack(pady=10)

resultado_label = tk.Label(tk_root, text="")
resultado_label.pack(pady=10)

tk_root.mainloop()
