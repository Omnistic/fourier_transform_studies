import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import signal, fft

freq_hz_1 = 50
freq_hz_2 = 1000
time_s = np.linspace(0, 0.1, 100000)

waveform_1 = (signal.square(2 * np.pi * freq_hz_1 * time_s, duty=0.5)+1)/2
waveform_2 = (signal.square(2 * np.pi * freq_hz_2 * time_s, duty=0.5)+1)/2

waveform_3 = waveform_1 + waveform_2
waveform_4 = 1.0*(waveform_3 < 1.0)

fourier_transform_1 = fft.fft(waveform_1)
fourier_transform_2 = fft.fft(waveform_2)
fourier_transform_3 = fft.fft(waveform_3)
fourier_transform_4 = fft.fft(waveform_4)

fig = make_subplots(rows=4, cols=2, subplot_titles=["Waveform 1", "Fourier Transform 1", "Waveform 2", "Fourier Transform 2", "Combined Waveform", "Fourier Transform of Combined Waveform", "Clipped Combined Waveform", "Fourier Transform of Clipped Combined Waveform"])
fig.add_trace(go.Scatter(x=time_s, y=waveform_1, mode='lines', name='Waveform 1'), row=1, col=1)
fig.add_trace(go.Scatter(x=np.fft.fftfreq(len(waveform_1), d=(time_s[1] - time_s[0])), y=np.abs(fourier_transform_1), mode='lines', name='Fourier Transform 1'), row=1, col=2)
fig.add_trace(go.Scatter(x=time_s, y=waveform_2, mode='lines', name='Waveform 2'), row=2, col=1)
fig.add_trace(go.Scatter(x=np.fft.fftfreq(len(waveform_2), d=(time_s[1] - time_s[0])), y=np.abs(fourier_transform_2), mode='lines', name='Fourier Transform 2'), row=2, col=2)
fig.add_trace(go.Scatter(x=time_s, y=waveform_3, mode='lines', name='Combined Waveform'), row=3, col=1)
fig.add_trace(go.Scatter(x=np.fft.fftfreq(len(waveform_3), d=(time_s[1] - time_s[0])), y=np.abs(fourier_transform_3), mode='lines', name='Fourier Transform of Combined Waveform'), row=3, col=2)
fig.add_trace(go.Scatter(x=time_s, y=waveform_4, mode='lines', name='Clipped Combined Waveform'), row=4, col=1)
fig.add_trace(go.Scatter(x=np.fft.fftfreq(len(waveform_4), d=(time_s[1] - time_s[0])), y=np.abs(fourier_transform_4), mode='lines', name='Fourier Transform of Clipped Combined Waveform'), row=4, col=2)
fig.update_layout(title_text="Square Waveforms and Their Fourier Transforms", showlegend=False)
fig.update_xaxes(range=[10, 2000], row=1, col=2)
fig.update_xaxes(range=[10, 2000], row=2, col=2)
fig.update_xaxes(range=[10, 2000], row=3, col=2)
fig.update_xaxes(range=[10, 2000], row=4, col=2)
fig.show()