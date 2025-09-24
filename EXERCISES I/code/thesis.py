import array
thesis_log = [23,65,76,32,70,76,34,54,23,67,98]
# calculate the thesis log
total_thesis = sum(thesis_log)
average_thesis = round(total_thesis / len(thesis_log), 2)
min_thesis = min(thesis_log)
max_thesis = max(thesis_log)
# the reports of thesis log
report = (
    f" The report of Thesis log {thesis_log} are. \n"
    f" The total value of Thesis log: {total_thesis}\n"
    f" The average value of Thesis log: {average_thesis}\n"
    f" The minimum value of Thesis log: {min_thesis}\n"
    f" The maximum value of Thesis log: {max_thesis}\n"

)
print(report)
# Boolean threshold condition
threshold = 50
if max_thesis >= threshold and average_thesis >= threshold:
    print("Thesis log: Above standard")
else:
    print("Thesis log: Below standard")
#add new element
newData = 80
thesis_log.append(newData)
print(f"Thesis log: New data we appended is: {newData} the thesis log: {thesis_log}")

for data in thesis_log:
    if data <50:
        thesis_log.remove(data)
        print(f"Thesis log: {data} removed")
        break

print(f" the thesis log before sort is: {thesis_log}")
thesis_log.sort()
print(f" the thesis log after sort is: {thesis_log}")

# array

thesis_array = array.array('i', thesis_log)
sum_thesis_array = sum(thesis_array)
sum_thesis_list = sum(thesis_log)
if sum_thesis_array == sum_thesis_list:
    print (f"thesises is matched {sum_thesis_array} and {sum_thesis_list}")
else:
    print(f"thesises is NOT matched {sum_thesis_array} and {sum_thesis_list}")
# dictionary
thesis_dict = [{'id': 1, 'name': 'Alice', 'value': 14},
{'id': 2, 'name': 'Bob', 'value': 12},
{'id': 3, 'name': 'Charlie', 'value': 18},
{'id': 4, 'name': 'Diana', 'value': 10},
{'id': 5, 'name': 'Eve', 'value': 23},
{'id': 6, 'name': 'Frank', 'value': 24}]
# update one record
for record in thesis_dict:
    print(record)
    if record['id'] == 4:
        record['value'] = 95
        print(f"\n the record thesis dictionary update{thesis_dict} \n")
        # Delete record
thesis_members = [record for record in thesis_dict if record['id'] != 2]

# total of record
total_value = sum(record['value'] for record in thesis_dict)
print(f"Total value of Thesis log dictionary: {total_value}")