import subprocess

shell = subprocess.Popen(["bash"], shell=True, stdin=subprocess.PIPE)


while True:
    comm = input("what command do you want to run?")
    b = comm.encode('utf-8')

    shell.communicate(input=b)