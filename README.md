<div  align=center>
	<h1>Determine shared songs between two Spotify playlists</h1>
	<br>
   <img src = "https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/0fac243e-58bd-486f-827c-7905c40c564f" height="40px" width="40px">
   <img src = "https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/9f32097b-f8bb-46ff-9397-9e1bde9c632e" height="40px" width="40px">
		<br>
</div>

# Introduction 
In the spirit of decluttering for a more organized New Year, I was seeking to reorganize my playlists on Spotify. One problem I faced was that I had over time taken many songs of my favourite genre and stored them in many separate small, random playlists, which I sought to amalgamate into one larger cohesive playlist. 

Since I had over 1000 songs, I decided to have two playlists: one for my old songs before 2021, and one for my new songs discovered after 2021, but after I had compiled all of my newer songs into a "master" playlist, I had noticed that there were a lot of repeats between songs on that playlist and songs on my old playlist, which I wanted to remove, so that each playlist would contain unique songs. 

I wasn't looking forward to solving this problem: if each playlist had around 500 songs, was I supposed to compare each and every one by hand? I realized having a script take care of this would result in much more happiness. 

# Usage 

In order to use the Spotify Web API, I first created a [developer profile](https://developer.spotify.com/) and later, an app, on Spotify, which provides a Client ID and a Client Secret which can be found in the app's settings and are needed to make requests to the endpoint. 

![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/a4e5a07b-45fa-47b5-a367-c4fd65bf9d30)

Next, to test the script, I found two 2000's throwback playlists because I thought it would make sense for them to have shared tracks. 

![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/74f1a948-b322-45f3-a49c-acbd40bdbbc1)
![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/b7742427-6aeb-4fb3-a2c8-1a458f0948b8)


This is how the script performed on the given playlists. 

![294568934-62c96e00-155d-4d33-b873-419bc05b2773](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/eaa99870-0dc9-446a-8c79-56d1ec6e8e57)

As another example, these two playlists did not have common tracks. 

![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/e5ac1e72-4a61-473b-95c6-418dc9f6c5d6)


# Explanation 
The script will first ask for a user's client id and secret and obtain an access token. Then, it will obtain the IDs of the two playlists which are to be compared. For each playlist, the name and number of tracks will be obtained via an HTTP GET request using the Python requests library and the previously obtained access token. A maximum of 50 playlist tracks will be returned for each request, so multiple requests are needed to access all songs. A for-loop is used to call a helper function that will offset into the playlist further and further until all tracks are obtained. After all the names of each playlist's tracks have been obtained in two sets, the duplicates are simply the songs contained in their intersection. 

# Conclusion 
My personal two playlists that inspired me to write this script had 102 shared songs, which would have probably taken over 2 hours to remove by hand. Although I spent over two hours working on this script, it was a great oppurtunity to learn more about Python libraries and working with APIs, that I am very happy to have come accross. 

![image](https://github.com/macaroonforu/Spotify-Duplicate-Playlist-Checker/assets/121368271/94238f1c-f4fa-42b1-8c13-c9528309cd80)

I have blurred out my Client ID, and Client Secret, as the [Spotify Developer Terms](https://developer.spotify.com/terms#section-vi-access-usage-and-quotas) state that security codes should not be shared, but I can provide assistance with obtaining them to anyone who would need it. 


# Credits 
[This article](https://alpargur.medium.com/scrape-spotifys-api-in-within-20-mins-611885897851) and the code snippets it contained helped me get started.
