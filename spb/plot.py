import math
import matplotlib.pyplot as plt

# Constants
effective_mass = 1.05 
mu_zero = 99 
temperature = 1200
min_n = 1.0e18
max_n = 1.0e21

# Experimental values
n_exp = 0.20
S_exp = 400.00
mu_exp = 99.00
Pf_exp = 1.6021766341 * n_exp * mu_exp * (S_exp ** 2) * 0.000001 

# Calculate 'n' values
def calculate_n(min_n, max_n, index):
    result = 10 ** (
        math.log10(min_n) + (index - 1) * (math.log10(max_n) - math.log10(min_n)) / 100 - 19
    )
    return result

# Order of indices
order = list(range(1, 102))
ns = [calculate_n(min_n, max_n, index) for index in order]

# Calculate Seebeck values
def calculate_seebeck(effective_mass, temperature, n):
    result = 86.17333262 * math.log(
        1.075 + 2.509412225 * ((effective_mass * temperature / 300) ** (3/2)) * math.exp(2) / n
    )
    return result

seebecks = [calculate_seebeck(effective_mass, temperature, n) for n in ns]

# Calculate Mu values
def calculate_mu(mu_zero, effective_mass, temperature, n):
    result = mu_zero / (
        (1 + ((effective_mass * temperature / 300) ** (-3 / 2)) * n / 2 / 2.509412225) ** (1 / 3)
    )
    return result

mus = [calculate_mu(mu_zero, effective_mass, temperature, n) for n in ns]

# Calculate Power Factor (PF)
def calculate_PF(n, seebeck, mu):
    if n != "" and seebeck != "" and mu != "":
        result = 1.6021766341 * n * mu * (seebeck ** 2) * 0.000001
        return result
    else:
        return None 

power_factors = [calculate_PF(n, seebeck, mu) for n, seebeck, mu in zip(ns, seebecks, mus)]

fig, [pisarenko, carrier_mobility, power_factor] = plt.subplots(3, 1, figsize=(10, 15))

pisarenko.plot(ns, seebecks, label='S(n)', color='b')
pisarenko.scatter([n_exp], [S_exp], color='red', label='Experimental S(n)')  # Experimental point
pisarenko.set_title('Pisarenko Plot')
pisarenko.set_xlabel('n (log scale)')
pisarenko.set_ylabel('Seebeck (S(n))')
pisarenko.set_xscale('log')  # Logarithmic scale for x-axis
pisarenko.grid(True)
pisarenko.legend()

carrier_mobility.plot(ns, mus, label='μ(n)', color='g')
carrier_mobility.scatter([n_exp], [mu_exp], color='red', label='Experimental μ(n)')
carrier_mobility.set_title('Carrier Mobility')
carrier_mobility.set_xlabel('n (log scale)')
carrier_mobility.set_ylabel('Mu (μ(n))')
carrier_mobility.set_xscale('log')
carrier_mobility.grid(True)
carrier_mobility.legend()

power_factor.plot(ns, power_factors, label='PF', color='r')
power_factor.scatter([n_exp], [Pf_exp], color='red', label='Experimental PF(n)') 
power_factor.set_title('Power Factor')
power_factor.set_xlabel('n (log scale)')
power_factor.set_ylabel('Power Factor PF(n, S, μ)')
power_factor.set_xscale('log')
power_factor.grid(True)
power_factor.legend()

plt.tight_layout()
plt.show()
