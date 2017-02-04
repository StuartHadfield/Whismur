import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../lib/")
from utils import audio_reader as ar


def test_read():
    [sample_rate, data] = ar.read_audio_file("samples/around_the_world-atc.wav")
    print "it should read a sample rate"
    assert sample_rate == 22050
    print "it should read wav data"
    assert data.size == 4814784
