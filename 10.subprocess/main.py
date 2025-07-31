import subprocess
from subprocess import Popen,PIPE

subprocess.run(["echo","Hello World"])
subprocess.run("echo 'Hello World'",shell=True)
output=subprocess.run("echo 'Hello World'",check=True,shell=True,stdout=subprocess.PIPE,universal_newlines=True)
print(output)

p=Popen(["sleep","5"])
p.wait()

p1=Popen(["ls","-l"],stdout=PIPE)
p2=Popen(["grep","main"],stdin=p1.stdout,stdout=PIPE,universal_newlines=True)
output=p2.stdout.readline()
print(output)
p1.stdout.close()

process=subprocess.Popen(['ping','-c 4','python.org'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True)

while True:
    output=process.stdout.readline()
    print(output)
    return_code = process.poll()
    if return_code is not None:
        print('RETURN CODE', return_code)

        for output in process.stdout.readline():
            print(output)
        break

proc=subprocess.Popen(['ping','-c 4','google.com'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                        )


try:
    outs, _ = proc.communicate(timeout=3)
    print('RETURN CODE',proc.returncode)
    print(outs.decode('utf-8'))
except subprocess.TimeoutExpired:
    print('subprocess did not terminate in time')
    proc.terminate()
    print('RETURN CODE',proc.returncode)
