def unique_emails(emails):
    uniqueEmail = set()
    
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        uniqueEmail.add(f"{local}@{domain}")
    return len(uniqueEmail)

emails = ["tommy+mail@leetcode.com", "tommy@gmail.com"]
print(unique_emails(emails))

