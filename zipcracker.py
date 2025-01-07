import zipfile

zip_file = zipfile.ZipFile("stuff.zip")

with open("rockyou.txt", "rb") as file:
    for line in file:
        line = line.strip()

        try:
            zip_file.extractall(pwd=line)

            print("password found: ",line)
            break
        except:
            continue
