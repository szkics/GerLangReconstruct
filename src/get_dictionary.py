import io
import re

input_word_list = []
target_word_list = []

with io.open(
    "../german_english_dictionary/cdfcbfnndm-5219765-7ei959.txt",
    mode="r",
    encoding="utf-8",
) as f:
    for line in f:
        if "{" in line:
            processed_line = re.split("{[a-z]*}", line)
            if len(processed_line) > 1:
                separate_meaning = processed_line[1].split("\t")
                if len(separate_meaning) > 1:
                    actual_meaning = separate_meaning[1]
                else:
                    separate_meaning = processed_line[2].split("\t")
                    if len(separate_meaning) > 1:
                        actual_meaning = separate_meaning[1]
                input_word = processed_line[0]
                if (len(actual_meaning.split()) == 1):
                    input_word_list.append(input_word)
                    target_word_list.append(actual_meaning)

        else:
            processed_line = re.split("\t", line)
            input_word = processed_line[0]
            if len(processed_line) > 1:
                actual_meaning = processed_line[1]
                if (len(actual_meaning.split()) == 1):
                    input_word_list.append(input_word)
                    target_word_list.append(actual_meaning)
f.close()

with open("./german_english_dictionary.csv", "a") as f:
    for i in range(0,len(input_word_list)):
        f.write(input_word_list[i] + "," + target_word_list[i] + "\n")