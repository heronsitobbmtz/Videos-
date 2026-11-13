# Guía: cómo se hacen los reels virales de productos (katana, paraguas, silla)

Basado en: análisis cuadro por cuadro del video que mandaste + guía oficial de Google para Veo 3.1 + guías de dropshipping 2026.

---

## 0. Lo que descubrí (y corrige cosas que te dije antes)

1. **No todo es IA.** Muchos de estos anuncios usan **videos reales del proveedor**. Casi todos los productos en AliExpress / CJ Dropshipping traen videos demo en el anuncio. Los vendedores los descargan y los re-editan (gancho + cortes + música). La katana parece de este tipo. La IA se usa sobre todo para tomas imposibles o caras de grabar (el paraguas cilindro es IA: el producto no puede existir así).
2. **Los cortes son MUCHO más rápidos de lo que te dije.** Medí los cortes del video de la katana: después del gancho hay un corte cada **0.5 a 1 segundo** (4.1s, 4.9s, 5.7s, 6.9s, 7.5s, 8.0s, 8.5s, 9.0s, 9.6s, 10.1s). Van al ritmo de la música (~120 BPM = 1 corte por beat). Yo te había dicho 1.5–2 s: estaba mal.
3. **Veo puede hacer varias tomas coherentes en UN solo video** con "timestamp prompting" (abajo). Esto arregla tu problema de coherencia: mismo cuarto, misma luz, mismo producto.
4. **No escribas "no X" en Veo.** Google recomienda describir lo que SÍ quieres ("una calle vacía" en vez de "sin gente"). Yo te puse muchos "no ..." — quítalos.

---

## 1. La estructura viral (fórmula exacta de los 3 videos)

| Tiempo | Parte | Qué pasa | Ejemplo katana |
|---|---|---|---|
| 0–1.5 s | **Gancho** | Texto grande arriba + imagen que intriga. El texto NO dice qué es el producto. | "Do NOT show this to a Anime lover..." + caja larga misteriosa |
| 1.5–4 s | **Revelación** | Se muestra el producto (unboxing, antes/después) | Abrir la caja, katana blanca |
| 4–8 s | **Ritual / demo** | Cortes rápidos (0.5–1 s) mostrando cómo se usa | Aceite, ponerla en el soporte, control remoto |
| 8–11 s | **Momento WOW** | La toma más espectacular, se queda un poco más | Humo + LED |
| 11 s+ | **CTA + loop** | "Comment X if you want one" y corta de golpe para que se repita | Vuelve a la caja |

**Fórmulas de gancho que usaron:**
- "Do NOT show this to a [tipo de persona]..." → curiosidad + público objetivo
- "The Problem 😩 / VS... / The Solution 🤩" → antes/después
- "Bro refuses to [acción]..." / "The old heads bout to call the cops 💀" → humor meme, no parece anuncio

**CTA:** "Comment [PALABRA] if you want one" + ManyChat manda el link por DM. Cada comentario = más alcance.

**Duración total:** 10–15 s. Corto para que se vea 2–3 veces (loop).

---

## 2. Ruta A (la más fácil y la de mejor calidad): video real del proveedor

1. Busca el producto en AliExpress / CJ / Alibaba (`katana humidifier`, `sword aroma diffuser LED`).
2. Descarga los videos del anuncio (y pide más al proveedor por chat; muchos los mandan gratis).
3. En CapCut: corta cada toma a 0.5–1 s, al beat de una canción en tendencia.
4. Pon el gancho arriba (0–4 s) y el CTA después.
5. Usa IA solo para la toma WOW si el video del proveedor no la tiene.

⚠️ TikTok penaliza videos reposteados sin cambios ("contenido no original"). Re-edítalos de verdad: tu gancho, tu orden, tu música, recortes, zoom.

---

## 3. Ruta B: todo con IA (Nano Banana Pro + Veo 3.1 en Flow)

### Paso 1 — Imágenes de referencia ("ingredientes")
En Nano Banana Pro haz 3 imágenes limpias:
- **[PRODUCTO]**: la katana sola, fondo neutro (a partir de la foto del proveedor).
- **[CUARTO]**: el cuarto blanco gamer vacío.
- **[MANOS]** (opcional): manos con suéter blanco y anillos plateados.

### Paso 2 — "Ingredients to Video" en Flow
Sube las 3 imágenes y en el prompt nómbralas: "Using the provided images for the katana, the room and the hands...". Veo mantiene el mismo producto y cuarto en cada toma.

### Paso 3 — Timestamp prompting (varias tomas en un clip de 8 s)
Fórmula de Google para cada toma: **[Cámara] + [Sujeto] + [Acción] + [Contexto] + [Estilo]**. Audio con `SFX:` y `Ambient noise:`.

**Clip 1 (0–8 s) — gancho + revelación + ritual:**
```
Using the provided images for the white katana, the white gaming bedroom and the hands.
Handheld iPhone footage, amateur vertical video, soft daylight, cool white tones, slight grain.

[00:00-00:02] POV shot looking down, two hands in a white knit sweater lift a long white box with the word "BladeMist" and tilt it toward the camera. SFX: cardboard sliding.
[00:02-00:04] POV close-up, the box lid opens revealing the white katana lying in black foam with a white ribbon. SFX: soft gasp.
[00:04-00:05] Close-up, a hand with silver rings drips oil from a glass dropper into the top of the katana handle. SFX: soft drip.
[00:05-00:06] Medium close-up, the hand lowers the katana onto a black wooden stand on the white desk. SFX: soft wooden click.
[00:06-00:08] POV, the thumb presses a small white remote; the katana blade lights up with bright white LED. SFX: click and soft electronic beep.
Ambient noise: quiet bedroom.
```

**Clip 2 (0–8 s) — momento WOW:**
```
Using the provided images for the white katana and the white gaming bedroom.
Handheld iPhone footage, vertical, daylight mixed with a blue LED strip, slight grain.

[00:00-00:03] Low angle from the desk surface beside the handle, the katana rests on its black stand with its blade glowing white; thick white mist pours out of the top of the blade and rises in slow swirling clouds. SFX: soft humidifier hiss.
[00:03-00:05] Slow push-in along the glowing blade as the mist rolls down over the stand onto the desk.
[00:05-00:08] Extreme close-up of the glowing LED strip along the blade, mist drifting across it, the keyboard softly blurred behind.
Ambient noise: calm room.
```

Consejos:
- Usa **Veo 3.1 Fast** para probar (barato), **Quality** para el final. (Fast/Quality se retiran el 5 dic 2026 → luego Omni Flash 1.2 / Veo 3.1 Lite.)
- Genera 4 versiones de cada clip y elige.
- Si una toma sale mal, rehaz solo esa con **First frame** (imagen fija) o **First + Last frame**.

### Paso 4 — Montaje en CapCut
- Corta cada toma a **0.5–1 s** al beat (usa "Auto beat" de CapCut). Deja el WOW 2–3 s.
- Texto gancho 0–4 s, CTA desde el WOW.
- Grano leve, nitidez −10, exporta 1080p.
- Termina en corte seco para que haga loop.

---

## 4. Para el video tipo paraguas (antes/después)

1. Foto "antes" (persona + producto normal) en Nano Banana.
2. EDITA esa misma foto: "keep everything the same, only add [producto]". → foto "después" idéntica.
3. "VS..." = corte seco de foto antes a foto después.
4. Tomas "Problem": POV con **First + Last frame** (frame sin salpicar → frame con salpicadura ya hecha en Nano Banana). Así el coche SÍ salpica.

---

## 5. Checklist antes de publicar
- [ ] ¿Gancho en el primer segundo, sin decir qué es el producto?
- [ ] ¿Cortes de 0.5–1 s al ritmo?
- [ ] ¿Mismo producto/cuarto/manos en todas las tomas?
- [ ] ¿Manos con 5 dedos, texto legible, física creíble?
- [ ] ¿El producto se ve como el real? (si no → devoluciones)
- [ ] ¿Etiqueta "AI info" si es contenido realista generado (regla de Meta)?
- [ ] ¿ManyChat configurado con la palabra del CTA?

---

## Fuentes
- Google Cloud — Ultimate prompting guide for Veo 3.1: https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- Google Flow Help — modelos: https://support.google.com/flow/answer/16352836?hl=en
- InReels — Product video ads for dropshippers: https://www.inreels.ai/blog/product-video-ads-for-dropshippers
- Ryze — TikTok dropshipping (contenido reusado): https://www.get-ryze.ai/blog/tiktok-dropshipping
- GISuser — Product still to motion brief (Veo): https://gisuser.com/2026/11/from-product-still-to-motion-brief-a-veo-3-ai-video-generator-workflow-for-short-ad-concepts/
- Lead Stories — paraguas IA viral: https://leadstories.com/hoax-alert/2026/04/fact-check-video-of-floating-drone-powered-umbrella-is-not-real.html
- inro — Reels 3-second hook: https://inro.social/blog/instagram-reels-3-second-hook-leads
- ManyChat — Comment to DM: https://get.manychat.com/use-case/comment-to-dm
