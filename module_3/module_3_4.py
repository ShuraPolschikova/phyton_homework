def single_root_words(root_word, *other_words):
    same_words = list()
    words = []

    for i in range(len(other_words)):
        root_word = root_word.lower()
        words = str(other_words[i])

        if root_word in words.lower() or words.lower() in root_word:
            same_words.append(other_words[i])

    print(same_words)

single_root_words('rich', 'richest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')