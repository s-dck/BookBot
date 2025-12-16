def sort_by_num(item):
    return item[1]

def get_num_words(file):
    return len(file.split())

def get_num_characters(file):
    file = file.lower()
    d = dict()
    for char in file:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

def print_report(file):
    d = get_num_characters(file)
    
    report_list = list(d.items())
    
    report_list.sort(key=sort_by_num, reverse=True) 
    
    words = str(get_num_words(file))
    
    print("============ BookBot ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")   
    print("--------- Character Count -------")
    
    for char, count in report_list:
        if char.isalpha():
                print(f"'{char}': {count}")
    
    print("============= END ===============")
                

        
                

                

                

        


                

        
        


