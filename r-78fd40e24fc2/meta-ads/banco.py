import sys, os, json
sys.path.insert(0,'/home/user/.perplexity/skills/user/editor-contenido-clinnio/scripts')
from crear_pieza import fuente, mezcla, logo, asterisco, pildora, envolver, VERDE, CELESTE, CREMA, GRIS
from PIL import Image, ImageDraw
FONDOS={'verde':VERDE,'crema':CREMA,'celeste':CELESTE,'mostaza':(227,193,111),'terracota':(229,171,146),'lavanda':(196,187,221),'salvia':(169,190,155)}
# zonas seguras: 9:16 Reels de Meta (arriba 14 %, abajo 35 %, lados 6 %); 1:1 y 4:5 con margen de 7 %
FMT={'1x1':(1080,1080,(76,76,76,76)),'4x5':(1080,1350,(76,80,76,80)),'9x16':(1080,1920,(72,280,72,680))}
def pieza(s, fmt, out, guias=False):
    W,H,(ml,mt,mr,mb)=FMT[fmt]
    fn=s['fondo']; bg=FONDOS[fn]; verde=fn=='verde'
    tinta=CREMA if verde else VERDE; acento=CELESTE
    im=Image.new('RGB',(W,H),bg)
    col=mezcla(bg, CREMA if verde else (255,255,255), 0.07 if verde else 0.22)
    asterisco(im, s.get('asterisco','der'), col, int(W*1.05))
    d=ImageDraw.Draw(im)
    ancho=W-ml-mr; top=mt; bot=H-mb
    LW={'1x1':230,'4x5':250,'9x16':250}[fmt]
    logo(im, ml, top, LW, CREMA if verde else VERDE)
    y=top+ (95 if fmt!='9x16' else 105)
    # pie reservado
    fp=fuente('Bold',36); pie=s.get('pie','Muy pronto en Caracas')
    pie_h=88; nota_h=46 if s.get('nota') else 0
    limite=bot-pie_h-nota_h-24
    tam={'1x1':100,'4x5':108,'9x16':104}[fmt]
    lineas=s['lineas']
    while True:
        f=fuente('ExtraBold',tam)
        if all(d.textlength(l,font=f)<=ancho-30 for l in lineas): break
        tam-=4
    fc=fuente('SemiBold',38 if fmt=='1x1' else 40)
    cuerpo=envolver(d,s['cuerpo'],fc,ancho) if s.get('cuerpo') else []
    bloques=(80 if s.get('etiqueta') else 0)+int(len(lineas)*tam*1.2)+20+(int(len(cuerpo)*fc.size*1.4)+24 if cuerpo else 0)
    while y+bloques>limite and tam>64:
        tam-=4; f=fuente('ExtraBold',tam); bloques=(80 if s.get('etiqueta') else 0)+int(len(lineas)*tam*1.2)+20+(int(len(cuerpo)*fc.size*1.4)+24 if cuerpo else 0)
    if y+bloques>limite: raise SystemExit(f"{s['id']} {fmt}: no cabe")
    y+=int((limite-y-bloques)*0.4)
    if s.get('etiqueta'):
        pildora(im,(ml,y),s['etiqueta'].upper(),fuente('Bold',30),CELESTE if verde else VERDE,VERDE if verde else CREMA,rel=28); y+=80
    for i,l in enumerate(lineas,1):
        if s.get('clave')==i and not verde:
            w=int(d.textlength(l,font=f))+56
            capa=Image.new('RGBA',(w+20,int(tam*1.3)),(0,0,0,0)); cd=ImageDraw.Draw(capa)
            cd.rounded_rectangle((10,4,w+10,int(tam*1.25)),30,fill=VERDE); cd.text((38,int(tam*0.02)),l,font=f,fill=CREMA)
            capa=capa.rotate(1.2,resample=Image.BICUBIC,expand=True); im.paste(capa,(ml-28,y-8),capa)
        else:
            d.text((ml,y),l,font=f,fill=acento if (s.get('clave')==i and verde) else tinta)
        y+=int(tam*1.2)
    y+=20
    for l in cuerpo:
        d.text((ml,y),l,font=fc,fill=tinta); y+=int(fc.size*1.4)
    w=int(d.textlength(pie,font=fp))+96; py=bot-nota_h-pie_h
    d.rounded_rectangle((ml,py,ml+w,py+pie_h),44,fill=CREMA if verde else VERDE)
    d.text((ml+48,py+18),pie,font=fp,fill=VERDE if verde else CREMA)
    if s.get('nota'):
        d.text((ml,bot-34),s['nota'],font=fuente('Medium',26),fill=tinta)
    if guias:
        d.rectangle((ml,mt,W-mr,H-mb),outline=(255,0,90),width=4)
    os.makedirs(out,exist_ok=True)
    p=os.path.join(out,f"{s['id']}_{fmt}{'_guias' if guias else ''}.png"); im.save(p,optimize=True); return p
if __name__=='__main__':
    specs=json.load(open('banco.json',encoding='utf-8'))
    g='--guias' in sys.argv
    for s in specs:
        for fmt in FMT: print(pieza(s,fmt,'guias' if g else 'out',g))
