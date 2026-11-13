# Investigación: por qué las imágenes IA se ven falsas y cómo llegan al realismo los anuncios virales

## 1. El video original (wearpawket)
- **Wearpawket es una marca real** que vende la "Pawket Pet Pouch Hoodie" (sudadera de sherpa con bolsa con cierre para perros/gatos de hasta 15 lb). Su página dice tener 4.8 estrellas y más de 20 mil valoraciones (dato del propio vendedor, no verificado). Fuente: wearpawket.store/products/pawket (vía búsqueda; la página no se pudo abrir desde aquí).
- **No pude confirmar si el reel de los policías es IA o grabación real.** Las señales que creí ver (letras raras en la placa) no sirven: la captura es de 640 px comprimida por Instagram. Al ser una marca real con producto físico, **es muy posible que sea grabado con actores**.
- Conclusión: puede que estuviéramos comparando imágenes IA contra una grabación real.

## 2. Qué dice la ciencia
**Estudio con 50,444 participantes (arXiv 2502.11989, "Characterizing Photorealism and Artifacts in Diffusion Model-Generated Images"):**
- **La curación humana es lo que más engaña:** cuando una persona elige las mejores imágenes de muchas generaciones, son más difíciles de detectar que el 84% de las imágenes sin elegir hechas con los mismos prompts.
- **Cuanto más compleja la escena, más errores aparecen y más fácil es detectarla.** Más personas, objetos y texto significan más oportunidades de fallar.
- **El tiempo que se mira importa:** con más tiempo, la gente detecta más. En un reel se ve 1–2 segundos.

**Everypixel (2026):** la gente acierta solo entre un 29 y un 63% al identificar imágenes IA. Lo que todavía las delata: geometría inconsistente, luz poco realista e imágenes "demasiado perfectas".

**SAGE 2026 ("AI slop"):** las imágenes IA tienen una estética "pulida, inquietante, casi hiperreal". Lo falso no es la mala calidad: es el exceso de perfección.

## 3. Lo que delata una imagen IA (consenso de las fuentes)
1. **Perfección:** piel sin defectos, simetría, luz uniforme, todos guapos.
2. **Inconsistencia de la escena:** cada detalle se ve bien por separado, pero el conjunto no cuadra (luz, escala, física).
3. **Texto:** "sopa de letras" en letreros, placas y paredes.
4. **Ojos:** "muertos", sin brillo, o demasiado abiertos.
5. **Manos y proporciones:** cuellos o brazos raros. La IA arma el cuerpo por partes.
6. **Plausibilidad:** ¿podría pasar esto de verdad?

## 4. Métodos que funcionan (tutoriales verificados)
**Curious Refuge, "How to Create the Most Realistic AI Images Possible"** (84k vistas). Probaron sus imágenes contra fotos reales y Gemini solo acertó 2 de 9:
1. **Prompt estructurado con datos de cámara:** "iPhone 16 Pro, 1x, f/2, raw, unedited", ISO, grano, luz natural y artefactos sutiles de lente.
2. **Re-prompting (el más potente):** subes una **FOTO REAL** a Gemini, le pides "write a prompt to generate this image with Nano Banana Pro" y luego cambias solo el contenido (personas, producto). Así heredas la luz, el color y la cámara de una foto real.
3. **Generar muchas (4–12 a la vez) y elegir la mejor.** Es iterativo y nunca sale a la primera.
4. **Pasada final de imperfección** en Photoshop: desenfoque leve en zonas, grano o textura de película, polvo y rayones sutiles. "El problema de las imágenes IA es que son demasiado perfectas."
5. Una referencia de imagen directa copia demasiado; el re-prompting da más flexibilidad.

**Higgsfield y Dan Kieft (vistos antes):** hojas de referencia de producto, pruebas en movimiento, mapa o esquema de posiciones, "el anuncio final son los mejores segundos de 100 intentos", técnicas de cámara humana y bajar la resolución a propósito.

## 5. Conclusiones para tu caso
1. **Si quieres realismo garantizado, graba con personas reales** (lo más probable es que wearpawket lo hiciera así). La IA sirve para probar ideas o para tomas imposibles.
2. **Si usas IA:**
   - **Simplifica la escena:** menos personas, nada de texto en paredes, placas pequeñas o tapadas. Cada elemento extra es una oportunidad de error.
   - **Re-prompting desde una foto REAL** de un centro comercial (no desde un frame de anuncio).
   - **Genera muchas y elige.** La curación es lo que más engaña.
   - **Añade imperfección al final:** desenfoque en zonas, grano y compresión.
   - **Júzgala como la verá la gente:** en movimiento, en el celular y 1–2 segundos. No con zoom.

## Fuentes
- Wearpawket: https://wearpawket.store/products/pawket
- Estudio 50k participantes: https://arxiv.org/pdf/2502.11989
- Everypixel: https://journal.everypixel.com/trust-in-ai-images
- SAGE 2026: https://journals.sagepub.com/doi/10.1177/08944393251361449
- Why AI images look fake (13 causas): https://genimagepro.com/blog/why-ai-images-look-fake
- Plastic skin: https://medium.com/ai-analytics-diaries/your-ai-photos-look-fake-heres-how-to-fix-plastic-looking-skin-746202ceb7de
- Curious Refuge (YouTube): https://www.youtube.com/watch?v=gEHe1-1futI
- 6 formas de detectar IA (YouTube): https://www.youtube.com/watch?v=APRo-b6eHy8
- Higgsfield 3-step workflow: https://www.youtube.com/watch?v=3rDs6FhFoUQ
- Dan Kieft realismo: https://www.youtube.com/watch?v=2hJsvDSPWYM
