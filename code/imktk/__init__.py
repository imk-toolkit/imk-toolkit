from .toolkit import xtend_dataarray, xtend_dataset, _load_from_env

_load_from_env(mode='da')
_load_from_env(mode='ds')

def main():
    print(f"It works! 1 + 1 = {1 + 1}")


if __name__ == "__main__":
    main()
