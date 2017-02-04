import os
import scipy.io.wavfile as wavfile


def read_audio_file(path_to_file):
    file_ext = os.path.splitext(path_to_file)[1]

    if file_ext.lower() == '.wav':
        return wavfile.read(path_to_file)
    else:
        print "Error reading file - wrong format!"
