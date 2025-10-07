import pandas as pd
from app.chains import generate_walmart_content

from app.logger import logger

def process_csv(input_path: str, output_path: str):
    logger.info("Reading CSV")
    df = pd.read_csv(input_path)
    results = []

    for _, row in df.iterrows():
        try:
            new_data = generate_walmart_content(row)
            results.append({**row.to_dict(), **new_data})
        except Exception as e:
            logger.exception(f"found Exception -> {e}")

    output_df = pd.DataFrame(results)
    output_df.to_csv(output_path, index=False)
    return output_path
