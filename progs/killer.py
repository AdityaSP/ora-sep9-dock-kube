import subprocess
output = subprocess.check_output('tasklist', shell=True).decode().split("\n")

pids = [ line.split()[1] for line in output if 'MicrosoftEdge' in line ]

for pid in pids:
    subprocess.call('taskkill /f /pid ' + pid, shell=True)



#VERSION 1
#import subprocess
#output = subprocess.check_output('tasklist', shell=True).decode()
#
## str to list of lines
#output_lines = output.split("\n")
#
## filter only lines MicrosoftEdge
#me = list(filter(lambda x : 'MicrosoftEdge' in x , output_lines))
#me = [ line for line in output_lines if 'MicrosoftEdge' in line ]
#print(me[:5])
#
## extract the pids
#pids = list( map(lambda x : x.split()[1], me))
#pids = [ line.split()[1] for line in me]
#print(pids)
#
## execute the kill commands - taskkill /f /pid <pid>   kill -9 <pid>
#for pid in pids:
#    subprocess.call('taskkill /f /pid ' + pid, shell=True)
#    