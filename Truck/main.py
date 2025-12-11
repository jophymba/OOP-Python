from truck import Truck

Volvo = Truck()

Volvo.naloz(10000) # nelze nalozit
Volvo.naloz(500)
Volvo.vyloz(300)
Volvo.vyloz(1000) # nelze vylozit

Volvo.vypis_nalozeni()