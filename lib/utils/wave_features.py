def energy(frame):
    return sum([abs(x)**2 for x in frame]) / len(frame)


class WaveFeatures(object):

    def __init__(self, rate, data):
        self.rate = rate
        self.data = data

    def calc_features(self):
        # does something
        print "calculating features"
        short_term_energy = [energy(frame) for frame in self.data]
        print short_term_energy

    def zero_crossing_rate():
        print "ZCR"

    def entropy_of_energy():
        '''https://en.wikipedia.org/wiki/Zero-crossing_rate'''
        print "entropy of energy"

    def major_spectral_centroid():
        '''https://en.wikipedia.org/wiki/Spectral_centroid'''
        print "major spectral centroid"

    def minor_spectral_centroid():
        '''https://en.wikipedia.org/wiki/Spectral_centroid'''
        print "minor spectral centroid"

    def spectral_flux():
        '''https://en.wikipedia.org/wiki/Spectral_flux'''
        print "spectral flux"

    def spectral_entropy():
        '''http://dsp.stackexchange.com/questions/23689/what-is-spectral-entropy'''
        print "spectral entropy"

    def mfcc():
        '''https://en.wikipedia.org/wiki/Mel-frequency_cepstrum'''
        print "Mel Frequency Cepstral Coefficient"

    def chroma_vector():
        '''https://en.wikipedia.org/wiki/Harmonic_pitch_class_profiles'''
        print "chroma vector"

    def bpm():
        print "bpm"
