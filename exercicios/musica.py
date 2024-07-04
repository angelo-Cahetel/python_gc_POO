class Musica:
    musicas = []
    def __init__(self, nome,artista, genero):
        self.nome = nome
        self.artista = artista
        self.genero = genero
        Musica.musicas.append(self)

    def __str__(self):
        return f"{self.nome} | {self.artista}"
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f"{musica.nome} | {musica.artista} | {musica.genero}")


musica1 = Musica("Big black car", "Gregory Alan Isakov", "Folk")

musica2 = Musica("Folsom prision Blues", "Johnny Cash", "Country")

musica3 = Musica("Daisy", "Switchfoot", "Indie Rock")

Musica.listar_musicas()