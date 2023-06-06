# Να γράψετε πρόγραμμα που ζητάει επαναληπτικά δύο ακεραίους και 
# επιστρέφει το άθροισμα και το γινόμενο τους. 
# Να ελέγχει την ορθότητα της εισόδου και να τερματίζει με τη λέξη stop. 

while True:
    x = input("Δώσε τον πρώτο ακέραιο ή stop για τερματισμό:")
    if x.lower()=='stop':
        break
    if not x.isnumeric():
        continue
    x = int(x)
  
    y = input("Δώσε τον δεύτερο ακέραιο:")
    if not y.isnumeric():
        continue

    y = int(y)
    
    print(f'Άθροισμα: {x+y}, Γινόμενο {x*y}')