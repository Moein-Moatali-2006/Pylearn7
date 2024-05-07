import pysynth as ps

test = (('c', 4), ('e', 4), ('g', 4),
		('c5', -2), ('e6', 8), ('d#6', 2))

ps.make_wav(test, fn = "test.wav")