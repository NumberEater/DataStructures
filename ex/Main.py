from os import system

def pause():
    print()
    system("pause")

colors = {
"red": "\u001b[31m",
"green": "\u001b[32m",
"blue": "\u001b[34m",
"reset": "\u001b[0m"
}

system("color")

print(colors["red"] + "Red Text")
print(colors["green"] + "Green Text")
print(colors["blue"] + "Blue Text")
print(colors["reset"] + "White Text")

pause()
