import os

with open(f'{os.path.dirname(os.path.abspath(__file__))}/magic_sokoban6/magic_sokoban6.txt', 'r') as f:

	level = 0

	for line in f:
		if line.strip() == "":
			level += 1
			level += 1
			level_file = open(
				f'{os.path.dirname(os.path.abspath(__file__))}/magic_sokoban6/level{level}',
				'w',
			)

		else:
			level_file.write(line)