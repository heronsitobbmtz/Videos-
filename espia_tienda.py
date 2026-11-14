"""Espia de tiendas Shopify (gratis, sin dependencias).

Uso:
    python espia_tienda.py latienda.com
    python espia_tienda.py latienda.com --comparar   (compara con la ultima vez que la revisaste)

Que hace:
  1. Comprueba si la tienda es Shopify.
  2. Lista sus productos mas vendidos EN ORDEN (pagina publica best-selling de Shopify).
  3. Lee su catalogo publico (/products.json): precios, fecha de cada producto, edad de la tienda.
  4. Guarda una foto (snapshot) para comparar en unos dias: productos nuevos,
     productos borrados, cambios de precio y variantes que se agotan.

No muestra ventas reales: nadie puede verlas salvo el dueno. Son senales para estimar.
"""
import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
CARPETA = Path(__file__).resolve().parent / "espia_snapshots"


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "replace")


def productos(base):
    todos, page = [], 1
    while page <= 10:
        data = json.loads(get(f"{base}/products.json?limit=250&page={page}"))
        lote = data.get("products", [])
        if not lote:
            break
        todos += lote
        page += 1
        time.sleep(1)
    return todos


def mas_vendidos(base):
    html = get(f"{base}/collections/all?sort_by=best-selling")
    orden = []
    for h in re.findall(r'/products/([a-z0-9\-]+)', html):
        if h not in orden:
            orden.append(h)
    return orden


def fecha(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def resumen(base, prods, top):
    por_handle = {p["handle"]: p for p in prods}
    ahora = datetime.now(timezone.utc)
    creados = [fecha(p.get("created_at")) for p in prods if p.get("created_at")]
    print(f"\n=== {base}")
    print(f"Productos en el catalogo: {len(prods)}")
    if creados:
        mas_viejo = min(creados)
        print(f"Producto mas antiguo: {mas_viejo:%Y-%m-%d}  (la tienda vende desde hace ~{(ahora - mas_viejo).days} dias)")
    print("\nMAS VENDIDOS (orden real de Shopify):")
    for i, h in enumerate(top[:15], 1):
        p = por_handle.get(h)
        if not p:
            print(f"  {i:2d}. {h}")
            continue
        precios = [float(v["price"]) for v in p.get("variants", []) if v.get("price")]
        agotadas = sum(1 for v in p.get("variants", []) if v.get("available") is False)
        c = fecha(p.get("created_at"))
        dias = (ahora - c).days if c else "?"
        rango = f"{min(precios):.2f}-{max(precios):.2f}" if precios else "?"
        print(f"  {i:2d}. {p['title'][:60]}  | precio {rango} | subido hace {dias} dias"
              f" | variantes agotadas {agotadas}/{len(p.get('variants', []))}")
    if not top:
        print("  (no se pudo leer la pagina best-selling)")


def snapshot(prods):
    snap = {}
    for p in prods:
        snap[p["handle"]] = {
            "titulo": p["title"],
            "updated_at": p.get("updated_at"),
            "precios": sorted(float(v["price"]) for v in p.get("variants", []) if v.get("price")),
            "agotadas": sorted(str(v["id"]) for v in p.get("variants", []) if v.get("available") is False),
        }
    return snap


def comparar(viejo, nuevo):
    print("\nCAMBIOS DESDE LA ULTIMA REVISION:")
    nuevos = set(nuevo) - set(viejo)
    borrados = set(viejo) - set(nuevo)
    for h in nuevos:
        print(f"  + producto nuevo: {nuevo[h]['titulo']}")
    for h in borrados:
        print(f"  - producto borrado (probablemente no vendia): {viejo[h]['titulo']}")
    for h in set(viejo) & set(nuevo):
        a, b = viejo[h], nuevo[h]
        if a["precios"] != b["precios"]:
            print(f"  $ cambio de precio en {b['titulo']}: {a['precios']} -> {b['precios']}")
        nuevas_agotadas = set(b["agotadas"]) - set(a["agotadas"])
        if nuevas_agotadas:
            print(f"  ! {len(nuevas_agotadas)} variante(s) se agotaron en {b['titulo']} (senal de ventas)")
    if not (nuevos or borrados):
        print("  (sin productos nuevos ni borrados)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    dominio = sys.argv[1].replace("https://", "").replace("http://", "").strip("/")
    base = f"https://{dominio}"
    try:
        prods = productos(base)
    except Exception as e:
        print(f"No parece una tienda Shopify o bloquea el acceso ({e}).")
        return
    try:
        top = mas_vendidos(base)
    except Exception:
        top = []
    resumen(base, prods, top)

    CARPETA.mkdir(exist_ok=True)
    archivo = CARPETA / f"{dominio}.json"
    nuevo = snapshot(prods)
    if "--comparar" in sys.argv and archivo.exists():
        comparar(json.loads(archivo.read_text()), nuevo)
    archivo.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1))
    print(f"\nFoto guardada en {archivo}. Vuelve en 3-7 dias con --comparar.")


if __name__ == "__main__":
    main()
