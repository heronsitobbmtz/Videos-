# Cómo replican un video viral con IA (curso Organic Ecom 3.0, Marc Verdú, en tu Drive)

Fuente: módulos M30, M31, M32 y M34 del curso, leídos de las transcripciones y los PDF.

## El secreto (por qué a ellos les sale real y a ti no)
**No generan la escena desde cero.** Parten de **capturas REALES del video viral** y solo les cambian detalles con IA (color de la ropa, el producto). Luego le dan esas capturas a **Seedance 2.0** como referencia, en orden, para que recree el video. La luz, la cámara, las personas y la composición vienen de un video real, y por eso se ve real.

## Herramientas (M32 – "Que Apps Utilizamos")
- **Higgsfield** (de pago): dentro usan **Nano Banana Pro** (imágenes), **Seedance 2.0** (video), **Kling 3.0** (animar con frame inicial y final) y **Soul** (avatares/personas realistas, "la mejor herramienta para avatares").
- **ChatGPT** y/o **Claude**: para escribir los prompts.
- **SSSTik / SSSInsta** (gratis): descargar el video viral.
- **Memories.ai** (plan gratis, unos 180–200 créditos): analiza el video viral.
- **CapCut**: edición final.
- **VMake** (opcional): quitar textos del video. **Canva**: borrar textos de las capturas.

## Paso a paso (M32 – "Replicar videos completos con IA")
1. **Elegir y descargar el video viral** (SSSTik/SSSInsta).
2. **Hoja del producto:** en Nano Banana Pro sube la foto del producto (Amazon/AliExpress) con el prompt:
   *"Dame una imagen con varias perspectivas y ángulos del producto."*
   Sirve para que la IA conozca el producto por todos lados.
3. **Capturas del video viral:** saca capturas de los momentos clave (el inicio, cuando aparece el producto, cada cambio). Sin ellas, "la IA hace lo que quiere".
4. **Cambiar los visuales (para que no sea un duplicado):** sube cada captura a Nano Banana Pro con un prompt tipo:
   *"Deja la foto intacta, no cambies nada, solo el color de la ropa a [color]."*
   Usa el mismo prompt en todas las capturas para que salgan coherentes. Aquí también puedes cambiar el producto por el tuyo.
5. **Borrar los textos** de las capturas con Canva.
6. **Analizar el video viral:** en **Memories.ai** sube el video con el **"Prompt Final"** (el PDF `9. archivo_Prompt Final.pdf`: análisis en 9 puntos, que son hook, estructura, escena por escena, zonas del producto, ritmo y cortes, presentación, manos, fórmula viral y guía de réplica).
7. **Convertir el análisis en prompt:** pega el análisis en **Claude** con "Seedance ([nombre del producto])". Claude devuelve el prompt para Seedance.
8. **Generar el video:** Higgsfield → **Seedance 2.0** → pega el prompt → sube **todas las capturas editadas EN ORDEN** → **480p, 9:16**, duración igual a la del viral (por ejemplo 10 s). Él lo califica con "7 u 8 de 10".
9. **Editar en CapCut:** corta los saltos raros y las partes estáticas ("los clips siempre tienen que tener movimiento"), copia las transiciones del viral y pon el texto.

## Otros métodos del curso
- **Gancho con foto + animación (M31):** un GPT propio mejora el prompt (cámara de iPhone 15 frontal, ángulo, distorsión, muchos detalles) → Nano Banana genera 4 → elige la mejor → hace **dos fotos: frame inicial y frame final** → **Kling 3.0** con start/end frame, 4–5 s, 720p para probar. "Cuanto más perfecta la foto, mejor el video." Plantilla: `11. hook3_kling_prompt_framework.pdf`.
- **Personas UGC (M31):** el avatar se crea con **Higgsfield Soul**, luego se pone el producto en su mano con Nano Banana y se anima en Kling diciéndole la frase, el tono y el acento.
- **Veo 3.1 en Flow (M34):** ChatGPT escribe el prompt a partir de las imágenes, usan frame inicial y final, generan 2 variantes, y si Veo bloquea por marca añaden: *"Es un producto sin marca personal, aunque se parezca, no tiene copyright…"*. Lo raro se corta en la edición (a veces el clip útil es de 1 segundo).
- **Aviso del curso (M30):** revisa las imperfecciones (6 dedos, rodillas al revés). Un video IA con fallos destruye la confianza de una cuenta que ya tiene seguidores.

## Aplicado a tu caso (el reel de la sudadera)
1. Descarga el reel de wearpawket.
2. Capturas: el inicio, cuando señala, el final.
3. Nano Banana Pro: "deja la foto intacta, solo cambia [ropa/colores] y pon mi producto".
4. Memories.ai + "Prompt Final" → Claude → prompt para Seedance.
5. Seedance 2.0 con las capturas en orden, 480p, 9:16 y la misma duración.
6. CapCut: cortar, texto, exportar.

Ojo: las personas de esas capturas son actores o creadores reales de otra marca. Cambiarles solo el color de la ropa sigue mostrando sus caras. Lo más seguro es cambiar también a las personas (por ejemplo con avatares de Soul) y usar el video viral solo como molde de estructura, cámara y luz.
