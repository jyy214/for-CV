def calculate_bonus(employeeName, employeeQuota, employeeSales):
    baseBonus = 200
    bonusPerDollar = 0.10

    if employeeSales > employeeQuota:
        bonus = baseBonus + (employeeSales - employeeQuota) * bonusPerDollar
    else:
        bonus = baseBonus

    return bonus

def main():
    while True:
        employeeName = input("Enter employee name: ")
        employeeQuota = int(input("Enter employee quota ($1000-$2000): "))
        if employeeQuota < 1000 or employeeQuota > 2000:
            print("Quota must be in the range of $1000-$2000 inclusive.")
            continue

        employeeSales = int(input("Enter employee sales ($1-$3500): "))
        if employeeSales < 1 or employeeSales > 3500:
            print("Sales must be in the range of $1-$3500 inclusive.")
            continue

        totalBonus = calculate_bonus(employeeName, employeeQuota, employeeSales)

        print("Employee Name:", employeeName)
        print("Employee Quota:", employeeQuota)
        print("Employee Sales:", employeeSales)
        print("Total Bonus:", totalBonus)

        continue_flag = input("Do you want to continue (YES/NO)? ").strip().upper()
        if continue_flag != "YES":
            break

if __name__ == "__main__":
    main()
