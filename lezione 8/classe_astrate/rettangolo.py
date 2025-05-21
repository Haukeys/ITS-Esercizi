from formagenerica import Formagenerica

class Rettangolo(Formagenerica):

    #initialisation d un objet de la classe rettangolo
    def __init__(self):
        super().__init__()

        self.setShape('rettangolo')

    def draw(self):

        print(f"\n{self.getShape()}\n")

        #outer for
        for i in range(5):
            #inner for
            for j in range(5*2):

                # latto a e latto b del rettangolo
                if i==0 or i==5-1:
                    print("*",end=" ")
                # latto b e latto c del rettangolo
                elif j==0 or j==5*2-1:
                    print("*",end=" ")
                # spazi bianchi
                else:
                    print(" ", end=" ")
            print("\n", end="")

