def bottle_song():
	for num in reversed(range(2,100)): 
		if num > 2:
			print(f'{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottles of beer on the wall.')
		else: 
			print(f'{num} bottles of beer on the wall, {num} bottles of beer. Take one down and pass it around, {num-1} bottle of beer on the wall. {num-1} bottle of beer on the wall, {num-1} bottle of beer.')
			
			print('Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.')

bottle_song()

# Take one down and pass it around, 1 bottle of beer on the wall.
# 1 bottle of beer on the wall, 1 bottle of beer.
# Take one down and pass it around, no more bottles of beer on the wall.
# No more bottles of beer on the wall, no more bottles of beer.
# Go to the store and buy some more, 99 bottles of beer on the wall.