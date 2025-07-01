liked_songs = {
    'FAMOUS' : 'All Day Project',
    'Lemon Drop' : 'ATEEZ',
    'Manchild' : 'Sabrina Carpenter',
    'Gameboy' : 'KATSEYE'
}

#Function to to display and write liked songs in a file
def write_liked_songs_to_file(songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked Songs:\n')
        for song, artist in songs.items():
            file.write(f' {song} by {artist}\n')

# Write liked songs to a .txt file
write_liked_songs_to_file(liked_songs, "liked_songs.txt")
