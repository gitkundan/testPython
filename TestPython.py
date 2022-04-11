##================csv module and matplotib===========START
# from datetime import date, datetime
# import csv
# import matplotlib.pyplot as plt
# # filename="C:/Users/John/PythonLearning/ehmatthes-pcc_2e-078318e/chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv"
# filename="C:/Users/John/PythonLearning/ehmatthes-pcc_2e-078318e/chapter_16/the_csv_file_format/data/sitka_weather_2018_simple.csv"
# with open(filename) as f:
#     reader=csv.reader(f)
#     header_row=next(reader) #TODO: GOTCHA- The reader object continues from where it left off in the CSV file and automatically returns each line following its current position. Because we’ve already read the header row, the loop will begin at the second line where the actual data begins. 
#     lows,highs,dates=[],[],[]
#     # print(list(enumerate(header_row))) #TODO
#     for row in reader:
#         #     print(row)  #TODO: gives csv row output i..e excel view on screen
#         low=int(row[6])
#         lows.append(low)

#         high=int(row[5])
#         highs.append(high)

#         current_date=datetime.strptime(row[2],'%Y-%m-%d')
#         dates.append(current_date)

# # print(highs)
# # print(lows)
# # print(dates)
# #Plot the high temperatures
# plt.style.use('ggplot')
# fig, ax=plt.subplots()
# ax.plot(dates,highs, c='red',alpha=0.5)
# ax.plot(dates,lows, c='blue',alpha=0.5)
# plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# #Format plot
# plt.title("Daily high temperatures",fontsize=24)
# plt.xlabel("",fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature(F)",fontsize=16)
# plt.tick_params(axis='both',which='major',labelsize=16)
# plt.show()
##================csv module and matplotib===========END
##================json module=========================START
import json

filename="C:/Users/John/PythonLearning/ehmatthes-pcc_2e-078318e/chapter_16/mapping_global_data_sets/data/eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data=json.load(f)

readable_filename="C:/Users/John/PythonLearning/ehmatthes-pcc_2e-078318e/chapter_16/mapping_global_data_sets/data/finalResults.json"
with open(readable_filename,'w') as f:
    json.dump(all_eq_data,f,indent=4)

with open(readable_filename) as f:
    print(f.read())