# Reel 14 v10 · La llave del consultorio en fieltro · Doble verificación

Pasada de correcciones sobre V-173 (v9), por orden directa de César (26/11/2026).
Estado: borrador para la revisión completa nueva de Polimnia. No se publica ni se programa. El uso público de las filas 12, 13, 14, 23 y 24 depende de la prueba T140 del 30/11/2026 y de la confirmación escrita de Francis (A-022). Además hace falta el texto literal de César en la columna O.
ID de versión: Clío lo asigna en «Decisiones y acciones». Sustituye a la v9 (V-173).

## Qué cambia frente a la v9

1. Sillón dental (orden de César): dentro del consultorio ya no se ve la camilla. En su lugar hay un sillón dental de fieltro lavanda, reclinable, con cabecero, apoyabrazos, base color crema y lámpara dental en su brazo. El cambio está en todos los cuadros del video y en la portada. Se hizo sin regenerar las tomas: el sillón se diseñó una vez con edición de imagen con IA sobre una vista limpia del interior. Luego se colocó cuadro a cuadro siguiendo el movimiento de cámara, y quedan por delante el marco y el canto de la puerta, el pomo, el cabello, la mano, la manga y la llave.
2. Final de la toma C (M6 de Polimnia): la toma se congela en el cuadro 650 (21,67 s), cuando ella aún sostiene la llave con el llavero lavanda. Los 0,93 s restantes, cuadros 650 a 677, son ese cuadro limpio con el acercamiento digital, que sigue hasta 1,05. Ya no hay cuadros con la llave deformada ni con el llavero que desaparece. El audio no cambia.
3. Texto (F5 de Polimnia): en la tabla del guion y en el texto alternativo, «Ella lleva la llave a la cerradura» pasa a ser «Ella levanta la llave en la puerta del consultorio».
4. Texto alternativo: además de la corrección F5, se agregó que por la puerta abierta se ve un sillón dental de fieltro, para que describa lo que hay en pantalla. El caption no cambia.

## Se mantiene

Todo lo de la v9: uniforme médico azul marino con gorro quirúrgico según la referencia de César, letrero solo con el isotipo cosido, notas con título de 40 px y filas de 28 px a 95 px de los bordes, sello «Verificado por Clinnio» con el isotipo al centro y declaración de IA solo en el caption y en el texto alternativo (D-104 y D-106). Estilo fieltro con rostros (excepción registrada para este estilo), la dueña joven y la llave como objeto protagonista. También el mismo guion y las filas 12, 13, 14, 23 y 24 de Afirmaciones. Audio de la v6 sin recodificar (voz de Carito y música de Pixabay de V-073, «Music Promotion No Copyright», MiroMaxMusic, pista 513944: https://pixabay.com/music/corporate-music-promotion-no-copyright-513944/). Subtítulos en la franja de 1530 a 1618 px y «enlace en la bio» en #344C4C. Sin etiquetas de IA ni «Personajes ilustrativos» en pantalla ni en la portada. La puerta no se abre hacia la cámara: está abierta hacia dentro del consultorio todo el tiempo. Los checks de «Consultorio» quedan completos a los 10,7 s: «Identidad del dueño» con «consultorio» (8,96 s), «Documentos del espacio» con «dueño» (10,33 s) y el sello a los 10,40 s. Eso ocurre antes de que la llave salga de la mano de la dueña. La llave se ve hasta el último cuadro. Mostrador en cuadro desde el primer cuadro y notas a más de 90 px de los bordes. Tarjeta final con letra de 40 px, a más de 90 px de los bordes. Cabello sin tapar «en Caracas», rótulos del letrero visibles durante el acercamiento y texto de la portada dentro del margen de 90 px.

## Ficha técnica

- Archivo: Reel_14_v10_fieltro.mp4. 1080x1920, 30 fps, H.264 + AAC 48 kHz, 22,6 s (678 cuadros), −14,0 LUFS y pico de −1,4 dBFS (verificado con ffprobe y ebur128).
- Cuadro inicial: el primer cuadro de la v8 editado con IA, con el uniforme y el gorro azul marino y el letrero en blanco.
- Toma A (0 a 8,0 s): IA, Veo 3.1 Fast, sin audio, cámara fija. La profesional llega al mostrador y deja su credencial. La dueña espera junto a la puerta con la llave.
- Toma B (8,0 a 14,58 s): IA desde el último cuadro de A. La dueña extiende la llave desde los 9,5 s y la llave pasa a la profesional entre los 11,1 y los 11,3 s. Se corta antes de que la toma deje la llave sobre el mostrador.
- Toma C (14,58 a 22,6 s): IA desde el cuadro de B en el que ella sostiene la llave. Se usan los primeros 5,8 s de la toma, a 0,73x, para cortar antes de que la puerta se cierre y la llave salga de cuadro. En la v10 se congela en el cuadro global 650 (21,67 s).
- Encima de las tomas van el letrero con el isotipo, que sigue el movimiento de cámara y queda limitado al fieltro verde, y las notas con sello, que se desvanecen de 16,4 a 16,9 s. También van la tarjeta de cierre, los subtítulos y el acercamiento digital moderado de 1,00 a 1,05 entre 19,6 y 22,6 s.
- Sillón dental: hom.py (seguimiento del interior cuadro a cuadro), silla.py (alineación del sillón diseñado con IA) y silla_comp.py (composición con lo que va por delante).
- Python con ffmpeg: escena_v10.py (montaje), piezas_v9.py (isotipo, sello y notas), escena_v7.py y fieltro_logo.py (subtítulos, tarjeta y utilidades), portada_v10.py.

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

Reel_14_v10_fieltro_portada.png, 1080x1920. Es el mismo cuadro de la v9 (toma B, 10,9 s), ahora con el sillón dental en el interior: la llave cruza de la dueña a la profesional sobre el mostrador, con el letrero del isotipo arriba, sin notas y sin etiquetas. Lleva «Para profesionales y dueños de consultorios» (Poppins SemiBold de 32 px, de x = 155 a 925 px, en cinta lavanda) y la promesa «¿Es quien dice ser?» (Bold de 92 px). Todo queda dentro de la zona segura (y 285 a 1635) y del recorte 3:4 de la grilla (y 240 a 1680). César la fija desde la app de Instagram.

## Prueba anti-parecido (frente a V-173 v9, V-172 v8 y V-171 v7)

Es una corrección de la misma pieza, no una pieza nueva de la grilla. Comparte composición con la v9 y la v8 por continuidad y las sustituye. No hay titular flotante ni estructura de tarjetas nueva.

## Puntos para la revisión de Polimnia

- Sillón dental compuesto: el sillón se agregó sobre las tomas y no viene de la generación de video. Conviene revisarlo a tamaño completo en tres momentos. Primero, de 0 a 14,6 s, cuando se ve por la rendija junto al canto de la puerta. Después, de 14,6 a 22,6 s, cuando la cámara se acerca y el interior se ve entero. Por último, en el paso de la mano y la manga de la dueña por delante (unos 17 a 21 s). Quedan algunos puntos oscuros pequeños en el piso, junto al marco izquierdo, que vienen de las sombras de la camilla original.
- En el interior el sillón se ve quieto: se mueve con la cámara, pero no tiene sombra propia cambiante. Revisar que se lea como parte de la escena.
- Final congelado: de 21,67 a 22,6 s la imagen está quieta y solo avanza el acercamiento digital. Coincide con «Únete a la lista de espera» y la tarjeta ya está en pantalla.
- Siguen de la v9: la entrega de la llave desde junto a la puerta (la llave sigue en la mano de la dueña hasta los 11,1 s, con los checks completos a los 10,7 s), la toma C a 0,73x y el acercamiento propio de la cámara desde unos 17 s.
- Texto alternativo con la corrección F5 y el sillón dental. El caption no cambia.

## Herramienta

Generación de video con IA para las tres tomas (única vía para mantener los títeres de stop-motion en horas), edición de imagen con IA para el cuadro inicial (uniforme y letrero en blanco) y para el sillón dental, la pista de audio de la v6 (ElevenLabs para Carito y Pixabay para la música) y Python con ffmpeg para el resto. Descript no aplica: no hay grabación que editar.
