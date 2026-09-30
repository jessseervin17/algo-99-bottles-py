
def bottle_song(beer_count):
    lyrics = ""
    while beer_count>=0:
        if beer_count>1:
            lyrics += f"Take one down and pass it around, {beer_count} bottles of beer on the wall. \n{beer_count} bottles of beer on the wall, {beer_count} bottles of beer on the wall.\n"
            beer_count -= 1
        elif beer_count == 1:
            lyrics += f"Take one down and pass it around, {beer_count} bottle of beer on the wall. \n{beer_count} bottle of beer on the wall, {beer_count} bottle of beer on the wall.\n"
            beer_count -= 1
        else:
            lyrics += f"Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
            beer_count-=1
    return lyrics


print(bottle_song(0))


