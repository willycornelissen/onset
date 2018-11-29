import argparse
from pydub import AudioSegment
from os import listdir
from os.path import isfile, join, splitext

parser = argparse.ArgumentParser(description='Compute the number of frames.')
parser.add_argument('folder', metavar='N', nargs='+', help='Folder with the files to be processed.')
args = parser.parse_args()
folder = args.folder[0]
files = [f for f in listdir(folder) if isfile(join(folder, f))]

one_second = AudioSegment.silent(duration=1000)
interval25 = AudioSegment.silent(duration=25)
interval50 = AudioSegment.silent(duration=50)
tick       = AudioSegment.from_wav('tick1ms.wav')

for f in files:
    wave       = AudioSegment.from_wav(folder + "/" + f)
    instrument = splitext(f)[0]

    # Generate exact onsets
    onset      = one_second + tick + wave
    onset.export(instrument + "-onset.wav", format='wav')

    # Generate onsets with a 25ms delay before
    silence = one_second + wave
    onsetbefore25 = silence.overlay(tick, position=975)
    onsetbefore25.export(instrument + "-25.wav", format='wav')

    # Generate onsets with a 25ms delay after
    silence = one_second + wave
    onsetafter25 = silence.overlay(tick, position=1025)
    onsetafter25.export(instrument + "+25.wav", format='wav')

    # Generate onsets with a 25ms delay before
    silence = one_second + wave
    onsetbefore50 = silence.overlay(tick, position=950)
    onsetbefore50.export(instrument + "-50.wav", format='wav')

    # Generate onsets with a 25ms delay after
    silence = one_second + wave
    onsetafter50 = silence.overlay(tick, position=1050)
    onsetafter50.export(instrument + "+50.wav", format='wav')





# # Generate audio starting with 1 second of silence
# onset = one_second + tick + wave
# onset.export('waves/Onset.wav', format='wav')
#
# # Generate decay start time
# silence_wave = one_second + wave
# decay = silence_wave.overlay(tick, position=1034)
# decay.export('waves/Decay.wav', format='wav')
#
# # Generate middle tick
# silence_wave = one_second + wave
# middle = silence_wave.overlay(tick, position=1017)
# middle.export('waves/Middle.wav', format='wav')
#
# # Generate pre-onset
# silence_wave = one_second + wave
# preonset = silence_wave.overlay(tick, position=990)
# preonset.export('waves/PreOnset.wav', format='wav')
#
# # Generate pos decay
# silence_wave = one_second + wave
# posonset = silence_wave.overlay(tick, position=1044)
# posonset.export('waves/PosDecay.wav', format='wav')
#
# # Put the originals with the generated ones
# wave.export('waves/'+args.fileName[0], format='wav')
# silentwave = one_second + wave
# silentwave.export('waves/Silent-' + args.fileName[0], format='wav')
