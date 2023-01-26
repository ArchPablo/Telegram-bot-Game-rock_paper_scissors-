import pandas
# Load the xlsx file
excel_data = pd.read_excel(f'.data_timetable.demo_timetable.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['Sales Date', 'Sales Person', 'Amount'])
# Print the content
print("The content of the file is:\n", data)
