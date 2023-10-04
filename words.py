#dictionary format is category : word
import random;

sitcom = "Sitcom";
anime = "Anime";
movie = "Movie";
videogameseries = "Video Game";
cartoon = "cartoon";
country = "country";
poem = "poem";
rapper = "rapper";
boxer = "boxer";
college = "college";
animal = "animal";
technology = "technology"
language = "language"
programminglanguage = "programming language"
wordDictionary = {
    "laos": country,
    "cambodia": country,
    "united states of america": country,
    "canada": country,
    "cuba": country,
    "dominican republic": country,
    "jamaica": country,
    "belize": country,
    "somalia": country,
    "ethiopia": country,
    "egypt": country,
    "russia": country,
    "china": country,
    "north korea": country,
    "south korea": country,
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
    "fairy tail": anime,
    "death note": anime,
    "attack on titan": anime,
    "jojos bizarre adventure": anime,
    "akame ga kill": anime,
    "kill la kill": anime,
    "code geass": anime,
    "evangelion": anime,
    "hunter x hunter": anime,
    "blue lock": anime,
    "fullmetal alchemist": anime,
    "fullmetal alchemist brotherhood": anime,
    "one piece": anime,
    "cowboy bebop": anime,
    "jujutsu kaise": anime,
    "johnny test": cartoon,
    "dragon ball z": anime,
    "the godfather": movie,
    "21 jump street": movie,
    "22 jump street": movie,
    "get out": movie,
    "space jam": movie,
    "space jam a new legacy": movie,
    "coach carter": movie,
    "he got game": movie,
    "kurokos basketball": anime,
    "hoop dreams": movie,
    "casablanca": movie,
    "gone with the wind": movie,
    "oppenheimer": movie,
    "barbie": movie,
    "sound of freedom": movie,
    "42": movie,
    "woodlawn": movie,
    "race": movie,
    "spongebob": cartoon,
    "the proud family": cartoon,
    "the boondocks": cartoon,
    "mario bros": videogameseries,
    "sonic superstars": videogameseries,
    "sonic the hedgehog 1": videogameseries,
    "megaman 1": videogameseries,
    "megaman 2": videogameseries,
    "megaman 3": videogameseries,
    "megaman 4": videogameseries,
    "megaman 5": videogameseries,
    "megaman 6": videogameseries,
    "fire emblem fates": videogameseries,
    "fire emblem three houses": videogameseries,
    "fire emblem awakening": videogameseries,
    "fire emblem shadows of valentia": videogameseries,
    "fire emblem heroes": videogameseries,
    "fire emblem radiant dawn": videogameseries,
    "fire emblem path of radiance": videogameseries,
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
    "florida international university": college,
    "florida tech": college,
    "duke": college,
    "university of miami": college,
    "florida atlantic university": college,
    "yale": college,
    "penn": college,
    "princeton": college,
    "harvard": college,
    "university of georgia": college,
    "university of florida": college,
    "university of south florida": college,
    "university of central florida": college,
    "stanford": college,
    "MIT": college,
    "johns hopkins university": college,
    "northwestern university": college,
    "dog": animal,
    "cat": animal,
    "elephant": animal,
    "giraffe": animal,
    "kangaroo": animal,
    "horse": animal,
    "bear": animal,
    "snake": animal,
    "fly": animal,
    "cockroach": animal,
    "computer": technology,
    "television": technology,
    "phone": technology,
    "central processing unit": technology,
    "random access memory": technology,
    "hard disk": technology,
    "flash drive": technology,
    "english": language,
    "spanish": language,
    "french": language,
    "german": language,
    "italian": language,
    "sign language": language,
    "yoruba": language,
    "igbo": language,
    "swahili": language,
    "arabic": language,
    "romanian": language,
    "hindi": language,
    "filipino": language,
    "japanese": language,
    "mandarin": language,
    "cantonese": language,
    "russian": language,
    "ukranian": language,
    "portugese": language,
    "xhosa": language,
    "somali": language,
    "fortran": programminglanguage,
    "php": programminglanguage,
    "csharp": programminglanguage,
    "python": programminglanguage,
    "cpp": programminglanguage,
    "c": programminglanguage,
    "java": programminglanguage,
    "javascript": programminglanguage,
    "rust": programminglanguage,
    "sql": programminglanguage,
    "html": programminglanguage,
    "css": programminglanguage,
    "lua": programminglanguage,
    "ti basic": programminglanguage,
    "swift": programminglanguage,
    "kotlin": programminglanguage,
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



