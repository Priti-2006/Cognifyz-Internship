# ─────────────────────────────────────────
# Cognifyz Internship — Level 1, Task 2
# Number Patterns Program
# ─────────────────────────────────────────

def display_menu():
    print("\n" + "="*45)
    print("      NUMBER PATTERN GENERATOR")
    print("="*45)
    print("  1. Right Triangle Pattern")
    print("  2. Pyramid Pattern")
    print("  3. Inverted Triangle Pattern")
    print("  4. Diamond Pattern")
    print("  5. Floyd's Triangle")
    print("  6. Exit")
    print("="*45)

def get_rows():
    while True:
        try:
            rows = int(input("\nEnter number of rows (1-10): "))
            if 1 <= rows <= 10:
                return rows
            else:
                print("❌ Please enter a number between 1 and 10.")
        except ValueError:
            print("❌ Invalid input! Please enter a whole number.")

# Pattern 1 — Right Triangle
def right_triangle(rows):
    print("\n--- Right Triangle Pattern ---\n")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Pattern 2 — Pyramid
def pyramid(rows):
    print("\n--- Pyramid Pattern ---\n")
    for i in range(1, rows + 1):
        # Print spaces
        print(" " * (rows - i), end="")
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()

# Pattern 3 — Inverted Triangle
def inverted_triangle(rows):
    print("\n--- Inverted Triangle Pattern ---\n")
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Pattern 4 — Diamond
def diamond(rows):
    print("\n--- Diamond Pattern ---\n")
    # Upper half
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()
    # Lower half
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()

# Pattern 5 — Floyd's Triangle
def floyds_triangle(rows):
    print("\n--- Floyd's Triangle ---\n")
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

def main():
    print("\nWelcome to the Number Pattern Generator!")
    print("Developed for Cognifyz Technologies Internship")

    while True:
        display_menu()
        choice = input("\nChoose a pattern (1-6): ").strip()

        if choice in ['1','2','3','4','5']:
            rows = get_rows()

            if choice == '1':
                right_triangle(rows)
            elif choice == '2':
                pyramid(rows)
            elif choice == '3':
                inverted_triangle(rows)
            elif choice == '4':
                diamond(rows)
            elif choice == '5':
                floyds_triangle(rows)

        elif choice == '6':
            print("\n👋 Thank you for using Pattern Generator!")
            print("Cognifyz Technologies — Where Data Meets Intelligence")
            break
        else:
            print("\n❌ Invalid choice! Please select 1-6.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()