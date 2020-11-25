import os, sys, getopt
import pandas as pd

def adaptive_reduce_size(dataframe, error = 0.0005):
	data_list = dataframe.values.tolist()

	new_list = [data_list[0]]

	for index in range(1, len(data_list)):
		if (data_list[index][1] < (new_list[-1][1] * (1 - error))) or (data_list[index][1] >= (new_list[-1][1] * (1 + error))):
			new_list.append(data_list[index])

	print('File reduced by {:.2f}%.'.format(len(data_list) / len(new_list) * 100))
	print()

	return pd.DataFrame(new_list, columns = ['Time (s)', 'Pressure Turbo (mbar)', 'Pressure Evap (mbar)', 'Frequency (Hz)'])


def calculate_on_df(dataframe, baseline):
	dataframe['Time (s)'] = dataframe['Time (s)'] / 60
	dataframe.rename(columns={'Time (s)':'Time (min)'}, inplace=True)
	
	dataframe['Frequency Change (Hz)'] = dataframe['Frequency (Hz)'] - baseline

	return dataframe

def main(argv):

	inputfile = ""
	outputfile = ""
	error = ""
	baseline = float(5977920)
	try:
		opts, args = getopt.getopt(argv,"hi:o:e:b:",["ifile=","ofile=", "error=", "baseline="])
	except getopt.GetoptError:
		print('reduce_size.py -i <inputfile> -o <outputfile> -e <error> -b <baseline>')
		sys.exit()

	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -i <inputfile> -o <outputfile> -e <error> -b <baseline>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-e", "--error"):
			error = float(arg)
		elif opt in ("-b", "--baseline"):
			if arg == "":
				pass
			else:
				baseline = float(arg)

		if outputfile == "":
			outputfile = os.path.basename(inputfile)



	print('Reducing file {}.'.format(outputfile))
	df = pd.read_csv(inputfile, sep = '\t')
	index_pressure = df['Pressure Turbo (mbar)'].where(df['Pressure Turbo (mbar)'] == 1000).last_valid_index()

	df = df.iloc[index_pressure:]
	df['Time (s)'] = df['Time (s)'].subtract(df['Time (s)'].values[0])

	new_df = calculate_on_df(adaptive_reduce_size(df, error = error), baseline)


	if not os.path.exists('reduced_files\\' + str(error)):
		os.mkdir('reduced_files\\' + str(error))

	new_df.to_csv('reduced_files\\' + str(error) + '\\' + outputfile, sep = '\t', index = False )


if __name__ == '__main__':
	main(sys.argv[1:])

# for file in os.listdir():
# 	error = 0.01
# 	if file.endswith(".txt"):
		# print('Reducing file {}.'.format(file))
		# df = pd.read_csv(file, sep = '\t')
		# index_pressure = df['Pressure (mbar)'].where(df['Pressure (mbar)'] == 1000).last_valid_index()

		# df = df.iloc[index_pressure:]
		# df['Time (s)'] = df['Time (s)'].subtract(df['Time (s)'].values[0])

		# new_df = calculate_on_df(adaptive_reduce_size(df, error = error))


		# if not os.path.exists('reduced_files\\' + str(error)):
		# 	os.mkdir('reduced_files\\' + str(error))

		# new_df.to_csv('reduced_files\\' + str(error) + '\\' + file, sep = '\t', index = False )





