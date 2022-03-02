def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"Reverse {fruit_list}")

    fruit_list.append("Orange")
    print(f"Append Orange {fruit_list}")

    pos = fruit_list.index("apple")
    fruit_list.insert(pos, "cherry")
    print(f"insert cherry: {fruit_list}")

    fruit_list.remove("banana")
    print(f"Remove Banana: {fruit_list}")

    last = fruit_list.pop()
    print(f"pop {last}: {fruit_list}")

    fruit_list.sort()
    print(f"Sorted: {fruit_list}")

    fruit_list.clear()
    print(f"cleared: {fruit_list}")
if __name__ == "__main__":
    main()