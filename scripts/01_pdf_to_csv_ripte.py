from pathlib import Path
import camelot
import pandas as pd

# 1. Ruta base (donde está tu script)
base_path = Path(__file__).resolve().parent

# 2. Ruta al PDF
pdf_path = base_path / "../data/01.raw/ripte_enero_2026-mdch.pdf"

# 3. Leer tablas del PDF
tables = camelot.read_pdf(
    str(pdf_path),
    pages="all",
    flavor="stream"   # clave para este tipo de PDF
)

# 4. Convertir todas las tablas en DataFrames
dfs = [table.df for table in tables]

# 5. Unir todo en uno solo
df = pd.concat(dfs, ignore_index=True)

# 6. Ruta de salida
output_path = base_path / "../data/01.raw/ripte_raw.csv"

# Crear carpeta si no existe
output_path.parent.mkdir(parents=True, exist_ok=True)

# 7. Guardar CSV
df.to_csv(output_path, index=False)

print("CSV guardado en:", output_path)