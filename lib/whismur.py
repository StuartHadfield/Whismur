# Imports
from utils import audio_reader as ar
from utils import wave_features as wf

# from classifiers import knn


class Whismur(object):
    def __init__(self, file, classifier, trim_silence, bpm):
        self.sound_wave = file
        self.classifier = classifier
        self.trim = trim_silence
        self.bpm = bpm
        self.evaluate()

    def evaluate(self):
        [sample_rate, data_size] = ar.read_audio_file(self.sound_wave)
        new_features = wf.WaveFeatures(sample_rate, data_size)
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
