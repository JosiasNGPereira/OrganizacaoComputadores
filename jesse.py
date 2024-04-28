def CPI(a,b):
    CPI = [5+1(25-1)]/25
    return CPI

def pipeline ():
    with open("binarioText.txt", "r") as arquivo:
        lineFile=len(arquivo)
        Tcpu = 25 * CPI(5, lineFile) * 5
        Tcpu2 = 38 * CPI(5, lineFile) * 5
        desempenho = Tcpu/Tcpu2
        print(f"Tempo CPU sem NOPs e:{Tcpu}")
        print(f"Tempo CPU adicionando NOPs e:{Tcpu2}")


        