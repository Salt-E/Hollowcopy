# Audio System for Hollow Knight Visual Novel
# Using the actual Hollow Knight soundtrack files

# Music track definitions
define audio.enter_hallownest = "audio/01. Enter Hallownest.mp3"
define audio.dirtmouth = "audio/02. Dirtmouth.mp3"
define audio.crossroads = "audio/03. Crossroads.mp3"
define audio.greenpath = "audio/05. Greenpath.mp3"
define audio.hornet_battle = "audio/06. Hornet.mp3"
define audio.city_of_tears = "audio/09. City of Tears.mp3"
define audio.fungal_wastes = "audio/12. Fungal Wastes.mp3"
define audio.resting_grounds = "audio/15. Resting Grounds.mp3"
define audio.nosk = "audio/20. Nosk.mp3"
define audio.white_palace = "audio/23. White Palace.mp3"
define audio.sealed_vessel = "audio/24. Sealed Vessel.mp3"
define audio.radiance = "audio/25. Radiance.mp3"

# Audio management functions
init python:
    def play_area_music(area):
        """Play appropriate music for each area"""
        music_map = {
            "dirtmouth": "audio/02. Dirtmouth.mp3",
            "crossroads": "audio/03. Crossroads.mp3", 
            "greenpath": "audio/05. Greenpath.mp3",
            "crystal_peak": "audio/03. Crossroads.mp3",  # Using Crossroads music for Crystal Peak
            "fungal": "audio/12. Fungal Wastes.mp3",
            "city": "audio/09. City of Tears.mp3",
            "nosk": "audio/20. Nosk.mp3",
            "resting_grounds": "audio/15. Resting Grounds.mp3",
            "white_palace": "audio/23. White Palace.mp3",
            "temple": "audio/01. Enter Hallownest.mp3"
        }
        
        if area in music_map:
            renpy.music.play(music_map[area], channel="music", fadein=2.0, loop=True)
    
    def play_battle_music(boss_name):
        """Play boss battle music"""
        battle_music = {
            "hornet": "audio/06. Hornet.mp3",
            "hollow_knight": "audio/24. Sealed Vessel.mp3", 
            "radiance": "audio/25. Radiance.mp3"
        }
        
        if boss_name in battle_music:
            renpy.music.play(battle_music[boss_name], channel="music", fadein=1.0, loop=True)
    
    def play_opening_music():
        """Play opening theme"""
        renpy.music.play("audio/01. Enter Hallownest.mp3", channel="music", fadein=3.0, loop=True)
    
    def stop_music():
        """Stop music"""
        renpy.music.stop(channel="music", fadeout=1.0)