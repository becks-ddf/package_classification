def sort(width, height, length, mass) -> str:
    hashmap = {0: 'STANDARD', 1: 'SPECIAL', 2: 'REJECTED'}
    bulky = bool(width * height * length // 1000000 or width // 150 or
                                                  height // 150 or length // 150)
    heavy = bool(mass // 20)
    return hashmap[int(bulky) + int(heavy)]
