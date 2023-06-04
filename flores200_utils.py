import os

def load_test_set(name, number=None):
    f = open(name, 'r')
    lines =[line.strip() for line in f.readlines()]
    lang_code = name.split("/")[-1].split("_")[0]
    result= {"lang_code": lang_code}
    if number:
        result ["lines"] = lines[:number]
    else:
        result["lines"] = lines
    return result

def load_all_tests(test_dir, number=None):
    entries = os.listdir(test_dir)
    test_sets = {}
    for entry in entries:
        f_name = os.path.join(test_dir, entry)
        data = load_test_set(f_name, number)
        test_sets[data["lang_code"]] = data["lines"]
    return test_sets


if __name__ == '__main__':
    test_dir= 'data/flores200_dataset/devtest'
    test_data = load_all_tests(test_dir, 1)
    print(test_data)