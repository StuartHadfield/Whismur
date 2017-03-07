# Imports
from utils import audio_reader as ar
from utils import wave_features as wf

# from classifiers import knn


def chunk_data(data, samples_per_frame):
    for i in range(0, len(data), samples_per_frame):
        yield data[i:i + samples_per_frame]


class Whismur(object):
    def __init__(self, file, classifier, trim_silence, bpm):
        self.sound_wave = file
        self.classifier = classifier
        self.trim = trim_silence
        self.bpm = bpm
        self.evaluate()

    def evaluate(self):
        frameSizeInMs = 0.01
        frequency = 44100  # Frequency of the input data
        numSamplesPerFrame = int(frequency * frameSizeInMs)

        [sample_rate, data] = ar.read_audio_file(self.sound_wave)

        # import ipdb; ipdb.set_trace()
        chunkedData = list(chunk_data(list(data), numSamplesPerFrame))

        new_features = wf.WaveFeatures(sample_rate, chunkedData)

        new_features.calc_features()

    def classify(sound_wave):
        # knn.classify(sound_wave)
        print "does nothing"
        # call some classifier function from a selection, defined in classfiers/

    def bpm(sound_wave):
        # call some filtering function from filters/
        print "does nothing"

    def visualise(classification):
        # probs call in classifier
        # call some visualisation technique from visualizers/
        print "does nothing"
