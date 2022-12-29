import random

#database
champions = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios', 'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath", 'Corki', 'Darius', 'Diana', 'Dr. Mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger', 'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'Sa", 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle', 'Kayn', 'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'LeBlanc', 'Lee Sin', 'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nocturne', 'Nunu', 'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Rell', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar', "Vel'Koz", 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
boots = ["Berserker's Greaves", "Boots of Swiftness", "Ionian Boots of Lucidity", "Mercury's Treads", "Mobility Boots", "Plated Steelcaps", "Sorcerer's Shoes"]
mythic_items = ["Divine Sunderer", "Duskblade of Draktharr", "Eclipse", "Everfrost", "Frostfire Gauntlet", "Galeforce", "Goredrinker", "Hextech Rocketbelt", "Immortal Shieldbow", "Imperial Mandate", "Kraken Slayer", "Liandry's Anguish", "Locket of the Iron Solari", "Luden's Echo", "Moonstone Renewer", "Night Harvester", "Prowler's Claw", "Riftmaker", "Shurelya's Battlesong", "Stridebreaker", "Sunfire Aegis", "Trinity Force", "Turbo Chemtank"]
legendary_items = ["Abyssal Mask", "Anathema's Chains", "Archangel's Staff", "Ardent Censer", "Banshee's Veil", "Black Cleaver", "Black Mist Scythe", "Blade of the Ruined King", "Bloodthirster", "Bulwark of the Mountain", "Chempunk Chainsword", "Chemtech Putrifier", "Cosmic Drive", "Dead Man's Plate", "Death's Dance", "Demonic Embrace", "Edge of Night", "Essence Reaver", "Force of Nature", "Frozen Heart", "Gargoyle Stoneplate", "Guardian Angel", "Guinsoo's Rageblade", "Horizon Focus", "Hullbreaker", "Infinity Edge", "Knight's Vow", "Lich Bane", "Lord Dominik's Regard", "Manammune", "Maw of Malmortius", "Mejai's Soulstealer", "Mercurial Scimitar", "Mikael's Blessing", "Morellonomicon", "Mortal Reminder", "Muramana", "Nashor's Tooth", "Navori Quickblades", "Pauldrons of Whiterock", "Phantom Dancer", "Rabadon's Deathcap", "Randuin's Omen", "Rapid Firecannon", "Ravenous Hydra", "Redemption", "Runaan's Hurrican", "Rylai's Crystal Scepter", "Seraph's Embrace", "Serpent's Fang", "Serylda's Grudge", "Shard of True Ice", "Silvermere Dawn", "Spirit Visage", "Staff of Flowing Water", "Sterak's Gage", "Stormrazor", "The Collector", "Thornmail", "Titanic Hydra", "Umbral Glaive", "Vigilant Wardstone", "Void Staff", "Warmog's Armor", "Wit's End", "Youmuu's Ghostblade", "Zeke's Convergence", "Zhonya's Hourglass"]
spells = ["Heal", "Ghost", "Barrier", "Exhaust", "Teleport", "Smite", "Cleanse", "Ignite"]
rune_pages = ["Precision", "Domination", "Sorcery", "Resolve", "Inspiration"]
abilities = ["q", "w", "e"]
roles = ["Top", "Jungle", "Mid", "ADC", "Support"]
Precision = {"Press the Attack":"Keystone", "Lethal Tempo":"Keystone", "Fleet Footwork":"Keystone", "Conqueror":"Keystone", "Overheal":"Slot 1", "Triumph":"Slot 1", "Presence of Mind":"Slot 1", "Alacrity":"Slot 2", "Tenacity":"Slot 2", "Bloodline":"Slot 2", "Coup de Grace":"Slot 3", "Cut Down":"Slot 3", "Last Stand":"Slot 3"}
Domination = {"Electrocute":"Keystone", "Predator":"Keystone", "Dark Harvest":"Keystone", "Hail of Blades":"Keystone", "Cheap Shot":"Slot 1", "Taste of Blood":"Slot 1", "Sudden Impact":"Slot 1", "Zombie Ward":"Slot 2", "Ghost Poro":"Slot 2", "Eyeball Collection":"Slot 2", "Ravenous Hunter":"Slot 3", "Ingenious Hunter":"Slot 3", "Relentless Hunter":"Slot 3", "Ultimate Hunter":"Slot 3"}
Sorcery = {"Summon Aery":"Keystone", "Arcane Comet":"Keystone", "Phase Rush":"Keystone", "Nullifying Orb":"Slot 1", "Manaflow Band":"Slot 1", "Nimbus Cloak":"Slot 1", "Transcendence":"Slot 2", "Celerity":"Slot 2", "Absolute Focus":"Slot 2", "Scorch":"Slot 3", "Waterwalking":"Slot 3", "Gathering Storm":"Slot 3"}
Resolve = {"Grasp of the Undying":"Keystone", "Aftershock":"Keystone", "Guardian":"Keystone", "Demolish":"Slot 1", "Font of Life":"Slot 1", "Shield Bash":"Slot 1", "Conditioning":"Slot 2", "Second Wind":"Slot 2", "Bone Plating":"Slot 2", "Overgrowth":"Slot 3", "Revitalize":"Slot 3", "Unflinching":"Slot 3"}
Inspiration = {"Glacial Augment":"Keystone", "Unsealed Spellbook":"Keystone", "Prototype: Omnistone":"Keystone", "Hextech Flashtraption":"Slot 1", "Magical Footwear":"Slot 1", "Perfect Timing":"Slot 1", "Future's Market":"Slot 2", "Minion Dematerializer":"Slot 2", "Biscuit Delivery":"Slot 2", "Cosmic Insight":"Slot 3", "Approach Velocity":"Slot 3", "Time Warp Tonic":"Slot 3"}

#ability max order chooser
random.shuffle(abilities)

#role and champ chooser
cur_role = random.choice(roles)
cur_champ = random.choice(champions)

#spell chooser
cur_spells = []
if cur_role == "Jungle":
    cur_spells.append("Smite")
else:
    cur_spells.append(random.choice(spells))
cur_spells.append("Flash")

#item chooser
items = []
cur_mythic = random.choice(mythic_items)
items.append(cur_mythic)
cur_boots = random.choice(boots)
items.append(cur_boots)
legendary_1 = random.choice(legendary_items)
items.append(legendary_1)
legendary_2 = ""
legendary_3 = ""
legendary_4 = ""
while legendary_2 not in items and legendary_3 not in items and legendary_4 not in items:
    for i in range(1):
        legendary_2 = random.choice(legendary_items)
        legendary_3 = random.choice(legendary_items)
        legendary_4 = random.choice(legendary_items)
        items.append(legendary_2)
        items.append(legendary_3)
        items.append(legendary_4)

#primary rune page chooser
primary_rune_page_theoretical = random.choice(rune_pages)
if primary_rune_page_theoretical == "Precision":
    primary_rune_page = Precision
elif primary_rune_page_theoretical == "Domination":
    primary_rune_page = Domination
elif primary_rune_page_theoretical == "Sorcery":
    primary_rune_page = Sorcery
elif primary_rune_page_theoretical == "Resolve":
    primary_rune_page = Resolve
else:
    primary_rune_page = Inspiration

#secondary rune page chooser
secondary_rune_page_theoretical = ""
while secondary_rune_page_theoretical == "" or secondary_rune_page_theoretical == primary_rune_page_theoretical:
    for i in range(1):
        secondary_rune_page_theoretical = random.choice(rune_pages)

if secondary_rune_page_theoretical == "Precision":
    secondary_rune_page = Precision
elif secondary_rune_page_theoretical == "Domination":
    secondary_rune_page = Domination
elif secondary_rune_page_theoretical == "Sorcery":
    secondary_rune_page = Sorcery
elif secondary_rune_page_theoretical == "Resolve":
    secondary_rune_page = Resolve
else:
    secondary_rune_page = Inspiration

def primary_rune_picker(primary_rune_page):
    primary_runes = []
    keystones = []
    slot_1s = []
    slot_2s = []
    slot_3s = []
    for i in primary_rune_page:
        if primary_rune_page[i] == "Keystone":
            keystones.append(i)
        elif primary_rune_page[i] == "Slot 1":
            slot_1s.append(i)
        elif primary_rune_page[i] == "Slot 2":
            slot_2s.append(i)
        else:
            slot_3s.append(i)
    primary_runes.append(random.choice(keystones))
    primary_runes.append(random.choice(slot_1s))
    primary_runes.append(random.choice(slot_2s))
    primary_runes.append(random.choice(slot_3s))
    return primary_runes

def secondary_rune_picker(secondary_rune_page):
    secondary_runes = []
    slots = ['1', '2', '3']
    slot_1s = []
    slot_2s = []
    slot_3s = []
    choice_1 = random.choice(slots)
    choice_2 = ""
    while choice_2 == "" or choice_2 == choice_1:
        choice_2 = random.choice(slots)
    for i in secondary_rune_page:
        if secondary_rune_page[i] == "Slot 1":
            slot_1s.append(i)
        elif secondary_rune_page[i] == "Slot 2":
            slot_2s.append(i)
        elif secondary_rune_page[i] == "Slot 3":
            slot_3s.append(i)
    if choice_1 == '1':
        secondary_runes.append(random.choice(slot_1s))
    elif choice_1 == '2':
        secondary_runes.append(random.choice(slot_2s))
    elif choice_1 == '3':
        secondary_runes.append(random.choice(slot_3s))
    if choice_2 == '1':
        secondary_runes.append(random.choice(slot_1s))
    elif choice_2 == '2':
        secondary_runes.append(random.choice(slot_2s))
    elif choice_2 == '3':
        secondary_runes.append(random.choice(slot_3s))
    return secondary_runes

def get_shards():
    options_a = ['Adaptive', 'Attack Speed', 'Haste']
    options_b = ['Adaptive', 'Armour', 'Magic Resistance']
    options_c = ['Health', 'Armour', 'Magic Resistance']
    return (random.choice(options_a), random.choice(options_b), random.choice(options_c))

primary_runes = primary_rune_picker(primary_rune_page)
secondary_runes = secondary_rune_picker(secondary_rune_page)

#output  
print("Champion:", cur_champ)
print("Role:", cur_role)
print("Spells:", cur_spells)
print("Items:", items)
print("Ability max order: " + abilities[0] + " -> " + abilities[1] + " -> " + abilities[2])
print("Primary rune page:", primary_rune_page_theoretical)
print("Secondary rune page:", secondary_rune_page_theoretical)
print("Primary runes:", primary_runes)
print("Secondary runes:", secondary_runes)
print("Shards: ", get_shards())

inp = input("-: ")