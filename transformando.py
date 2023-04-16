numero= int(input('Digite um número:')) 

n= numero 

un= numero %10 

dz= (numero //10) %10 

cent=  (numero //100) %10 

milh= (numero//1000) %10 

print('o número é: {}'. format(n)) 

print('sua unidade é: {}'. format(un)) 

print('sua dezena é de: {}'. format(dz)) 

print('sua centena é de: {}'. format(cent)) 

print('sua milhar é de: {}'. format(milh)) 