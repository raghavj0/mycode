#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Ansible Runner is a tool and python library that helps when interfacing with Ansible directly or as part of another system whether that be through a container image interface, as a standalone tool, or as a Python module that can be imported. The goal is to provide a stable and consistent interface abstraction to Ansible.
"""

# python3 -m pip install ansible_runner
import ansible_runner

# run() takes inputs (either provided as direct inputs to the function or from the Runner Input Directory Hierarchy), and executes Ansible
# returns runner object
r = ansible_runner.run(private_data_dir='/home/student/mycode/arun/', playbook='playbook-apt.yml')

# explore some of the returned data
print("****** PLAYBOOK RUN BREAKDOWN ******\n")

#Status: successful
#RunCode: 0
print(f"Status: {r.status}\nRunCode: {r.rc}\n")

#print("Exit Stats") to a file
with open('runnerstat.txt', 'w') as f:
    print("****** PLAYBOOK RUN BREAKDOWN ******\n", file=f)
    print(r.stats, file=f, end='\n\n') # breakdown of how the playbook ran

    for each_host_event in r.events:
        print("EVENT: ", each_host_event['event'], file=f)
        if each_host_event.get('event_data'):
            print("TASK: ", each_host_event.get('event_data').get('task'), file=f)
        print("UUID: ", each_host_event.get('uuid'), end="\n\n", file=f)

