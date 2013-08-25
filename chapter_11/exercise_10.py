# Write another function called db_consistent that takes a dictionary of dictio-
# naries in the format described in the previous question and returns True
# if and only if every one of the inner dictionaries has exactly the same keys.
# (This function would return False for the previous example, since Rosalind
# Franklin's entry doesn't contain the 'author' key.)

dict_of_dicts = {
  'jgoodall'  : {'surname'  : 'Goodall',
                 'forename' : 'Jane',
                 'born'     : 1934,
                 'died'     : None,
                 'notes'    : 'primate researcher',
                 'author'   : ['In the Shadow of Man',
                               'The Chimpanzees of Gombe']},                 
  'rfranklin' : {'surname'  : 'Franklin',
                 'forename' : 'Rosalind',
                 'born'     : 1920,
                 'died'     : 1957,
                 'notes'    : 'contributed to discovery of DNA'},
    
    
   'rcarson'  : {'surname'  : 'Carson',
                 'forename' : 'Rachel',
                 'born'     : 1907,
                 'died'     : 1964,
                 'notes'    : 'raised awareness of effects of DDT',
                 'author'   : ['Silent Spring']}
}

def db_consistent(dict):
    test_keys = set()
    result = True

    for key in dict:
        if len(test_keys) == 0:
            test_keys = set(dict[key])
        else:
            if not (set(dict[key]) == test_keys):
                result = False

    return result