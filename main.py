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
        self.NOP = ""
        
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
    
    def separarBinario(self, conteudo, rangeA, rangeB):
        x = range(rangeA, rangeB)    
        numBinario =""
        for i in x:
            numBinario += conteudo[i]
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
 #Rascunho
 
"""
vetorInstrucao = [] 

with open("binarioText.txt", "r") as arquivo:
    arquivoBinarios = arquivo.readlines()
    for linha in arquivoBinarios:
        #print(linha)
        numerosBinarios = instrucaoBinario()
        numerosBinarios.setOPCODE(linha)
        #print(f"IDENTIFICACAO OP:{numerosBinarios.BINARIO}")
        numerosBinarios.setRD(linha)
        numerosBinarios.setFUNCT3(linha)
        numerosBinarios.setRS1(linha)
        numerosBinarios.setRS2(linha)
        numerosBinarios.setIMEDIATO(linha)
        vetorInstrucao.append(numerosBinarios)
        #numerosBinarios.deletarInstrucao()
        #print(f"Objeto limpo: {numerosBinarios.BINARIO}")
        
def mostrarVetor(vetorInstrucao,):
    for i in range(25):
        print(f"OPCODE: {vetorInstrucao[i].getOPCODE()}")
        print(f"RD: {vetorInstrucao[i].getRD()}")
        print(f"FUNCT3: {vetorInstrucao[i].getFUNCT3()}")
        print(f"RS1: {vetorInstrucao[i].getRS1()}")
        print(f"RS2: {vetorInstrucao[i].getRS2()}")
        print(f"IMEDIATO: {vetorInstrucao[i].getIMEDIATO()}")
        print(f"FUNCT7: {vetorInstrucao[i].getFUNCT7()}")
        print(f"BINARIO: {vetorInstrucao[i].getBINARIO()}")
     
def adicionarNOP(vetorInstrucao,auxVetorInstrucao):
    NOP = "00000000000000000000000000110011"
    x = len(vetorInstrucao)
    i = 0
    while i < x:
        auxVetorInstrucao.append(vetorInstrucao[i].getBINARIO())
        if i + 1 < x:
            if vetorInstrucao[i].getRD() == vetorInstrucao[i + 1].getRS1() or vetorInstrucao[i].getRD() == vetorInstrucao[i + 1].getRS2():
                auxVetorInstrucao.append(NOP+'\n')
                auxVetorInstrucao.append(NOP+'\n')
                i += 1
                continue

        if i + 2 < x:
            if vetorInstrucao[i].getRD() == vetorInstrucao[i + 2].getRS1() or vetorInstrucao[i].getRD() == vetorInstrucao[i + 2].getRS2():
                auxVetorInstrucao.append(NOP+'\n')
                i += 1
                continue

        i += 1

def mostrarVetorBinario(vetorInstrucao):
    x = len(vetorInstrucao)
    print(f"TAMANHO:{x}")
    for i in range(x):
        print(vetorInstrucao[i])
     
             
auxVetorInstrucao = []
#mostrarVetor(vetorInstrucao)
adicionarNOP(vetorInstrucao,auxVetorInstrucao)
#mostrarVetorBinario(auxVetorInstrucao)

with open("ResultadoBinario.txt", "w") as arquivo:
    for linha in auxVetorInstrucao:
        arquivo.write(linha)


arquivo.close()

time_clock=int(input("Digite o tempode clock:"))

def CPI(time_clock,line_count):
    time_clock+1
    line_count-1
    CPIobj = time_clock*line_count
    print(CPIobj)
    line_count
    resultado = CPIobj/line_count
    print(resultado)
    return resultado

def pipeline(time_clock):
    with open("binarioText.txt", "r") as arquivo:
          line_count = sum(1 for line in arquivo)
    with open("ResultadoBinario.txt", "r") as abc:
        line_count2 = sum(1 for line in abc)
        
    Tcpu = line_count * CPI(time_clock, line_count) * time_clock
    Tcpu2 = line_count2 * CPI(time_clock, line_count2) * time_clock
    desempenho = Tcpu / Tcpu2
    print(f"Tempo CPU sem NOPs: {Tcpu}")
    print(f"Tempo CPU adicionando NOPs: {Tcpu2}")
    print(f"Desempenho: {desempenho}")
   
    arquivo.close()
    abc.close()

    
pipeline(time_clock)



