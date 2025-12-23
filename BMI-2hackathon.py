# BMI + Diet Plan Project
# Uses only variables, strings, conditionals, lists, and tuples

# --- Inputs (variables) ---
name = "tuera"
height_cm = 145
weight_kg = 60
has_kitchen = True  # True = Yes, False = No

# --- BMI calculation (variables + data types) ---
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

# --- BMI category (conditionals) ---
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
else:
    category = "Overweight"

# --- Diet plans (lists/tuples) ---
underweight_diets = ["Eggs", "Paneer", "Dal", "Nuts", "Banana milkshake"]
normal_diets = ["Roti", "Sabzi", "Dal", "Fruits", "Curd"]
overweight_diets = ["Oats", "Boiled veggies", "Fruits", "Moong dal", "Salads"]
hostel_tips = ("Fruits", "Curd", "Chana", "Avoid fried food", "Drink more water")  # tuple example

# --- Choose plan (conditionals + lists/tuples) ---
if has_kitchen:
    if category == "Underweight":
        plan = underweight_diets
    elif category == "Normal":
        plan = normal_diets
    else:
        plan = overweight_diets
else:
    plan = hostel_tips

# --- Output (strings) ---
print("----- BMI & Diet Report -----")
print("Name:", name)
print("Height (cm):", height_cm)
print("Weight (kg):", weight_kg)
print("Kitchen access:", "Yes" if has_kitchen else "No")
print("BMI:", round(bmi, 1))
print("Category:", category)
print("Diet Plan:", ", ".join(plan))
print("-----------------------------")