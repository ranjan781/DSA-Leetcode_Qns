import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    pd=players.shape
    return list(pd)