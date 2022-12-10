#regular expressions
import re

pattern = re.compile("^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$")
email_id = "fxnczqmelcwdzbngaz@tmmwj.com"

if re.search(pattern,email_id):
    print("Este bun")
else: print("NU este bun")