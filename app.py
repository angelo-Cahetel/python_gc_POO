from models.restaurante import Restaurante

restaurante_CafeTG = Restaurante("CafeTG", "Cafeteria")
restaurante_CafeTG.receber_avaliacao("Angelo", 10)
restaurante_CafeTG.receber_avaliacao("Mayni", 9)


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()