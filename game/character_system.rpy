# Character System Enhancement for Hollow Knight Visual Novel

# Advanced character definitions with personality tracking
default knight_personality = "neutral"
default combat_style = "balanced" 
default hornet_relationship = 0
default quirrel_relationship = 0
default myla_relationship = 0

# Inventory system
default inventory_simple_key = False
default inventory_dream_nail = False
default inventory_mantis_claw = False
default inventory_monarch_wings = False
default inventory_void_heart = False

# Story progression flags
default dreamers_defeated = 0
default myla_warned = False
default heard_crystal_voices = False
default hornet_battle_style = "neutral"
default pale_ore_collected = 0

# Character relationship system
init python:
    class Character_Relationship:
        def __init__(self, name):
            self.name = name
            self.trust = 0
            self.respect = 0
            self.affection = 0
            self.fear = 0
        
        def modify_relationship(self, trust=0, respect=0, affection=0, fear=0):
            self.trust = max(-100, min(100, self.trust + trust))
            self.respect = max(-100, min(100, self.respect + respect))
            self.affection = max(-100, min(100, self.affection + affection))
            self.fear = max(-100, min(100, self.fear + fear))
        
        def get_relationship_status(self):
            total = self.trust + self.respect + self.affection - self.fear
            if total >= 75:
                return "devoted"
            elif total >= 50:
                return "close"
            elif total >= 25:
                return "friendly"
            elif total >= 0:
                return "neutral"
            elif total >= -25:
                return "wary"
            elif total >= -50:
                return "hostile"
            else:
                return "enemy"

# Initialize character relationships
default hornet_rel = Character_Relationship("Hornet")
default quirrel_rel = Character_Relationship("Quirrel")
default elderbug_rel = Character_Relationship("Elderbug")

# Character callback for relationship-based dialogue variations
init python:
    def character_callback(event, interact=True, **kwargs):
        if not interact:
            return
        
        # Get the current character
        char_name = kwargs.get('who', '')
        
        # Simple callback without sound effects
        return

# Character appearance system
image side knight = "characters/knight_side.png"
image side hornet = "characters/hornet_side.png"
image side elderbug = "characters/elderbug_side.png"
image side quirrel = "characters/quirrel_side.png"

# Advanced character definitions with relationship-based dialogue
define knight = Character("The Knight", color="#ffffff")
define hornet = Character("Hornet", color="#ff0000", 
    callback=character_callback)
define elderbug = Character("Elderbug", color="#8b7355",
    callback=character_callback)
define quirrel = Character("Quirrel", color="#4169e1",
    callback=character_callback)

# Advanced choice system with consequences
init python:
    def make_choice_with_consequences(choice_text, consequences):
        """
        Make a choice that affects character relationships and story flags
        consequences: dict with keys like 'hornet_trust', 'story_flag', etc.
        """
        for key, value in consequences.items():
            if key == 'hornet_trust':
                hornet_rel.modify_relationship(trust=value)
            elif key == 'hornet_respect':
                hornet_rel.modify_relationship(respect=value)
            elif key == 'quirrel_affection':
                quirrel_rel.modify_relationship(affection=value)
            elif key.startswith('set_'):
                flag_name = key[4:]  # Remove 'set_' prefix
                setattr(store, flag_name, value)
            elif key.startswith('add_'):
                flag_name = key[4:]  # Remove 'add_' prefix
                current_value = getattr(store, flag_name, 0)
                setattr(store, flag_name, current_value + value)

# Dialogue variations based on relationships
init python:
    def get_hornet_greeting():
        relationship = hornet_rel.get_relationship_status()
        if relationship == "enemy":
            return "You again... I should have finished you when I had the chance."
        elif relationship == "hostile":
            return "What do you want now?"
        elif relationship == "wary":
            return "...Little ghost."
        elif relationship == "neutral":
            return "So, we meet again."
        elif relationship == "friendly":
            return "Hello, little ghost. You've proven yourself capable."
        elif relationship == "close":
            return "My sibling... it's good to see you again."
        else:  # devoted
            return "Little ghost... I'm glad you're safe."

# Combat system with different approaches
init python:
    def resolve_combat(enemy, approach):
        """
        Resolve combat encounters based on player's chosen approach
        """
        if approach == "aggressive":
            # Quick victory but potential relationship damage
            result = "victory_brutal"
            if enemy == "hornet":
                hornet_rel.modify_relationship(fear=10, respect=5)
        elif approach == "defensive":
            # Slower victory but shows wisdom
            result = "victory_careful"
            if enemy == "hornet":
                hornet_rel.modify_relationship(respect=10)
        elif approach == "tactical":
            # Balanced approach, best outcomes
            result = "victory_skillful"
            if enemy == "hornet":
                hornet_rel.modify_relationship(respect=15, trust=5)
        
        return result

# Story branching based on player choices and relationships
label check_hornet_relationship:
    $ relationship = hornet_rel.get_relationship_status()
    
    if relationship in ["close", "devoted"]:
        jump hornet_ally_path
    elif relationship in ["hostile", "enemy"]:
        jump hornet_enemy_path
    else:
        jump hornet_neutral_path
    
    return

label hornet_ally_path:
    show hornet at center
    hornet "Little ghost... you've become more than I ever expected."
    hornet "Perhaps together we can save what remains of this kingdom."
    return

label hornet_enemy_path:
    show hornet at center
    hornet "I won't let you destroy what I've sworn to protect!"
    hornet "If you won't stop willingly, I'll stop you myself!"
    return

label hornet_neutral_path:
    show hornet at center
    hornet "You've proven yourself capable, but I still don't fully trust you."
    hornet "Show me that you truly care about this kingdom's fate."
    return