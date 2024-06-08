def calculate_total_balance(denominations, notes):
    total_balance = 0
    for denom, note in zip(denominations, notes):
        total_balance += denom * note
    return total_balance

try:
    denominations = []
    notes = []
    for i in range(1, 5):
        denomination = int(input("Enter the {}st Denomination: ".format(i)))
        note = int(input("Enter the {}st Denomination number of notes: ".format(i)))
        denominations.append(denomination)
        notes.append(note)

    total_balance = calculate_total_balance(denominations, notes)
    print("Total Available Balance in ATM:", total_balance)
except ValueError:
    print("Invalid input. Please enter valid denominations and number of notes.")
