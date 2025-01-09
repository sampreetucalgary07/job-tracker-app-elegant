import pandas as pd
import datetime
import streamlit as st

def read_job_df(df_path):
    """
    Read the job tracker DataFrame from the specified path.

    Args:
    - df_path (str): The path to the job tracker DataFrame.

    Returns:
    - pd.DataFrame: The job tracker DataFrame.
    """
    df = pd.read_csv(df_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Closing Date'] = pd.to_datetime(df['Closing Date'])
    return df
    
    
config_col = {
    'Date': st.column_config.DateColumn('Date',required=True,default=datetime.datetime.now().date() ,format="MM.DD.YYYY"),
    'Company': st.column_config.TextColumn('Company',required=True),
    'Position': st.column_config.TextColumn('Position',required=True),
    'Link': st.column_config.LinkColumn('Link',required=True),
    'Location': st.column_config.TextColumn('Location',required=False),
    'Closing Date': st.column_config.DateColumn('Closing Date',required=False,format="MM.DD.YYYY"),
    'Applied': st.column_config.CheckboxColumn('Applied',required=True, default=False),
    'Cover Letter': st.column_config.CheckboxColumn('Cover Letter',required=True, default=False),
    'Optimized': st.column_config.CheckboxColumn('Optimized',required=True, default=False),
    'LinkedIn Reach': st.column_config.CheckboxColumn('LinkedIn Reach',required=True, default=False),
    'Cold Email': st.column_config.CheckboxColumn('Cold Email',required=True, default=False),
    'Selected': st.column_config.CheckboxColumn('Selected',required=True, default=False),
    'Stage': st.column_config.SelectboxColumn('Stage', default='Applied',
                                              options=['Not Applied',' Applied', 'Interview', 'Offer', 'Rejected'],
                                              required=True)
    
    
}