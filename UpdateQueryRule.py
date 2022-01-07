import argparse
import yaml
import os
import shutil

sigma_tool_path = "C:\\Users\\Admin\\Desktop\\UpdateRule_sigma2elastalert\\sigma\\tools"

def setArg():
	argparser = argparse.ArgumentParser(description="Convert Sigma rules into SIEM signatures.")
	argparser.add_argument("--newRule", "-n", help="New rule file use to update(Format:Sigma)", default=None, type = str)
	argparser.add_argument("--oldRule", "-o", help="Old rule file need to update(Format:Elastalert)", default=None, type = str)

	return argparser
def backup_old_rule():
	argparser = setArg()
	cmdargs = argparser.parse_args()

	old_rule_file = cmdargs.oldRule

	filepath = old_rule_file

	with open(filepath, mode="r") as f:
		try:
			old = f.read()
			with open(filepath + ".bak", mode="w") as f1:
				try:
					f1.write(old)
				except Exception as e:
					print(e)
				finally:
					f1.close()
		except Exception as e:
			print(e)
		finally:
			f.close()

def convert_rule():
	argparser = setArg()
	cmdargs = argparser.parse_args()
	try:
		os.mkdir('./temp')
	except Exception:
		pass
	output_file = os.path.basename(cmdargs.newRule)
	os.system('python '+sigma_tool_path+'/sigmac -t elastalert -c '+sigma_tool_path+'/config/winlogbeat-modules-enabled.yml '+cmdargs.newRule+' -o ./temp/'+output_file)


def update_rule():

	argparser = setArg()
	cmdargs = argparser.parse_args()

	new_rule_file = './temp/'+os.path.basename(cmdargs.newRule)
	old_rule_file = cmdargs.oldRule

	with open(new_rule_file) as f:
		new = yaml.safe_load(f)
	with open(old_rule_file) as f:
		old = yaml.safe_load(f)

		print('Before Update:'+'\n'+old['filter'][0]['query']['query_string']['query'])
		
	old['filter'][0]['query']['query_string']['query'] = new['filter'][0]['query']['query_string']['query']
		
	with open(old_rule_file, 'w') as f:
		yaml.safe_dump(old, f, default_flow_style=False)

	print('\n'+'-------------------------------------------------------------------------------------------------'+'\n')
	print('After Update:'+'\n'+new['filter'][0]['query']['query_string']['query'])
def main():
	backup_old_rule()
	convert_rule()
	update_rule()
	shutil.rmtree('./temp')


if __name__ == "__main__":
	main()