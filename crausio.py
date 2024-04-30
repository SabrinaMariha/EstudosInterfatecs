entrada1=input()
entrada2=input()
comandos=input()
entrada1Sep=entrada1.split(" ")
entrada2Sep=entrada2.split(" ")
linhas=int(entrada1Sep[0])
colunas=int(entrada1Sep[1])
bateria=int(entrada1Sep[2])
linhaICrausio=int(entrada2Sep[0])
colunaICrausio=int(entrada2Sep[1])
bateu=0;
crausio=[linhaICrausio,colunaICrausio];
for i in range(bateria):
    if comandos[i]=="C" or comandos[i]=="B":
        if comandos[i]=="C":
            if(linhaICrausio==1):
                bateu+=1
            else:
                linhaICrausio-=1

        if comandos[i]=="B":
            if(linhaICrausio==linhas):
                bateu+=1;
            else:
               linhaICrausio+=1

    if comandos[i]=="E" or comandos[i]=="D":
        if comandos[i]=="E":
            if(colunaICrausio==1):
                bateu+=1
            else:
                colunaICrausio-=1

        if comandos[i]=="D":
            if(colunaICrausio==colunas):
                bateu+=1
            else:
                colunaICrausio+=1
crausio[0]=linhaICrausio
crausio[1]=colunaICrausio
print(crausio[0]," ",crausio[1]," ",bateu)
