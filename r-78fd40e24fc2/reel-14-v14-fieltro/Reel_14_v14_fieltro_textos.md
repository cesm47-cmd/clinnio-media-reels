# Reel 14 v14 · La llave del consultorio en fieltro · Doble verificación

Pasada de corrección sobre la v13 (no registrada: Rogelio detuvo su registro), aprobada por César el 26/11/2026, con una corrida de Computer autorizada.
Estado: borrador para la revisión completa de Polimnia. No se publica ni se programa. El uso público de las filas 12, 13, 14, 23 y 24 depende de la prueba T140 del 30/11/2026 y de la confirmación escrita de Francis (A-022). Además hace falta el texto literal de César en la columna O.
ID de versión: Clío la registra en «Decisiones y acciones» después de la revisión de Polimnia. Sustituye a la v13 y a la v12 (V-176).

## Qué cambia frente a la v13

1. Cámara fija en toda la toma C (cuadros 438 a 677). En la v13 la placa del interior seguía el paneo y el acercamiento de la cámara, así que el sillón se estiraba y se encogía. Lo detectó César y lo confirmó Rogelio en los cuadros 540, 580, 620 y 660. Polimnia midió que el bloque del interior se deslizaba de 6 a 10 px y cambiaba de escala cerca de 1 % frente al marco de la puerta. En la v14 la toma C ya no tiene paneo, acercamiento de cámara ni acercamiento digital.
2. Todo el fondo de la toma es UNA placa fija (placa14.png) en coordenadas absolutas de pantalla: la recepción, el banco, el mostrador, la puerta y el interior con el sillón, la lámpara y las repisas. La placa es idéntica en todos los cuadros y no se deforma, ni se escala, ni se desplaza para compensar nada, igual que la llave congelada del cuadro 650. Sale del primer cuadro de la toma C, igual al último de la toma B, así que el corte de B a C no salta. Por la puerta se ve el sillón recogido y vertical, la lámpara a un lado y la hoja restaurada delante.
3. Los personajes van delante con su animación: la profesional, la dueña, el paciente, la llave y el llavero. Para que no patinen sobre el fondo fijo, en cada cuadro se deshace el movimiento de cámara de la toma original, medido en la pared. El mostrador del frente siempre queda delante de ellos.
4. Se quitó el acercamiento digital de 1,00 a 1,05 de la toma C, que iba de los 19,6 a los 22,6 s. Esto estaba previsto y aprobado: es parte del arreglo. El letrero con «Muy pronto en Caracas», la tarjeta «Únete a la lista de espera» y las notas quedan en su sitio, sin moverse.
5. Fondo reconstruido donde estaban los personajes en el cuadro 437. Al moverse, los personajes dejan a la vista partes del fondo: el banco donde estaba sentado el paciente, el mostrador de atrás y la pared. Esas partes se tomaron de los cuadros en que ese punto está libre, alineados con el cuadro 437. Se eligió el valor más claro de cada punto (percentil 75), para no copiar sombras ni restos de personajes. El extremo izquierdo del banco nunca se ve libre en la toma original, así que se prolongó con sus tablas horizontales. Todo esto queda fijo en la placa.
6. Se conserva el arreglo de la v12: la cabeza de la dueña va delante del interior en los cuadros 568 a 613.
7. No cambia nada más. El audio es idéntico bit a bit al de la v12 y la v13. Los cuadros 0 a 437 son los de la v13, sin otra diferencia que el ruido de codificación.

## Verificación del movimiento en coordenadas absolutas

- Antes de codificar, el fondo fuera de los personajes es idéntico píxel a píxel a la placa en los 140 cuadros de la toma C: diferencia máxima de 0. En el montaje a 1080x1920, el sillón, la lámpara, las repisas, la hoja y el marco de los cuadros 535, 540, 570, 580, 600, 620, 630, 660 y 670 difieren del cuadro 438 en 2 niveles sobre 255 como máximo, por el suavizado del borde de los personajes.
- En el video final, el sillón y el marco de la puerta se midieron frente al cuadro 438 en los cuadros 448 a 668, cada 10 cuadros, y en 535, 540, 570, 580, 600, 620, 630, 660, 670 y 677. Se usó alineación afín con máscara fuera de los personajes. El sillón se desplaza 0,007 px como máximo en x y 0,013 px en y, y frente al marco nunca más de 0,015 px. Su escala varía menos de 0,005 %. El criterio de aprobación era 1 px. La diferencia que queda es de 2 a 3 niveles sobre 255 y viene del ruido de codificación H.264.
- El cuadro 437 es el último de la toma B. Frente al 438 tiene una diferencia de unos 0,25 px, que trae la generación original de las tomas y que ya estaba en la v9 a la v13. No cambia de una versión a otra.

| Cuadro | Sillón dx, dy (px) | Marco dx, dy (px) | Sillón frente al marco (px) | Escala del sillón |
|---|---|---|---|---|
| 438 | +0,000, -0,000 | +0,000, +0,000 | 0,000 | 1,00000 |
| 448 | -0,003, -0,002 | -0,003, +0,010 | 0,012 | 1,00001 |
| 498 | -0,000, +0,004 | -0,001, +0,013 | 0,009 | 0,99998 |
| 535 | -0,005, +0,002 | -0,007, -0,000 | 0,002 | 0,99998 |
| 540 | -0,007, +0,002 | -0,008, -0,000 | 0,002 | 0,99999 |
| 570 | -0,005, +0,005 | -0,008, +0,002 | 0,003 | 0,99999 |
| 580 | -0,002, -0,011 | -0,006, +0,002 | 0,013 | 0,99999 |
| 600 | -0,002, -0,008 | -0,005, +0,003 | 0,011 | 0,99999 |
| 620 | -0,003, +0,003 | -0,005, +0,003 | 0,002 | 0,99995 |
| 630 | -0,003, -0,000 | -0,006, +0,009 | 0,009 | 0,99996 |
| 660 | -0,004, +0,001 | -0,003, +0,006 | 0,005 | 0,99997 |
| 670 | -0,004, +0,001 | -0,003, +0,006 | 0,005 | 0,99997 |
| 677 | -0,004, +0,001 | -0,003, +0,006 | 0,005 | 0,99997 |

Datos completos en scripts/medicion_v14.json.

## Historial de la v13 (sustituida, no registrada)

1. La v13 congeló el interior como una placa que seguía la pared con el paneo y el acercamiento de la cámara. El sillón se estiraba y se encogía, y el interior se deslizaba frente al marco. La v14 lo sustituye con cámara fija y fondo sin transformar.

## Historial de la v12 (se mantiene)

1. Rostro de la dueña (M6 de Polimnia): entre los cuadros 578 y 602 su cabeza, con piel y cabello, va delante del interior con el sillón. Se aplica a los cuadros 568 a 613.

## Historial de la v11 (se mantiene)

1. Hoja de la puerta: la hoja abierta de la v9 sigue delante del sillón dental, con el canto verde continuo, la manilla y la placa.

## Historial de la v10 (se mantiene)

1. Sillón dental (orden de César): dentro del consultorio ya no se ve la camilla. En su lugar hay un sillón dental de fieltro lavanda, reclinable, con cabecero, apoyabrazos, base color crema y lámpara dental en su brazo. El cambio está en todos los cuadros del video y en la portada. Se hizo sin regenerar las tomas: el sillón se diseñó una vez con edición de imagen con IA sobre una vista limpia del interior. Luego se colocó cuadro a cuadro siguiendo el movimiento de cámara, y quedan por delante el marco y el canto de la puerta, el pomo, el cabello, la mano, la manga y la llave.
2. Final de la toma C (M6 de Polimnia): la toma se congela en el cuadro 650 (21,67 s), cuando ella aún sostiene la llave con el llavero lavanda. Los 0,93 s restantes, cuadros 650 a 677, son ese cuadro limpio con el acercamiento digital, que sigue hasta 1,05. Ya no hay cuadros con la llave deformada ni con el llavero que desaparece. El audio no cambia.
3. Texto (F5 de Polimnia): en la tabla del guion y en el texto alternativo, «Ella lleva la llave a la cerradura» pasa a ser «Ella levanta la llave en la puerta del consultorio».
4. Texto alternativo: además de la corrección F5, se agregó que por la puerta abierta se ve un sillón dental de fieltro, para que describa lo que hay en pantalla. El caption no cambia.

## Se mantiene

Todo lo de la v9: uniforme médico azul marino con gorro quirúrgico según la referencia de César, letrero solo con el isotipo cosido, notas con título de 40 px y filas de 28 px a 95 px de los bordes, sello «Verificado por Clinnio» con el isotipo al centro y declaración de IA solo en el caption y en el texto alternativo (D-104 y D-106). Estilo fieltro con rostros (excepción registrada para este estilo), la dueña joven y la llave como objeto protagonista. También el mismo guion y las filas 12, 13, 14, 23 y 24 de Afirmaciones. Audio de la v6 sin recodificar (voz de Carito y música de Pixabay de V-073, «Music Promotion No Copyright», MiroMaxMusic, pista 513944: https://pixabay.com/music/corporate-music-promotion-no-copyright-513944/). Subtítulos en la franja de 1530 a 1618 px y «enlace en la bio» en #344C4C. Sin etiquetas de IA ni «Personajes ilustrativos» en pantalla ni en la portada. La puerta no se abre hacia la cámara: está abierta hacia dentro del consultorio todo el tiempo. Los checks de «Consultorio» quedan completos a los 10,7 s: «Identidad del dueño» con «consultorio» (8,96 s), «Documentos del espacio» con «dueño» (10,33 s) y el sello a los 10,40 s. Eso ocurre antes de que la llave salga de la mano de la dueña. La llave se ve hasta el último cuadro. Mostrador en cuadro desde el primer cuadro y notas a más de 90 px de los bordes. Tarjeta final con letra de 40 px, a más de 90 px de los bordes. Cabello sin tapar «en Caracas», rótulos del letrero visibles durante el acercamiento y texto de la portada dentro del margen de 90 px.

## Ficha técnica

- Archivo: Reel_14_v14_fieltro.mp4. 1080x1920, 30 fps, H.264 + AAC 48 kHz, 22,6 s (678 cuadros), −14,0 LUFS y pico de −1,4 dBFS (verificado con ffprobe y ebur128).
- Cuadro inicial: el primer cuadro de la v8 editado con IA, con el uniforme y el gorro azul marino y el letrero en blanco.
- Toma A (0 a 8,0 s): IA, Veo 3.1 Fast, sin audio, cámara fija. La profesional llega al mostrador y deja su credencial. La dueña espera junto a la puerta con la llave.
- Toma B (8,0 a 14,58 s): IA desde el último cuadro de A. La dueña extiende la llave desde los 9,5 s y la llave pasa a la profesional entre los 11,1 y los 11,3 s. Se corta antes de que la toma deje la llave sobre el mostrador.
- Toma C (14,58 a 22,6 s): IA desde el cuadro de B en el que ella sostiene la llave. Se usan los primeros 5,8 s de la toma, a 0,73x, para cortar antes de que la puerta se cierre y la llave salga de cuadro. En la v10 se congela en el cuadro global 650 (21,67 s). En la v14 la cámara de esta toma queda fija.
- Encima de las tomas van el letrero con el isotipo, que sigue el movimiento de cámara y queda limitado al fieltro verde, y las notas con sello, que se desvanecen de 16,4 a 16,9 s. También van la tarjeta de cierre, los subtítulos y, solo hasta la v13, el acercamiento digital de 1,00 a 1,05 entre 19,6 y 22,6 s, que en la v14 se quitó.
- Hoja de la puerta: canto.py detecta el canto en cada cuadro (canto.json) y silla_comp.py lo conserva delante del sillón.
- Rostro de la dueña (v12): silla_comp.py, función cabeza(), crea una máscara de piel y cabello con los ojos y la boca rellenos y la deja delante del sillón en los cuadros fuente 76 a 102 de la toma C (carpeta frC12).
- Sillón dental: hom.py (seguimiento del interior cuadro a cuadro), silla.py (alineación del sillón diseñado con IA) y silla_comp.py (composición con lo que va por delante).
- Python con ffmpeg: escena_v14.py (montaje), piezas_v9.py (isotipo, sello y notas), escena_v7.py y fieltro_logo.py (subtítulos, tarjeta y utilidades), portada_v11.py.
- Interior fijo (v13): cam13.py mide el movimiento de cámara en la pared (rasgos SIFT, personas excluidas, suavizado) y lo guarda en cam13.json. plate13.py arma la placa del interior a partir del cuadro 437 y genera plate13.png y region13.png. seg13.py y seg13b.py segmentan a los personajes con rembg (modelos u2net_human_seg e isnet-general-use). mask13.py une las dos máscaras, las afina con GrabCut y las propaga entre cuadros con flujo óptico DIS. comp13.py compone la placa detrás de los personajes y deja los cuadros en la carpeta frC13. En los primeros 6 cuadros de la toma C, un anillo de 8 px junto a la silueta pasa de la v12 a la placa para que el corte no salte.
- Cámara fija (v14): stab14.py lleva cada cuadro de la toma C a las coordenadas absolutas del cuadro 437, deshaciendo el movimiento medido en la pared (cam13.json). plate14.py arma la placa fija: el cuadro 437, el interior de la v13 en esas mismas coordenadas y el fondo que dejan a la vista los personajes, tomado de los cuadros alineados con traslación ECC y percentil 75. Genera placa14.png y mostrador14.png. comp14.py compone placa y personajes (carpeta frC14). La máscara de los personajes une los modelos rembg u2net_human_seg e isnet-general-use con una prueba de diferencia frente a la placa cerca de ellos; dentro de la puerta usa la máscara afinada de la v13. medir14.py hace la verificación del movimiento y genera medicion_v14.json. escena_v14.py usa en la toma C el letrero del cuadro 437 y no aplica acercamiento.

## Guion (una sola tensión: ¿el otro lado es quien dice ser?)

| Tiempo | Escena y acción | Voz |
|---|---|---|
| 0,0–3,4 s | Con el mostrador ya en cuadro, la profesional, con uniforme médico azul marino y gorro quirúrgico, llega con su credencial. La dueña espera junto a la puerta con la llave del llavero lavanda. El paciente aguarda en el banco. | ¿Quien está del otro lado es quien dice ser? |
| 3,4–8,0 s | La profesional deja su credencial en el mostrador y asiente. En la nota «Profesional» se marcan «Identidad» y «Credencial profesional», y aparece el sello «Verificada por Clinnio». | En Clinnio, verificamos identidad y credencial profesional. |
| 8,0–10,8 s | La dueña sonríe y extiende la llave hacia la profesional. En la nota «Consultorio» se marcan «Identidad del dueño» y «Documentos del espacio», y aparece el sello «Verificado por Clinnio»: todo completo a los 10,7 s. | Y verificamos al consultorio y a su dueño: |
| 10,8–14,6 s | La llave pasa de la mano de la dueña a la de la profesional (11,1 a 11,3 s) y ella la levanta, sonriendo. | su identidad y los documentos del espacio. La reserva ocurre entre partes verificadas. |
| 14,6–19,6 s | Con la llave en la mano, la profesional camina hacia la puerta del consultorio; la dueña la señala y el paciente se levanta y la sigue. En el letrero aparece «Muy pronto en Caracas». | Muy pronto, en Caracas. |
| 19,6–22,6 s | La cámara se acerca un poco. Ella levanta la llave en la puerta del consultorio. En el frente del mostrador aparece la tarjeta cosida «Únete a la lista de espera · enlace en la bio». | Únete a la lista de espera. |

Afirmaciones (pestaña Afirmaciones), con la misma formulación de la v4 a la v8: filas 12 y 13 («En Clinnio, verificamos identidad y credencial profesional.»), filas 23 y 14 (lado del consultorio), fila 24 («La reserva ocurre entre partes verificadas») y fila 21 (solo «Muy pronto» y la lista de espera). Sin porcentajes, tarifas, Cashea ni pantallas. La llave es un recurso narrativo: no se afirma que Clinnio entregue llaves ni custodie accesos.

## Caption

¿Quien está del otro lado es quien dice ser?

En Clinnio, verificamos identidad y credencial profesional.

Y verificamos al consultorio y a su dueño: su identidad y los documentos del espacio. La reserva ocurre entre partes verificadas.

Muy pronto en Caracas. Únete a la lista de espera: enlace en la bio.

Video y voz generados con IA. Personajes ilustrativos.

#Clinnio #Caracas #Consultorios #Odontología #Psicología #Fisioterapia #Nutrición #SaludVenezuela

## Texto alternativo

Animación generada con IA, en estilo stop-motion de fieltro, con títeres de fieltro y lana en la recepción de un consultorio en Caracas, con el Ávila en la ventana. En la pared cuelga un letrero de fieltro verde cosido a mano con el asterisco del logo de Clinnio. Una profesional de pelo rizado y lentes redondos, con uniforme médico azul marino y gorro quirúrgico, llega al mostrador y deja su credencial. En una nota cosida al mostrador se marcan su identidad y su credencial profesional, con un sello con el asterisco de Clinnio que dice «Verificada por Clinnio». En otra nota se marcan la identidad del dueño y los documentos del espacio, con el sello «Verificado por Clinnio». La dueña del consultorio, una mujer joven de pelo recogido y cárdigan verde, le entrega una llave de fieltro con llavero lavanda. Por la puerta abierta se ve un sillón dental de fieltro. La profesional camina hacia la puerta del consultorio, seguida por un paciente que se levanta del banco. Ella levanta la llave en la puerta del consultorio. El letrero dice «Muy pronto en Caracas» y en el mostrador aparece una tarjeta cosida: «Únete a la lista de espera, enlace en la bio».

## Portada

Esta pasada no toca la portada. La portada oficial es Reel_14_v11_fieltro_portada_titulo_superior.png (1080x1920, md5 43d379c07ac7a72967f58337ffd085a2). Sale del cuadro 327 de la toma B. El arreglo de la v14 solo cambia cuadros de la toma C (438 a 677), así que la portada no se ve afectada. La portada original de la v11 (Reel_14_v11_fieltro_portada.png, md5 55672785078f97aeeb5d73b96bf46a6c) se conserva archivada. Las dos se copian a la carpeta de la v14 sin cambios y con los mismos md5. César fija la portada desde la app de Instagram.

## Prueba anti-parecido (frente a la v13, V-176 v12 y V-175 v11)

Es una corrección de la misma pieza, no una pieza nueva de la grilla. Comparte composición con la v13 y la v12 por continuidad y las sustituye.

## Puntos para la revisión de Polimnia

1. Movimiento en coordenadas absolutas: comparar el fondo en los cuadros 535, 570, 600, 630 y 670, y también en 540, 580, 620 y 660. Confirmar que el sillón, la lámpara, las repisas, la puerta y el mostrador ocupan exactamente la misma posición y forma en todos ellos, sin deformación, y que la cámara de la toma C está fija. Las hojas de revisión llevan líneas guía rojas en posiciones fijas de la pantalla.
2. Rostro de la dueña: confirmar que el arreglo de la v12 sigue intacto en los cuadros 578 a 602 y en la entrada y salida de 568 a 613.
3. Hallazgos nuevos: confirmar que no hay. Conviene mirar las zonas reconstruidas del fondo: el banco cuando el paciente se levanta, desde el cuadro 500, el mostrador de atrás y la pared junto a la puerta. También los bordes de los personajes sobre el fondo fijo y el paso de las piernas del paciente detrás del extremo izquierdo del mostrador, hacia los cuadros 545 a 560.
4. Ya no hay acercamiento al final de la toma C: los cuadros 600 a 677 se ven con el mismo encuadre que el 438. Es parte del arreglo aprobado. Siguen de versiones anteriores la toma C a 0,73x y el final congelado desde el cuadro 650.

## Archivos y verificación

- Reel_14_v14_fieltro.mp4: md5 76a16de7a8f654055dc395674fe8fb6b. 1080x1920, 30 fps, H.264 + AAC 48 kHz, 22,6 s, 678 cuadros, −14,0 LUFS y pico de −1,4 dBFS. El md5 del flujo de audio es 486cc9030ae8b7d23288bbd29ccbb157, igual al de la v12 y la v13.
- Reel_14_v11_fieltro_portada_titulo_superior.png (portada oficial, sin cambios): md5 43d379c07ac7a72967f58337ffd085a2.
- Reel_14_v11_fieltro_portada.png (portada original de la v11, archivada, sin cambios): md5 55672785078f97aeeb5d73b96bf46a6c.
- Repositorio de medios cesm47-cmd/clinnio-media-reels, carpeta r-78fd40e24fc2/reel-14-v14-fieltro/. Los archivos se comprobaron en GitHub.
- Proyecto: contenido/reels/reel-14-v14-fieltro/, con el video, las portadas, este documento, las hojas de revisión, los scripts y las tomas (incluidas placa14.png y mostrador14.png).

## Herramienta

Generación de video con IA para las tres tomas (única vía para mantener los títeres de stop-motion en horas), edición de imagen con IA para el cuadro inicial (uniforme y letrero en blanco) y para el sillón dental, la pista de audio de la v6 (ElevenLabs para Carito y Pixabay para la música) y Python con ffmpeg para el resto. Descript no aplica: no hay grabación que editar. La v13 y la v14 suman segmentación con rembg y GrabCut, estabilización y composición sobre placa fija, todo local y sin regenerar tomas.
