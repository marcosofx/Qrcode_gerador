import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def gerar_qrcode(link, logo_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(link)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    logo = Image.open(logo_path)
    logo = logo.resize((80, 80))
    qr_img.paste(logo, (int((qr_img.size[0] - logo.size[0]) / 2), int((qr_img.size[1] - logo.size[1]) / 2)))

    filename = "qrcode_com_logo.png"
    qr_img.save(filename)

    return ImageTk.PhotoImage(Image.open(filename))

def gerar_link_e_qrcode():
    modelo = entry_modelo.get()
    serie = entry_serie.get()
    
    link_gerado = f"https://app.mcopy.com.br:8443/newdataservice/#/qrcode/{modelo}/{serie}"

    messagebox.showinfo("Link Gerado", f"Link: {link_gerado}")

    imagem_qrcode = gerar_qrcode(link_gerado, logo_path="C:/Users/OFICINASP00/OneDrive/Área de Trabalho/Lgerador/logo/logcenter.png")
    label_qrcode.config(image=imagem_qrcode)
    label_qrcode.image = imagem_qrcode
    

    janela.update_idletasks()

janela = tk.Tk()
janela.title("Gerador de Links e QR Code")

label_instrucao_modelo = tk.Label(janela, text="Digite o modelo:")
label_instrucao_modelo.pack(pady=10)

entry_modelo = tk.Entry(janela, width=30)
entry_modelo.pack(pady=10)

label_instrucao_serie = tk.Label(janela, text="Digite a série:")
label_instrucao_serie.pack(pady=10)

entry_serie = tk.Entry(janela, width=30)
entry_serie.pack(pady=10)

botao_gerar = tk.Button(janela, text="Gerar Link e QR Code", command=gerar_link_e_qrcode)
botao_gerar.pack(pady=20)

label_qrcode = tk.Label(janela)
label_qrcode.pack(pady=20)

janela.mainloop()