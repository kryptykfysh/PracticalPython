##8. The function convert_to_celsius from Section 3.3, Defining Our Own Functions,
##on page 36, converts from Fahrenheit to Celsius. Wikipedia, however,
##discusses eight temperature scales: Kelvin, Celsius, Fahrenheit, Rankine,
##Delisle, Newton, Rèaumur, and Rømer. Visit http://en.wikipedia.org/wiki/Compar-
##ison_of_temperature_scales to read about them.

##a. Write a convert_temperatures(t, source, target) function to convert temperature
##t from source units to target units, where source and target are each one
##of "Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle", "Newton", "Reaumur", and
##"Romer" units.

def convert_to_kelvin(t, source):
    if source == 'Celsius':
        return t + 273.15
    elif source == 'Fahrenheit':
        return (t + 459.67) * (5 / 9)
    elif source == 'Rankine':
        return t * (5 / 9)
    elif source == 'Delisle':
        return 373.15 - (t * 2 / 3)
    elif source == 'Newton':
        return (t * 100 / 33) + 273.15
    elif source == 'Reaumur':
        return (t * 5 / 4) + 273.15
    elif source == 'Romer':
        return ((t - 7.5) * 40 / 21) + 273.15

def convert_temperature(t, source, target):
    temperature_in_kelvin = 0

    if source == target:
        return t
    elif source == 'Kelvin':
        temperature_in_kelvin = t
    else:
        temperature_in_kelvin = convert_to_kelvin(t, source)
    
    if target == 'Kelvin':
        return temperature_in_kelvin
    elif target == 'Celsius':
        return t - 273.15
    elif target == 'Farenheit':
        return (t * 9 / 5) - 459.67
    elif target == 'Rankine':
        return t * 9 / 5
    elif target == 'Delisle':
        return (373.15 + t) * 3 / 2
    elif target == 'Newton':
        return (t - 273.15) * 33 / 100
    elif target == 'Reaumur':
        return (t - 273.15) * 4 / 5
    elif target == 'Romer':
        return ((t - 273.15) * 21 / 40) + 7.5

##Hint: On the Wikipedia page there are eight tables, each with two
##columns and seven rows. That translates to an awful lot of if state-
##ments—at least 8 * 7—because each of the eight units can be converted
##to the seven other units. Possibly even worse, if you decided to add
##another temperature scale, you would need to add at least sixteen
##more if statements: eight to convert from your new scale to each of
##the current ones and eight to convert from the current ones to your
##new scale.
##A better way is to choose one canonical scale, such as Celsius. Your
##conversion function could work in two steps: convert from the source
##scale to Celsius and then from Celsius to the target scale.

##b. Now, if you added a new temperature scale, how many if statements
##would you need to add?

## 2