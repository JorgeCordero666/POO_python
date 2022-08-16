# Tema: Herencia Multiple
class Telefono:
    def __init__(self):
        pass

    def llamar(self):
        print("Llamando...")

    def ocupado(self):
        print("Ocupado...")


class Camara:
    def __init__(self):
        pass

    def tomarFoto(self):
        print("tomando foto...")


class Repoduccion:
    def __init__(self) -> None:
        pass

    def reproducirMusica(self):
        print("Reproduciendo Musica")

    def reproducirVideo(self):
        print("Reproducir Video")


class SmartPhone(Telefono, Camara, Repoduccion):
    def __del__(self):
        print("Telefono Apagado")


movil = SmartPhone()
print(movil.tomarFoto())
print(movil.llamar())
print(movil.reproducirMusica())
