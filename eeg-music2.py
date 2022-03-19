import time
import brainflow
import numpy as np
from midiutil import MIDIFile

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations, WindowFunctions, DetrendOperations, NoiseTypes

def main():
    params = BrainFlowInputParams()
    params.board_id = 1
    board_id = 1
    params.serial_port = 'COM5'
    sampling_rate = BoardShim.get_sampling_rate(board_id)

    board = BoardShim(board_id, params)
    board.prepare_session()
    board.start_stream()
    BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')

    time.sleep(10)
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()
  
    eeg_channels = board.get_eeg_channels(board_id)
    timestamp = BoardShim.get_timestamp_channel(board_id)
    
        
    eeg_channel = eeg_channels[3]
    psd = DataFilter.get_psd_welch(data[eeg_channel], nfft, nfft // 2, sampling_rate, WindowFunctions.NO_WINDOW.value)
    df = pd.DataFrame(np.transpose(data))
    plt.figure()
    df[eeg_channels[:3]].plot(subplots=True)
    plt.savefig("before_processing.png")

    # for demo apply different filters to different channels, in production choose one
    for count, channel in enumerate(eeg_channels):
        # # filters work in-place
        DataFilter.perform_bandpass(data[channel], BoardShim.get_sampling_rate(board_id), 22.0, 18.0, 4,
                                        FilterTypes.BUTTERWORTH.value, 0)
        DataFilter.remove_environmental_noise(data[channel], BoardShim.get_sampling_rate(board_id), NoiseTypes.FIFTY.value)

    
    bands = DataFilter.get_avg_band_powers(data, eeg_channels, sampling_rate, True)

    df = pd.DataFrame(np.transpose(data))
    plt.figure()
    df[eeg_channels[:3]].plot(subplots=True)
    plt.savefig("after_processing.png")

    cycled_data = []
    for i in enumerate(data[eeg_channels[0]]):
        if i[0] % 50 == 0:
            cycled_data.append(i[1])

    print("Cycling through data...")
    musical_notes = []
    # Yes... it's really just a bunch of if statments 😅
    for i in cycled_data:
        if i < 1 and i > 0:
            musical_notes.append(60)
        if i < 0 and i > -1:
            musical_notes.append(59)
        if i < -1 and i > -2:
            musical_notes.append(58)
        if i < -2:
            musical_notes.append(57)
        if i > 1 and i < 2:
            musical_notes.append(62)
        if i > 2 and i < 3:
            musical_notes.append(63)
        if i > 3 and i < 4:
            musical_notes.append(64)
        if i > 4 and i < 5:
            musical_notes.append(65)
        if i > 5:
            musical_notes.append(66)

    print("Converting data into music notes")

    track     = 0
    channel   = 0
    time_beat = 0   # In beats
    duration  = 1   # In beats
    tempo     = 250  # In BPM
    volume    = 100 # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track automatically created)
    MyMIDI.addTempo(track,time_beat, tempo)

    for pitch in musical_notes:
        MyMIDI.addNote(track, channel, pitch, time_beat, duration, volume)
        time_beat = time_beat + 1

    with open("le-music.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

    
    print("Conversion completed, play file le-music.mid")


if __name__ == "__main__":
    main()
