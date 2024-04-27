class instrucaoBinario: 
    def __init__(self):
        self.OPCODE = ""
        self.RD = ""
        self.RS1 = ""
        self.RS2 = ""
        self.IMEDIATO = ""
        self.BINARIO = ""
        self.FUNCT3 = ""
        self.FUNCT7 = ""
        
    def criarInstrucao(self, conteudo):
        return
    
    def deletarInstrucao(self):
        self = None
    
    def getOPCODE(self):
        return self.OPCODE
    
    def getRD(self):
        return self.RD
    
    def getRS1(self):
        return self.RS1
    
    def getRS2(self):
        return self.RS2
    
    def getIMEDIATO(self):
        return self.IMEDIATO
    
    def getBINARIO(self):
        return self.BINARIO
    
    def getFUNCT3(self):
        return self.FUNCT3
    
    def getFUNCT7(self):
        return self.FUNCT7
    
    def getprintBinario(numBinario):
        print(f"NUMERO BINARIO:  {numBinario}\n")
    
    def separarBinario(self, conteudo, rangeA ,RangeB):
        for linha in conteudo:
            binario = linha 
        x = range(rangeA,RangeB)
        numBinario =""
        for i in x:
            numBinario += binario[i]
        return numBinario
        
    def setOPCODE(self, conteudo):
        numBinario = self.separarBinario(conteudo, 25, 32)
        self.BINARIO = conteudo
        
        U = ["011011", "001011"]
        J = "1101111"
        I = ["1100111", "0010011", "0001111", "0000011", "1110011"] 
        B = "1100011"
        S = "0100011"
        R = "0110011"
        
        for x in U:
            if (numBinario == x):
                self.OPCODE = "U"
                
        for x in I:
            if (numBinario == x):
                self.OPCODE =  "I"

        if (numBinario == J):
            self.OPCODE = "J"
            
        elif (numBinario == B):
            self.OPCODE = "B"
            
        elif (numBinario == S):
            self.OPCODE = "S"
        elif (numBinario == R):
            self.OPCODE = "R"
            
    def setRD(self, conteudo):
        numBinario = self.separarBinario(conteudo, 20, 25)
        self.RD = numBinario
              
    def setFUNCT3(self, conteudo):
        numBinario = self.separarBinario(conteudo, 17, 20)
        
        if(self.OPCODE == "U" or self.OPCODE == "J"):
            aux = self.separarBinario(conteudo, 1, 22)
            self.FUNCT3 = aux
        else:
            self.FUNCT3 = numBinario
            
    def setRS1(self, conteudo):
        numerosBinario = self.separarBinario(conteudo, 12, 17)
        if(self.OPCODE == "U" or self.OPCODE == "J"):
            return
        else:
            self.RS1 = numerosBinario
        
    def setRS2(self, conteudo):
        numerosBinario = self.separarBinario(conteudo,7, 12)
        auxBinario = self.separarBinario(conteudo, 25, 32)
        aux2Binario = self.separarBinario(conteudo, 1,12 )
        
        if(auxBinario == "0010011" and self.FUNCT3 == "001" or self.FUNCT3 == "101" ):
            self.RS2 = numerosBinario 
            
        elif(self.OPCODE == "I"):
            self.IMEDIATO = aux2Binario
            
        elif(self.OPCODE == "B" or self.OPCODE == "S" or self.OPCODE == "R"):
            self.RS2 = numerosBinario

    def setIMEDIATO(self, conteudo):
        numerosBinario = self.separarBinario(conteudo,1, 7)
        if(self.OPCODE == "S" or self.OPCODE == "B" or self.OPCODE == "R"):
           self.IMEDIATO = numerosBinario 
        
        
        

        
"""
def separarBinario(conteudo):
    for linha in conteudo:
        print(linha)
        binario = linha  
        print("teste")
        print(binario +"\n")
       
        x = range(25,32)
        primeiraVerificacao =""
        for i in x:
            primeiraVerificacao += binario[i]
        print(primeiraVerificacao+"\n")
        op_code(primeiraVerificacao)
"""
vetorInstrucao = []
with open("binarioText.txt", "r") as arquivo:
    arquivoBinarios = arquivo.readlines()
    for linha in arquivoBinarios:
        print(linha)
        numerosBinarios = instrucaoBinario()
        #numerosBinarios.criarInstrucao(arquivoBinarios)
        numerosBinarios.setOPCODE(linha)
        numerosBinarios.setRD(linha)
        numerosBinarios.setFUNCT3(linha)
        numerosBinarios.setRS1(linha)
        numerosBinarios.setRS2(linha)
        numerosBinarios.setIMEDIATO(linha)
        vetorInstrucao.append(linha)
        numerosBinarios.deletarInstrucao()
"""""
vetorInstrucao = []

arquivoBinarios = open("binarioText.txt", "r")

for linha in arquivoBinarios: 
    print(linha)
    numerosBinarios = instrucaoBinario()
    #numerosBinarios.criarInstrucao(arquivoBinarios)
    numerosBinarios.setOPCODE(linha)
    numerosBinarios.setRD(linha)
    numerosBinarios.setFUNCT3(linha)
    numerosBinarios.setRS1(linha)
    numerosBinarios.setRS2(linha)
    numerosBinarios.setIMEDIATO(linha)
    vetorInstrucao.append(numerosBinarios)
    numerosBinarios.deletarInstrucao()
    


#separarBinario(conteudo)
"""""
arquivo.close()

print(f"OPCODE:{numerosBinarios.getOPCODE()}\nRD:{numerosBinarios.getRD()}\nFUCNT3:{numerosBinarios.getFUNCT3()}\nRS1:{numerosBinarios.getRS1()}\nRS2:{numerosBinarios.getRS2()}")
print(f"BINARIO:{numerosBinarios.getBINARIO()}\nIMEDIATO:{numerosBinarios.getIMEDIATO()}\nFUNCT7:{numerosBinarios.getFUNCT7()}\n")
#instrucao.getOPCODE(self)
