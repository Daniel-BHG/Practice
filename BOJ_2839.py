weight = int(input())
if weight % 5 != 0 and weight % 3 != 0:
    print(-1)
else:
    if ((weight % 5) % 3 == 0):
        five_kg = weight // 5
        print(f"five_kg = {five_kg}ea")
        three_kg = (five_kg % 5) // 3
        print(f"three_kg = {three_kg}ea")
        print(f"Total = {five_kg + three_kg}")
    
    else:
        three_kg = weight // 3
        print(f"Total = {three_kg}")

    
