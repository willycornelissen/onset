import argparse
import librosa
import numpy

parser = argparse.ArgumentParser(description='Trim Audio files.')
parser.add_argument('fileName', metavar='N', nargs='+', help='Audio file name.')
args = parser.parse_args()

x, sr = librosa.load(args.fileName[0])
xt = numpy.asarray(librosa.effects.trim(x,15))[0]
librosa.output.write_wav('trimmed.wav', xt, sr)
