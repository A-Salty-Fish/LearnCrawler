import csv
# with open('test.csv', 'r', encoding='UTF-8') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     for row in csv_reader:
#         print(row)
#     csvfile.close()
with open('test.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
    output_list = ['1', '2', '3', '4']
    w = csv.writer(csvfile)
    w.writerow(output_list)