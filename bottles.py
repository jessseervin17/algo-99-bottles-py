def bottle_song(beer_count, lyrics): #function to verify beer is within reasonable range
    if beer_count>99:
        return "The wall doesn't have that much room..."
    elif beer_count <0:
        return "C'mon, we need to have a little fun!"
    else:
        def generate_bottle_lyrics(beer_count, lyrics): #function to generate song lyrics
            if beer_count>1:
                new_lyrics = lyrics + f"Take one down and pass it around, {beer_count} bottles of beer on the wall. \n{beer_count} bottles of beer on the wall, {beer_count} bottles of beer.\n"
                beer_number = beer_count - 1
                generate_bottle_lyrics(beer_number, new_lyrics)
            elif beer_count == 1:
                new_lyrics = lyrics + f"Take one down and pass it around, {beer_count} bottle of beer on the wall. \n{beer_count} bottle of beer on the wall, {beer_count} bottle of beer.\n"
                beer_number = beer_count - 1
                generate_bottle_lyrics(beer_number, new_lyrics)
            else:
                new_lyrics = lyrics + "Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
                return new_lyrics
        song_lyrics = lyrics
        beer_number = beer_count
        return generate_bottle_lyrics(beer_number, song_lyrics)
        

car_to_do = bottle_song(3, "")
print(car_to_do(3, ""))

