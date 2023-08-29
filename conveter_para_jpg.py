from PIL import Image
import os

def converter_png_para_jpg(caminho_png, caminho_jpg):
    try:
        imagem = Image.open(caminho_png)
        imagem_rgb = imagem.convert('RGB')
        imagem_rgb.save(caminho_jpg, quality=95)
        return True
    except Exception as e:
        print(f"Ops! Algo deu errado com a imagem {caminho_png}: {e}")
        return False

def processar_pasta(caminho_pasta):
    arquivos = os.listdir(caminho_pasta)
    pngs = [arquivo for arquivo in arquivos if arquivo.endswith('.png')]

    for png in pngs:
        caminho_png = os.path.join(caminho_pasta, png)
        caminho_jpg = os.path.join(caminho_pasta, png[:-3] + 'jpg')
        
        if converter_png_para_jpg(caminho_png, caminho_jpg):
            print(f"{png} foi transformado em JPG! Que maravilha!")
            # Apagando o PNG como quem limpa o prato após uma refeição saborosa
            os.remove(caminho_png)
            print(f"{png} foi apagado, deixando a cozinha limpa!")
        else:
            print(f"{png} não pôde ser convertido. Melhor deixar como está.")

# Testando a função na pasta desejada
caminho_pasta = 'coloque o caminho da pasta'  # Substitua pelo caminho da pasta onde estão os PNGs
processar_pasta(caminho_pasta)

print("Tudo em ordem, chef! As imagens PNG foram transformadas em JPGs e a cozinha está limpa!")
