from polls.models import Category, Question, Choice

categories = [
    ("Let's get political", "Family dinner is not the best place to voice your political thoughts. Do it here."),
    ("Would you rather", "Hypothetical answers to hypothetical questions.They say those can be a nice ice breaker or even sort of a game to liven up a party."),
    ("Serious questions", "A questions that tormented million minds thoughtout the centuries. Get your vote into the mysteries of life and universe."),
    ("Personal preferences", "Chrome or Mozilla? iOS or Android? Take your pick! It's 'one' vs 'one' time"),
    ("Movie night", "Watched a movie, read a book, finished a TV Show? Vote up your enjoyment or vote away your sorrows!"),
    ("I'm here to have fun!", "Unclassified, unrelated, unusual!")
]

def create_category(categories):
    for name, description in categories:
        Category.objects.create(name=name, description=description)

would_questions = [
    {"question_text": "Would you rather be forced to dance every time you heard music or be forced to sing along to any song you heard?", 
    "choices": ["Im a lousy singer! I will dance <3", "Let's make this life a musical! I'm singing <3"]},
    {"question_text": "Would you rather visit 100 years in the past or 100 years in the future?",
    "choices": ["100 years in the the past", "100 years in the future"]},
    {"question_text": "Would you rather Be the funniest person in the room or the most intelligent?",
    "choices": ["Intelligent", "I'd like to be the funniest!"]},
    {"question_text": "Would you rather be a famous director or a famous actor?", 
    "choices": ["Actor all the way", "Someone said director! Count me in!"]}, 
    {"question_text": "Would you rather live in a cave or live in a tree house?",
    "choices": ["Cave does it for me!", "I always wanted a tree house!"]},
    {"question_text": "Would you rather be able to control fire or water?", 
    "choices": ["Fire! I'll rock on a camping trips", "72 percent of Earth is water!I will be unstoppable"]},
    {"question_text": "Would you rather be able to teleport anywhere or be able to read minds?", 
    "choices": ["I'll travel! It is SO cool!", "Mind reading will come in handy!"]},
    {"question_text": "Would you rather be unable to use search engines or unable to use social media?", 
    "choices": ["Like I could live without Google?! Please!", "Be an outcast?! Uh-uh, no way"]},
    {"question_text": "Would you rather live the next 10 years of your life in China or Russia?", 
    "choices": ["Not a fan of crowded places! Mother Russia. Here I come!", "你好吗? 我很好"]},
    {"question_text": "Would you rather be lost at night in a bad part of town or lost in the forest?", 
    "choices": ["A forest would be a safer option", "Not all people are bad! I'll find someone good in the city"]},
    {"question_text": "Would you rather give up bathing for a month or give up the internet for a month?", 
    "choices": ["WHAT?!? No internet?! Not happening", "There is no way, I'm giving up bathing. Besides, people have lived without internet before"]},
    {"question_text": "Would you rather never have to clean a bathroom again or never have to do dishes again?", 
    "choices":["Dishes! There are just too many of them", "Bathroom! Doing dishes in not gross."]},
    {"question_text": "Would you rather never lose your phone again or never lose your keys again?", 
    "choices": ["Keys! I hate looking for them all over the place", "Phone! I can live without keys"]},
    {"question_text": "Would you rather never get angry or never be envious?", 
    "choices":["I'll dump anger! Hopefully I won't need anger management therapy anymore", "I'll drop envy! I can finally be happy that my friend bought a new car"]},
    {"question_text": "Would you rather be fluent in all languages and never be able to travel or be able to travel anywhere but never be able to learn a word of a different language?",
    "choices": ["I'll travel, who needs to know the language anyway?", "I just love to show my language skills.You can't take it away from me!"]},
    {"question_text":"Would you rather be famous when you are alive and forgotten when you die or unknown when you are alive but famous after you die?", 
    "choices": ["Famous while Alive. Surely, the correct choice!", "People will read about me in the books!! Nice!"]},
    {"question_text": "Would you rather have a horrible job, but be able to retire comfortably in 10 years or have your dream job, but have to work until the day you die?",
    "choices": ["I't my dream job! I love doing it!", "10 years and be free? Sounds like not a bad deal!"]},
    {"question_text":"Would you rather be blind or be dumb", 
    "choices": ["F**ck! Do I really have to choose? I'll be dumb", "I can't possibly think of a reason to chose blindness."]},
    {"question_text":" Would you rather be too busy or be bored?", 
    "choices": ["I'm always busy!I've got used to that", "Ugh! I hate rushing! I would rather be bored"]},
]

def create_would_questions(would_questions):
    category = Category.objects.get(name="Would you rather")
    for i in range(len(would_questions)):
        question = Question.objects.create(question_text=would_questions[i]['question_text'])
        category.question.add(question)
        choices = would_questions[i]['choices']
        for choice in choices:
            question.choice_set.create(choice_text=choice)
            
political = [
    {"question_text": "Guns or no guns", 
    "choices": ["No guns no life", "Make Love not war"]}, 
    {"question_text": "Should prostitution be legalized and taxated", 
    "choices": ["No doubt!", "What? Are you insane?!No!No, No!!", "I don't really care"]},
    {"question_text": "Does vaccination should be obligatory", 
    "choices": ["NO!", "It really depends!", "Well, yeah! It is only logical"]},
    {"question_text": "Abortion?", 
    "choices": ["Should be banned", "Should be accessible", "Um, I don't really care`"]},
    {"question_text": "Should MJ be legalized?", 
    "choices": ["Hell, yeah!", "Hell, no!", "Hell.."]},
]

def create_polit_questions(political):
    category = Category.objects.get(name="Let's get political")
    for i in range(len(political)):
        question = Question.objects.create(question_text=political[i]['question_text'])
        category.question.add(question)
        choices = political[i]['choices']
        for choice in choices:
            question.choice_set.create(choice_text=choice)

serious_questions = [
    {"question_text": "Which came first: the chicken or the egg?",
    "choices": ["Duh, the egg was first!", "Obviously, Chicken came first"]},
    {"question_text": "Which came first, the seed or the plant?", 
    "choices": ["Seed. No seed no plant", "Actually, it was plant!"]},
    {"question_text": "Is 2 + 2 always 4?", 
    "choices": ["In a simple math maybe! But our math is complex", "What else would it be! It is so simple!"]},
    {"question_text": "Can God create a stone so heavy that he could not lift it ?", 
    "choices": ["Sure thing! He is omnipotent", "Well, no! It will contradict his omnipotence!"]},
    {"question_text": "Does the barber shave himself?", 
    "choices": ["He can't! Barber is the one who shaves the others", "Sure! Him shaving himself doesn't change the fact that he is barber"]},
    {"question_text": "If man evolved from monkeys, how come we still have monkeys?", 
    "choices": ["That is an interesting thought", "You could not have be more wrong! Humans DID NOT evolved from monkeys!"]},
    {"question_text": "Which came first, DNA or protein?", 
    "choices": ["DNA!!", "It was obviously protein!!"]},
    {"question_text": "How do you know you exist?", 
    "choices": ["I think therefore I am", "I don't know that!", "We live in a matrix!"]},
    {"question_text": "Is the Earth Flat?", 
    "choices": ["..(sigh)", "Not sure! I have not seen it from far out", "Earth IS Flat!!"]},
    {"question_text": "Is zebra black or white?", 
    "choices": ["Black!", "White!", "Zebra is striped"]},
]

def create_serious_questions(serious_questions):
    category = Category.objects.get(name="Serious questions")
    for i in range(len(serious_questions)):
        question = Question.objects.create(question_text=serious_questions[i]['question_text'])
        category.question.add(question)
        choices = serious_questions[i]['choices']
        for choice in choices:
            question.choice_set.create(choice_text=choice)

vs = [
    {"question_text": "McDonald's or Burger King?", 
    "choices": ["I'll have some Mac, thanks", "I could not live without Whooper"]}, 
    {"question_text": "Cat or Dog?", 
    "choices": ["Dog", "Cat", "Hamster"]},
    {"question_text": "Batman or Superman?", 
    "choices": ["Is there even a question? Superman", "Batman is way cooler"]},
    {"question_text": "Coffee or Tea?", 
    "choices": ["The Britain in me picks Tea!", "I need more Coffee"]},
    {"question_text": "Kylie or Kendall?", 
    "choices": ["Kylie is so fricking sexy", "Kendall is an absolute beauty"]},
    {"question_text": "Manga or Anime?", 
    "choices": ["I prefer my stories full. Manga!", "I'm more of a watcher kinda guy/gal"]},
    {"question_text": "Facebook or Twitter?", 
    "choices": ["Good old Fb feels like home", "Tweet-tweet-tweet-tweet"]},
    {"question_text": "V or Jungkook?", 
    "choices": ["There is no easy choice! But..V", "It has always been Jungkook! I am sorry.", "Can I have both?"]},
    {"question_text": "Love or Money", 
    "choices": ["Money cuz no money no honey", "Love cuz no money no problems"]},
    {"question_text": "Vampires or Werewolves?", 
    "choices": ["Vampires! Ain't werewolves are basically dogs anyway?!", "Definitely, Werewolves!They seems to be stronger than Vampires!"]},
    {"question_text": "TikTok or Snapchat?", 
    "choices": ["Like I have a choice now?! TikTok wiil be banned soon!!", "Well, Snapchat users seems to be a bit older"]},
    {"question_text": "Saitama or Zeno?", 
    "choices": ["Zeno would erase Saitama out of existence", "Saitama EASILY one-punches Zeno out!"]},
    {"question_text": "City or suburbs?", 
    "choices": ["The city is too loud! Suburbs is what does it for me", "City never sleeps so am I!"]},
    {"question_text": "Scrambled or Sunny Side Up?", 
    "choices": ["I prefer my eggs Scrambled!", "There is nothing better than Sunny Side Up eggs for breakfast!"]},
    {"question_text": "Apple or Android?", 
    "choices": ["There is no better products than Apple", "It has always been Android for me! It's easy and nice!"]}
]
def create_preference_questions(vs):
    category = Category.objects.get(name="Personal preferences")
    for i in range(len(vs)):
        question = Question.objects.create(question_text=vs[i]['question_text'])
        category.question.add(question)
        choices = vs[i]['choices']
        for choice in choices:
            question.choice_set.create(choice_text=choice)

movie = [
    {"question_text": "Lucifer?", 
    "choices": ["I LOVE it!", "Haven't seen it!", "Average"]},
    {"question_text": "Better call Saul?", 
    "choices": ["Masterpiece! Brilliant!", "I liked Breaking Bad better", "I don't know any Saul!"]},
    {"question_text": "Game of Thrones?", 
    "choices": ["The best show of all times!", "Dissapponting! Especially the ending!", "Haven't seen it! Is it any good?"]},
    {"question_text": "Bloodshot?", 
    "choices": ["Loved it!", "Well, that was..dissapponting", "It's was okay!"]},
    {"question_text": "Tenet?", 
    "choices": ["Can't wait!", "What is the big deal, it is just a movie", "I'll watch once it is out."]},
    {"question_text": "'The Lying Life of Adults' by Elena Ferrante", 
    "choices": ["Thanks for reminding! I'll go buy it now!", "Who has time to read nowadays?! Will be there a movie based on this?", "It was definitely worth every penny"]},
    {"question_text": "'The Glass Hotel' by Emily St. John Mandel ?", 
    "choices": ["Definitely in my 'To read' list!", "Didn't I said, I don't read a lot!!", "It's excellent"]},
]

def create_movie_questions(movie):
    category = Category.objects.get(name="Movie night")
    for i in range(len(movie)):
        question = Question.objects.create(question_text=movie[i]['question_text'])
        category.question.add(question)
        choices = movie[i]['choices']
        for choice in choices:
            question.choice_set.create(choice_text=choice)


fun = [
    {"question_text": "I talked to myself a lot! Crazy much?", 
    "choices": ["It is fine as long as no one hears you!", "Wait, are you saying it isn't normal and I should start worrying about myself?!", "Woah, you are one crazy guy"]},
    {"question_text": "I want to become famous", 
    "choices": ["Yeah? Well, get in line!", "Why would you want something meaningless?!", "And I want to be beautifull"]},
    {"question_text": "I am bored!", 
    "choices": ["Watch something!", "Read a book! You halfwit!!", "Hi, Bored! You have unique name!"]},
    {"question_text": "I spend all my free time in front of the computer. Am I addicted?", 
    "choices": ["Yup! There is no mistake!", "Nah, you are fine! I do the same!", "Who cares? As long as you have fun"]},
]


def create_fun_questions(fun):
    category = Category.objects.get(name="I'm here to have fun!")
    for i in range(len(fun)):
        question = Question.objects.create(question_text=fun[i]['question_text'])
        category.question.add(question)
        choices = fun[i]['choices']
        for choice in choices:
            question.choice_set.create(choice_text=choice)