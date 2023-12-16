import sys , os 
given_path = sys.argv[1]
folder_path = given_path.split('\\')
given_path_1 = '\\'.join(folder_path[:-1])
os.makedirs(given_path_1,exist_ok=True)
file = open(given_path,'w')
file.close()