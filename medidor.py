"""Compara imagenes generadas contra una referencia y da una calificacion.

Uso: python3 medidor.py referencia.png prueba1.png [prueba2.png ...]
Recorta la barra del telefono (arriba) y la interfaz (abajo) automaticamente.
"""
import sys
from PIL import Image, ImageFilter, ImageStat


def cargar(ruta):
    im = Image.open(ruta).convert("RGB")
    w, h = im.size
    # quitar barra de estado y barra inferior / interfaz
    im = im.crop((0, int(h * 0.06), int(w * 0.85), int(h * 0.82)))
    return im.resize((540, int(540 * im.size[1] / im.size[0])))


def medir(im):
    g = im.convert("L")
    hist = g.histogram()
    n = sum(hist)
    hsv = im.convert("HSV")
    sat = ImageStat.Stat(hsv).mean[1]
    r, gr, b = ImageStat.Stat(im).mean
    lap = g.filter(ImageFilter.Kernel((3, 3), [0, 1, 0, 1, -4, 1, 0, 1, 0], 1, 128))
    return {
        "brillos %": 100 * sum(hist[225:]) / n,
        "sombras %": 100 * sum(hist[:30]) / n,
        "contraste": ImageStat.Stat(g).stddev[0],
        "saturacion": sat,
        "nitidez": ImageStat.Stat(lap).stddev[0],
        "calidez (R-B)": r - b,
    }


# peso de cada metrica en la calificacion y tolerancia
PESOS = {
    "brillos %": (25, 3.0),
    "sombras %": (10, 10.0),
    "contraste": (15, 15.0),
    "saturacion": (20, 30.0),
    "nitidez": (20, 8.0),
    "calidez (R-B)": (10, 25.0),
}


def calificar(ref, prueba):
    total = 0
    for k, (peso, tol) in PESOS.items():
        diff = abs(prueba[k] - ref[k])
        total += peso * max(0.0, 1 - diff / tol)
    return total


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    ref = medir(cargar(sys.argv[1]))
    print(f"{'imagen':30s} " + " ".join(f"{k:>14s}" for k in ref) + "   CALIF/100")
    print(f"{'REFERENCIA':30s} " + " ".join(f"{v:14.1f}" for v in ref.values()))
    for ruta in sys.argv[2:]:
        m = medir(cargar(ruta))
        print(f"{ruta[-30:]:30s} " + " ".join(f"{v:14.1f}" for v in m.values())
              + f"   {calificar(ref, m):6.0f}")
        consejos = []
        if m["brillos %"] < ref["brillos %"] * 0.5:
            consejos.append("faltan brillos: pide 'real highlights, shiny skin, glowing lights, clean whites'")
        if m["saturacion"] < ref["saturacion"] * 0.9:
            consejos.append("colores apagados: pide 'vivid Christmas red, vivid colors'")
        if m["nitidez"] < ref["nitidez"] * 0.85:
            consejos.append("poco detalle real: genera a 2K/4K, usa Quality y haz upscale")
        if m["nitidez"] > ref["nitidez"] * 1.3:
            consejos.append("demasiado afilada: quita 'ultra sharp', pide 'natural detail, no oversharpening'")
        if abs(m["calidez (R-B)"] - ref["calidez (R-B)"]) > 15:
            consejos.append("balance de color distinto: ajusta temperatura en CapCut o pide 'warm indoor light'")
        for c in consejos:
            print("   -> " + c)


if __name__ == "__main__":
    main()
