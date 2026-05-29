import pandas as pd
import matplotlib.pyplot as plt

# Lectura del dataset utilizando rutas relativas
ventas = pd.read_csv("datos/ventas.csv")

# Se calcula el importe total por registro
ventas["total"] = ventas["cantidad"] * ventas["precio"]

# Indicador: ventas totales
ventas_totales = ventas["total"].sum()

# Indicador: producto más vendido
producto_mas_vendido = (
    ventas.groupby("producto")["cantidad"]
    .sum()
    .idxmax()
)

# Conversión de fecha
ventas["fecha"] = pd.to_datetime(ventas["fecha"])

# Ventas por mes
ventas["mes"] = ventas["fecha"].dt.to_period("M")

ventas_mes = (
    ventas.groupby("mes")["total"]
    .sum()
)

# Guardado del resumen
with open("resultados/resumen_ventas.txt", "w", encoding="utf-8") as archivo:
    archivo.write(f"Ventas Totales: ${ventas_totales}\n")
    archivo.write(f"Producto Más Vendido: {producto_mas_vendido}\n")
    archivo.write("\nVentas por Mes:\n")
    archivo.write(str(ventas_mes))

# Gráfico
ventas_mes.plot(kind="bar")

plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto")

plt.tight_layout()

plt.savefig("resultados/grafico_ventas.png")

print("Proceso finalizado correctamente.")
