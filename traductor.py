import re
import os
import sys


def conversion(m,lista,i,c): #lista es el cp
    if '@' in lista:
        listan=str(lista)
        idindex=listan.index('@')
        num=listan[idindex + 1:]
        lenOct = str(num)
        le = len(lenOct)
        octal = 0
        for i in (range(le)):
            octal = octal + int(lenOct[i])* pow(8, le-1)
            le -= 1
        b1n=int(octal)
        hext=bin(b1n)[2:]
        lecturalinea(m,lista,hext,i,c)
    elif '$' in lista:
        listan=str(lista)
        idindex=listan.index('$')
        num=listan[idindex + 1:]
        numero=(num)
        hext="{0:08b}".format(int(numero, 16))
        lecturalinea(m,lista,hext,i,c)
    elif '%' in lista:
        listan=str(lista)
        idindex=listan.index('%')
        num=listan[idindex + 1:]
        hext=num
        lecturalinea(m,lista,hext,i,c)
    else:
        listastr=str(lista)
        list_num = ([int(s) for s in re.findall(r'-?\d+\.?\d*', listastr)])
        strings = [str(integer) for integer in list_num]
        a_string = "". join(strings)
        num = int(a_string)
        hext=bin(num)[2:]
        lecturalinea(m,lista,hext,i,c)

def lecturalinea(ins,lista,hext,i,c): #ins parametro mnomico
    i=i+1
    num=str(hext)
    long = len(num)
    oper = (lista[0])
    if ins == 'ORG':
        if oper=='#':
            print('Funcion invalida')
        else:
            c=int(lista[1:])
            f = open ('prueba.lst','w')
            f.write('        '+ins+' '+lista +'\n')
            f.close()
            main(i,c)
    elif ins == 'ABA':
        if oper=='#':
            print('Funcion invalida')
        else:
            f = open ('prueba.lst','a')
            f.write('4002     ' + ins + '           INH           (LI=2) \n')
            f.close()
            main(i,c)
            
    elif ins == 'ABX':
        if long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'IDX 1A'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ABY':
        if long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
            else:
                mne= 'IDX 19'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ADCA':
        if long <= 24 and long > 16:
            mne= 'IDX2 A9'
            print(long)
            validacion(mne,lista,ins,long,num)
        elif long <= 16 and long > 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
            else:
                mne= 'EXT B9'
                validacion(mne,lista,ins,long,num,i,c)
        elif long<= 8:
            if oper=='#':
                mne= 'IMM 89'
                validacion(mne,lista,ins,long,num,i,c)
            else:
                mne= 'DIR 99'
                validacion(mne,lista,ins,long,num,i,c)
        else:
            print('Funcion invalida')
            os.system("pause")  
                 
    elif ins == 'ADCB':
        if long <= 24 and long > 16:
            mne= 'IDX2 E9'
            validacion(mne,lista,ins,long,num,i,c)
        elif long <= 16 and long > 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
            else:
                mne= 'EXT F9'
                validacion(mne,lista,ins,long,num,i,c)
        elif long<= 8:
            if oper=='#':
                mne= 'IMM C9'
                validacion(mne,lista,ins,long,num,i,c)
            else:
                mne= 'DIR D9'
                validacion(mne,lista,ins,long,num,i,c)
        else:
            mne= 'FUERA DE RANGO'
            validacion(mne,lista,ins,long,num,i,c)  
                 
    elif ins == 'ADDA':
        if long <= 24 and long > 16:
            mne= 'IDX2 AB'
            validacion(mne,lista,ins,long,num,i,c)
        elif long <= 16 and long > 8:
            if oper=='#':
                mne= 'FUERA DE RANGO'
                validacion(mne,lista,ins,long,num,i,c) 
                
            else:
                mne= 'EXT BB'
                validacion(mne,lista,ins,long,num,i,c)
        elif long<= 8:
            if oper=='#':
                mne= 'IMM 8B'
                validacion(mne,lista,ins,long,num,i,c)
            else:
                mne= 'DIR 9B'
                validacion(mne,lista,ins,long,num,i,c)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ADDB':
        if long <= 24 and long > 16:
            mne= 'IDX2 EB'
            validacion(mne,lista,ins,long,num)
        elif long <= 16 and long > 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'EXT FB'
                validacion(mne,lista,ins,long,num)
        elif long<= 8:
            if oper=='#':
                mne= 'IMM CB'
                validacion(mne,lista,ins,long,num)
            else:
                mne= 'DIR DB'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ADDD':
        if long <= 24 and long > 16:
            mne= 'IDX2 E3'
            validacion(mne,lista,ins,long,num)
        elif long <= 16 and long > 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'EXT F3'
                validacion(mne,lista,ins,long,num)
        elif long<= 8:
            if oper=='#':
                mne= 'IMM C3'
                validacion(mne,lista,ins,long,num,i,c)
            else:
                mne= 'DIR D3'
                validacion(mne,lista,ins,long,num,i,c)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ANDA':
        if long <= 24 and long > 16:
            mne= 'IDX2 A4'
            validacion(mne,lista,ins,long,num)
        elif long <= 16 and long > 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'EXT B4'
                validacion(mne,lista,ins,long,num)
        elif long<= 8:
            if oper=='#':
                mne= 'IMM 84'
                validacion(mne,lista,ins,long,num)
            else:
                mne= 'DIR 94'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ANDB':
        if long <= 24 and long > 16:
            mne= 'IDX2 E4'
            validacion(mne,lista,ins,long,num)
        elif long <= 16 and long > 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'EXT F4'
                validacion(mne,lista,ins,long,num)
        elif long<= 8:
            if oper=='#':
                mne= 'IMM C4'
                validacion(mne,lista,ins,long,num)
            else:
                mne= 'DIR D4'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ANDCC':
        if long<= 8:
            if oper=='#':
                mne= 'IMM 10'
                validacion(mne,lista,ins,long,num)
            else:
                print('Funcion invalida')
                os.system("pause")  
                
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ASL':
        if long <= 24 and long > 16:
            mne= 'IDX2 68'
            validacion(mne,lista,ins,long,num)
        elif long <= 16 and long > 8:
            if oper=='#':
                mne= 'FUERA DE RANGO'
                validacion(mne,lista,ins,long,num,i,c) 
            else:
                mne= 'EXT 78'
                validacion(mne,lista,ins,long,num)
        elif long<= 8:
            if oper=='#':
                f = open ('prueba.lst','a')
                f.write('4015     ' + ins + '#20        INH       58  (LI=2) \n')
                f.close()
                main(i,c)  
                
            else:
                mne= 'IDX 68'
                validacion(mne,lista,ins,long,num,i,c)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ASLD':
        if long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'INH 59'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'ASR':
        if long <= 24 and long > 16:
            mne= 'IDX2 67'
            validacion(mne,lista,ins,long,num)
        elif long <= 16 and long > 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'EXT 77'
                validacion(mne,lista,ins,long,num)
        elif long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'IDX 67'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'BCC':
        if long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                f = open ('prueba.lst','w')
                f.write('       '+ins+' '+lista +'\n'+lista[1:])
                f.close()
                main(i)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'BCLR':
        if long <= 32 and long > 24:
            mne= 'IDX2 0D'
            validacion(mne,lista,ins,long,num)
        elif long <= 24 and long > 16:
            mne= 'IDX1 0D'
            validacion(mne,lista,ins,long,num)
        elif long <= 16 and long > 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'DIR 4D'
                validacion(mne,lista,ins,long,num)
        elif long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                print('Funcion invalida')
                os.system("pause")  
                
        else:
            print('Funcion invalida')
            os.system("pause")  
                 
    elif ins == 'BCS':
        if long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'REL 25'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'BEQ':
        if long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'REL 27'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'BGE':
        if long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                mne= 'REL 2C'
                validacion(mne,lista,ins,long,num)
        else:
            print('Funcion invalida')
            os.system("pause")  
            
    elif ins == 'BGND':
        if long<= 8:
            if oper=='#':
                print('Funcion invalida')
                os.system("pause")  
                
            else:
                print('Funcion invalida')
                os.system("pause") 
                
        else:
            os.system("pause")  
    else:
        print('Funcion invalida')
        os.system("pause") 


def validacion(mne,hext,ins,long,num,i,c):
    if long <= 4:
        numero=str(num)
        b2=(hex(int(numero, 2)))
        b3=b2.split('x') 
        hex1=(b3[1])
        hexnum1='0' + hex1
        hexnum=str(hexnum1)
        resultado(mne,hext,hexnum,ins,i,c)
    elif long <= 8 and long>4:
        numero=str(num)
        b2=(hex(int(numero, 2)))
        b3=b2.split('x') 
        hexnum=(b3[1])
        resultado(mne,hext,hexnum,ins,i,c)
    elif long > 8 and long <= 16:
        h1=num[-12:-8]
        numerolong=len(h1)
        if numerolong<= 4:
            numero=str(num)
            b2=(hex(int(numero, 2)))
            b3=b2.split('x') 
            hex1=(b3[1])
            hexnum1='0' + hex1
            hexnum=str(hexnum1)
            resultado(mne,hext,hexnum,ins,i,c)
        else:
            numero=str(num)
            b2=(hex(int(numero, 2)))
            b3=b2.split('x') 
            hexnum=(b3[1])
            resultado(mne,hext,hext,hexnum,ins,i,c)
    elif long > 16 and long <= 24:
        h1=num[-20:-16]
        numerolong=len(h1)
        if numerolong<= 4:
            numero=str(num)
            b2=(hex(int(numero, 2)))
            b3=b2.split('x') 
            hex1=(b3[1])
            hexnum1='0' + hex1
            hexnum=str(hexnum1)
            resultado(mne,hext,hexnum,ins,i,c)
        else:
            numero=str(num)
            b2=(hex(int(numero, 2)))
            b3=b2.split('x') 
            hexnum=(b3[1])
            resultado(mne,hext,hexnum,ins,i,c)
    elif long > 24 and long <= 32:
        h1=num[-28:-24]
        numerolong=len(h1)
        if numerolong<= 4:
            numero=str(num)
            b2=(hex(int(numero, 2)))
            b3=b2.split('x') 
            hex1=(b3[1])
            hexnum1='0' + hex1
            hexnum=str(hexnum1)
            resultado(mne,hext,hexnum,ins,i,c)
        else:
            numero=str(num)
            b2=(hex(int(numero, 2)))
            b3=b2.split('x') 
            hexnum=(b3[1])
            resultado(mne,hext,hexnum,ins,i,c)
    else:
        print('Valor invalido, excede el los byte')

def resultado(mne,hext,hexnum,ins,i,c):
    div=(mne.split())
    md=(div[0])
    cp1="".join(div[1])
    cp=(cp1 + hexnum.upper())
    longhex=len(cp)/2
    longhex=int(longhex)
    c=str(c)
    f = open ('prueba.lst','a')
    f.write( '{:<9}{}{:<10}{:<10}{}(Li={})\n'.format(c,ins,hext,md,cp,longhex))
    f.close()
    c=int(c)
    c=(c+longhex)
    contador=str(c)
    contadors=len(contador)
    if contadors == 1:
        c='000' + str(c)
        main(i,c)
    elif contadors == 2:
        c='00' + str(c)
        main(i,c)
    else:
        main(i,c)









def main(i,c):
    mnemonico=['ORG','ABA','ADDD','ADCA','ADCB','BSZ','FILL','BGND','ADDA','START','DC.B','DC.W','FCC','FCB','END'] #Solo los mnemonico escritos aqui pueden ser validados
    valor_condicion='[0-9 A-F @ # % ,]' #Esta funcion valida que el codigo de operacion este escrito correctamente
    with open('P7.asm','r') as f:
        lineas = [linea.strip() for linea in f]
    for m in mnemonico:
        if re.search(m,lineas[i]):
            caja1=str(lineas[i])
            contcaja1=len(caja1.split()) #Es la cantidad de palabras de la linea
            if contcaja1==2:
                caja2=caja1.split()
                cp=caja2[1] # es el codigo de operacion
                if re.search(valor_condicion,cp):
                    if caja2[0]=='FILL':     #caja2[0] es el mnemonico
                        cpjunto=int(cp[2]) * str('0'+cp[0])
                        cp=int(cp[2]) * str(' 0'+cp[0]) #Se multiplica el primer valor por el segundo y agrega 0
                        chex=hex(c)
                        chex=chex[2:]
                        f = open ('prueba.lst','a')
                        f.write('00{:<6}{}\n'.format(chex,cp))
                        f.close()
                        i=i+1
                        c=int(c)
                        contador=len(cpjunto)/2
                        contador=int(contador)
                        c=c+contador
                        main(i,c)
                    elif caja2[0]=='DC.B':     #caja2[0] es el mnemonico
                        if ',' in cp:
                            cplist=[]
                            cplist.append(cp[0:2])
                            cplist.append(cp[3:5])
                            cpjunto = "". join(cplist) #cp junto para modificarlo
                            cp = " ". join(cplist) #cp codigo de operacion para bloc de notas
                            chex=hex(c)
                            chex=chex[2:]
                            f = open ('prueba.lst','a')
                            f.write('000{:<6}{}\n'.format(chex,cp))
                            f.close()
                            i=i+1
                            c=int(c)
                            contador=len(cpjunto)/2
                            contador=int(contador)
                            c=c+contador
                            main(i,c)
                        else:
                            chex=hex(c)
                            chex=chex[2:]
                            f = open ('prueba.lst','a')
                            f.write('000{:<6}{}\n'.format(chex,cp))
                            f.close()
                            i=i+1
                            c=int(c)
                            contador=len(cp)/2
                            contador=int(contador)
                            c=c+contador
                            main(i,c)
                    elif caja2[0]=='FCB':
                        chex=hex(c)
                        chex=chex[2:]
                        f = open ('prueba.lst','a')
                        f.write('00{:<6}{}\n'.format(chex,cp))
                        f.close()
                        i=i+1
                        c=int(c)
                        contador=len(cp)/2
                        contador=int(contador)
                        c=c+contador                            
                        main(i,c)
                    elif caja2[0]=='BSZ':     #caja2[0] es el mnemonico
                        cpjunto='00'*int(cp)
                        cp='00 '*int(cp)
                        chex=hex(c)
                        chex=chex[2:]
                        f = open ('prueba.lst','a')
                        f.write('000{:<6}{}\n'.format(chex,cp))
                        f.close()
                        c=int(c)
                        contador=len(cpjunto)/2
                        contador=int(contador)
                        c=c+contador
                        i=i+1
                        main(i,c)
                          
                    elif caja2[0]=='DC.W':     #caja2[0] es el mnemonico
                        cpjunto='000' + cp[0] + '000' + cp[2]
                        cp='000' + cp[0] + ' 000' + cp[2]
                        chex=hex(c)
                        chex=chex[2:]
                        f = open ('prueba.lst','a')
                        f.write('00{:<6}{}\n'.format(chex,cp))
                        f.close()
                        i=i+1
                        c=int(c)
                        contador=len(cpjunto)/2
                        contador=int(contador)
                        c=c+contador
                        main(i,c)
                    elif caja2[0]=='FCC':     #caja2[0] es el mnemonico
                        if '/' in cp:
                            cp=cp[1:5]
                            cpjunto=cp.encode("utf-8").hex()
                            cp=cp.encode("utf-8").hex(' ')
                            chex=hex(c)
                            chex=chex[2:]
                            f = open ('prueba.lst','a')
                            f.write('00{:<6}{}\n'.format(chex,cp))
                            f.close()
                            i=i+1
                            c=int(c)
                            contador=len(cpjunto)/2
                            contador=int(contador)
                            c=c+contador
                            main(i,c)

                        else:
                            conversion(m,cp,i,c)
                    else:
                        conversion(m,cp,i,c)
                else:
                    print('no esta')
            elif contcaja1==1:
                if caja1=='START':
                    f = open ('prueba.lst','a')
                    f.write('{:<9}{}\n'.format(c,caja1))
                    f.close()
                    c='0000'
                    i=i+1
                    main(i,c)
                elif caja1== 'DC.B':
                    caja1='00'
                    f = open ('prueba.lst','a')
                    f.write('{:<9}{}\n'.format(c,caja1))
                    f.close()
                    i=i+1
                    c=int(c)
                    contador=len(caja1)/2
                    contador=int(contador)
                    c=c+contador
                    main(i,c)
                elif caja1== 'DC.W':
                    caja1='0000'
                    chex=hex(c)
                    chex=chex[2:]
                    f = open ('prueba.lst','a')
                    f.write('00{:<6}{}\n'.format(chex,caja1))
                    f.close()
                    i=i+1
                    c=int(c)
                    contador=len(caja1)/2
                    contador=int(contador)
                    c=c+contador
                    main(i,c)
                elif caja1== 'END':
                    chex=hex(c)
                    chex=chex[2:]
                    f = open ('prueba.lst','a')
                    f.write('00{:<6}{}\n'.format(chex,caja1))
                    f.close()
            break
c=0
i=0
main(i,c)