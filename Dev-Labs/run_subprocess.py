import subprocess

#subprocess.run(["ls", "-l"]) 

result = subprocess.run(["powershell", "pwd"], shell=True, capture_output=True, text=True)
print(result.stdout)