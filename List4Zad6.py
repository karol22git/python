class Produkt:
    def __init__(self, nazwa: str, cena: float):
        self.nazwa = nazwa
        self.cena = cena

    def oblicz_cene_z_vat(self,vat: float):
        return self.cena + self.cena*vat  # Domyślnie VAT 23%
    
    def rabat(self,vat: float, r: float) -> float:
        if r>1 or r<0:
            return self.cena
        return (1-r)*self.oblicz_cene_z_vat(vat)

p = Produkt("x",100)
print(p.oblicz_cene_z_vat(0.23))
print(p.rabat(0.23,0.1))