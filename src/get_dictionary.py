import io
import re

german_english_dictionary = dict()
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
                german_english_dictionary[input_word] = actual_meaning
        else:
            processed_line = re.split("\t", line)
            input_word = processed_line[0]
            if len(processed_line) > 1:
                actual_meaning = processed_line[1]
                german_english_dictionary[input_word] = actual_meaning
f.close()

with open("german_english_dictionary.txt", "w") as f:
    print(german_english_dictionary, file=f)
f.close()
