class Piramide():
    def __init__(self):
        self.ast = "*"

    def trig(self, numero):
        for i in range(0, numero):
            print(self.ast)
            self.ast += "*"

def main():
    piramide = Piramide()
    piramide.trig(int(input("Ingrese su numero>> ")))

main()