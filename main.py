import sys
import os
from application.build import build
from application.interface import interface


def run():

	index_exists = True
	try:
		open("InvertedIndex.p", 'rb').close()
	except FileNotFoundError:
		index_exists = False


	if len(sys.argv) > 1:
		if os.path.isdir(sys.argv[1]):
			build(sys.argv[1]+'\\')
		elif os.path.isdir("analyst"):
			build()
		else:
			print("No valid directory, terminating program.")
			return -1
	else:
		if not index_exists:
			if os.path.isdir("analyst"):
				build()
			else:
				print("No valid directory, terminating program.")
				return -1
		else:
			pass

	print("Indexing complete. Ready to begin search.")

	interface()
	
	return 0

run()