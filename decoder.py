import hashlib
def unmatrix(l,k,t):
    tex=l[0]
    key=l[1]
    code=''
    for x in range(len(tex)):
        if tex[x] not in k[0]:
            code+=tex[x]
        else:
            l=tex[x]
            n=int(key[x])
            pos=k[n].index(l)
            let=t[pos]
            code+=let
    return code
def unpermutar(mat,h,v,f,c):
    per=list()
    for x in range(v):
        if x<v-c:
            col=x+c
        else:
            col=x-(v-c)
        l=str()
        for z in range(h):
            if z<h-f:
                let=z+f
            else:
                let=z-(h-f)
            l+=mat[col][0][let]
        per.append([l])
    tex=str()
    for lin in per:
        tex+=lin[0]
    return tex
def uncubex(tex,h,v,f,c):
    if len(tex)>h*v:
        tex=tex[0:h*v]
    mat=list()
    for x in range(v):
        mat.append([tex[x*h:(x+1)*h]])
    code=unpermutar(mat,h,v,f,c)
    return code
def limpieza(tex):#solo limpia el texto de elementos extras
    while tex[-1]=='-':
        tex=tex[0:len(tex)-1]
    return tex


otros=open("datos.txt","r")
t=otros.readline()
t0=otros.readline()
t1=otros.readline()
t2=otros.readline()
t3=otros.readline()
keys=otros.readline()
thash=otros.readline()
#keys es la clave entregada por la sustitución
#


txt=open("mensajeseguro.txt","r")
xet=txt.read()

#permutación inversa
cua=uncubex(xet,6,26,2,13)
tre=uncubex(cua,13,12,8,11)
dos=uncubex(tre,9,17,5,3)
uno=uncubex(dos,19,8,7,3)

#sustitución inversa
k=[t0,t1,t2,t3]
xet=uno
l=[xet,keys]
tex=unmatrix(l,k,t)



""" cambiar el mensaje aquí para comprobar integridad """
tex=limpieza(tex)




#hash
ha=hashlib.sha256()
ha.update(tex.encode())
has=ha.hexdigest()

if has==thash:
    inte='El mensaje es integro y su hash es: \n'+has
else:
    inte='el mensaje no es íntegro, hash diferentes'


print('______Texto recibido______')
print(xet,'\n')
print('______Decodificaciones de permutación______\n')
print('>>>'+cua+'\n\n>>>'+tre+'\n\n>>>'+dos+'\n\n>>>'+uno+'\n')
print('______Decodificación de sustitucion______\n')
print(tex+'\n')
print(inte)
