# Reel 14 v13 · La llave del consultorio en fieltro · Doble verificación

Pasada de corrección sobre V-176 (v12), aprobada por César (26/11/2026).
Estado: borrador para la revisión completa de Polimnia. No se publica ni se programa. El uso público de las filas 12, 13, 14, 23 y 24 depende de la prueba T140 del 30/11/2026 y de la confirmación escrita de Francis (A-022). Además hace falta el texto literal de César en la columna O.
ID de versión: Clío lo registra en «Decisiones y acciones» como la versión siguiente a V-178. Sustituye a la v12 (V-176).

## Qué cambia frente a la v12

1. Interior quieto en toda la toma C (defecto detectado por César y verificado por Rogelio en los cuadros 560 a 620 de la v12): en la v12 el interior que se ve por la puerta se movía solo. El sillón lavanda se reclinaba y extendía el reposapiernas, la lámpara cambiaba de lugar y terminaba encendida sobre el sillón, y la hoja de la puerta se desplazaba. Ahora el interior es una sola placa fija para los cuadros 437 a 677. El sillón queda recogido y vertical, la lámpara queda a un lado y la hoja de la puerta queda restaurada delante, con su canto verde, la manilla y la placa. Las repisas, el botiquín, la planta y la sala no cambian de forma, de posición ni de estado. Es la misma técnica de congelado del cuadro 650 aplicada a toda la toma.
2. Referencia del interior: el primer cuadro de la toma C (cuadro 437), que es igual al último de la toma B. Muestra el mismo estado pedido para el cuadro 560: sillón recogido y vertical, lámpara a un lado y hoja delante. Se eligió ese cuadro para que el corte de B a C no salte. En el cuadro 437 la v13 es igual a la v12 (diferencia máxima de 7 niveles sobre 255).
3. La placa solo acompaña el paneo de la cámara. La toma C tiene un paneo de unos 90 px y una escala de 0,98, y luego viene el acercamiento digital de 1,00 a 1,05. La placa se mueve con la pared, con una similaridad medida en la pared en cada cuadro. Dentro de la placa ningún píxel cambia. Así el interior no flota respecto de la pared.
4. Personajes delante: la dueña, la profesional, el paciente, la llave y el llavero siguen con su animación delante de la placa. Su silueta sale de una máscara por cuadro hecha con dos modelos de segmentación (rembg u2net_human_seg e isnet-general-use), afinada con GrabCut y propagada entre cuadros con flujo óptico.
5. Se conserva el arreglo de la v12: la cabeza de la dueña va delante del interior en los cuadros 568 a 613.
6. Zonas reconstruidas de la placa: detrás de la dueña en el cuadro 437 hay una franja del interior que ese cuadro no muestra. Se completó con la vista limpia del interior con el sillón de la v10, con un relleno espejado y con inpaint. La barra verde y la placa de la hoja girada, que solo existían en cuadros posteriores, se reemplazaron por pared lisa. Por eso la hoja ya no gira en ningún cuadro.
7. No cambia nada más. El audio es idéntico bit a bit al de la v12 (mismo md5 del flujo AAC). Los cuadros 0 a 436 son los de la v12, sin cambios fuera del ruido de codificación.

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

- Archivo: Reel_14_v13_fieltro.mp4. 1080x1920, 30 fps, H.264 + AAC 48 kHz, 22,6 s (678 cuadros), −14,0 LUFS y pico de −1,4 dBFS (verificado con ffprobe y ebur128).
- Cuadro inicial: el primer cuadro de la v8 editado con IA, con el uniforme y el gorro azul marino y el letrero en blanco.
- Toma A (0 a 8,0 s): IA, Veo 3.1 Fast, sin audio, cámara fija. La profesional llega al mostrador y deja su credencial. La dueña espera junto a la puerta con la llave.
- Toma B (8,0 a 14,58 s): IA desde el último cuadro de A. La dueña extiende la llave desde los 9,5 s y la llave pasa a la profesional entre los 11,1 y los 11,3 s. Se corta antes de que la toma deje la llave sobre el mostrador.
- Toma C (14,58 a 22,6 s): IA desde el cuadro de B en el que ella sostiene la llave. Se usan los primeros 5,8 s de la toma, a 0,73x, para cortar antes de que la puerta se cierre y la llave salga de cuadro. En la v10 se congela en el cuadro global 650 (21,67 s).
- Encima de las tomas van el letrero con el isotipo, que sigue el movimiento de cámara y queda limitado al fieltro verde, y las notas con sello, que se desvanecen de 16,4 a 16,9 s. También van la tarjeta de cierre, los subtítulos y el acercamiento digital moderado de 1,00 a 1,05 entre 19,6 y 22,6 s.
- Hoja de la puerta: canto.py detecta el canto en cada cuadro (canto.json) y silla_comp.py lo conserva delante del sillón.
- Rostro de la dueña (v12): silla_comp.py, función cabeza(), crea una máscara de piel y cabello con los ojos y la boca rellenos y la deja delante del sillón en los cuadros fuente 76 a 102 de la toma C (carpeta frC12).
- Sillón dental: hom.py (seguimiento del interior cuadro a cuadro), silla.py (alineación del sillón diseñado con IA) y silla_comp.py (composición con lo que va por delante).
- Python con ffmpeg: escena_v13.py (montaje), piezas_v9.py (isotipo, sello y notas), escena_v7.py y fieltro_logo.py (subtítulos, tarjeta y utilidades), portada_v11.py.
- Interior fijo (v13): cam13.py mide el movimiento de cámara en la pared (rasgos SIFT, personas excluidas, suavizado) y lo guarda en cam13.json. plate13.py arma la placa del interior a partir del cuadro 437 y genera plate13.png y region13.png. seg13.py y seg13b.py segmentan a los personajes con rembg (modelos u2net_human_seg e isnet-general-use). mask13.py une las dos máscaras, las afina con GrabCut y las propaga entre cuadros con flujo óptico DIS. comp13.py compone la placa detrás de los personajes y deja los cuadros en la carpeta frC13. En los primeros 6 cuadros de la toma C, un anillo de 8 px junto a la silueta pasa de la v12 a la placa para que el corte no salte.

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

Esta pasada no toca la portada. La portada oficial es Reel_14_v11_fieltro_portada_titulo_superior.png (1080x1920, md5 43d379c07ac7a72967f58337ffd085a2). Sale del cuadro 327 de la toma B. El arreglo de la v13 solo cambia cuadros de la toma C (437 a 677), así que la portada no se ve afectada. La portada original de la v11 (Reel_14_v11_fieltro_portada.png, md5 55672785078f97aeeb5d73b96bf46a6c) se conserva archivada. Las dos se copian a la carpeta de la v13 sin cambios y con los mismos md5. César fija la portada desde la app de Instagram.

## Prueba anti-parecido (frente a V-176 v12, V-175 v11 y V-174 v10)

Es una corrección de la misma pieza, no una pieza nueva de la grilla. Comparte composición con la v12 por continuidad y la sustituye.

## Puntos para la revisión de Polimnia

1. Movimiento: comparar el interior en los cuadros 535, 570, 600, 630 y 670, y si se quiere en toda la toma C de 437 a 677. Confirmar que el sillón, la lámpara, las repisas y la hoja de la puerta no cambian de posición, de forma ni de estado. Lo único que se mueve es el paneo de cámara, junto con la pared, y el acercamiento final. Medición: al llevar cada uno de esos cuadros a las coordenadas de la placa, la diferencia media con la placa fuera de los personajes es de 2,0 a 2,3 niveles sobre 255, que es el error del remuestreo.
2. Rostro de la dueña: confirmar que el arreglo de la v12 sigue intacto en los cuadros 578 a 602, y en la entrada y salida de 568 a 613.
3. Bordes de los personajes: revisar el cabello y el cárdigan de la dueña y la manga y la mano de la profesional sobre el interior. No debe haber halos, restos del interior anterior ni recortes. Revisar también el corte de B a C en el cuadro 437.
4. Hallazgos nuevos: confirmar que no aparece ninguno. Siguen de la v12: unos puntos oscuros pequeños en el piso junto al marco izquierdo, el final congelado desde el cuadro 650, la toma C a 0,73x y el acercamiento de la propia cámara.

## Archivos y verificación

- Reel_14_v13_fieltro.mp4: md5 f111a831c19b76b9b7a4aef0d5a7907f. 1080x1920, 30 fps, H.264 + AAC 48 kHz, 22,6 s, 678 cuadros, −14,0 LUFS y pico de −1,4 dBFS. El md5 del flujo de audio es 486cc9030ae8b7d23288bbd29ccbb157, igual al de la v12.
- Reel_14_v11_fieltro_portada_titulo_superior.png (portada oficial, sin cambios): md5 43d379c07ac7a72967f58337ffd085a2.
- Reel_14_v11_fieltro_portada.png (portada original de la v11, archivada, sin cambios): md5 55672785078f97aeeb5d73b96bf46a6c.
- Repositorio de medios cesm47-cmd/clinnio-media-reels, carpeta r-78fd40e24fc2/reel-14-v13-fieltro/. Los archivos se comprobaron en GitHub.
- Proyecto: contenido/reels/reel-14-v13-fieltro/, con el video, las portadas, este documento, las hojas de revisión, los scripts y las tomas (incluidas plate13.png y region13.png).

## Herramienta

Generación de video con IA para las tres tomas (única vía para mantener los títeres de stop-motion en horas), edición de imagen con IA para el cuadro inicial (uniforme y letrero en blanco) y para el sillón dental, la pista de audio de la v6 (ElevenLabs para Carito y Pixabay para la música) y Python con ffmpeg para el resto. Descript no aplica: no hay grabación que editar. La v13 suma segmentación con rembg y GrabCut, todo local y sin regenerar tomas.
