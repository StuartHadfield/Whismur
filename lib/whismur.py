# Imports

# from classifiers import knn


class Whismur(object):
    def __init__(self, file, classifier, trim_silence, bpm):
        self.sound_wave = file
        self.classifier = classifier
        self.trim = trim_silence
        self.bpm = bpm
        print "done setting shit"
        self.evaluate()

    def evaluate(self):
        print "evaluating!"

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
