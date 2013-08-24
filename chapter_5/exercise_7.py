##The variables population and land_area refer to floats.

##a. Write an if statement that will print the population if it is less than
##10,000,000.

def low_population(population):
    """ (float) -> string

    Prints the population if less than 10,000,000

    >>> low_population(9999999)
    9999999
    >>> low_population(10000000)
    """

    if population < 10000000:
        print(population)
        
##b. Write an if statement that will print the population if it is between
##10,000,000 and 35,000,000.

def median_population(population):
    """ (float) -> string

    print the population if it is between 10,000,000 and 35,000,000

    >>> median_population(1)
    >>> median_population(10000000)
    10000000
    >>> median_population(20000000)
    20000000
    >>> median_population(40000000)
    >>> median_population(35000000)
    35000000
    """

    if 10000000 <= population <= 35000000:
        print(population)
        
##c. Write an if statement that will print "Densely populated" if the land density
##(number of people per unit of area) is greater than 100.


##d. Write an if statement that will print "Densely populated" if the land density
##(number of people per unit of area) is greater than 100, and "Sparsely
##populated" otherwise.

def population_density(population, land_area):
    """ (float, float) -> string

    Print 'Densely populated' if land density > 100, or 'Sparsely populated'
    otherwise.

    >>> population_density(100, 1)
    Sparsely populated
    >>> population_density(200, 1.5)
    Densely populated
    """

    if population / land_area > 100:
        print('Densely populated')
    else:
        print('Sparsely populated')
            
