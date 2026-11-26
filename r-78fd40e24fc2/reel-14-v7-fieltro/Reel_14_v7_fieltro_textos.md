# Reel 14 v7 · La llave del consultorio en fieltro · Doble verificación

Pasada de corrección de V-170, por orden directa de César (26/11/2026).
Estado: borrador para la revisión completa de Polimnia. No se publica ni se programa. El uso público de las filas 12, 13, 14, 23 y 24 depende de la prueba T140 del 30/11/2026 y de la confirmación escrita de Francis (A-022). Además hace falta el texto literal de César en la columna O.
ID de versión: Clío lo asigna en «Decisiones y acciones». Sustituye a la v6 (V-170).

## Qué cambia frente a la v6

1. Personajes (César):
   - La profesional lleva un uniforme de odontología de una pieza (enterizo) en fieltro verde salvia, con cuello mao, cremallera y bolsillo cosidos. Ya no lleva suéter.
   - La dueña del consultorio es una mujer joven, de pelo oscuro recogido en moño, con cárdigan gris verdoso, blusa crema y pantalón verde oscuro.
2. Letrero (César): el letrero «clinnio*» es una pieza de fieltro cosida a mano dentro del set. Las letras y el asterisco son aplicaciones de fieltro crema con volumen, borde recortado y puntada corrida visible, sobre el panel de fieltro verde con borde pespunteado. La forma sale de la máscara del logo auténtico, no se redibuja. No hay logo impreso ni digital encima de la escena. «Muy pronto en Caracas» va con el mismo acabado de letras cosidas. Lo mismo en la portada.
3. Ajustes de Polimnia sobre V-170:
   - Etiqueta completa: «Video y voz generados con IA» en pantalla durante toda la pieza y en el caption. El texto alternativo empieza por «Animación generada con IA, en estilo stop-motion de fieltro…». La etiqueta «Información de IA» de Instagram se activa al publicar (se anota en la fila).
   - El mostrador está en cuadro desde el primer cuadro. Se regeneraron las tres tomas con cámara fija: nada entra deslizándose ni tapa las piernas de la dueña.
   - Notas fijas: x fijo en las dos tomas (nota «Profesional» de x = 100 a 530 px; nota «Consultorio» de x = 550 a 980 px). Solo siguen la deriva vertical del mostrador, suavizada, sin saltos en los cortes de 8 y 16 s.
   - Tarjeta final «Únete a la lista de espera · enlace en la bio»: letra de 40 px, de x = 236 a 844 px (más de 90 px de margen), cosida al frente del mostrador. La dueña queda por debajo del letrero en todo el cierre; su pelo no tapa «en Caracas».
   - Etiquetas: una sola fila bajo el letrero, sobre el canto del mostrador (x = 161 a 919 px), lejos del espacio de respeto del logo, también durante el acercamiento. «Personajes ilustrativos» se ve en toda la pieza.
   - Portada: «Para profesionales y dueños de consultorios» en 32 px, de x = 155 a 925 px, dentro del margen de 90 px.
4. Subtítulos: misma franja de 1530 a 1618 px. Si una frase es muy ancha, la letra se reduce para que la píldora quede a 90 px o más de los bordes.

## Se mantiene

Estilo fieltro con rostros (excepción registrada para este estilo), voz de Carito, música de Pixabay de V-073 («Music Promotion No Copyright», MiroMaxMusic, pista 513944: https://pixabay.com/music/corporate-music-promotion-no-copyright-513944/), mismo guion y afirmaciones (filas 12, 13, 14, 23 y 24), la llave como objeto protagonista, acento lavanda #C4BBDD y «enlace en la bio» en #344C4C.

## Ficha técnica

- Archivo: Reel_14_v7_fieltro.mp4. 1080x1920, 30 fps, H.264 + AAC 48 kHz, 22,6 s, −14,0 LUFS, pico −1,4 dBFS.
- Producción: un cuadro inicial editado con IA desde la escena de la v6 (nuevo vestuario, nueva dueña, letrero en blanco) y tres tomas de 8 s con IA (Veo 3.1 Fast, sin audio), cada una desde el último cuadro de la anterior. La tercera se usa hasta 6,6 s. Acercamiento moderado digital de 1,00 a 1,05 entre 19,6 y 22,6 s.
- La pista de audio (voz de Carito y música, ya mezclada a −14 LUFS) es la misma de la v6, con los mismos tiempos.
- Letrero, notas, tarjeta, etiquetas y subtítulos: Python con ffmpeg (escena_v7.py y fieltro_logo.py). El letrero solo se ve sobre el fieltro verde del panel: si alguien pasa delante, lo tapa.

## Guion (una sola tensión: ¿el otro lado es quien dice ser?)

| Tiempo | Escena y acción | Voz |
|---|---|---|
| 0,0–3,4 s | Con el mostrador ya en cuadro, la profesional con uniforme de odontología llega con su credencial. La dueña espera junto a la puerta con la llave del llavero lavanda. El paciente aguarda en el banco. | ¿Quien está del otro lado es quien dice ser? |
| 3,4–8,0 s | La profesional deja su credencial en el mostrador y asiente. En la nota «Profesional» se marcan «Identidad» y «Credencial profesional», y aparece el sello «Verificada por Clinnio». | En Clinnio, verificamos identidad y credencial profesional. |
| 8,0–13,7 s | La dueña se acerca al mostrador. En la nota «Consultorio» se marcan «Identidad del dueño» y «Documentos del espacio», y aparece el sello «Verificado por Clinnio». | Y verificamos al consultorio y a su dueño: su identidad y los documentos del espacio. |
| 13,7–16,5 s | La dueña le extiende la llave y la profesional la recibe con las dos manos, sonriendo. | La reserva ocurre entre partes verificadas. |
| 16,5–19,6 s | La profesional camina con la llave hacia la puerta del consultorio; la dueña la señala y el paciente se levanta y la sigue. En el letrero aparece «Muy pronto en Caracas». | Muy pronto, en Caracas. |
| 19,6–22,6 s | La cámara se acerca un poco. Ella lleva la llave a la cerradura. En el frente del mostrador aparece la tarjeta cosida «Únete a la lista de espera · enlace en la bio». | Únete a la lista de espera. |

Afirmaciones (pestaña Afirmaciones), con la misma formulación de la v4 a la v6: filas 12 y 13 («En Clinnio, verificamos identidad y credencial profesional.»), filas 23 y 14 (lado del consultorio), fila 24 («La reserva ocurre entre partes verificadas») y fila 21 (solo «Muy pronto» y la lista de espera). Sin porcentajes, tarifas, Cashea ni pantallas. La llave es un recurso narrativo: no se afirma que Clinnio entregue llaves ni custodie accesos.

## Caption

¿Quien está del otro lado es quien dice ser?

En Clinnio, verificamos identidad y credencial profesional.

Y verificamos al consultorio y a su dueño: su identidad y los documentos del espacio. La reserva ocurre entre partes verificadas.

Muy pronto en Caracas. Únete a la lista de espera: enlace en la bio.

Video y voz generados con IA. Personajes ilustrativos.

#Clinnio #Caracas #Consultorios #Odontología #Psicología #Fisioterapia #Nutrición #SaludVenezuela

## Texto alternativo

Animación generada con IA, en estilo stop-motion de fieltro, con títeres de fieltro y lana en la recepción de un consultorio en Caracas, con el Ávila en la ventana. En la pared cuelga un letrero de fieltro verde cosido a mano con el logo de Clinnio en letras de fieltro. Una profesional de pelo rizado y lentes redondos, con uniforme de odontología verde, llega al mostrador y deja su credencial. En una nota cosida al mostrador se marcan su identidad y su credencial profesional, con el sello «Verificada por Clinnio». En otra nota se marcan la identidad del dueño y los documentos del espacio, con el sello «Verificado por Clinnio». La dueña del consultorio, una mujer joven de pelo recogido y cárdigan verde, le entrega una llave de fieltro con llavero lavanda. La profesional camina hacia la puerta del consultorio, seguida por un paciente que se levanta del banco. El letrero dice «Muy pronto en Caracas» y en el mostrador aparece una tarjeta cosida: «Únete a la lista de espera, enlace en la bio».

## Portada

Reel_14_v7_fieltro_portada.png, 1080x1920. La llave cruza de la dueña a la profesional sobre el mostrador, con el letrero de fieltro arriba y sin notas. Lleva «Para profesionales y dueños de consultorios» (32 px, de x = 155 a 925 px), la promesa «¿Es quien dice ser?» y las etiquetas «Video y voz generados con IA» y «Personajes ilustrativos» abajo a la izquierda, desde x = 90 px. Todo dentro de la zona segura (y 285 a 1635) y del recorte 3:4 de la grilla (y 240 a 1680). César la fija desde la app de Instagram.

## Prueba anti-parecido (frente a V-170 v6, V-168 v5 y V-167 v4)

- ¿Comparte posición de logo? Con la v6 sí (letrero colgado en la pared): es una corrección de la misma pieza, no una pieza nueva de la grilla. Frente a la v5 y la v4, no.
- ¿Comparte posición y peso del titular? No hay titular flotante.
- ¿Comparte estructura de bloques o tarjetas? Las notas del mostrador siguen, como en la v6, por pedido de continuidad.
- ¿Se distingue en la miniatura sin leer? Frente a la v4 y la v5, sí (fieltro con volumen). Sustituye a la v6, no convive con ella en la grilla.

## Puntos para la revisión

- En la toma B la dueña entrega la llave hacia los 11 a 12 s, un poco antes que en el guion de la v6 (13,7 s). La voz sigue con el lado del consultorio mientras tanto.
- En la toma B la dueña no deja un documento propio sobre el mostrador; la nota «Consultorio» lleva esa parte.
- Hacia el final de la toma C el paciente queda en parte detrás de la profesional.

## Herramienta

Generación de imagen y video con IA para la escena en fieltro (única vía para títeres de stop-motion en horas), la pista de audio de la v6 (ElevenLabs para Carito y Pixabay para la música) y Python con ffmpeg para el letrero cosido, notas, tarjeta, etiquetas y subtítulos. Descript no aplica: no hay grabación que editar.
