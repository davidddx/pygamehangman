#dictionary format is category : word
import random;

sitcom = "Sitcom";
anime = "Anime";
movie = "Movie";
videogameseries = "Video Game Series";
cartoon = "cartoon";
country = "country";
poem = "poem";
rapper = "rapper";
boxer = "boxer";

wordDictionary = {
    "laos": country,
    "cambodia": country,
    "united states of america": country,
    "canada": country,
    "cuba": country,
    "dominican republic": country,
    "panama": country,
    "haiti": country,
    "lebanon": country,
    "spain": country,
    "france": country,
    "nigeria": country,
    "algeria": country,
    "libya": country,
    "detective pikachu": movie,
    "friends": sitcom,
    "bleach": anime,
    "demon slayer": anime,
    "my hero academia": anime,
    "naruto": anime,
    "johnny test": cartoon,
    "dragon ball z": anime,
    "the godfather": movie,
    "21 jump street": movie,
    "22 jump street": movie,
    "spongebob": cartoon,
    "the proud family": cartoon,
    "the boondocks": cartoon,
    "mario": videogameseries,
    "sonic": videogameseries,
    "modern family": sitcom,
    "a space odyssey": movie,
    "the birds": movie,
    "the thinning": movie,
    "the road not taken": poem,
    "fire and ice": poem,
    "the raven": poem,
    "final fantasy": videogameseries,
    "lil wayne": rapper,
    "kanye west": rapper,
    "lil durk": rapper,
    "baby keem": rapper,
    "nicki minaj": rapper,
    "cardi b": rapper,
    "floyd mayweahther": boxer,
    "wonder over younder": cartoon,
    "phineas and ferb": cartoon,
    "jay z": rapper,
    "tupac": rapper,
    "big l": rapper,
    "biggie smalls": rapper,
    "lil 2z": rapper,
    "quin nfn": rapper,
    "j cole": rapper,
    "kendrick lamar": rapper,
    "king von": rapper,
    "tee grizzly": rapper,
    "asap rocky": rapper,
    "big sean": rapper,
    "avatar the last airbender": cartoon,
    "adventure time": cartoon,
    "ed edd n eddy": cartoon,
    "dexters laboratory": cartoon,
    "courage the cowardly dog": cartoon,
    "futurama": cartoon,
    "steven universe": cartoon,
    "samurai jack": cartoon,
    "teen titans": cartoon,
    "teen titans go": cartoon,
    "ben 10": cartoon,
    "johnny bravo": cartoon,

}

def getword():
    keys = wordDictionary.keys();
    wordlist = list(keys);
    # print(wordlist);
    word = random.choice(wordlist);
    # print(word);
    return word;

def getcategory(word):
    category = wordDictionary[word];
    return category;

def generateguessString(word):
    idx = 0;
    guessString = "";
    for letter in word:
        if(letter != ' '):

            guessString = guessString + '_'
        else:
            guessString = guessString + ' ';

        guessString = guessString + ' ';

        idx+=1;
    return str(guessString);


