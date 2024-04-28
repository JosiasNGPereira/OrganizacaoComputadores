
time_clock=input("Digite o tempode clock:")

def CPI(time_clock,line_count):
    CPIobj = (time_clock+1*(line_count-1))/line_count
    return CPIobj

def pipeline(time_clock):
    with open("binarioText.txt", "r") as arquivo:
         line_count= len(arquivo)
    with open("ResultadoBinario.txt", "r") as arquivo2:
        line_count2= len(arquivo2)
   
    Tcpu = line_count * CPI(time_clock, line_count) * time_clock
    Tcpu2 = line_count2 * CPI(time_clock, line_count2) * time_clock
    desempenho = Tcpu / Tcpu2
    print(f"Tempo CPU sem NOPs: {Tcpu}")
    print(f"Tempo CPU adicionando NOPs: {Tcpu2}")
    print(f"Desempenho: {desempenho}")

pipeline(time_clock)


        