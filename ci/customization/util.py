class r_versions(str):
    def compare(self, other: str) -> int:
        yearA, monthA = map(int, self.split("."))
        yearB, monthB = map(int, other.split("."))

        if yearA < yearB or (yearA == yearB and monthA < monthB):
            return -1
        elif yearA == yearB and monthA == monthB:
            return 0
        else:
            return 1

    def is_less_than(self, other: str) -> bool:
        return self.compare(other) == -1

    def is_greater_than(self, other: str) -> bool:
        return self.compare(other) == 1
