import time

import numpy as np
import pandas as pd
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter


def main(timesleep=10, filename='test.csv'):
    BoardShim.enable_dev_board_logger()

    # use synthetic board for demo
    params = BrainFlowInputParams()

    # See https://brainflow.readthedocs.io/en/stable/SupportedBoards.html
    # for all supported boards
    board_id = BoardIds.SYNTHETIC_BOARD.value 
    
    # modify parameters, there are several properties
    params.serial_port = '' # serial port is as a string, on windows
                            # would be 'COM#'

    board = BoardShim(board_id, params)

    board.prepare_session()
    board.start_stream()
    
    BoardShim.log_message(LogLevels.LEVEL_INFO.value, 'start sleeping in the main thread')
    time.sleep(timesleep)

    # assign or append data to local variable, this can be 
    # repeatedly done in a loop as well
    data = board.get_board_data()
    
    board.stop_stream()
    board.release_session() 

    # demo how to convert it to pandas DF and plot data

    # you can utilize the subset of eeg_channels in all channels
    # to save only data you want. (there is typically more than
    # just EEG such as accelerometer data, battery level, etc...)
    eeg_channels = BoardShim.get_eeg_channels(board_id)
  
    # Validate that the top 'head' of data looks legit
    df = pd.DataFrame(np.transpose(data))
    print('Data From the Board')
    print(df.head(10))

    # demo for data serialization using brainflow API, we recommend to use it instead pandas.to_csv()
    DataFilter.write_file(data, filename, 'w')  # use 'a' for append mode
   
   
    # Validate that restored data is identical
    restored_data = DataFilter.read_file(filename)
    restored_df = pd.DataFrame(np.transpose(restored_data))
    print('Data From the File')
    print(restored_df.head(10))


if __name__ == "__main__":
    main(timesleep=10, filename='test.csv')