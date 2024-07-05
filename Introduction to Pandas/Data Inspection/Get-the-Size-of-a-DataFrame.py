# 2878. Get the Size of a DataFrame

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    sizes = []
    players_len = sizes.append(players.shape[0])
    players_len = sizes.append(players.shape[1])

    return sizes
