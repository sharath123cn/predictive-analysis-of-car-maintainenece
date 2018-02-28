import csv
import re


header_row = ['Date','H','V','A']
date_re_pattern = r'[0-9][0-9].[0-9][0-9].[0-9][0-9]'


def remove_white_space(input_list):
	mod_list = []
	for val in input_list:
		if val == "":
			continue
		else:
			mod_list.append(val)
	return mod_list

def date_extractor(input_list):
	date_list = []
	for val in input_list:
		if re.match(date_re_pattern,val):
			date_list.append(val)
	return date_list


def H_processor(input_list):	
	pass
def csv_converter():
	with open("machine_data.csv","r") as file_in:
		reader = csv.reader(file_in)
		H_VALUES = []
		V_VALUES = []
		A_VALUES = []
		cnt = 0
		for row in reader:
			cnt += 1
			if cnt == 5:
				component_list = row
			elif cnt == 6:
				H_VALUES = row
			elif cnt == 7:
				V_VALUES = row
			elif cnt == 8:
				A_VALUES = row
				break

		component_list = remove_white_space(component_list)
		H_VALUES = remove_white_space(H_VALUES)
		V_VALUES = remove_white_space(V_VALUES)
		A_VALUES = remove_white_space(A_VALUES)

		date_list = date_extractor(component_list)
		H_VALUES = H_VALUES[3:]
		V_VALUES = V_VALUES[1:]
		A_VALUES = A_VALUES[1:]
		print(H_VALUES,V_VALUES,A_VALUES,len(H_VALUES),len(V_VALUES),len(A_VALUES))
		return date_list,H_VALUES,V_VALUES,A_VALUES


def write_to_csv(date_list,H_VALUES,V_VALUES,A_VALUES):
	with open("processed_data.csv","w") as file_out:
		writer = csv.writer(file_out)
		writer.writerow(header_row)
		for index in range(len(date_list)):
			write_list = [date_list[index],H_VALUES[index],V_VALUES[index],A_VALUES[index]]
			writer.writerow(write_list)

if __name__ == "__main__":
	date_list,H_VALUES,V_VALUES,A_VALUES = csv_converter()
	write_to_csv(date_list,H_VALUES,V_VALUES,A_VALUES)