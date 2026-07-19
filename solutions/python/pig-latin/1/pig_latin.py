def translate_word(word):
    if word[0] in "aeiou" or word.startswith(("xr", "yt")):
        return word + "ay"

    if "qu" in word:
        qu_index = word.find("qu")
        if all(char not in "aeiou" for char in word[:qu_index]):
            front = word[:qu_index + 2]
            back = word[qu_index + 2:]

            return back + front + "ay"

    for i in range(len(word)):
        if word[i] in "aeiou" or (i > 0 and word[i] == "y"):
            front = word[:i]
            back = word[i:]
            return back + front + "ay"

def translate(text):

    words = text.split()

    translated_words = [translate_word(w) for w in words]

    return " ".join(translated_words)