import os

ruta = input("📂 Escribe la ruta de la carpeta que quieres revisar:\n→ ")

# Si la ruta no es absoluta, asumimos que está dentro del HOME
if not os.path.isabs(ruta):
    ruta = os.path.join(os.path.expanduser("~"), ruta)
else:
    ruta = os.path.expanduser(ruta)

ruta = os.path.abspath(ruta)
print(f"\n🔎 Ruta procesada: {ruta}\n")

if os.path.exists(ruta):
    print(f"🔍 Analizando carpeta: {ruta}\n")
    encontrados = 0

    for carpeta_actual, subcarpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith(".exe") or archivo.endswith(".bat"):
                print(f"⚠️ Archivo sospechoso: {archivo} → en: {carpeta_actual}")
                encontrados += 1

    if encontrados == 0:
        print("\n✅ Todo limpio. No se encontraron archivos .exe o .bat.")
else:
    print("❌ Error: la carpeta que escribiste no existe.")
