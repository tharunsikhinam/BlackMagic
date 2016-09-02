# BlackMagic
Music Application
# Musicapp
my music application
To run it in Dev mode
# Music Folder

 all songs are stored in /web/dist/public/ 
 
 under file1  and file2
 
 file1 can store songs with .m4a extension
 
 and file2 can store songs with .mp3 extension
 
 
 there are preloaded list of songs, do not pull them *(add ur own list of songs from local repo)
#Web server 

Runs on Node.js, required npm and node installed ..
 
>cd web

>npm install

>npm start

to run it in prod

>cd deployment/env

>sh run.sh stage/production stage (single time)

>sh run.sh stage/production web (every new feature)

#Helper Scripts

written in python 

in MusicAppscripts to load fresh songs every day into ur MusicFolders
