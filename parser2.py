import excel2json as e2j
import sys
## How to use -> Put as sys.argv[1] the xlxs file and as sys.argv[2] the sheet you want to parse
## Do NOT forget to execute passing the output to a file
## Example:
##	python3 parser2.py <xlxs file> <sheetname>.json > output.json

# Excel parser -> Creates formatted files based on xlxs's sheets
e2j.convert_from_file(sys.argv[1])

#Edit file that you want to parse
file = open(sys.argv[2],'r')
print('{"name":"'+ str(sys.argv[2])  +'","targets": '+ file.read() + '}')
file.close()
