import os
for file in os.listdir():
	if file[-3:] == '.ui':
		print(file)
		os.system(f"python -m PyQt5.uic.pyuic -x {file} -o {file[:-3]}.py")
