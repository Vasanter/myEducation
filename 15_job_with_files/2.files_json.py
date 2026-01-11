import json


data = {"name": "Mike", "age": 30, "city": "New York"}

file = open(r'C:\Automation\myEducation\15_job_with_files\data.json', 'w')
json.dump(data, file)
file.close()

file = open(r'C:\Automation\myEducation\15_job_with_files\data.json', 'r')
loaded_data = json.load(file)
print(loaded_data)
file.close()
