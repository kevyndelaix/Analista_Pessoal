from models.registro_diario import RegistroDiario
from models.diario import Diario

f1 = RegistroDiario("12/09/2026", 7,1,3,3,0,70,50)
f2 = RegistroDiario("13/09/2026",5,1,4,3,0,71,0)

meu_diario = Diario()
meu_diario.add_ficha(f1)
meu_diario.add_ficha(f2)

print(len(meu_diario.registros))

