# pySokoban
Sokoban is a japanese transport puzzle game originally developped by Hiroyuki Imabayashi in 1982. The name comes from Japan and means "warehouse keeper". The player pushes boxes or crates around in a warehouse, trying to get them to storage locations. This implementation is based on Python & pyGame Library.

## System Requirements
Python 2.7 & pyGame 1.9

## How to play
Use arrows keys to move player  
U   => Undo move  
R   => Reset level  
ESC => Exit game  

## Themes
To change theme change the following line of code into sokoban.py file  
```theme = "soft"```  

At this moment three themes are supported. [soft | default | ksokoban]

## Level Sets
Original game (published 1982 by Thinking Rabbit) included 20 levels. Sokoban 2 (1984) included 50 levels. Spectrum HoloByte was the first game company to bring Sokoban to gamers outside Japan with it's 1988 release called Soko-Ban. This release included 50 levels and are those levels called "original" nowdays.  
In pySokoban levels are plain text files. It uses the most commonly used format for representing a level wich is the following:  

| Level element         |  Character |
|:---------------------:|:----------:|
| Wall                  | #          |
| Player                | @          |
| Player on goal square | +          |
| Box                   | $          |
| Box on goal square    | *          |
| Goal square	        | .          |
| Floor                 | (Space)    |

## Screenshots
Default theme  
!["Screenshot of the game"](themes/default/images/screenshot.png?raw=true "Screenshot of the game")  
Soft theme  
!["Screenshot of the game"](themes/soft/images/screenshot.png?raw=true "Screenshot of the game")  
Ksokoban theme  
!["Screenshot of the game"](themes/ksokoban/images/screenshot.png?raw=true "Screenshot of the game")  

