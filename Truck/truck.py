class Truck:
     max_zatizeni = 3000
     hmotnost_nakladu = 0

     def naloz(self, hmotnost):
          if self.hmotnost_nakladu + hmotnost <= self.max_zatizeni:
               self.hmotnost_nakladu += hmotnost

     def vyloz(self, hmotnost):
          if hmotnost <= self.hmotnost_nakladu:
               self.hmotnost_nakladu -= hmotnost

     def vypis_nalozeni(self):
          print(f"V trucku je nalozeno {self.hmotnost_nakladu} kg")                    


     