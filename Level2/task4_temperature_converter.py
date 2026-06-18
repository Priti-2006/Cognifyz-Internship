# ─────────────────────────────────────────
# Cognifyz Internship — Level 2, Task 4
# Temperature Converter Program
# ─────────────────────────────────────────

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def display_menu():
    print("\n" + "="*40)
    print("   🌡️  TEMPERATURE CONVERTER")
    print("="*40)
    print("  1. Celsius → Fahrenheit")
    print("  2. Fahrenheit → Celsius")
    print("  3. Celsius → Kelvin")
    print("  4. Kelvin → Celsius")
    print("  5. Exit")
    print("="*40)

def get_temperature_input(unit):
    while True:
        try:
            temp = float(input(f"\nEnter temperature in {unit}: "))
            return temp
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

def main():
    print("\nWelcome to the Temperature Converter!")
    print("Developed for Cognifyz Technologies Internship")

    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == '1':
            temp = get_temperature_input("Celsius (°C)")
            result = celsius_to_fahrenheit(temp)
            print(f"\n✅ {temp}°C = {result:.2f}°F")

        elif choice == '2':
            temp = get_temperature_input("Fahrenheit (°F)")
            result = fahrenheit_to_celsius(temp)
            print(f"\n✅ {temp}°F = {result:.2f}°C")

        elif choice == '3':
            temp = get_temperature_input("Celsius (°C)")
            result = celsius_to_kelvin(temp)
            print(f"\n✅ {temp}°C = {result:.2f}K")

        elif choice == '4':
            temp = get_temperature_input("Kelvin (K)")
            if temp < 0:
                print("❌ Kelvin cannot be negative!")
            else:
                result = kelvin_to_celsius(temp)
                print(f"\n✅ {temp}K = {result:.2f}°C")

        elif choice == '5':
            print("\n👋 Thank you for using Temperature Converter!")
            print("Cognifyz Technologies — Where Data Meets Intelligence")
            break

        else:
            print("\n❌ Invalid choice! Please select 1-5.")

        input("\nPress Enter to continue...")

# Run the program
if __name__ == "__main__":
    main()