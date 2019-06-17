import os

folder = 'C:\\Users\\eliadani\\Desktop\\ITPs Temp'

for filename in os.listdir(folder):
    os.rename(folder + '\\' + filename, folder + '\\' + filename.replace('SIM_',''))
    print(filename.replace('SIM_', ''))