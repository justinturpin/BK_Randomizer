# Contacting Me

I'm really bad at looking at social media messages, but here are different ways to try to reach me:
* Twitter: https://twitter.com/GiantJigglypuff
* YouTube: https://www.youtube.com/channel/UCipn0cYaHIAOtnEAc6NOw8g
* Twitch: https://www.twitch.tv/giantjigglypuff3
* BK Rando Server: https://discord.gg/wkbm4jTE5P

# Intro

### What Is A Randomizer?
A randomizer takes a game and randomly generates all sorts of aspects, such as what enemy spawns, the location of an item, and what order certain tasks must be accomplished. To learn what the Banjo-Kazooie Randomizer does, look at Feature Overview and Feature Details.

### Who Made The Banjo-Kazooie Randomizer?
In terms of coding the randomizer, almost all of it was coded by myself, GiantJigglypuff3. I will mention others who have contributed in the Special Thanks section. As far as hacking, I did almost nothing. I had a lot of help in terms of information and how ROM hacking works from the Banjo-Kazooie modding community (known as Banjo's Backpack). I hope the Banjo-Kazooie Randomizer serves as a small demonstration of what the Banjo-Kazooie modding community is capable of. Please go visit their discord server and try out some of their hacks (Here's an invite to the server: https://discord.gg/KSkN3yf4dt).

### Why Make The Banjo-Kazooie Randomizer?
Banjo-Kazooie is my favorite game, and I'm sure others love the game as well. When I saw both Ocarina of Time and Super Mario 64 had randomizers, I felt the need to attempt to create one for Banjo-Kazooie. It may not be as good as the other randomizers, but I'm proud of how far it has gone.

# How To Use

### Requirements
1) Emulator or Everdrive+Console
2) A v1.0 NTSC ROM File of Banjo-Kazooie
Note: I am not providing anyone the ROM file, nor does the script create the ROM file for them. It takes the user's software and creates a copy, then modifies that copy. It is up to the user to obtain a copy of the software legally.

### Setting Up
1. Go to https://github.com/CyrusKashef/BK_Randomizer/releases.
2. Locate the latest version of the Banjo-Kazooie Randomizer at the top of the screen (as of this README, the latest version is 2.0.Open_Beta).
3. Download the zip file called "BK_Randomizer". If your computer is giving you issues about the zip file being a virus, go to the "Common Problems" section of this README for a work around.
4. Extract the contents of the zip file to a folder.
5. Place your software copy of the Banjo-Kazooie v1.0 ROM file into the extracted folder.
6. Select your ROM and desired settings (descriptions below).
7. Click "Submit" and wait for the progress bar to turn completely blue (Mumbo will say when it's done). The generated seed will be in the "Randomized_ROM" folder labeled "Banjo-Kazooie_Randomized_Seed_<Seed_Number>.z64".

### Running

# Feature Overview
* Shuffle/Randomize Collectables: Challenges the player to search the levels for collectable locations.
* Shuffle Warps: Challenges the player to remember what leads where and what moves are needed for specific locations.
* Shuffle/Randomize Enemies: Allows players to face against selected enemies.
* Aesthetic Features: Changes how he game looks and sounds.
* Customizable Features: Neither competitive nor merely asthetic features with modifiable JSON files for modders to explore with.
* World Specific Features: Changes unique things about each world.
* Miscellaneous Features: None of these affect gameplay, but may prove useful.

# Feature Details

If you don't feel like reading all of this, I made a video a while back, though I need to update it:
https://www.youtube.com/watch?v=eIVAZJl08N4

### Overall Buttons
* Load Config: Reads a JSON file to configure the settings automatically. If settings are changed between versions, a warning will appear letting you know how much has changed.
* Save Config: Writes a JSON file for future use. See LOAD CONFIG.
* Open README: Opens the README.txt file (If you're reading this, bless your heart).
* Submit: Runs the randomizer with the current features, barring everything is set correctly. If not, a window should appear telling you what is incorrect/missing.

### General
* ROM File: Displays the directory path of the ROM file the user has selected.
* Select ROM Button (Folder): Click on the folder button to open a file browser and select the BK ROM file.
* Seed: Allows the player to pick a seed to match other people's randomized ROM.
* Random Seed Button (Acorn): Randomly generates a seed value.
* Generate Settings Code: Generates a string of your settings, not including seed, aesthetic changes, and misc options. PLEASE DOUBLE CHECK AND COMPARE THE SETTINGS WITH A FRIEND. Every time a feature is added or removed, this feature needs changing and mistakes happen. The other option to this is to share the JSON configuration with your friend.
* Apply Settings Code: Applies a predetermined configuration to your settings, not including seed, aesthetic changes, and misc options.
* Randomly Select Configurations: Selects a saved configuration in the "Configurations" folder and applies the settings.
* Randomly Select EVERY Setting: Randomly generates every setting.

### Collectables
##### All Items
* None: Skips the setting.
* Shuffle (World): Takes all items of that set and swaps the Object IDs within the world (can be overriden for Click Clock Wood; see World Specific Features).
* Shuffle (Game): Takes all items of that set and swaps the Object IDs within all worlds/lair. This will override the World Specific Feature for Click Clock Wood.
##### Jiggy, Empty Honeycomb, & Mumbo Token Specific
* Include Abnormalities: Some items have special properties that won't softlock the game, but create weird effects.
* Include Potential Softlocks: Some items create scenarios that may prevent the player from 100%-ing or finishing the seed.
* Door Of Grunty Only: All worlds will automatically open, and the value for the Door Of Grunty can be set on the side (from 0 to 99). A value can be chosen at random by pressing the Jiggy button.
* Base Game Costs: The costs for transformations for each world are the same as base game.
* World Order Scaled Costs: The cost for transformations are determined by the order in which the world appears. 1st -> 5, 2nd -> 10... 5th -> 25.
* Free Transformations: All Mumbo transformations won't cost you a single Mumbo Token.
* One Health Only: You will only have one health the entire game, no matter how many Empty Honeycombs you pick up. Good luck not getting hit or falling!
* Remove Floating Jiggies: Any non-spawning Jiggy gets removed from the game, limiting the number of Jiggies to 56 (the randomizer will only allow 50 jiggies to be required to allow for double health and possible softlock features).
##### Notes, Blue Eggs, Red Feathers, & Gold Feathers
* Randomize: Based on the number of notes needed to complete the game, the odds of a note appearing will be adjusted. Adds another dropdown to have the exact number of notes or have 1.1 times more than required.
* All Notes: All eggs and feathers become notes. Brentildas are replaced with egg and feather refills. The refill at that Brentilda location is random.
* Scaling Note Doors: Depending on how many notes you set the 810 Note Door Value to, the number of notes needed per proceeding door will be increased/decreased accordingly.
* Final Note Door Only: Removes all note doors proceeding the 810 Note Door, and sets the value of the 810 Note Door to the desired value. A random value can be chosen by clicking the Note button.
* Item Carrying Capacity: Sets the number of each item the player can carry before and after visiting Cheato between 0 and 255, inclusively.
* Note Door Warning: Before opening any Note Door, the player must talk to Bottles at the 50 Note door. In order to add to the Quality of Life, a bottles is added to the 810 Note Door Location for Final Note Door Only mode.
* Item Capacity Warning: I'm not sure if the game will break if you set the After Cheato value to a value smaller than the Before Cheato value. Please be weary.
* Note Limit Warning: The player can only collect 127 notes in a world while still being able to leave the game file with the game saving properly. If a player collects over 127 notes and either game overs, save and quits, or turns off the console, the note count will be the remainder of their total notes divided by 128. Save states are recommended for emulator.
##### Jinjos, 1-Ups, & Misc Objects
* Include Abnormalities: Some areas have Eggs and Feathers that aren't formatted like regular Eggs and Feathers, so they can be swapped with this category if checked.
* Starting Life Count: Can be set anywhere from 0 to "technically 255", but I'm not sure what happens if you overflow the value, so please just make it max of 100.

### Warps
##### World Order Warps
* None: Skips the setting.
* Basic Shuffle: Simplified shuffling to guarantee a solution. Mumbo's Mountain is always the first level, with the moves Talon Trot, Shock Jump Pad, and Beak Buster. All other world and moves are random.
* Bottles Shuffle: More complicated shuffle. Worlds are placed in a logical order so that the previous worlds will give the needed moves to progress the game. Logic might not work if worlds are skipped. Bottles mounds are shuffled with Jinjos, Extra Lives, and Miscellaneous Object locations to promote more exploration.
* You can select whether BK Warp pads at the start of the level send you to the entrance you entered from or the entrance the world normally has, affecting the warp logic.
* Start Game With All Moves: You start the game with all of the moves, though you won't be given Eggs and Feathers to start with.
* Note: Some jump pads and flight pads are always active. This was not a randomizer feature; these pads are always active in the base game as well.
##### Within World Warps
* None: Skips the setting
* Shuffle By World: All warps within a level are shuffled, barring some constraints. Excludes transformation warps.
* Shuffle By Game: All warps within the levels (not including Gruntilda's Lair) are shuffled, barring some constraints. Excludes transformation warps. WARNING: This feature is crash heavy.
##### Starting Area
* New Game Start Area: Starting a new game will start you here. Loading a game may start you here depending on what flags you hit, but I'm not entirely sure. Exiting Banjo's House will also take you to this location.
* Skip Intro Cutscene: Skips the cutscene when starting a new game, but not the one where the player enters the lair for the first time.
* Please watch the intro cutscene at least once. I worked hard on making custom dialog...

### Enemies
* None: Skips the setting.
* Shuffle: Shuffles the enemies by category (Ground, Flying, Wall).
* Randomize: Randomizes the enemies by category (Ground, Flying, Wall). Some enemies only appear in specific worlds.
* Select All Non-Softlock Enemies: Checks all of the non-softlock enemy boxes.
* Remove All Enemies: Unchecks all of the enemy boxes.
* Checkboxes: Select the enemies you want to appear when using the Randomize option. Must select at least 1 generic Ground, Wall, and Flying enemy each. Enemies with an asterisks may softlock/crash the game. If no enemy is checked for a category, no enemy will appear.
* Warning: A recent fix for Yum-Yums were put into the game. If your game crashes in TTC, please contact GiantJigglypuff3.

### Aesthetics

##### Banjo-Kazooie Model Color
* Dropbox: Select from presets of color combinations.
* Random Preset: Randomly sets a preset for colors.
* Random Colors: Randomly sets colors.
* Note: When setting your own colors, longer entries are made for 32-bit and shorter entries are made for 16-bit. If you're using a 16-bit color, the last value must be odd in order to be visible. You can use the following link to convert the colors: https://trolsoft.ru/en/articles/rgb565-color-picker
##### Short Sounds, Fanfare/Jingles, & Looped Music
* Shuffle Sounds: Sounds last about a second long. This includes things like Eggs, Feathers, Honeycombs, Mumbo Tokens, etc.
* Shuffle Jingles: Jingles last a few seconds. This includes the Jiggy Jig, successfully finishing a task, etc.
* Shuffle Music: Music is typically long and potentially loops. This includes level background music, mini games music, and ambient noises.
* Include Beta Sounds: Some songs not used in the final game but are present in the data are including in shuffling for all checked categories.
* Include Jarring Sounds: Some noises are painful to listen to repeatedly. Use this feature at your own risk.
##### Sprites & Textures
* Shuffle Skyboxes: Shuffles the skies and the clouds of the levels.
* Shuffle Talking Sprites: Shuffles the head sprites used in conversations.

### MAP Config

##### Models, Animations, & Properties
* Select a checkbox to swap aesthetics (A) or death properties (P). Some changes are guaranteed while some may randomly return to the base game status.
* Aesthetic changes mean model and animation swapping
* Death properties change the user interacts with the object and how that object interacts when BK makes contact. Example: What an enemy is weak to, how many honeycombs the enemy drops upon dying, what the enemy is weak to, etc.

##### How To Edit The JSON Files
* Go to the directory leading to "BK_Rando_v2.0\Randomization_Processes\Misc_Manipulation\Models_Animations_Properties\JSON_Files\".
* The JSON is broken into 3 sections: Model, Animation, Properties.
* Each section has subsections. The names of the subsections don't matter, but they must be distinct from the other subsections.
* Each subsection may have different types:
  - Original/Replacements: Each original will be randomly replaced with a replacement. For models and animations, replacements must be the same size or smaller than the original and each replacement will only be used once. For properties, any number of original/replacement files are allowed and each property can be used more than once.
  - Swap: Swap1 will swap into Swap2, Swap2=>Swap3... Last Swap#=>Swap1.
  - Shuffle: All items in the subcategory will be shuffled within each other.
* For more address values, check out Hack64.net under ROM Map.

### World Specific

##### Gruntilda's Lair
* Skip Furnace: Going past the 765 Note Door will skip the Furnace Fun pad area and lead straight to the 810 Note Door room. Also changes Brentilda's text to potentially give useful hints.
* No Detransformations: Removes all transformation barriers in the lair. Warning: Some areas may softlock the transformations.
* Final Battle Difficulty: On a scale of 1 to 3, it adds effects to the grunty fight. Zero turns off the feature.
* Monster House: Replaces some items with enemies. Each level adds a layer of enemies.
* What Floor?: Removes collision with the floor. Shock Jump Pads are placed on the field to help move around, and the pillars will still have collision. Each level removes Shock Jump Pads.
* Mini Me: Gruntilda shrinks in size, making her harder to hit. Each level makes her smaller.

##### Mumbo's Mountain
* Include Flowers: If the notes/eggs/feathers feature is not set to 'none', the flowers in the level will be included in shuffling.

##### Treasure Trove Cove
* Scattered Notes/Eggs/Feathers: Notes, eggs, and feathers are scattered across the level, both in the water and in the air, based on the location they would normally appear. (I think as of releasing this, sometimes notes and feathers don't get shuffled, but that's a problem for future me).
* Super Slippery Sand: At some point, you'll trigger the anti-tampering and you won't be able to change direction unless you jump. Have fun!

##### Clanker's Cavern
* Shuffle Clanker Ring Order: Clanker's ring order is shuffled.

##### Bubblegloop Swamp
* Shuffle Croctus Order: Croctus spawn order is shuffled.
* Mr. Vile Bigger, Badder Crocodile: Makes Mr. Vile appear larger. He still moves at the same speed and eats at the same distance, but it's harder to see where the Yumblies and Grumblies spawn.
* Tiptup Choir: The turtles are scattered across the room, with their heads barely appearing above the floor. One may be off-screen; this is intentional.

##### Freezeezy Peak
* Boggy Races Moved Flags: Flag poles for the Boggy race are either tighter left, tighter right, lowered to the floor to make harder to see, or rotated.

##### Gobi's Valley
* Shuffle Ancient Ones Order: Ancient Ones order is shuffled.
* Shuffle Maze Jinxy Heads Order: Jinxy heads to raise King Sandybutt's Tomb order is shuffled.
* Randomize Matching Puzzle: The matching puzzle changes the colors of the tiles that the player has to match, rather than the icons themselves.

##### Mad Monster Mansion
* Pots Are Lit: The flower pots located in the graveyard switch places with the fire pain objects, which are shown with sparkles and steam. Look at torches and other fire places for sparkles. If you don't see it, shoot/poop an egg in.
* Randomize Motzand's Song: Randomly selects new keys to press. Follow Motzand to find the pattern.

##### Rusty Bucket Bay
* Randomized Button Combo: Generates a random 6-digit combination of 1s, 2s, and 3s for the whistle buttons and places the code over the original code spot.

##### Click Clock Wood
* By Season: All shuffling happens within each seasons/lobby area. This makes it easier for players to track what they are missing.
* Within World: All shuffling happens throughout the level.

### Miscellaneous
* Create Cheat Sheet(s): Writes helpful into to files that gives hints item locations, warps, and some misc info.
* Remove Extra Files: Removes the compressed and decompressed files extrated from the ROM. Useful for BK modders or debugging an issue.
* Show Tool Tips: With the feature on, hovering over a Brentilda icon will inform the user what the feature does.

# Premade Configurations

The configurations will have a value at the front to display approximate difficulty.

### 01 Basic Settings
Shuffles all items within each world and randomizes enemies. Includes minor aesthetic changes. Very easy mode to get your feet wet.

### 02 Basic World Shuffle
World order shuffle that's beginner friendly. Only required to obtain 35 Jiggies and 400 Notes, with all worlds and note doors being opened with the exception of the final ones.

### 03 Meme Percent
420 Notes, 69 Jiggies. Open worlds and removed note doors. Just have fun ^_^

### 03 One Floating Note
There are 5 notes in Mumbo's Mountain's huts, 5 notes in Bubblegloop Swamp's huts, and 1 note floating somewhere in the game. Good luck finding it!
(If you're having trouble, talk to Brentilda).

### 04 World Order Shuffle (Advanced)
World order shuffle made for more veteran players. You'll need the base game number of Jiggies and Notes while still having to deal with random world order.

### 04 No Floating Jiggies
The only Jiggies available are the ones that are spawned. All of the world specific settings are also on, so they will be tougher to obtain.

### 04 Only Hard Grunty Fight
This warps you to the end of the game with all of the moves. Gruntilda's altered final battles will be at their hardest. Good luck!

### 06 One Health Mode
I skipped 5 because this is extremely hard. Can you collect everything in the game with just one health and a bunch of other settings? Kudos if you do.

### Nothing/Everything
Just made to have a clean slate or check everything for developer purposes. Don't overthink this. REALLY don't recommend "Everything".

# Common Problems

### Computer Says Randomizer Is A Virus
If you go to virustotal.com and upload the BK Randomizer, it will tell you that about 10% (this value changes) of Anti-Virus softwares will claim this is a virus. This is a common issue when using pyinstaller to turn the python code into an exectuable file. I will have my code in a GitHub repository if anyone would like to check to see that the BK Randomizer is not doing anything malicious. If you trust me that the randomizer is not a virus, there is a work around to the Windows Defender Anti-Virus, demonstrated in the following YouTube video: https://www.youtube.com/watch?v=_5gbWPEcHZs

### GUI Errors/Warnings
* ROM file must be a Banjo-Kazooie ROM v1.0 NTSC (.z64). Other formats are currently not supported. Randomizer WILL NOT work on top of other BK mods.
* All numbers must be positive integers, including seeds.
* Python Files, Folders, and GZIP.EXE must be in their original locations with the BK ROM in the main folder.
* **While the processes are running, if Mumbo says there is an error, take a screenshot of the error, generate the randomizer setting code, and send the screenshot, the randomizer setting code, and the seed to GiantJigglypuff3. Link to the BK Rando Discord server at the top**
* If you're not able to generate the randomizer settings code, go to Configurations, open the "Last_Used_Configuration" json file, remove your ROM File directory parameter, and send that to GiantJigglypuff3 as well. Example: "ROM_File": "C:/Users/Name/eclipse-workspace/BK_Rando_v2.0/Banjo-Kazooie.z64" -> "ROM_File": ""
* If the progression bar gets stuck at the very beginning, make sure there are no special or accented characters in your directory, such as "�".

### Potential Softlocks
* When turning on the 'Potential Softlock' features, the game may be put into a state where a collectable cannot be reached or the game cannot be progressed without resetting.
* If performing RBA (Reverse Bee Adventure, where you avoid the detransformation areas to roam the rest of the game as the bee), the bee can get stuck in a lot of places.
* For "Bottles Warps", the logic was created under the assumption of world shuffle, not game shuffle or 1-HP only.
* In general, the more features that are turned on, the less likely the seed will be completeable. A lot of thought was put into the logic for the game, but some things do slip by.

### Known Bugs/Crashes
* There's a possible chance the game will crash due to the lack of cameras in a room with a move that's not normally there. The work around is to start the dialog, end the dialog using L+R+B, then reactivate the dialog to read what the move does.
* In specific areas, such as Treasure Trove Cove and Furnace Fun, the game may crash. The reason is unknown, and there are currently no work arounds. This shouldn't prevent the player from restarting the console and replaying the level. If it does, please contact me.
* In Mad Monster Mansion, Napper may be indefinetly awake and guarding a Jiggy. The reason is unknown, but should only occur with potential softlocks checked on.
* In Click Clock Wood, there is an occasional glitch where the player can collect 11/10 Jiggies when items are only shuffled within the world. The reason is unknown, but may only occur with abnormal or potential softlock Jiggies/Tokens/Honeycombs.
* Randomizing the warps within worlds by game may result in warps that crash the game.
* Some of the Model/Animation/Properties features may crash the credits.

# FAQ

### Where Could I Find A Banjo-Kazooie v1.0 NTSC ROM File?
I am not providing anyone the ROM file for Banjo-Kazooie, nor does the script create the ROM file for them. It takes the users software and creates a copy, then modifies that copy. It is up to the user to obtain a copy of the software legally.

### Could ___ Feature Be Added?
If you have any suggestions for new features, feel free to let me know. I honestly didn't think people would care about shuffling music, but that turned out to be a really funny feature. If you don't like a feature, don't use it, but if you have an idea of how it can be changed, let me know. Even if your feedback is "This part of the game is too easy", I could try to figure out some way to make it harder.
Not-Planned Features:
* Non-Collectable Objects, such as trees, crates, etc
* Bosses, such as Conga, Nipper, etc

### My Game Crashed, What Do I Do?
1) Write down the circumstances before the crash.
2) Try to replicate the crash.
3) If you're able to replicated it, check the settings for any "softlock" features you may have turned on. If any are enabled, maybe try with them disabled.
4) If no softlock features were enabled, generate the settings code. Send the settings code and seed to GiantJigglypuff3. 

# Special Thanks
* The RARE staff, for making such an impactful game. Big shoutouts to Grant Kirkhope for an amazing soundtrack and being an amazing person in general.
* The Developers Of Banjo-Kazooie Modding/Viewing Tools, such as Banjo's Backpack, GEDecompressor, CRC Tool, and BK2BT. Also thank you to anyone who posted information on Hack64. I cannot name everyone by name, but your work is very appreciated and on behalf of the Banjo-Kazooie modding community, we cannot thank you enough. Discord link is listed in Contributing.
* People Who Played The Randomizer, whether it was playtesting, casually experiencing, or racing others. All feedback was taken seriously. All features that could reasonable be added were attempted at the very least. All issues brought up were either fixed or a work around was needed. Big shoutout to g0go, BlackDragonMax, HatWearingGamer, Wizzard, and Brittanykins for beta testing and feedback.
* Wizzard for providing the general basis for the Within World Warps code logic.
* Trynan for providing a more adaptable GUI interface.
* Mittenz for providing the checksum calculating code in C/C++, which was translated to Python for this project.
* Wedarobi for patching the Yum-Yum crash and providing a solution to some checksum calculations.
* Banjo's Backpack Discord, for everything ranging from technical support to emotional support. Big shoutouts to Jombo for most of the technical support. Other shoutouts go to BanjoFreak64, ThatCowGuy, PaleKing, Atezian, TheSourOG, Bynine, RetroNuva, and SapChap99.
* OoT And SM64 Randomizers, for inspiring me to find the Banjo's Backpack discord.

# Contributing
* If you'd like to take the source code to use for your own purposes, feel free. If you plan on making your own randomizer from the one I've made, consider the next bullet point or at least giving me credit somewhere.
* I currently wrote this code in Python, which is simple to pick up if anyone would like to learn. If you'd like to continue working on the Python version or need help creating a randomizer in a different coding language or something, I'll try to provide comments and answer questions as to what I personally did to randomize the ROM. Keep in mind that I'm learning how to randomize Banjo-Kazooie as I go, and might not have all of the answers to your questions.
* There's a community dedicated to Banjo-Kazooie modding called "Banjo's Backpack". There's a lot of smart people there, though most of us are still trying to learn as we go. Here is an invite: https://discord.gg/KSkN3yf4dt

If you read all of this, bless your heart.
