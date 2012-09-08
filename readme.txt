GAMETAPE
A launcher for "videogame mixtapes"
by @nihilocrat
===============

PLAYERS:
Run gametape.exe, choose your game, and play! Remember to FLIP the cassette to see Side B!


GAMETAPE MAKERS:

Put your games in the "Games" subdirectory.

Modify "games.txt" to change the games listed on the cassette. The configuration sections are marked "sideA" and "sideB". The text to the left of the colon (:) is the name as it appears on the cassette. The text to the right is the path to the game's executable.

You can customize graphics by modifying "sideA.jpg" and "sideB.jpg".


KNOWN BUGs / ISSUES:
I threw this app together in an afternoon, so my apologies.

- "games.txt" is a JSON file. Look up the syntax on the internet if you run into issues. I will make a simpler format (like an .ini) later.
- For now, you need to use .jpgs for the tape graphics, and they need to be the same size as the current ones
- There's a border on the window and no support for transparency. I couldn't get this working correctly in time.
- Gametape will hang when you run a game. Don't worry, it will respond again when you are finished with the game.