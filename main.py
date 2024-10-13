def main():
    with open("books/frankenstein.txt") as f:
        book_content = f.read()
        print(book_content)

def count_words(string):
    return len(string.split())

main()
