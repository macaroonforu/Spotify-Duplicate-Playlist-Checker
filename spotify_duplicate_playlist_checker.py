import requests
import json 
import sys 
import math 

#Obtain access token to make requests 
def get_access_token(client_id, client_secret): 
    url = f'https://accounts.spotify.com/api/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
    response = requests.post(url, headers={'Content-Type':'application/x-www-form-urlencoded'})
    access_token = 'Bearer ' + json.loads(response.text)['access_token']
    return access_token 

#Get the name and number of tracks in a given playlist
def get_playlist_tracks (access_token, playlist_id='3cEYpjA9oz9GiPac4AsH4n'): 
    name_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    name_response = requests.get(name_url, headers={'Authorization': access_token})
    name = json.loads(name_response.text)["name"]

    num_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=total%2C'
    num_response = requests.get(num_url, headers={'Authorization': access_token})
    num_tracks = json.loads(num_response.text)

    num_requests = math.ceil(num_tracks["total"]/50) 
    total_tracks = [] 
    for i in range(0, num_requests): 
        total_tracks.extend(get_page_tracks(access_token, playlist_id, i))

    return name, set(total_tracks) 

#Helper function for above
def get_page_tracks(access_token, playlist_id, page_number): 
    offset= page_number*50 
    track_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items%28track%28name%29%29&offset={offset}'
    track_response = requests.get(track_url, headers={'Authorization': access_token})
    track_dict = json.loads(track_response.text)
    tracks = [] 
    for song in track_dict["items"]: 
        tracks.append(song["track"]["name"]) 
    return tracks 

def main(): 
    client_id, client_secret =  input("\x1B[3m" + "Welcome to the duplicate checker! Please enter your client id and client secret in order to use the Spotify Web API: " + "\x1B[0m").split() 
    access_token = get_access_token(client_id, client_secret)
    playlist1_id, playlist2_id = input("\x1B[3m" + "Thank you for providing this information. Now, please enter the two ids of the playlists you would like to compare: " + "\x1B[0m").split() 
    playlist1_name, playlist1_tracks = get_playlist_tracks(access_token, playlist1_id)
    playlist2_name, playlist2_tracks = get_playlist_tracks(access_token, playlist2_id)
    dups = playlist1_tracks.intersection(playlist2_tracks)
    if dups: 
        print('\n' + f"{playlist1_name} and {playlist2_name} had {len(dups)} shared tracks. Here they are: ")
        for item in dups: 
            print('\x1b[6;30;41m' + item + '\x1b[0m')
    else: 
        print('\n' + '\x1b[6;30;42m' + f'There were no duplicate tracks between {playlist1_name} and {playlist2_name}.' + '\x1b[0m')

main() 

