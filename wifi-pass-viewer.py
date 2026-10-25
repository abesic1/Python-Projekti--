import subprocess

profiles = subprocess.check_output("netsh wlan show profiles", shell=True).decode()

names = [line.split(":")[1].strip() for line in profiles.splitlines() if "All User Profile" in line]

for i, n in enumerate(names, 1):
    print(f"{i}. {n}")

ch = int(input("Odaberi wifi po broju: "))
wifi = names[ch - 1]
try:
    result = subprocess.check_output(
        ["netsh", "wlan", "show", "profile", f"name={wifi}", "key=clear"],
        stderr=subprocess.STDOUT,
    ).decode(errors="replace")

except subprocess.CalledProcessError as error:
    print(f"Pošlo je po grešci {wifi!r}:")
    print(error.output.decode(errors="replace"))
    raise SystemExit(1)

print("\n" + result)