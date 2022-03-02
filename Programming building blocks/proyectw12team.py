
chosen_volume = input("Which volume of scripture would you like to learn about? ")

largest_chapter_scriptures = -1
largest_book_scriptures = ""
with open("books_and_chapters.txt") as scriptures:
    for line in scriptures:
        parts = line.split(":")
        book = parts[0].strip()
        chapter = int(parts[1])
        scripture = parts[2].strip()
        if scripture.lower() == chosen_volume.lower():

            print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")

        if chapter > largest_chapter_scriptures:
            largest_chapter_scriptures = chapter
            largest_book_scriptures = book

print(f"The book with the most chapters in the {chosen_volume} is: {largest_book_scriptures}")
print(f"It has {largest_chapter_scriptures} chapters.")



