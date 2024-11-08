# -*- coding: utf-8 -*-
"""
Arbeidskrav 1

Oversikt over årlige driftskostnader for elbil og bensinbil, samt differanse mellom disse

RBL

2024 11 08
"""


# Totalt kjørte kilometer pr år
total_km_pr_år = 17000

# Trafikkforsikringsavgift
t_avgift_pr_dag = 8.38  # Denne er lik for begge biltyper
t_avgift_pr_år = t_avgift_pr_dag * 365 # Årlig kostnad for trafikkforsikringsavgift

# Kostnad forsikring
elbil_forsikring = 5000 # Kostnad med forsikring pr år for elbil
bensinbil_forsikring = 7500 # Kostnad med forsikring pr år for bensinbil

# Andre kostnader elbil
bomavgift_elbil_pr_km = 0.1 # Bomavgift pr kjørte kilometer
bomavgift_elbil_pr_år = bomavgift_elbil_pr_km * total_km_pr_år
strømpris = 2.0 # Kr pr kwh
drivstofforbruk_elbil_pr_km = 0.2 # kwh pr kjørte kilometer
drivstofforbruk_elbil_pr_år = drivstofforbruk_elbil_pr_km * total_km_pr_år * strømpris

# Andre kostnader bensinbil
bomavgift_bensinbil_pr_km = 0.3 # Bomavgift pr kjørte kilometer
bomavgift_bensinbil_pr_år = bomavgift_bensinbil_pr_km * total_km_pr_år # Årlig bomavgift ut fra antall kjørte kilometer
drivstofforbruk_bensinbil_pr_km = 1 # kr pr kjørte kilometer
drivstofforbruk_bensinbil_pr_år = drivstofforbruk_bensinbil_pr_km * total_km_pr_år # Årlig kostnad for drivstoff

# Utrekning av total årlig driftskostnad for bensinbil
bensinbil_totalkostnad = (t_avgift_pr_år + bomavgift_bensinbil_pr_år + drivstofforbruk_bensinbil_pr_år + bensinbil_forsikring)

# Utrekning av total årlig driftskostnad for elbil
elbil_totalkostnad = (t_avgift_pr_år + bomavgift_elbil_pr_år + drivstofforbruk_elbil_pr_år + elbil_forsikring)

# Årleg kostnadsdifferanse mellom bensinbil og elbil
kostnadsdifferanse = bensinbil_totalkostnad - elbil_totalkostnad

# Utskrift av resultat
print(f"Årlige totalkostnader for elbil: {elbil_totalkostnad:.2f} kr")
print(f"Årlige totalkostnader for bensinbil: {bensinbil_totalkostnad:.2f} kr")
print(f"Årlig kostnadsdifferanse (Bensinbil-Elbil): {kostnadsdifferanse:.2f} kr")

