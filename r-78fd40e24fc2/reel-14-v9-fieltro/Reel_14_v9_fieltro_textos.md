# Reel 14 v9 · La llave del consultorio en fieltro · Doble verificación

Pasada de correcciones sobre V-172 (v8), por órdenes directas de César (26/11/2026).
Estado: borrador para la revisión completa nueva de Polimnia. No se publica ni se programa. El uso público de las filas 12, 13, 14, 23 y 24 depende de la prueba T140 del 30/11/2026 y de la confirmación escrita de Francis (A-022). Además hace falta el texto literal de César en la columna O.
ID de versión: Clío lo asigna en «Decisiones y acciones». Sustituye a la v8 (V-172).

## Qué cambia frente a la v8

1. Uniforme (orden de César, con la foto de referencia de un odontólogo real): la profesional lleva ahora uniforme médico azul marino en fieltro, con cuello mao y broches, pantalón azul marino y gorro quirúrgico azul marino, con sus rizos asomando. Sigue siendo una mujer, con rostro y lentes redondos. Para que el uniforme sea el mismo en toda la pieza, la escena completa se regeneró en tres tomas nuevas con IA a partir de un único cuadro inicial editado.
2. Logo (decisión de César): el letrero lleva solo el isotipo de Clinnio, el asterisco, en fieltro blanco cosido, hecho con la máscara del asterisco auténtico. Ya no lleva las letras «clinnio». Desde los 17,6 s el isotipo pasa a ser pequeño, arriba, y debajo aparece «Muy pronto en Caracas» en letras de fieltro.
3. Notas de requisitos más grandes: título en Poppins Bold de 40 px y filas en Poppins Medium de 28 px. Las notas miden 440 px de ancho, van de x = 95 a 535 px y de x = 545 a 985 px (a 95 px de cada borde) y terminan por encima de la franja de subtítulos.
4. Sello de marca: el sello «Verificada / Verificado por Clinnio» es ahora un sello circular verde #344C4C, con un círculo interior lavanda, una costura y el isotipo de Clinnio en el centro. Junto a él va una cinta lavanda con el texto en Poppins SemiBold de 25 px.
5. Declaración de IA (cambio de César del 26/11/2026): queda solo en el caption y en el texto alternativo, como quedó en D-104.
6. Texto alternativo: se actualizó para describir el uniforme azul marino con gorro quirúrgico y el letrero con el isotipo, porque el anterior hablaba de un «uniforme de odontología verde» y de un logo «en letras de fieltro». El caption no cambia.

## Se mantiene

Estilo fieltro con rostros (excepción registrada para este estilo), la dueña joven y la llave como objeto protagonista. También el mismo guion y las filas 12, 13, 14, 23 y 24 de Afirmaciones. Audio de la v6 sin recodificar (voz de Carito y música de Pixabay de V-073, «Music Promotion No Copyright», MiroMaxMusic, pista 513944: https://pixabay.com/music/corporate-music-promotion-no-copyright-513944/). Subtítulos en la franja de 1530 a 1618 px y «enlace en la bio» en #344C4C. Sin etiquetas de IA ni «Personajes ilustrativos» en pantalla ni en la portada. La puerta no se abre hacia la cámara: está abierta hacia dentro del consultorio todo el tiempo. Los checks de «Consultorio» quedan completos a los 10,7 s: «Identidad del dueño» con «consultorio» (8,96 s), «Documentos del espacio» con «dueño» (10,33 s) y el sello a los 10,40 s. Eso ocurre antes de que la llave salga de la mano de la dueña. La llave se ve hasta el último cuadro. Mostrador en cuadro desde el primer cuadro y notas a más de 90 px de los bordes. Tarjeta final con letra de 40 px, a más de 90 px de los bordes. Cabello sin tapar «en Caracas», rótulos del letrero visibles durante el acercamiento y texto de la portada dentro del margen de 90 px.

## Ficha técnica

- Archivo: Reel_14_v9_fieltro.mp4. 1080x1920, 30 fps, H.264 + AAC 48 kHz, 22,6 s (678 cuadros), −14,0 LUFS (verificado con ffprobe y ebur128).
- Cuadro inicial: el primer cuadro de la v8 editado con IA, con el uniforme y el gorro azul marino y el letrero en blanco.
- Toma A (0 a 8,0 s): IA, Veo 3.1 Fast, sin audio, cámara fija. La profesional llega al mostrador y deja su credencial. La dueña espera junto a la puerta con la llave.
- Toma B (8,0 a 14,58 s): IA desde el último cuadro de A. La dueña extiende la llave desde los 9,5 s y la llave pasa a la profesional entre los 11,1 y los 11,3 s. Se corta antes de que la toma deje la llave sobre el mostrador.
- Toma C (14,58 a 22,6 s): IA desde el cuadro de B en el que ella sostiene la llave. Se usan los primeros 5,8 s de la toma, a 0,73x, para cortar antes de que la puerta se cierre y la llave salga de cuadro.
- Encima de las tomas van el letrero con el isotipo, que sigue el movimiento de cámara y queda limitado al fieltro verde, y las notas con sello, que se desvanecen de 16,4 a 16,9 s. También van la tarjeta de cierre, los subtítulos y el acercamiento digital moderado de 1,00 a 1,05 entre 19,6 y 22,6 s.
- Python con ffmpeg: escena_v9.py (montaje), piezas_v9.py (isotipo, sello y notas), escena_v7.py y fieltro_logo.py (subtítulos, tarjeta y utilidades), portada_v9.py.

## Guion (una sola tensión: ¿el otro lado es quien dice ser?)

| Tiempo | Escena y acción | Voz |
|---|---|---|
| 0,0–3,4 s | Con el mostrador ya en cuadro, la profesional, con uniforme médico azul marino y gorro quirúrgico, llega con su credencial. La dueña espera junto a la puerta con la llave del llavero lavanda. El paciente aguarda en el banco. | ¿Quien está del otro lado es quien dice ser? |
| 3,4–8,0 s | La profesional deja su credencial en el mostrador y asiente. En la nota «Profesional» se marcan «Identidad» y «Credencial profesional», y aparece el sello «Verificada por Clinnio». | En Clinnio, verificamos identidad y credencial profesional. |
| 8,0–10,8 s | La dueña sonríe y extiende la llave hacia la profesional. En la nota «Consultorio» se marcan «Identidad del dueño» y «Documentos del espacio», y aparece el sello «Verificado por Clinnio»: todo completo a los 10,7 s. | Y verificamos al consultorio y a su dueño: |
| 10,8–14,6 s | La llave pasa de la mano de la dueña a la de la profesional (11,1 a 11,3 s) y ella la levanta, sonriendo. | su identidad y los documentos del espacio. La reserva ocurre entre partes verificadas. |
| 14,6–19,6 s | Con la llave en la mano, la profesional camina hacia la puerta del consultorio; la dueña la señala y el paciente se levanta y la sigue. En el letrero aparece «Muy pronto en Caracas». | Muy pronto, en Caracas. |
| 19,6–22,6 s | La cámara se acerca un poco. Ella lleva la llave a la cerradura de la puerta. En el frente del mostrador aparece la tarjeta cosida «Únete a la lista de espera · enlace en la bio». | Únete a la lista de espera. |

Afirmaciones (pestaña Afirmaciones), con la misma formulación de la v4 a la v8: filas 12 y 13 («En Clinnio, verificamos identidad y credencial profesional.»), filas 23 y 14 (lado del consultorio), fila 24 («La reserva ocurre entre partes verificadas») y fila 21 (solo «Muy pronto» y la lista de espera). Sin porcentajes, tarifas, Cashea ni pantallas. La llave es un recurso narrativo: no se afirma que Clinnio entregue llaves ni custodie accesos.

## Caption

¿Quien está del otro lado es quien dice ser?

En Clinnio, verificamos identidad y credencial profesional.

Y verificamos al consultorio y a su dueño: su identidad y los documentos del espacio. La reserva ocurre entre partes verificadas.

Muy pronto en Caracas. Únete a la lista de espera: enlace en la bio.

Video y voz generados con IA. Personajes ilustrativos.

#Clinnio #Caracas #Consultorios #Odontología #Psicología #Fisioterapia #Nutrición #SaludVenezuela

## Texto alternativo

Animación generada con IA, en estilo stop-motion de fieltro, con títeres de fieltro y lana en la recepción de un consultorio en Caracas, con el Ávila en la ventana. En la pared cuelga un letrero de fieltro verde cosido a mano con el asterisco del logo de Clinnio. Una profesional de pelo rizado y lentes redondos, con uniforme médico azul marino y gorro quirúrgico, llega al mostrador y deja su credencial. En una nota cosida al mostrador se marcan su identidad y su credencial profesional, con un sello con el asterisco de Clinnio que dice «Verificada por Clinnio». En otra nota se marcan la identidad del dueño y los documentos del espacio, con el sello «Verificado por Clinnio». La dueña del consultorio, una mujer joven de pelo recogido y cárdigan verde, le entrega una llave de fieltro con llavero lavanda. La profesional camina hacia la puerta del consultorio, seguida por un paciente que se levanta del banco. Ella lleva la llave a la cerradura. El letrero dice «Muy pronto en Caracas» y en el mostrador aparece una tarjeta cosida: «Únete a la lista de espera, enlace en la bio».

## Portada

Reel_14_v9_fieltro_portada.png, 1080x1920. Es un cuadro nuevo de la toma B (10,9 s): la llave cruza de la dueña a la profesional sobre el mostrador, con el letrero del isotipo arriba, sin notas y sin etiquetas. Lleva «Para profesionales y dueños de consultorios» (Poppins SemiBold de 32 px, de x = 155 a 925 px, en cinta lavanda) y la promesa «¿Es quien dice ser?» (Bold de 92 px). Todo queda dentro de la zona segura (y 285 a 1635) y del recorte 3:4 de la grilla (y 240 a 1680). César la fija desde la app de Instagram.

## Prueba anti-parecido (frente a V-172 v8, V-171 v7 y V-170 v6)

Es una corrección de la misma pieza, no una pieza nueva de la grilla. Comparte composición con la v8 y la v7 por continuidad y las sustituye. No hay titular flotante ni estructura de tarjetas nueva.

## Puntos para la revisión de Polimnia

- Entrega de la llave: en la toma nueva la dueña no camina al mostrador. Entrega la llave desde su sitio junto a la puerta, con el brazo extendido sobre el borde del mostrador. Extiende la llave desde los 9,5 s, pero la llave sigue en su mano hasta los 11,1 s. Revisar si basta con que los checks estén completos a los 10,7 s o si se pide el sello antes de que extienda la llave.
- Toma C a 0,73x: el movimiento final se ve algo más lento que el resto, con el ritmo propio del stop-motion. Se hizo así para no mostrar el cierre de la puerta ni la llave fuera de cuadro.
- Movimiento de cámara: en la toma C la cámara se acerca un poco por sí sola desde unos 17 s, antes del acercamiento digital de 1,00 a 1,05. El letrero lo sigue; revisar que el conjunto se vea moderado.
- Al final el llavero lavanda queda tras la mano de la profesional; la llave dorada se ve en todo momento.
- El gorro tapa casi todo el cabello de la profesional; se ven los rizos a los lados. Confirmar que se lee como uniforme médico, igual que en la referencia.
- Texto alternativo actualizado (uniforme e isotipo). El caption no cambia.
- En «Documentos del espacio» el texto queda cerca de la costura derecha de la nota (unos 10 px), sin tocarla.

## Herramienta

Generación de video con IA para las tres tomas (única vía para mantener los títeres de stop-motion en horas), edición de imagen con IA solo para el cuadro inicial (uniforme y letrero en blanco), la pista de audio de la v6 (ElevenLabs para Carito y Pixabay para la música) y Python con ffmpeg para el resto. Descript no aplica: no hay grabación que editar.
