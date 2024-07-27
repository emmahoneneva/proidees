import pandas as pd

centralities_df = pd.DataFrame(centralities, columns=['centrality'])
centralities_df.reset_index(inplace=True, drop=True)
