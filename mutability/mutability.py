from pprint import pprint
import json


def mutability():
    friends = {
        "ralf": 3,
        "jane": 4,
        "john": 1
    }
    print(json.dumps(friends, indent=4, sort_keys=True))
    

def main():
    mutability()


if __name__ == "__main__":
    main()
