def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        book_content = f.read()
        wordcount = count_words(book_content)
        lettercount = sort_and_filter_chars(count_chars(book_content))
        print(f"--- Begin report of {book} ---")
        print(f"{wordcount} words found in the document")

        for item in lettercount:
            print(f"The '{item["char"]}' character was found {item["count"]} times")

        print("--- End report ---")

def count_words(string):
    return len(string.split())

def count_chars(string):
    result = {}
    for i in string.lower():
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1
    return result

def sort_on(dict):
    return dict["count"]
    

def sort_and_filter_chars(dict):
    result = []
    for i in dict:
        if i.isalpha():
            result.append({"char": i, "count": dict[i]})
    result.sort(reverse=True, key=sort_on)
    return result





main()
