from classe import Veiculo
from classeConta import Conta, Corrente, Poupanca, Salario

c1 = Corrente(12345)
c2 = Poupanca(24680)
c3 = Salario('11223')

print(c1.verSaldo())
print(c2.verSaldo())
print(c3.verSaldo())

print(c1.depositar(500))
print(c2.depositar(600))
print(c3.depositar(400))

print(c1.verSaldo())
print(c2.verSaldo())
print(c3.verSaldo())

print(c1.sacar(200))
print(c2.sacar(200))
print(c3.sacar(200))

print(c1.verSaldo())
print(c2.verSaldo())
print(c3.verSaldo())

# Implementar na conta Poupança um limite de saque R$ 500,00