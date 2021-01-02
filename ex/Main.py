from os import system

def pause():
    print()
    system("pause")

def colored(r, g, b, text):
    system("color")
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

family_cars = {"my_car":
        {"brand": "Ford",
        "model": "Mustang",
        "year": 1994
        },
        "mom_car":
        {"brand": "Chevy",
        "model": "Traverse",
        "year": 2016
        },
        "sister_car":
        {"brand": "Chevy",
        "model": "HHR",
        "year": 2011
        },
        "dad_car":
        {"brand": "Tesla",
        "model": "Model X",
        "year": 2016
        }
}

print(colored(255, 0, 0, "My car:") + family_cars["my_car"]["brand"], family_cars["my_car"]["model"] + "\n")
print(colored(255, 255, 0, "My mom's car:") + family_cars["mom_car"]["brand"], family_cars["mom_car"]["model"] + "\n")
print(colored(255, 0, 153, "My sister's car:") + family_cars["sister_car"]["brand"], family_cars["sister_car"]["model"] + "\n")
print(colored(0, 0, 255, "My dad's car:") + family_cars["dad_car"]["brand"], family_cars["dad_car"]["model"] + "\n")

pause()
