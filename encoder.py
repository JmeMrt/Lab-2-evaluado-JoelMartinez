import hashlib

def matrix(l,k,t):
    abc=l[0]
    num=l[1]
    key=k
    tex=t
    code=str()
    k=''
    for x in range(len(tex)):
        if tex[x] not in abc:
            k+='-'
            code+=tex[x]
        else:
            p=int(abc.index(tex[x]))
            l=int(num[p])
            w=key[l][p]
            k+=num[p]
            code+=w
    return code, k
def permutar(mat,h,v,f,c):
    per=list()
    for x in range(v):
        if x<c:
            col=v-(c-x)
        else:
            col=x-c
        l=str()
        for z in range(h):
            if z<f:
                let=h-(f-z)
            else:
                let=z-f
            l+=mat[col][0][let]
        per.append([l])
    tex=str()
    for lin in per:
        tex+=lin[0]
    return tex
def cubex(tex,h,v,f,c):
    if len(tex ) > h*v:
        print('La multiplicación entre los números debe ser de al menos '+str(len(tex))+'\n')
        return
    else:
        if len(tex) < h*v:
            tex+=str((h*v-len(tex))*'-')
        mat=list()
        for x in range(v):
            mat.append([tex[x*h:(x+1)*h]])
        code=permutar(mat,h,v,f,c)
        return code

# --> t es un string con las letras del abecedario
# --> t0 t1 t2 t3 son string con el abecedario desordenado
# --> n es un string con numeros al azar, que van desde 0
#     hasta cuanos t_n existan menos 1 (0 - 3), un numero por cada letra
t= 'abcdefghijklmnñopqrstuvwxyz'
t0='erafdvugkicoxswhñntlympqzbj'
t1='qfgrmytkvbnlzoexscawdihpñuj'
t2='xibvoufqtcdzgeñkwmapjyslhrn'
t3='nygtwsbñxdhvreliqouzjcapkfm'
n= '021323013203120321023021303'
l=[t,n]
k=[t0,t1,t2,t3]

txt=open('mensajedeentrada.txt','r')
tex=txt.read()

#----hast
ha=hashlib.sha256()
ha.update(tex.encode())
has=ha.hexdigest()

#----sustitución
un=matrix(l,k,tex)
code=un[0]
keys=un[1]

#----permutación
uno=cubex(code,19,8,7,3)
dos=cubex(uno,9,17,5,3)
tre=cubex(dos,13,12,8,11)
cua=cubex(tre,6,26,2,13)

print('______Texto original______')
print(tex+'\n')
print('______Sustitución______\n')
print('>>>'+code+'\n')
print('______Permutaciones______\n')
print('>>>'+uno+'\n\n>>>'+dos+'\n\n>>>'+tre+'\n\n>>>'+cua+'\n\n______Texto resultado______')
print(cua)



cif=open("mensajeseguro.txt","w")
cif.write(cua)
cif.close()

otros=open("datos.txt","w")
otros.write(t+'\n')
otros.write(t0+'\n')
otros.write(t1+'\n')
otros.write(t2+'\n')
otros.write(t3+'\n')
otros.write(keys+'\n')
otros.write(has)
otros.close()
