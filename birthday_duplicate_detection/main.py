def duplicate_birthday(birthdays):
    """
    Checks if any birthday appears more than once.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()

    for bday in birthdays:
        if bday in seen:
            return f"🎉 {bday} is shared!"
        seen.add(bday)

    return "No shared birthdays 😢"


if __name__ == "__main__":
    sample = ["Jan 1", "Feb 14", "Mar 3", "Jan 1"]
    print(duplicate_birthday(sample))