dados = {
"ID"       : "19297",  
"nome"     : "Victor Bonomi",
"CPF"      : "1122334455",
"telefone" : "96039998",
"email"    : "vbonomi14@gmail.com "
} 
for x in dados.values():
    print("Dados: ",x) 
dados ["endereço"] = "Boa Vista"
dados ["sexo"]     = "Maculno" 
for x in dados:
    print(x +":",dados[x])