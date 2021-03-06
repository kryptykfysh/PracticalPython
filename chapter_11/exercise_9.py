# Programmers sometimes use a dictionary of dictionaries as a simple
# database. For example, to keep track of information about famous scien-
# tists, you might have a dictionary where the keys are strings and the
# values are dictionaries, like this:
# {
#   'jgoodall'  : {'surname'  : 'Goodall',
#                  'forename' : 'Jane',
#                  'born'     : 1934,
#                  'died'     : None,
#                  'notes'    : 'primate researcher',
#                  'author'   : ['In the Shadow of Man',
#                                'The Chimpanzees of Gombe']},                 
#   'rfranklin' : {'surname'  : 'Franklin',
#                  'forename' : 'Rosalind',
#                  'born'     : 1920,
#                  'died'     : 1957,
#                  'notes'    : 'contributed to discovery of DNA'},
    
    
#    'rcarson'  : {'surname'  : 'Carson',
#                  'forename' : 'Rachel',
#                  'born'     : 1907,
#                  'died'     : 1964,
#                  'notes'    : 'raised awareness of effects of DDT',
#                  'author'   : ['Silent Spring']}
# }
# Write a function called db_headings that returns the set of keys used in any
# of the inner dictionaries. In this example, the function should return
# set('author', 'forename', 'surname', 'notes', 'born', 'died').

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

def db_headings(dict):
    my_key = ''

    for key in dict:
        my_key = key
        break
    return set(dict[my_key])