
print("-="* 100)
print("ALUGUEL DE VEICULOS")
print("-="* 100)

tipoDoVeiculo= str(input("O veiculo é carro ou moto? [C/M]")).upper().strip()

while tipoDoVeiculo not in "CM":
    tipoDoVeiculo = str(input("Somente Carro ou Moto, Tente novamente: [C/M] ")).upper().strip()

tipoDoVeiculoConta= 0

if tipoDoVeiculo == "M":
    tipoDoVeiculoConta= 0.15
if tipoDoVeiculo == "C":
    tipoDoVeiculoConta= 2.15


diasAlugado= int(input("Quantos dias foi alugado o veiculo? "))
kmRodados= int(input("Quantos km o veículo rodou? "))
diariaDoVeiculo= int(input("Quanto é a diaria do veiculo? "))


diasAlugadoConta= diasAlugado * diariaDoVeiculo
kmRodadosConta= kmRodados * tipoDoVeiculoConta
total= diasAlugadoConta + kmRodadosConta

print("-="* 100)
print(f"Você rodou {kmRodados}Km e ficou {diasAlugado} dias com o veiculo;")
print(f"Tipo do veiculo: {tipoDoVeiculo}")
print(f"P/Dia: R${diariaDoVeiculo}")
print(f"P/Km: R${tipoDoVeiculoConta}")
print(f"Total a pagar: R${total:.2f}")
print("-="* 100)
