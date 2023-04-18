<h1 align="center">
  :clapper:OBStoHandBrake
</h1> 


<p align="center">
  <img src="https://user-images.githubusercontent.com/44716348/184879000-432f2952-0c37-4c84-96c8-304c8a257443.png" width="330" height="270" />
</p>

## :floppy_disk: Requirements
* To use this plugin, you will need to have the HandBrakeCLI.exe file downloaded onto your computer. You can find the download link for this file in the resources section below. HandBrakeCLI.exe [Link](https://handbrake.fr/downloads2.php)


## :open_book: Usage
To use the OBStoHandBrake plugin, follow these steps:
* Load the Python code by going to Tools -> Scripts and selecting the obs_to_handbrake.py file that you downloaded from this repository.
* Load the HandBrakeCLI.exe file that you downloaded onto your computer.
* Choose the folder where your video recordings are saved.
* Choose the folder where you want the converted video to be saved.
* Pick a preset from the list.

## :newspaper: The Decision

I decided to create this plugin because I needed a way to use OBS for video recording and then easily convert those recordings using HandBrake. Initially, I tried using HandBrake's GUI, but found it to be too slow on my computer. That's when I discovered HandBrake CLI, which was exactly what I needed.

## :bookmark_tabs: Long story short

I wanted to automate the process of converting my video recordings, so I started looking for a solution online. While browsing through GitHub, I stumbled upon a repository by dustractor that contained a script to open the folder where a just-recorded OBS file was saved. I realized that this code could be really helpful to me, so I decided to fork the repository and modify it to include built-in presets.

## :page_with_curl: Continuation 

I have already added the built-in presets, but there is still a bug that needs to be fixed. Currently, there is no default preset, so you have to choose one from the list before you can use the plugin. Additionally, the script sometimes doesn't run properly and needs to be refreshed before it will work.

#### :bookmark: Modification
	
* Done
  * Added built in presets.
* Plan
  * Fix bug.

#### :lady_beetle: Bug
There is currently no default preset, so you must choose one from the list before using the plugin. Additionally, sometimes the script doesn't run properly and needs to be refreshed. I plan to fix these issues in the near future.
