import subprocess
p = subprocess.Popen(['/opt/certcheck/ssl-cert-check.sh','-s','google.com','-p','443'], stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
out, err = p.communicate()
print out.rstrip(), err.rstrip()
