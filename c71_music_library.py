from c70 import albums 

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input("Enter an album: "))
    if 1 <= choice <= len(albums):
        song_list = albums[choice - 1][SONG_LIST_INDEX]
        print(song_list)
    else:
        break

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(song_list):
        print(f"{index + 1}: {song}")

    song_choice = int(input("Enter a song: "))
    if 1 <= song_choice <= len(song_list):
        title = song_list[song_choice - 1][SONG_TITLE_INDEX]
        print(f"Playing {title}")
        
    print("=" * 40)