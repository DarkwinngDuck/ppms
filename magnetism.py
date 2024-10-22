import numpy as np



def curie_weiss(T, C, thetha):
    return C / (T - thetha)


def susceptibility(df, sample_mass, sample_molecular_weight):
    TEMPERATURE = 'Temperature (K)'
    FIELD = 'Magnetic Field (Oe)'
    MOMENT = 'Moment (emu)'
    SUSCEPTIBILITY = 'Susceptibility'
    if sample_mass is None or sample_molecular_weight is None:
        raise ValueError("Sample mass and molecular weight must be valid numbers.")
    
    field = df[FIELD].replace(0, np.nan)
    moment = df[MOMENT]
    df[SUSCEPTIBILITY] = (moment / field) * (1 / sample_mass) * sample_molecular_weight
    
    return df[[TEMPERATURE, FIELD, MOMENT, SUSCEPTIBILITY]]
