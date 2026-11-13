# Análisis forense: tu imagen de Flow vs. el reel original (wearpawket)

38 pruebas medidas por computadora. Tercera columna = reel de la tienda (pocketpupp) como control.

## Resultados más fuertes

| Prueba | Original | Tuya | Tienda | Qué significa |
|---|---|---|---|---|
| Luz en la cara arriba-abajo | **+31.9** | **−9.4** | +29.5 | En las reales la frente está más iluminada que la barbilla (luz del techo). En la tuya es al revés: luz de frente/abajo, como flash o estudio. |
| Dirección de luz cara 1 / cara 2 | −10.7 / −24.2 (ambas desde la derecha) | **+19.5 / −8.1** (una desde la izq., otra desde la der.) | — | En la tuya cada persona está iluminada por una luz distinta → parecen pegadas. |
| % brillos (>225) | 3.43 | **0.28** (−92%) | 2.03 | No hay blancos ni reflejos reales. |
| Blanco más claro | 244 | **221** | 254 | Nada llega a blanco → todo gris y apagado. |
| Colorido (Hasler) | 84.4 | **49.4** (−41%) | 75.9 | Colores pobres, "lavados". |
| Colores distintos | 254 | **148** (−42%) | 166 | Paleta reducida → look de filtro IA. |
| Calidez del fondo R/B | 2.11 | **1.42** (−33%) | 1.18 | El centro comercial real brilla cálido; el tuyo es gris neutro. |
| Ruido en sombras | 8.6 | **4.7** (−45%) | 12.0 | Una cámara real mete ruido; la tuya está demasiado limpia. |
| Ruido en luces | 19.8 | **8.9** (−55%) | 17.8 | Igual. |
| % zonas totalmente lisas | 16.5% | **1.1%** (−93%) | 20.2% | En las reales hay zonas lisas (uniforme negro, pared). En la tuya TODO tiene textura → detalle inventado. |
| Patrón repetido (FFT) | 519 | **937** (+81%) | 596 | Confirma la cuadrícula artificial en la tela. |
| Detalle global | 27.0 | **17.3** (−36%) | 24.8 | Menos detalle real a pesar de verse "crujiente". |
| Detalle fondo/caras | 2.30 | **1.23** (−46%) | 1.96 | En las reales el fondo tiene más detalle que las caras; en la tuya están parejos. |
| Profundidad de sombras en cara | 74.8 | **88.6** (+18%) | 84.7 | Sombras más duras en la cara sin brillos → look dramático/serio. |

## Preguntas que me hice y respuestas

1. **¿Por qué se ve "falsa" si tiene mucho detalle?** Porque el detalle es inventado: no hay ruido de cámara (−45/−55%) pero no hay ni una zona lisa (1% vs 16%). Una cámara real produce ruido y deja zonas lisas; la IA pinta textura en todo.
2. **¿Por qué las personas parecen pegadas?** Dos razones medidas: cada cara tiene la luz de un lado distinto, y la piel y el fondo tienen calidez casi igual (0.25 de diferencia contra 0.47 en la original). En una foto real el ambiente cálido y la piel se distinguen pero comparten la misma luz.
3. **¿Por qué se ve "muerta"?** Ningún píxel llega a blanco (máx. 221) y casi no hay reflejos (0.28%). Sin brillos no hay vida.
4. **¿Por qué se ve como póster/estudio y no como celular?** La luz viene de frente/abajo (−9.4) en vez de desde arriba (+31.9). Los centros comerciales y tiendas tienen luz de techo; la foto de estudio tiene luz frontal.
5. **¿Por qué los colores no "pegan"?** Paleta 42% más pequeña y colorido 41% menor: la IA aplicó una gradación uniforme que aplana los colores.
6. **¿La sudadera tiene textura real?** No: el pico FFT +81% indica un patrón repetido (cuadrícula), típico del escalado o de la IA.
7. **¿El fondo está bien?** Le falta calidez (R/B 1.42 vs 2.11) y detalle relativo (1.23 vs 2.30). El de la original brilla dorado y está más detallado que las personas.
8. **¿Es la nitidez el problema?** No sola. Tienes menos detalle real (−36%) pero la sensación es "crujiente" porque la textura es uniforme y artificial.
9. **¿La compresión influye?** No: bloques JPEG igual en las tres (≈1.0).
10. **¿El tono de piel está mal?** Un poco más amarillo (18° vs 10°), pero la tienda también está en 18°. No es lo principal.

## Qué arreglar (en orden de impacto)
1. **Luz desde arriba, una sola fuente para todos:** "overhead mall ceiling lights from above, the same light falling on everyone, foreheads and noses catching highlights".
2. **Brillos reales:** "bright clean whites, glowing Christmas lights, shiny skin highlights".
3. **Ambiente cálido:** "warm golden mall ambience".
4. **Quitar la textura inventada y añadir ruido real:** "smooth plain fabric with no pattern, natural phone camera noise, plain dark uniforms". En CapCut: desenfoque 0.3 + grano.
5. **No escalar** la imagen en Flow (genera directo en 2K).
