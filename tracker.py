# 🏋️ Simple Personal Fitness Tracker 🏋️
# This program allows users to log and view their fitness data.

# Store fitness data in a list
fitness_data = []

def add_entry():
    """Function to add a new fitness entry."""
    print("\n➕ Adding a new fitness entry...\n" + "-"*40)

    # Get user input with proper validation
    date = input("📅 Enter Date (YYYY-MM-DD): ")
    workout = input("🏋️ Workout Type: ")
    
    while True:
        try:
            duration = int(input("⏳ Duration (minutes): "))
            if duration <= 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid positive number!")

    while True:
        try:
            calories = int(input("🔥 Calories Burned: "))
            if calories < 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    while True:
        try:
            weight = float(input("⚖️ Weight (kg): "))
            if weight <= 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid weight!")

    while True:
        try:
            steps = int(input("🚶 Steps Walked: "))
            if steps < 0:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    # Append new data to the list
    fitness_data.append({
        "Date": date,
        "Workout": workout,
        "Duration": duration,
        "Calories": calories,
        "Weight": weight,
        "Steps": steps
    })

    print("\n✅ Entry Added Successfully! 🎉\n" + "-"*40)

def view_progress():
    """Function to display stored fitness data."""
    if not fitness_data:
        print("\n⚠️ No data available! Add some entries first.\n")
        return
    
    print("\n📊 Your Fitness Progress:\n" + "="*40)
    total_duration = 0
    total_calories = 0

    for entry in fitness_data:
        print(f"📅 Date: {entry['Date']}")
        print(f"🏋️ Workout: {entry['Workout']} | ⏳ {entry['Duration']} min | 🔥 {entry['Calories']} cal")
        print(f"⚖️ Weight: {entry['Weight']} kg | 🚶 Steps: {entry['Steps']}\n")
        print("-"*40)
        total_duration += entry["Duration"]
        total_calories += entry["Calories"]

    print(f"📌 Total Workouts Logged: {len(fitness_data)}")
    print(f"⏳ Total Workout Duration: {total_duration} min")
    print(f"🔥 Total Calories Burned: {total_calories} cal")
    print("="*40)

# 🏋️ Program starts here 🏋️
print("\n💪 Welcome to the Personal Fitness Tracker! 💪")
print("Track your workouts, calories, weight, and steps effortlessly.\n")

# Simple Menu Loop
while True:
    print("\n🏋️ Main Menu 🏋️")
    print("1️⃣ Add Entry")
    print("2️⃣ View Progress")
    print("3️⃣ Exit")
    
    choice = input("👉 Choose an option: ")
    
    if choice == "1":
        add_entry()
    elif choice == "2":
        view_progress()
    elif choice == "3":
        print("\n👋 Exiting... Stay Fit and Healthy! 💪🚀\n")
        break
    else:
        print("\n❌ Invalid choice. Please try again.")
