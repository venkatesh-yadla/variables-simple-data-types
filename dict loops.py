favorite_languages = {        'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
   print(name.title() + "'s favorite language is " +
        language.title() + ".")

favorite_languages = {
    'jen': 'python',
    'hanta': 'c',
    'edward': 'ruby',
    'corona': 'python',
    }
friends = ['corona', 'hanta']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print("  Hi " + name.title() +
            ", I see your favorite language is " +
             favorite_languages[name].title() + "!")
