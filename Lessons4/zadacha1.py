from sys import argv

def salary (sum_hour,stavka, premiya):
    return sum_hour*stavka+premiya

sum_hour = int(argv[1])
stavka = int(argv[2])
premiya = int(argv[3])

print(f"Заработная плата сотрудника =  {salary(sum_hour, stavka, premiya)}")