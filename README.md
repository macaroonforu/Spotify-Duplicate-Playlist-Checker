# Spotify-Duplicate-Playlist-Checker
A python script that will compare songs in two Spotify playlists and check for duplicates. 

# Introduction 
In the spirit of decluttering for a more organized New Year, I was seeking to reorganize my playlists on Spotify. One problem I faced was that I had over time taken many songs of my favourite genre and stored them in many separate small playlists, which I sought to amalglamate into one larger cohesive playlist. Since I had over 1000 songs, I decided to have two playlists: one for my old songs before 2021, and one for my new songs discovered after 2021, but after I had compiled all of my new songs into a new "master" playlist, I had noticed that there were a lot of repeats between songs on that playlist and songs on my old playlist, which I wanted to remove, so that each playlist would contain unique songs. I wasn't sure how to tackle this problem: if each playlist had around 500 songs, was I supposed to compare each and every single one by hand? I decided to write a script that could offset this work to a computer. 

# Usage 

In order to use the Spotify Web API, I first created a [developer profile](https://developer.spotify.com/) and later, an app, on Spotify, which provides a client id and a client secret which can be found in the app's settings and are needed to make requests to the endpoint. 

![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/a4e5a07b-45fa-47b5-a367-c4fd65bf9d30)

Next, to test the script, I found two 2000's throwback playlists because I thought it would make sense for them to have shared tracks between them. 

![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/74f1a948-b322-45f3-a49c-acbd40bdbbc1)

![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/b7742427-6aeb-4fb3-a2c8-1a458f0948b8)


This is an example of how the script performs on the given playlists. 

![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/62c96e00-155d-4d33-b873-419bc05b2773)





