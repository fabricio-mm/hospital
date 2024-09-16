from triagem import*
from medico import*

triagem1 = Triagem()
a = triagem1.triagem()
b = triagem1.dar_pulseira()
medico1 = Medico()
if b == "vermelho" or b == "laranja":
    print(f'[{triagem1.nome}]: Encaminhando para o doutor!')
    doenca = medico1.diagnostico(b,a)
    medico1.receita(doenca)
    print("O paciente foi curado!")
    
else:
    print(f"[{medico1.nome}]: Encaminho paciente para o residente!")
    residente = Residente(b)
    diag_residente = residente.diagnostico()
    residente.receita(diag_residente)
    if diag_residente != medico1.diagnostico(b,a):
        ending = ["O paciente morreu 2 dias depois", 
                  f"{triagem1.a.nome}, ainda está com {medico1.diagnostico(b,a)} e chorando",
                  f"O estado de {triagem1.a.nome} agravou e ele(a) processou o hospital",
                  "O residente foi demitido"]
        print(random.choice(ending))
    else:
        print("O paciente melhorou")



