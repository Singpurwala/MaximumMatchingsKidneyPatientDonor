import csv

# print('fff')
# Opens the file with the csv reader
kidney_data = open("Dataset_Kidney_Project-1.csv", "r")
reader = csv.reader(kidney_data)  # reads the file using csv reader

# finding the patient donor pair = index of item in list + 1
patient_blood_type_list = []
donor_blood_type_list = []
life_expectancy_list = []

skip_rows = 2

for row in reader:
    if skip_rows == 0:  # skips first two rows which contain the keys for the csv

        # gets the blood type of the patient, donor and donor life expectancies from the row and adds them to lists

        patient_blood_type_list.append(row[1])  # from second column
        patient_blood_type_list.append(row[2])  # from third column
        life_expectancy_list.append(row[5:])  # from fifth column onwards

    else:
        skip_rows -= 1

kidney_data.close()


def print_best_match_info(patient_num):
    patient_index = patient_num - 1  # since the index starts at 0

    patient_life_expectancy_list = life_expectancy_list[patient_index]

    highest_life_expectancy = 0  # will store the highest life expectancy
    for index in range(0, len(patient_life_expectancy_list)):
        life_expectancy = float(patient_life_expectancy_list[index])

        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            matching_pair = index + 1  # saves the donor pair that was matched as the index + 1, since the index starts at 0

    print(f"\nPatient {patient_num}:")
    print(f"    Best Donor: {matching_pair}")
    print(f"    Life expectancy: {highest_life_expectancy} Years")

    if matching_pair == patient_num:
        print(f"    No Increase (Pair {patient_num} are already a best match)")

    else:
        percent_increase = round(
            100 - ((float(patient_life_expectancy_list[patient_index]) / highest_life_expectancy) * 100),
            2)  # gets the life expectancy percentage increase to 2 decimal places
        year_increase = round(highest_life_expectancy - float(patient_life_expectancy_list[patient_index]),
                              2)  # gets the life expectancy year increase

        print(f"    Increased by: {percent_increase}% ({year_increase} Years)")


def returnInt(s):
    try:
        int(s)
        return int(s)
    except ValueError:
        return False


user_input = 0
while (user_input != -1):
    user_input = returnInt(input("\nEnter Patient Number to find best donor match (-1 to exit): "))
    if user_input == -1:
        break
    if isinstance(user_input, int) and user_input < len(life_expectancy_list):
        print_best_match_info(user_input)
    else:
        print("\nError - Invalid Patient Number")
        gay
        L
        u