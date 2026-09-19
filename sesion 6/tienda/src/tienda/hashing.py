from pwdlib import PasswordHash

pwd = PasswordHash.recommended()

def main() -> None:
    print(
        pwd.hash("secreto"),
    )
    print(
        pwd.verify("secreto", "$argon2id$v=19$m=65536,t=3,p=4$MxXKZSLCW9XxCYE8GT5GIg$ychGVABZ4D/pi6QWh8lyIYvqIQ1a26RPqzvXCTbLoxg")
    )
