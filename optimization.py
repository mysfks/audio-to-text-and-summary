import librosa
import numpy as np
from scipy.signal import butter, lfilter, freqz
import soundfile as sf

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

audio_file = 'audios/haber.mp3'
y, sr = librosa.load(audio_file, sr=None)

lowcut = 300.0  # Düşük frekans sınırı
highcut = 3000.0  # Yüksek frekans sınırı
filtered_audio = bandpass_filter(y, lowcut, highcut, sr, order=6)

output_file = 'optimization/filtered_haber.mp3'
sf.write(output_file, filtered_audio, sr)


"""Açıklama:
butter_bandpass: Band geçiş filtresi için Butterworth filtresi parametrelerini oluşturur.
bandpass_filter: Belirli bir frekans aralığını izole etmek için ses sinyaline band geçiş filtresi uygular.
lowcut ve highcut: Bu frekanslar arasındaki sesleri geçirir, diğerlerini zayıflatır."""