def get_lines(path: str) -> list[int]:
    with open(path) as file:
        return [int(l.strip()) if l.strip() else l.strip() for l in file.readlines()]


def get_elves_from_lines(lines: list[int]) -> list[dict]:
    elves = []
    calories = 0
    index = 1
    for line in lines:
        if line != "":
            calories += line
        else:
            elves.append({"calories": calories, "index": index})
            index += 1
            calories = 0
    return elves


def sort_elves_by_calories(elves: list[dict]) -> list[dict]:
    return sorted(elves, key=lambda e: e["calories"], reverse=True)


def get_most_calories(elves: list[dict]) -> int:
    return elves[0]["calories"]


def get_sum_of_top_three_calories(elves: list[dict]) -> int:
    return sum([e["calories"] for e in elves[:3]])


def main():
    lines = get_lines("input.txt")
    elves = get_elves_from_lines(lines)
    sorted_elves = sort_elves_by_calories(elves)

    most_calories = get_most_calories(sorted_elves)
    print(f"The most calories held by an elf is {most_calories}")

    top_three_sum = get_sum_of_top_three_calories(sorted_elves)
    print(f"The sum of the top three calories held by elves is {top_three_sum}")


if __name__ == "__main__":
    main()
