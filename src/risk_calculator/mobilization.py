import os
import numpy as np
import pandas as pd
import glob

def fixed_data(inputs, columns_rm, c_origin, c_destination, c_type):
    # Creates output folder
    content_folder = os.path.join(inputs,"content")
    outputs_folder = os.path.join(inputs,"fixed")
    if not os.path.exists(outputs_folder):
        os.mkdir(outputs_folder)
    # Listing files
    
    files = glob.glob(os.path.join(content_folder, "*.csv"), recursive=True)
    for file in files:
        print("Processing: " + file)
        df = pd.read_csv(file, encoding = "ISO-8859-1")
        df["SIT_ORIGEN"] = df["SIT_ORIGEN"].astype(str).str.split('.', expand = True)[0]
        df["SIT_DESTINO"] = df["SIT_DESTINO"].astype(str).str.split('.', expand = True)[0]
        print("Removing columns")
        for c in columns_rm:
            if c in df.columns:        
                df = df.drop(columns=[c], axis=0)
                
        print("Pivoting data by year")
        columns_exclude = [c_origin, c_destination, c_type]
        df = pd.pivot_table(df, values=df.columns.drop(columns_exclude), index=columns_exclude, aggfunc=np.sum,fill_value=0.0)    
        df.reset_index(inplace=True)

        print("Summarizing mobilization")
        df['total'] = df.loc[:,df.columns.drop(columns_exclude)].sum(axis=1)

        print("Fixing columns names")
        df=df.rename(columns = {c_origin:'id_source'})
        df=df.rename(columns = {c_destination:'id_destination'})
        df=df.rename(columns = {c_type:'type_destination'})

        fl_paths = file.split(os.path.sep)
        output_file = os.path.join(outputs_folder, fl_paths[len(fl_paths)-1])
        print("Saving: " + output_file)
        df.to_csv(output_file, index = False, encoding = "ISO-8859-1")

        
        