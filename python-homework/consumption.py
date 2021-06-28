# (országúti fogyasztás, városi fogyasztás, országúton megtett út, városban megtett út, benzin ára)

fogy_orsz = float(input("Kérem az országúti fogyasztást"))
fogy_var = float(input("Kérem a városi fogyasztást"))
ut_orsz = float(input("Kérem az országúti távot"))
ut_var = float(input("Kérem a városi távot"))
benzin_ar = int(input("Kérem a benzin árát"))

print((ut_orsz / 100 * fogy_orsz * benzin_ar) + (ut_var / 100 * fogy_var * benzin_ar))
