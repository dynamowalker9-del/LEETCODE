import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    y=[len(players),len(players.columns)]
    return y
