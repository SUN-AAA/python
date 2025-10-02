original_s = "Park(Java city), Kim(C city), Kang(Bython city), Lee(Bythoncity), Hong(Ruby city), Cho(Bython city), Koo(C city), Ryu(C++city)"
correct_s = original_s.replace("Bython","Python")

print(f"Original text :\n{original_s}\n")
print(f"Corrected text :\n{correct_s}")

n = original_s.count("Bython")
print("The string Bython has been modified %d times"%n)