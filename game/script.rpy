# Hollow Knight Story - Visual Novel
# Background images - uniform sizing and positioning

# Background images with uniform transform properties
image bg dirtmouth = Transform("bg/dirtmouth.png", fit="cover", align=(0.5, 0.5))
image bg crossroads = Transform("bg/crossroads.png", fit="cover", align=(0.5, 0.5))
image bg greenpath = Transform("bg/greenpath.png", fit="cover", align=(0.5, 0.5))
image bg fungal = Transform("bg/fungal_wastes.png", fit="cover", align=(0.5, 0.5))
image bg city = Transform("bg/city_of_tears.png", fit="cover", align=(0.5, 0.5))
image bg nosk_lair = Transform("bg/nosk_lair.png", fit="cover", align=(0.5, 0.5))
image bg peak = Transform("bg/crystal_peak.png", fit="cover", align=(0.5, 0.5))
image bg abyss = Transform("bg/abyss.png", fit="cover", align=(0.5, 0.5))
image bg temple = Transform("bg/black_egg_temple.png", fit="cover", align=(0.5, 0.5))
image bg white_palace = Transform("bg/white_palace.png", fit="cover", align=(0.5, 0.5))
image bg dream = Transform("bg/dream_realm.png", fit="cover", align=(0.5, 0.5))
image bg blue_lake = Transform("bg/blue_lake.png", fit="cover", align=(0.5, 0.5))
image bg soul_sanctum = Transform("bg/soul_sanctum.png", fit="cover", align=(0.5, 0.5))
image bg mantis_village = Transform("bg/mantis_village.png", fit="cover", align=(0.5, 0.5))



# Character sprites - consistent sizing and positioning (positioned well above textbox)
image knight = Transform("characters/the_knight.png", zoom=0.8, align=(0.5, 0.65))
image hornet = Transform("characters/hornet.png", zoom=0.8, align=(0.5, 0.65))
image elderbug = Transform("characters/elderbug.png", zoom=0.8, align=(0.5, 0.65))
image quirrel = Transform("characters/quirrel.png", zoom=1.8, align=(0.5, 0.65))
image myla = Transform("characters/myla.png", zoom=0.8, align=(0.5, 0.65))
image lemm = Transform("characters/lemm.png", zoom=0.8, align=(0.5, 0.65))
image cornifer = Transform("characters/cornifer.png", zoom=1.8, align=(0.5, 0.65))
image cloth = Transform("characters/cloth.png", zoom=0.8, align=(0.5, 0.65))
image pale_king = Transform("characters/pale_king.png", zoom=1, align=(0.5, 0.65))
image white_lady = Transform("characters/white_lady.png", zoom=0.8, align=(0.5, 0.65))
image radiance = Transform("characters/radiance.png", zoom=1.8, align=(0.5, 0.65))
image hollow_knight = Transform("characters/the_hollow_knight.png", zoom=1.8, align=(0.5, 0.65))
image soul_master = Transform("characters/soul_master.png", zoom=1.2, align=(0.5, 0.65))
image nosk = Transform("characters/nosk.png", zoom=1.2, align=(0.5, 0.65))


# Transition definitions
define fade_slow = Fade(2.0, 0.5, 2.0)
define fade_fast = Fade(0.5, 0.2, 0.5)

# Custom positioning transforms to place sprites above textbox
transform above_textbox_center:
    xalign 0.5
    yalign 0.65

transform above_textbox_left:
    xalign 0.2
    yalign 0.65

transform above_textbox_right:
    xalign 0.8
    yalign 0.65

# This is a narrative adaptation of the Hollow Knight storyline

# Character definitions (knight, hornet, elderbug, quirrel are defined in character_system.rpy)
define myla = Character("Myla", color="#ffa500")
define lemm = Character("Lemm", color="#d2691e")
define sly = Character("Sly", color="#808080")
define cornifer = Character("Cornifer", color="#daa520")
define cloth = Character("Cloth", color="#ff69b4")
define ghost = Character("???", color="#cccccc")
define pale_king = Character("The Pale King", color="#f0f0f0")
define white_lady = Character("The White Lady", color="#e8f5e8")
define radiance = Character("The Radiance", color="#ffff00")
define hollow_knight = Character("The Hollow Knight", color="#000000")
define soul_master = Character("Soul Master", color="#9370db")
define nosk = Character("Nosk", color="#8b0000")
define narrator = Character(None)

# Start of the game
label start:
    # Opening with Enter Hallownest theme
    $ play_opening_music()
    
    scene black with fade_slow
    
    narrator "Long ago, a great kingdom rose beneath the ground."
    
    narrator "In the deepest reaches of the world, vessels were born from the Void itself."
    
    narrator "Countless shells, created for a single purpose - to contain an ancient infection."
    
    scene bg white_palace with fade_slow
    show pale_king at above_textbox_center with dissolve
    
    narrator "The Wyrm became the Pale King, and brought sapience to the bugs of Hollownest."
    
    hide pale_king with dissolve
    
    scene bg dream with fade_slow
    show radiance with dissolve
    
    narrator "But from the depths of dreams, a forgotten light began to call..."
    
    narrator "An infection spread through the kingdom, turning bugs into mindless husks."
    
    hide radiance with dissolve
    
    scene bg abyss with fade_slow
    
    narrator "To contain this plague, the Pale King created a plan - a Vessel, hollow and pure."
    
    narrator "In the deepest pit, vessels climbed endlessly, seeking to prove their worth."
    
    narrator "One vessel was chosen above all others, deemed perfect for the terrible task ahead."
    
    narrator "Sealed away was the Radiance, the source of infection, contained within the chosen vessel."
    
    scene bg temple with fade_slow
    
    narrator "For a time, the kingdom knew peace. The chosen vessel stood bound in eternal vigil."
    
    narrator "Chains of light held it fast, while three Dreamers maintained the seals."
    
    narrator "But no vessel is truly hollow... and no seal is perfect forever."
    
    narrator "The seals began to fail. The infection returned, seeping through cracks in the prison."
    
    scene bg abyss with fade_slow
    show knight at above_textbox_center with dissolve
    narrator "And so, a forgotten vessel awakens, drawn by an ancient call..."
    
    # Add a choice for player engagement
    menu:
        "What drives this awakening?"
        
        "An ancient calling compels you":
            $ knight_personality = "driven"
            show knight
            narrator "You rise, drawn by an inexorable force. Purpose flows through the void within."
            
        "Instinct guides your movements":
            $ knight_personality = "instinctual" 
            narrator "You move without thought or reason. The vessel simply acts as it was made to."
            
        "Nothing - you are empty":
            $ knight_personality = "hollow"
            narrator "You are void. You simply exist to act. Nothing more."
    
    scene bg dirtmouth with fade_slow
    $ play_area_music("dirtmouth")
    
    "You arrive at Dirtmouth, a small settlement on the surface above the kingdom."
    "The town is nearly deserted, with only a few stragglers remaining."
    "The wind whistles through empty buildings, carrying whispers of a lost civilization."
    
    show elderbug at above_textbox_center with dissolve
    elderbug "Oh! A visitor? I haven't seen a new face in quite some time."
    
    show elderbug
    elderbug "Welcome to Dirtmouth, little one. Though I'm afraid there's not much here anymore."
    
    show elderbug
    elderbug "Most everyone's gone. Driven away by the dreams... or lured down into that kingdom below."
    elderbug "If you're thinking of heading down there yourself, be careful."
    elderbug "There's something wrong with that place. The air itself feels... sick."
    
    menu:
        "How do you respond to Elderbug's warning?"
        
        "Nod silently and prepare to descend":
            show knight at above_textbox_right with dissolve
            elderbug "...I see that look. You're determined, aren't you?"
            elderbug "Well, if you must go, take this old key. Found it years ago."
            "Elderbug gives you a Simple Key."
            $ inventory_simple_key = True
            
        "Try to communicate your purpose":
            show knight at above_textbox_right with dissolve
            narrator "You gesture toward the well, then point to yourself."
            elderbug "Ah, you feel called to that place too, don't you?"
            elderbug "Many have felt that pull. Few have returned."
            
        "Show concern for the old bug":
            show knight at above_textbox_right with dissolve  
            elderbug "Worried about me? How kind..."
            elderbug "Don't you fret. I've survived this long by staying right here."
            elderbug "It's those who venture below that you should worry about."
    
    hide elderbug with dissolve
    
    "You descend into the well, entering the ruins of Hallownest."
    
    scene black with fade_fast
    "The darkness swallows you as you fall deeper..."
    
    scene bg crossroads with fade_slow
    $ play_area_music("crossroads")
    
    narrator "The Forgotten Crossroads - once a bustling intersection of the kingdom."
    
    narrator "Now, only husks remain, shambling mindlessly through the dark."
    
    narrator "A sickly orange haze permeates the air, making breathing difficult."
    
    narrator "The infection's presence is detectable, a wrongness in the air that your void senses."
    
    "You encounter infected bugs, their eyes glowing with an unnatural light."
    
    "They move with jerky, puppet-like motions, attacking without thought or reason."
    
    "The plague has consumed their minds, leaving only mindless aggression."
    
    menu:
        "How do you engage the infected creatures?"
        
        "Strike with mechanical precision":
            "You dispatch them with calculated strikes."
            "Each movement is efficient, purposeful."
            $ combat_style = "precise"
            
        "Move defensively, conserve motion":
            "You dodge their attacks, striking only when necessary."
            "The void guides your movements with cold efficiency."
            $ combat_style = "defensive"
            
        "Act on pure instinct":
            "The void within responds to threat with immediate action."
            "You move without thought, only purpose."
            $ combat_style = "aggressive"
    
    "After dispatching the infected creatures, an unsettling silence falls over the caverns."
    
    "As you explore deeper, you discover a map maker's tools and papers scattered about."
    
    show cornifer at above_textbox_center
    cornifer "Hmm? Oh! Another traveler! How delightful!"
    cornifer "I'm Cornifer, cartographer extraordinaire. I'm mapping these old ruins."
    cornifer "Here, I've made a spare map of this area. You can have it!"
    cornifer "If you find me again, I'll have maps of other areas too. Hm hm hmm!"
    
    hide cornifer
    
    "You continue deeper, finding remnants of the kingdom's former glory."
    
    label greenpath_section:
    scene bg greenpath
    $ play_area_music("greenpath")
    
    narrator "Greenpath - an overgrown area, reclaimed by nature."
    
    narrator "Yet even here, the infection festers."
    
    "The verdant growth seems almost alive, twisting and moving in your peripheral vision."
    
    "You press forward, your void senses detecting wrongness."
    
    "Suddenly, a needle flies past your head!"
    
    show hornet at above_textbox_center with dissolve
    hornet "So, another empty vessel makes its way to Hallownest."
    
    show hornet
    hornet "I've been waiting for you, little ghost."
    hornet "If you're here to take on the infection, you'll need to prove yourself."
    
    show hornet
    hornet "Show me you're more than just another walking husk!"
    
    # Interactive battle sequence
    scene black with fade_fast
    $ play_battle_music("hornet")
    
    narrator "The air crackles with tension as Hornet readies her needle."
    
    narrator "She moves with deadly grace, her silk cloak flowing behind her like shadow."
    
    narrator "This is more than a fight - it's a test of your very essence."
    
    "BATTLE: Hornet - Guardian of Greenpath"
    
    menu:
        "Hornet attacks with incredible speed. How do you respond?"
        
        "Focus on dodging and counterattacking":
            "You dash away from her strikes and find openings."
            $ hornet_battle_style = "tactical"
            
        "Match her aggression with your own":
            "You meet her blade with yours in a fierce exchange."
            $ hornet_battle_style = "aggressive"
            
        "Stay defensive and observe her patterns":
            "You block and parry, your void senses tracking her movements."
            $ hornet_battle_style = "defensive"
    
    scene bg greenpath with fade_fast
    $ play_area_music("greenpath")
    
    if hornet_battle_style == "tactical":
        show hornet at above_textbox_center with dissolve
        hornet "...Impressive. You fight with wisdom, not just instinct."
    elif hornet_battle_style == "aggressive": 
        show hornet at above_textbox_center with dissolve
        hornet "Such fury... You're more dangerous than I expected."
    else:
        show hornet at above_textbox_center with dissolve
        hornet "Cautious and observant. Perhaps there's hope for you yet."
    
    hornet "You have strength, and skill. But is that enough?"
    hornet "The path ahead will test you far more than I have."
    
    show hornet
    hornet "Prove yourself worthy of facing what lies in the Temple."
    hornet "And be warned - I am watching your progress."
    
    hide hornet with dissolve
    
    "Following paths revealed by your growing connection to the kingdom's memory..."
    "You sense something calling from the crystal mines above."
    
    label crystal_peak_section:
    scene bg peak
    $ play_area_music("crystal_peak")
    
    narrator "Crystal Peak - a mining operation where the infected seek the light of pure crystal."
    
    narrator "The pink crystals resonate with an eerie energy, their light both beautiful and unsettling."
    
    "You hear someone singing in the distance."
    
    "The melody is hauntingly beautiful, yet somehow sad."
    
    show myla at above_textbox_center with dissolve
    myla "♪ Bury my body and blacken my eyes ♪"
    myla "♪ Bury my body, don't blacken my eyes! ♪"
    
    show myla
    myla "Oh! Hello there! I'm Myla!"
    myla "I'm digging for treasure! The crystals here sing such pretty songs."
    
    show myla
    myla "Sometimes I hear voices in them... telling me to dig deeper..."
    myla "Do you hear them too?"
    
    menu:
        "How do you respond to Myla?"
        
        "Attempt to signal danger":
            show knight at above_textbox_right with dissolve
            narrator "You gesture mechanically, your void senses detecting wrongness."
            myla "Oh, you're trying to tell me something? That's sweet!"
            myla "But the voices are so lovely. They sing of wonderful things below..."
            $ myla_warned = True
            
        "Listen to the crystals yourself":
            show knight at above_textbox_right with dissolve
            narrator "You focus on the crystal sounds..."
            narrator "For a moment, you hear something... calling..."
            myla "You hear them too! Aren't they beautiful?"
            $ heard_crystal_voices = True
            
        "Simply observe her mining":
            show knight at above_textbox_right with dissolve
            narrator "You watch her work, noting her cheerful demeanor."
            narrator "Your void senses detect something amiss in this place, though she appears content."
            myla "Thanks for keeping me company! It gets lonely here."
    
    hide myla with dissolve
    hide knight with dissolve
    
    "You delve deeper into the crystal mines, the pink light growing ever brighter."
    
    "The crystals seem to pulse with the heartbeat of something vast and ancient."
    
    label fungal_section:
    scene bg fungal
    $ play_area_music("fungal")
    
    narrator "The Fungal Wastes - a network of caverns choked with mushrooms."
    narrator "The mantis tribes once kept order here."
    
    "You find a figure studying a tablet on the wall."
    
    show quirrel at above_textbox_center
    quirrel "Ah, hello there. Enjoying the sights?"
    quirrel "These structures are fascinating. The craftsmanship speaks of a civilization that reached great heights."
    quirrel "I've been traveling through Hallownest, trying to piece together its history."
    quirrel "Something brought me here... though I can't quite remember what."
    quirrel "Do you ever feel that way? Like you're following a path laid out long ago?"
    
    hide quirrel
    
    "You locate the Mantis Village and earn the respect of the Mantis Lords through combat."
    "They bow to you, granting passage to Deepnest."
    
    label city_section:
    scene bg city
    $ play_area_music("city")
    
    narrator "The City of Tears - capital of Hallownest."
    narrator "Once the jewel of the kingdom, now weeping with eternal rain."
    
    "You encounter more survivors and learn fragments of history."
    
    show lemm at above_textbox_center
    lemm "Hmm? What's this? You have relics? Let me see them."
    lemm "Fascinating... These are remnants of the old kingdom."
    lemm "This seal here, it bears the King's mark. He was the Pale King, the Wyrm."
    lemm "He raised this kingdom from nothing, gave the bugs here minds of their own."
    lemm "But something went wrong. The kingdom fell to some kind of plague."
    lemm "The King tried to stop it... but even he failed in the end."
    
    hide lemm
    
    "You discover the entrance to the Soul Sanctum, a tower of twisted knowledge."
    "The air reeks of soul magic and failed experiments."
    "Inside, you find the Soul Master - once a scholar, now a grotesque creature."
    
    show soul_master at above_textbox_center with dissolve
    "He floats in the air, surrounded by orbs of stolen soul energy."
    "His experiments on living bugs were his desperate attempt to combat the infection."
    "Now he is as corrupted as the plague he sought to cure."
    
    soul_master "Ahhhh... Another vessel comes seeking power?"
    soul_master "I have studied SOUL! I have mastered it! I am immortal!"
    
    narrator "The Soul Master laughs maniacally as he hurls magical attacks."
    narrator "His body phases between solid and ethereal, drunk on soul power."
    
    "BATTLE: Soul Master"
    
    narrator "The Soul Master's form begins to waver as his stolen SOUL energy dissipates."
    soul_master "Impossible... my research... my immortality..."
    narrator "His body crumbles to dust, the stolen souls finally freed."
    
    hide soul_master with dissolve
    
    "You explore deeper and find a memorial to the Hollow Knight."
    
    narrator "Here lies the Vessel, the Hollow Knight, chosen to seal the Radiance."
    narrator "Pure and hollow, free of thought and emotion."
    narrator "The kingdom's sacrifice... and its hope."
    
    label nosk_section:
    scene bg nosk_lair
    $ play_area_music("nosk")
    
    narrator "The twisted tunnels beneath Hallownest - a place where nightmares take shape."
    narrator "In these depths, something mimics the forms of those who enter..."
    
    "You navigate through the disturbing caverns, your void senses detecting a presence."
    "Strange sounds echo from the darkness - footsteps that match your own."
    
    "In the depths, you encounter a horrifying revelation."
    "Something has been following you, learning from you, copying you..."
    
    show knight at above_textbox_right
    "You see yourself across a chasm - but something is wrong."
    "The mirror image moves differently, with predatory intent."
    
    narrator "This is Nosk - a creature that mimics the forms of those who enter its domain."
    
    narrator "It has been hunting you, studying you, becoming you."
    
    menu:
        "How do you confront this twisted reflection?"
        
        "Approach directly without hesitation":
            "You move forward with mechanical precision."
            "If it seeks to copy you, it will find only emptiness."
            $ nosk_approach = "direct"
            
        "Observe the creature's form":
            "You study the creature with hollow focus."
            "It mimics your shell, but cannot replicate the void within."
            $ nosk_approach = "observant"
            
        "Strike without delay":
            "You act on pure instinct, no thought behind the motion."
            "The void recognizes a false copy and moves to eliminate it."
            $ nosk_approach = "instinctual"
    
    narrator "The creature's true form is revealed - a mass of writhing flesh and too many limbs."
    
    show nosk at above_textbox_center with dissolve
    narrator "It moves with unnatural speed, skittering across walls and ceiling."
    
    nosk "..."  # Nosk doesn't speak - only mimics sounds
    narrator "It lets out a horrible screech that sounds like your own voice, distorted."
    
    narrator "Every attack it makes mimics your own movements, but twisted and wrong."
    
    "BATTLE: Nosk - The Shapeshifter"
    
    if nosk_approach == "direct":
        "Your hollow nature proves impenetrable to the creature's mimicry."
        "It cannot copy what was never truly there."
    elif nosk_approach == "observant":
        "In defeating Nosk, you demonstrate the futility of imitation."
        "A shell can be copied, but the void within remains untouchable."
    else:
        "You eliminate the false copy without emotion or hesitation."
        "The void does not recognize imposters - it simply acts."
    
    narrator "Nosk's form collapses, its mimicry finally broken."
    narrator "The false knight dissolves into shadow and ichor."
    
    hide nosk with dissolve
    hide knight with dissolve
    
    "You encounter Herrah the Beast, one of the three Dreamers."
    "To break the seal on the Black Egg, you must defeat the Dreamers."
    
    "Using the Dream Nail, you enter her dreams."
    
    scene bg dream
    narrator "In dreams, you witness a memory..."
    narrator "The Pale King stood before Herrah the Beast."
    
    pale_king "The kingdom requires your sacrifice, Herrah."
    pale_king "Sleep eternal, to maintain the seals. This is the price of stopping the infection."
    
    "Herrah agreed, but on one condition - that she would have an heir."
    "The King agreed. Hornet was born, the gendered child."
    
    "You defeat Herrah's dream form, breaking one seal."
    
    scene bg nosk_lair
    
    label more_exploration:
    scene bg blue_lake
    $ play_area_music("resting_grounds")
    narrator "As your journey continues, you gather more fragments of the truth."
    
    "You find Quirrel again at the Blue Lake."
    
    show quirrel at above_textbox_center
    quirrel "Ah, it's you again. How far we've both come."
    quirrel "You know, I've been all through Hallownest now. I've seen its wonders and its horrors."
    quirrel "This lake... it's where my journey began, I think. And perhaps where it ends."
    quirrel "I remembered something. I was bound to someone once. Monomon the Teacher."
    quirrel "I was her student, her protector. But she's gone now, isn't she?"
    quirrel "You released her from her dream. Thank you for that."
    quirrel "I think... I think I can rest now."
    
    hide quirrel
    
    narrator "You never see Quirrel again. His nail rests by the lake."
    
    scene bg peak
    $ play_area_music("crystal_peak")
    "You pass through Crystal Peak again."
    "Myla is still there, mining."
    
    show myla at above_textbox_center
    myla "? ...dig... deeper... ?"
    "Her eyes glow orange. She doesn't recognize you anymore."
    "She attacks mindlessly. The infection has taken her."
    
    hide myla
    
    narrator "Another life claimed by the plague."
    
    label restinggrounds_section:
    scene bg temple
    $ play_area_music("resting_grounds")
    
    narrator "The Resting Grounds - where the dead are laid to rest."
    narrator "Here, dream and reality blur."
    
    "You defeat the other two Dreamers: Lurien the Watcher in the City, and Monomon the Teacher in Fog Canyon."
    
    "With all three seals broken, the way to the Black Egg Temple opens."
    
    show hornet at above_textbox_center
    hornet "Little ghost. You've proven yourself strong."
    hornet "The Dreamers are no more. The seal will break."
    hornet "But do you understand what you're walking into?"
    hornet "The vessel sealed within... it was meant to be hollow. Empty. Pure."
    hornet "But even it failed. The infection seeped in through cracks in its shell."
    hornet "What makes you think you'll succeed where it didn't?"
    
    knight "..."
    
    hornet "...I see. You don't care about success. You just do what you must."
    hornet "Very well. But know this - I am the daughter of Herrah and the Pale King."
    hornet "I am the last protector of this kingdom. If you fail..."
    hornet "I will be the one to stop you."
    
    hide hornet
    
    label black_egg:
    scene bg temple
    $ play_area_music("temple")
    
    narrator "The Temple of the Black Egg."
    narrator "The chains binding the door shatter. The way is open."
    
    "You enter the egg."
    
    scene bg abyss
    "In the darkness, a figure stands, held by chains of light."
    
    show hollow_knight at above_textbox_center
    "The Hollow Knight - your sibling, the Pure Vessel."
    "Infection leaks from cracks in its shell. Its eyes glow with orange light."
    "It raises its nail against you."
    
    $ play_battle_music("hollow_knight")
    narrator "Your sibling moves with practiced skill, but something is terribly wrong."
    narrator "Orange light leaks from cracks in its shell like infected blood."
    narrator "Each strike it makes seems to cause it pain, as if fighting against itself."
    
    "BATTLE: The Hollow Knight"
    
    narrator "As you fight, you see the truth - this vessel was never truly hollow."
    narrator "The Pale King's love for it created the first crack in its shell."
    narrator "Through that crack, the Radiance began to seep in over countless years."
    
    "As you fight, the Knight falters. It stabs itself, trying to contain the infection."
    "The blade pierces its own shell in a desperate attempt to release the pressure within."
    "But it's no use. The Radiance screams from within, demanding freedom."
    
    hide hollow_knight
    
    menu:
        "You have a choice."
        
        "Seal the infection within yourself (Hollow Knight Ending)":
            jump hollow_ending
            
        "Use the Dream Nail on the Hollow Knight (Continue)":
            jump dream_ending
    
    label hollow_ending:
    $ stop_music()
    narrator "You take your sibling's place."
    narrator "Hornet enters the temple as you are bound by the seals."
    
    show hornet at above_textbox_center
    hornet "So, you've chosen to become the seal."
    hornet "Just like it did. Just like the King intended."
    hornet "But you're no more hollow than it was."
    hornet "This won't last. The infection will return."
    hornet "But... perhaps you'll buy us time. Time to find another way."
    
    scene bg temple
    $ play_area_music("resting_grounds")  # Somber music for this bittersweet ending
    narrator "The door seals shut."
    narrator "Hallownest is saved... for now."
    narrator "But in the darkness, a new vessel sits, alone."
    narrator "And the cycle continues."
    
    "ENDING: The Hollow Knight"
    return
    
    label dream_ending:
    narrator "You plunge the Dream Nail into the Hollow Knight's head."
    narrator "Reality tears apart."
    
    scene bg dream
    $ play_battle_music("radiance")
    
    narrator "You stand in the dream realm."
    narrator "An ancient light burns before you."
    
    show radiance at above_textbox_center
    radiance "SO... ANOTHER VESSEL DARES TO CHALLENGE ME."
    radiance "THE WYRM THOUGHT HE COULD SUPPRESS ME. SEAL ME AWAY IN DARKNESS."
    radiance "BUT I AM LIGHT ITSELF. I CANNOT BE CONTAINED FOREVER."
    radiance "THESE BUGS WERE MINE. THEY WORSHIPPED ME, DREAMED OF ME."
    radiance "THEN HE CAME. HE GAVE THEM MINDS, MADE THEM FORGET ME."
    radiance "I ONLY WANTED TO BE REMEMBERED!"
    
    knight "..."
    
    radiance "YOU THINK YOU CAN DEFEAT ME? YOU ARE NOTHING. VOID. DARKNESS."
    radiance "LIGHT WILL ALWAYS TRIUMPH OVER DARK!"
    
    narrator "The dream realm shifts and warps around you as reality bends to her will."
    
    narrator "Pillars of pure light crash down where you once stood."
    
    narrator "The very air burns with her radiance, searing your shell."
    
    "FINAL BATTLE: The Radiance"
    
    narrator "You dodge between laser-like beams that carve through the dreamscape."
    
    narrator "Your void-touched blade meets her light, causing reality to fracture."
    
    narrator "She summons phantom swords of light, but your darkness consumes them."
    
    narrator "Finally, after endless strikes and void-touched attacks, she falters."
    
    radiance "NO... THIS CANNOT BE..."
    radiance "I WILL NOT... BE FORGOTTEN... AGAIN..."
    
    menu:
        "How does this end?"
        
        "Defeat the Radiance (Dream No More)":
            jump true_ending
            
        "You are not alone... (Godmaster Ending)" if False:
            jump godmaster_ending
    
    label true_ending:
    narrator "With one final strike, the Radiance screams."
    narrator "Light explodes outward, then dims."
    
    $ stop_music()
    scene bg abyss
    "You fall through darkness."
    "You see the Hollow Knight, free at last, collapsing."
    
    show hornet at above_textbox_center
    hornet "Little ghost... you actually did it."
    hornet "The infection is gone. The Radiance is defeated."
    
    scene bg temple
    $ play_area_music("dirtmouth")  # Peaceful music for the ending
    "Outside the temple, the orange haze begins to clear."
    "Hallownest can finally rest."
    
    show hornet at above_textbox_center
    hornet "What will you do now?"
    hornet "Your purpose is fulfilled. The kingdom is saved."
    hornet "But... I suppose even ghosts need a home."
    hornet "Welcome back, sibling."
    
    scene bg dirtmouth
    show elderbug at above_textbox_center
    elderbug "Oh my! Something's changed, hasn't it?"
    elderbug "The air feels... cleaner. Lighter."
    elderbug "Did you do something down there, little one?"
    elderbug "Well, whatever it was, thank you."
    elderbug "Perhaps Dirtmouth will become lively again someday."
    
    narrator "The infection is lifted. Hallownest is saved."
    narrator "The Knight rests, its duty complete."
    narrator "In the darkness of the Abyss, an ancient kingdom dreams of better days."
    
    "ENDING: Dream No More"
    return
    
    label godmaster_ending:
    scene bg abyss
    narrator "But there is something more..."
    narrator "Deep in the Abyss, the Void stirs."
    narrator "The siblings, countless vessels discarded, rise as one."
    
    "The Void unites. Ancient power awakens."
    "Together with your kin, you strike down the Radiance completely."
    
    narrator "Light is consumed by Void."
    narrator "The Radiance is erased from existence itself."
    
    "But the Void does not stop..."
    
    scene bg white_palace
    show white_lady at above_textbox_center
    white_lady "The Void... it has grown beyond our control..."
    white_lady "My King... what have we wrought?"
    
    narrator "The kingdom of Hallownest falls silent once more."
    narrator "Saved from one threat, but consumed by another."
    narrator "The Void is everything. The Void is nothing."
    
    "ENDING: Embrace the Void"
    return

# Additional content - The Pale King's past
label white_palace_flashback:
    scene bg white_palace
    $ play_area_music("white_palace")
    
    narrator "In the White Palace, hidden in dreams, the past echoes..."
    
    show pale_king at above_textbox_left
    show white_lady at above_textbox_right
    
    pale_king "The infection cannot be stopped by conventional means."
    pale_king "The Radiance exists in dreams, in memory. She is an idea."
    pale_king "But the Void... the Void is the absence of light. The absence of thought."
    pale_king "A vessel born of Void, trained and raised, made perfectly hollow..."
    pale_king "Such a being could contain the Radiance indefinitely."
    
    white_lady "And what of these vessels? They are our children, my King."
    
    pale_king "They are tools. Necessary sacrifices for the greater good."
    pale_king "We will create thousands if we must. Only the perfect one will be chosen."
    
    scene bg abyss
    narrator "In the Abyss, countless vessels were born."
    narrator "Most fell back into the darkness. Discarded. Failed."
    narrator "One climbed out. The Hollow Knight."
    narrator "But one thing doomed the plan from the start..."
    narrator "The King looked upon the Hollow Knight and felt pride."
    narrator "In that moment, the vessel was no longer hollow."
    narrator "An idea was planted. A bond was formed."
    narrator "The seal was flawed from the beginning."
    
    return
