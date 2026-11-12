import sys; sys.path.insert(0,'/home/user/.perplexity/skills/user/editor-contenido-clinnio/scripts')
from crear_pieza import *
from PIL import Image, ImageDraw
W,H=1640,624
guias = len(sys.argv)>1
im=Image.new('RGB',(W,H),VERDE)
# asteriscos decorativos fuera de zona segura
m=Image.open(os.path.join(ASSETS,'asterisco_clinnio_mascara.png')).convert('RGBA').split()[3]
for (x,y,a,c) in [(-150,250,460,mezcla(VERDE,CELESTE,0.35)),(1340,-170,420,mezcla(VERDE,CELESTE,0.22))]:
    mm=m.resize((a,a),Image.LANCZOS); capa=Image.new('RGBA',(a,a),c+(255,)); capa.putalpha(mm); im.paste(capa,(x,y),capa)
d=ImageDraw.Draw(im)
sx,sy,sw,sh=220,82,1200,460
LW=280; logo(im, (W-LW)//2, sy+45, LW, CREMA)
f=fuente('SemiBold',54)
lineas=['Consultorios por hora para','profesionales de la salud en Caracas']
y=sy+160
for l in lineas:
    d.text(((W-d.textlength(l,font=f))/2,y),l,font=f,fill=CREMA); y+=72
fp=fuente('Medium',34)
pw=int(d.textlength('Muy pronto',font=fp))+48
pildora(im,((W-pw)//2,y+30),'Muy pronto',fp,CELESTE,VERDE,rel=24)
if guias:
    d.rectangle((sx,sy,sx+sw,sy+sh),outline=(255,0,0),width=3)
im.save('Portada_Facebook_Clinnio_v1%s.png'%('_guias' if guias else ''))
