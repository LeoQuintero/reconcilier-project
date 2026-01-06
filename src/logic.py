# generate_dummy.py
import pandas as pd
import numpy as np
import uuid
from pathlib import Path


def generate_mock_data(num_records=50):
    # 1. Crear Dataset Maestro (La verdad absoluta)
    # Usamos semillas para que siempre salga la misma data aleatoria (reproducible)
    np.random.seed(42)

    data = {
        'tx_id': [str(uuid.uuid4())[:8] for _ in range(num_records)],
        'amount': np.round(np.random.uniform(10.0, 500.0, size=num_records), 2),
        'date': pd.date_range(start='2023-01-01', periods=num_records, freq='h')
    }
    df_master = pd.DataFrame(data)

    # 2. Crear Dataframe "Ventas" (El sistema local)
    df_sales = df_master.copy()
    df_sales['source'] = 'INTERNAL_SALES'

    # 3. Crear Dataframe "Banco" (El externo con diferencias)
    df_bank = df_master.copy()
    df_bank['source'] = 'BANK_API'

    # --- INYECCIÓN DE ERRORES INTENCIONALES ---

    # CASO A: Faltantes en Banco (El banco perdió registros)
    # Borramos los últimos 5 registros
    df_bank = df_bank.iloc[:-5]

    # CASO B: Faltantes en Ventas (Cobros que el banco tiene pero nosotros no)
    # Agregamos 2 registros nuevos al banco
    new_records = pd.DataFrame({
        'tx_id': ['GHOST-01', 'GHOST-02'],
        'amount': [100.00, 250.50],
        'date': [pd.Timestamp('2023-01-02'), pd.Timestamp('2023-01-02')],
        'source': 'BANK_API'
    })
    df_bank = pd.concat([df_bank, new_records], ignore_index=True)

    # CASO C: Discrepancia de Montos
    # Al primer registro le cambiamos el monto en el banco
    df_bank.at[0, 'amount'] = df_bank.at[0, 'amount'] - 0.50

    return df_sales, df_bank


if __name__ == "__main__":
    # Definir rutas usando Pathlib (funciona en Windows/Mac/Linux igual)
    base_path = Path(__file__).parent
    output_dir = base_path / "data" / "raw"

    # Crear carpetas si no existen
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generando datos en: {output_dir}")
    sales, bank = generate_mock_data()

    sales.to_csv(output_dir / 'sales_dump.csv', index=False)
    bank.to_csv(output_dir / 'bank_extract.csv', index=False)

    print("✅ Datos generados exitosamente.")