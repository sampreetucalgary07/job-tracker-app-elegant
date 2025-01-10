import pandas as pd
import datetime
import streamlit as st
import time
from src.utils import load_json, load_css
from src.mongodb import update_mongodb_db, read_mongodb_db


def display_job_tracker_interface():
    
    st.title("Job Application Tracker")
    st.divider() 
    # st.write("")

def read_job_df(df):
    """
    Read the job tracker DataFrame from the specified path.

    Args:
    - df_path (str): The path to the job tracker DataFrame.

    Returns:
    - pd.DataFrame: The job tracker DataFrame.
    """
    # df = pd.read_csv(df_path))
    df = df.drop(columns=["_id"])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Closing Date'] = pd.to_datetime(df['Closing Date'])
    return df
    
    
config_col = {
    'Date': st.column_config.DateColumn('Date',required=True,default=datetime.datetime.now().date() ,format="MM.DD.YYYY"),
    'Company': st.column_config.TextColumn('Company',required=True),
    'Position': st.column_config.TextColumn('Position',required=True, width="medium"),
    'Link': st.column_config.LinkColumn('Link',required=True, width="small"),
    'Location': st.column_config.TextColumn('Location',required=False),
    'Closing Date': st.column_config.DateColumn('Closing Date',required=False,format="MM.DD.YYYY", default=datetime.datetime.now().date()),
    'Stage': st.column_config.SelectboxColumn('Stage',
                                              options=['Not Submitted','Submitted', 'Pre-screen','Technical', 'Offer', 'Rejected'],default='Not Submitted',
                                              required=True),
    'Cover Letter': st.column_config.CheckboxColumn('Cover Letter',required=True, default=False),
    'Optimized': st.column_config.CheckboxColumn('Optimized',required=True, default=False),
    'LinkedIn Reach': st.column_config.CheckboxColumn('LinkedIn Reach',required=True, default=False),
    'Cold Email': st.column_config.CheckboxColumn('Cold Email',required=True, default=False),
    'Decision': st.column_config.SelectboxColumn('Decision',required=True,options=['Pending', 'Not Selected', 'Selected'], default='Pending'),
    
    
    
}


def on_change_function():
    st.session_state.dataframe_changed = True

def job_tracker_page():
    
    config = load_json("config.json")

    # Load the CSS file
    load_css(config["path"]["css_path"])
    
    df = read_job_df(read_mongodb_db())#config["path"]["job_tracker_csv_path"])
    
    display_job_tracker_interface()


    if "job_tracker_data_frame" not in st.session_state:
        st.session_state.job_tracker_data_frame = df
        
    if "dataframe_changed" not in st.session_state:
        st.session_state.dataframe_changed = False

    st.session_state.job_tracker_data_frame = st.data_editor(df, 
                            use_container_width=True,num_rows="dynamic", 
                            column_config=config_col,
                            key="job_tracker",width=1000,height=650,
                            on_change=on_change_function, hide_index=True
    )



    if st.session_state.dataframe_changed:
        if st.button("Save Changes"):
            st.session_state.save_change_button = True
            
            with st.spinner("Saving changes..."):

                update_mongodb_db(st.session_state.job_tracker_data_frame)
                time.sleep(1)
                st.success("Data loaded successfully")
                
                # st.session_state.job_tracker_data_frame.to_csv(
                #     config["path"]["job_tracker_csv_path"],
                #     index=False)
            
                # st.warning("Changes saved successfully!")
                st.session_state.dataframe_changed = False