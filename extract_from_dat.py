import pandas as pd
from magnetism import susceptibility

# TODO: refactor map
def extract_from_dat(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    TEMPERATURE = 'Temperature (K)'
    FIELD = 'Magnetic Field (Oe)'
    MOMENT = 'Moment (emu)'
    data_start = False
    data_lines = []
    sample_mass = None
    sample_molecular_weight = None
    DATA_HEADER = "[Data]"
    INFO_PREFIX = "INFO"
    

    for line in lines:
        line = line.strip()
        
        if line.startswith(DATA_HEADER):
            data_start = True
            continue
        
        if line.startswith(INFO_PREFIX):
            parts = line.split(',')
            print(f"Processing INFO line: {line}")
            if len(parts) == 3:
                try:
                    key = parts[2].strip()
                    value = float(parts[1].strip())
                    if key == "SAMPLE_MASS": 
                        sample_mass = value
                    elif key == "SAMPLE_MOLECULAR_WEIGHT":
                        sample_molecular_weight = value
                except ValueError:
                    print(f"Warning: Non-numeric value found in INFO line: {line}")
        
        if data_start and line:
            data_lines.append(line)

    data = [line.split(',') for line in data_lines]
    df = pd.DataFrame(data[1:], columns=data[0])
    df[TEMPERATURE] = pd.to_numeric(df[TEMPERATURE], errors='coerce')
    df[FIELD] = pd.to_numeric(df[FIELD], errors='coerce')
    df[MOMENT] = pd.to_numeric(df[MOMENT], errors='coerce')
    df_cleaned = df.dropna(subset=[TEMPERATURE, FIELD, MOMENT])
    try:
        dfWithSus = susceptibility(df_cleaned, sample_mass, sample_molecular_weight)
    except ValueError as e:
        print(f"Error calculating susceptibility: {e}")
        return

    dfWithSus.to_csv(output_file, index=False)
    return sample_mass, sample_molecular_weight, df
