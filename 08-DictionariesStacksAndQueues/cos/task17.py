

def convert_NATO(dict):
    your_word = str(input('enter word: '))
    nato_word = ''
    for letter in your_word:
        for key,val in dict.items():
            if letter.upper() == key:
                nato_word += val + ' '
    return nato_word





d =  {
    'A': 'Alpha',  'B': 'Bravo',   'C': 'Charlie',
    'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
    'G': 'Golf',   'H': 'Hotel',   'I': 'India',
    'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
    'M': 'Mike',   'N': 'November','O': 'Oscar',
    'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
    'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
    'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee', 'Z': 'Zulu'
    }

print(convert_NATO(d))