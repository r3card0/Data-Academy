import pandas as pd

# diccionario de listas
well_offset = {
    "well_name": ["ENCANTADA-500","ENCANTADA-501","PALMIRO-1","JUILE-1"],
    "depth_md" : [2908,1882,2504,553],
    "status" : ["closed","abandoned","abandoned","closed"]
}

well_offset_df = pd.DataFrame(well_offset)
print(well_offset_df)