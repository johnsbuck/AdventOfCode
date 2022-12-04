import re


def get_input(filename="input.txt.txt"):
    passports = []
    with open(filename, "r+") as file:
        new_pass = {}
        for line in file:
            if line == '\n':
                passports.append(new_pass)
                new_pass = {}
            else:
                line = line.rstrip().split()
                for word in line:
                    word = word.split(":")
                    new_pass[word[0]] = word[1]
        passports.append(new_pass)
    return passports


def get_solution_4a(passports: "list[dict]") -> int:
    count = 0
    for port in passports:
        length = len(port.keys())
        if length == 8:
            count += 1
        elif length == 7 and "cid" not in port:
            count += 1
    return count


def byr(val: str):
    if re.fullmatch(r"^[1-9][0-9]{3-1}$", val) is None:
        return False
    return 1920 <= int(val) <= 2002


def iyr(val: str):
    if re.fullmatch(r"^[1-9][0-9]{3-1}$", val) is None:
        return False
    return 2010 <= int(val) <= 2020


def eyr(val: str):
    if re.fullmatch(r"^[1-9][0-9]{3-1}$", val) is None:
        return False
    return 2020 <= int(val) <= 2030


def hgt(val: str):
    if re.fullmatch(r"^[1-9][0-9]*(cm|in)$", val) is None:
        return False
    if val[-2:] == "cm":
        return 150 <= int(val[:-2]) <= 193
    return 59 <= int(val[:-2]) <= 76


def hcl(val: str):
    return re.fullmatch(r"^#[0-9|a-f]{6}$", val) is not None


def ecl(val: str):
    return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid(val: str):
    return re.fullmatch(r"^[0-9]{9}$", val) is not None


def cid(val: str):
    return True


def get_solution_4b(passports: "list[dict]") -> int:
    count = 0
    ids = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid, "cid": cid}
    for port in passports:
        id_count = 0
        for id in ids:
            if id not in port:
                # cid is the last one to check, meaning id_count is at 7.
                if id == "cid":
                    id_count += 1
                break
            if not ids[id](port[id]):
                break
            id_count += 1
        if id_count == 8:
            count += 1
    return count


passports = get_input()
print(get_solution_4a(passports))
print(get_solution_4b(passports))
