import excel2json as e2j
import sys,os,requests

# Excel parser -> Creates formatted files based on xlxs's sheets
e2j.convert_from_file(sys.argv[1])

for jsons in os.listdir(os.getcwd()):
	if jsons.endswith('.json'):
		file = open(jsons,'r') #Parsed sheet
		file_name = file.name.split('.')
		grupo = '{"name":"'+ file_name[0] +'","targets": '+ file.read() + '}'
		#grupo = {"name":str(file.name),"targets": file.read()}
		file.close()
		#Send post request
		test = requests.post(sys.argv[2], grupo, verify=False, headers={'Authorization':sys.argv[3]})
		#test = requests.post(sys.argv[2], grupo, verify=False, headers={sys.argv[3]})
		print(test.text)
