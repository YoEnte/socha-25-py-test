class Rasse:

    bezeichnung: str

    def __init__(self, bezeichnung: str):
        self.bezeichnung = bezeichnung

    def __repr__(self) -> str:
        return self.bezeichnung

class Hund:

    name: str
    fellfarbe: str
    rasse: Rasse
    alter: int
    happines: int

    def __init__(self, name: str, farbe: str, rasse: Rasse, alter: int = 0) -> None:
        self.name = name
        self.fellfarbe = farbe
        self.rasse = rasse
        self.alter = alter
        self.happines = 100

    def altern(self) -> None:
        self.alter += 1

    def spielen(self, wert: int = 10) -> None:
        self.happines += wert;

    def istHappy(self) -> int:
        return self.happines
    
    def __repr__(self) -> str:
        return self.name + " ist ein " + self.fellfarbe + "er " + self.rasse.__repr__() + ", der schon " + str(self.alter) + " Jahre auf dem Buckel hat."


rasse1 = Rasse("Labrador");
schaefer = Rasse("Schäferhund")
print(schaefer)

timmi = Hund("Timmi", "schwarz", rasse1, 10)
print(timmi)
timmi.altern()
print(timmi)

print(timmi.istHappy())
timmi.spielen()
print(timmi.istHappy())
timmi.spielen(30)
print(timmi.istHappy())