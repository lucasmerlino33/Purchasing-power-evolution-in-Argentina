from pathlib import Path
import pandas as pd

# Base del proyecto (donde está tu script)
base_path = Path(__file__).resolve().parent

# Ruta input
input_path = base_path / "../data/01.raw/Indice de contratos de Locacion (ICL).xlsx"

# Ruta output
output_path = base_path / "../data/02.clean/icl_mensual.xlsx"

# Crear carpeta si no existe
output_path.parent.mkdir(parents=True, exist_ok=True)

# Leer archivo
df = pd.read_excel(input_path)

# Asegurar formato fecha
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Agrupar por mes y tomar último valor
df["Periodo"] = df["Fecha"].dt.to_period("M")

df_mensual = (
    df.sort_values("Fecha")
      .groupby("Periodo")
      .last()
      .reset_index()
)

df_mensual["Fecha"] = df_mensual["Periodo"].dt.to_timestamp()
df_mensual = df_mensual.drop(columns=["Periodo"])

# Normalizar periodo a fecha (primer día del mes)
df_mensual["Fecha"] = df_mensual["Fecha"].dt.to_period("M").dt.to_timestamp()

# Forzar julio 2020 = 100
df_mensual.loc[df_mensual["Fecha"] == "2020-07-01", "Valor"] = 100

# Guardar
df_mensual.to_excel(output_path, index=False)

print("Archivo generado en:", output_path)