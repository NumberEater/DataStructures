from os import system

def pause():
    print()
    system("pause")

example = {"my_car":
        {"brand": "Ford",
        "model": "Mustang",
        "year": 1964
        },
        "mom_car":
        {"brand": "Ford",
        "model": "Fusion",
        "year": 2011
        }
}

print(example["my_car"]["brand"], example["my_car"]["model"])
print(example["mom_car"]["brand"], example["mom_car"]["model"])

pause()
