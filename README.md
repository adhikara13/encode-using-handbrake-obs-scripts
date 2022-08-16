<h1 align="center">
  :clapper:OBStoHandBrake
</h1> 


<p align="center">
  <img src="https://user-images.githubusercontent.com/44716348/184879000-432f2952-0c37-4c84-96c8-304c8a257443.png" width="330" height="270" />
</p>

## :floppy_disk: Requirements
* HandBrakeCLI.exe [Link](https://handbrake.fr/downloads2.php)

## :open_book: Usage
* Load the python code by going to Tools -> Scripts and choose `obs_to_handbrake.py` code that you've downloaded from this repository.
* Load the HandBrakeCLI.exe downloaded in your computer.
* Choose folder where the recordings are saved into.
* Choose folder where you want the converted video be saved into.
* Pick preset.

## :newspaper: Decision

Why i decided to create this plugin, all was started with the fact that i was in need to use OBS for video recording and want to use the comfy of Handbrake for converting / encoding video that has been recorded. In the first time, i tried to use Handbrake GUI but then understood that it's pretty slow in my computer, so that's why i decided to find an alternative for it and found Handbrake CLI, which is for me what i needed the most.

### :bookmark_tabs: Long story short

The things is i want to make it automated using python, because i don't want to run a command everytime i need my video recording to be converted. So then i started to browse the internet and stackoverflow to find solution but didn't find one that's related to handbrake CLI. However one repo from dustractor was really interested for me because he made a script to open the folder to the file that has just been recorded in OBS. 

### :page_with_curl: Continuation 

After that i realized that this code really would be helpful for me, and i decided to fork the repo and modified it.

#### :bookmark: Modification
	
* Done
  * Added built in presets.
* Plan
  * Fix bug.

#### :lady_beetle: Bug
1) There's no default preset, need to choose from the list first in order to use.
2) Somehow can't run the script right away, have to refresh the plugin first in order it to be worked.
