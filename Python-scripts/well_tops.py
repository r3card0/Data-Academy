# listas de diccionarios
import pandas as pd

well_tops = [
    {"well_name":"well-1", "well_top":"JKS", "md":2308},
    {"well_name":"well-2", "well_top":"JKS", "md":2101},
    {"well_name":"well-3", "well_top":"KM", "md":1708}
]

well_tops_df = pd.DataFrame(well_tops)
print(well_tops_df)