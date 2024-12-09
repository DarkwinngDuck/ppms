import math

temperature = 300
n = 0.2
seebeck = 400 
sigma = 31.72

def calculate_mu_0(mu, m_star, temperature, n):
    """
    Calculate the value based on the given inputs h, j, a, and b.

    Args:
    h (float): The value of H2 in the Excel formula.
    j (float): The value of J2 in the Excel formula.
    a (float): The value of A2 in the Excel formula.
    b (float): The value of B2 in the Excel formula.

    Returns:
    float or str: The calculated result if j is not empty, otherwise an empty string.
    """
    if m_star:  # Check if J2 (j) is not empty
        term = (1 + (m_star * temperature / 300) ** (-3 / 2) * n / (2 * 2.509412225)) ** (1 / 3)
        return mu * term
    return ""

def calculate_effective_mass(temperature, n, seebeck):
    """
    Calculate the value based on the given inputs a, b, and c.

    Args:
    a (float): The value of A2 in the Excel formula.
    b (float): The value of B2 in the Excel formula.
    c (float): The value of C2 in the Excel formula.

    Returns:
    float or str: The calculated result if a, b, and c are not empty, otherwise an empty string.
    """
    if temperature and n and seebeck:  # Check if a, b, and c are not empty
        numerator = n / 2.509412225
        exponent = abs(seebeck) / 86.17333262 - 2
        term = math.exp(exponent) - 1.075 * math.exp(-2)
        result = (numerator * term) ** (2 / 3) * 300 / temperature
        return result
    return ""

def calculate_mu(n, sigma):
    """
    Calculate the mu based on sigma and n.
    
    Args:
    n (float): The value of B2 in the Excel formula.
    d (float): The value of D2 in the Excel formula.
    
    Returns:
    float or str: The calculated result if both b and d are not empty, otherwise an empty string.
    """
    if n and sigma:  # Check if both b and d are not empty
        return sigma / 1.6021766341 / n
    return ""

def calculate_PF(n, seebeck, sigma):
    """
    Calculate the value based on the given inputs b, c, and d.

    Args:
    b (float): The value of B2 in the Excel formula.
    c (float): The value of C2 in the Excel formula.
    d (float): The value of D2 in the Excel formula.

    Returns:
    float or str: The calculated result if b, c, and d are not empty, otherwise an empty string.
    """
    if n and seebeck and sigma:  # Check if b, c, and d are not empty
        return sigma * seebeck**2 * 0.000001
    return ""

def calculate_weighted_mobility(seebeck, sigma):
    """
    Calculate the value based on the given inputs c and d.

    Args:
    c (float): The value of C2 in the Excel formula.
    d (float): The value of D2 in the Excel formula.

    Returns:
    float or str: The calculated result if c and d are not empty, otherwise an empty string.
    """
    if seebeck and sigma:  # Check if both c and d are not empty
        term1 = sigma / 4.02052163221989
        exp_term = math.exp(seebeck / 86.17333262 - 2) - 1.075 * math.exp(-2)
        term2 = (1 + 0.5 / exp_term) ** (1 / 3)
        result = term1 * exp_term * term2
        return result
    return ""

def calculate_mu_W(temperature, mu_wt):
    """
    Calculate the value based on the given inputs a and m.

    Args:
    a (float): The value of A2 in the Excel formula.
    m (float): The value of M2 in the Excel formula.

    Returns:
    float or str: The calculated result if a and m are not empty, otherwise an empty string.
    """
    if temperature and mu_wt:  # Check if both a and m are not empty
        return mu_wt * (300 / temperature) ** (3 / 2)
    return ""

def calculate_PF_opt(mu_wt):
    """
    Calculate the value based on the given input m.

    Args:
    m (float): The value of M2 in the Excel formula.

    Returns:
    float or str: The calculated result if m is not empty, otherwise an empty string.
    """
    if mu_wt:  # Check if m is not empty
        return 0.12122458 * mu_wt
    return ""

def calculate_n_opt(n, seebeck):
    """
    Calculate the value based on the given inputs b and c.

    Args:
    b (float): The value of B2 in the Excel formula.
    c (float): The value of C2 in the Excel formula.

    Returns:
    float or str: The calculated result if b and c are not empty, otherwise an empty string.
    """
    if n and seebeck:  # Check if both b and c are not empty
        exp_term = math.exp(seebeck / 86.17333262 - 2) - 1.075 * math.exp(-2)
        return 1.255 * n * exp_term
    return ""


effective_mass = calculate_effective_mass(temperature, n, seebeck)
mu = calculate_mu(n, sigma)
mu_zero = calculate_mu_0(mu, effective_mass, temperature, n)
pf = calculate_PF(n, seebeck, sigma)
weighted_mobility = calculate_weighted_mobility(seebeck, sigma)
mu_w = calculate_mu_W(temperature, weighted_mobility)
pf_opt = calculate_PF_opt(weighted_mobility)
n_opt = calculate_n_opt(n, seebeck)

print(mu)
print(effective_mass)
print(pf)
print(mu_zero)
print(mu_w)
print(weighted_mobility)
print(pf_opt)
print(n_opt)