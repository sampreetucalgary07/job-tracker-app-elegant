import streamlit as st
# import os
from src.utils import load_json, load_css
from src.sections import display_job_tracker_interface   
from src.job_tracker import read_job_df
from src.job_tracker import config_col

def on_change_function():
    st.session_state.dataframe_changed = True

def main():
    
    st.set_page_config(page_title="AI Resume Latex", layout="wide")

    config = load_json("config.json")

    # Load the CSS file
    load_css(config["path"]["css_path"])

    df = read_job_df(config["path"]["job_tracker_csv_path"])

    display_job_tracker_interface()


    if "job_tracker_data_frame" not in st.session_state:
        st.session_state.job_tracker_data_frame = df
        
    if "dataframe_changed" not in st.session_state:
        st.session_state.dataframe_changed = False

    st.session_state.job_tracker_data_frame = st.data_editor(df, 
                            use_container_width=True,num_rows="dynamic", 
                            column_config=config_col,
                            key="job_tracker",width=1000,height=1000,
                            on_change=on_change_function, hide_index=False
    )



    if st.session_state.dataframe_changed:
        if st.button("Save Changes"):
            st.session_state.save_change_button = True
            
            with st.spinner("Saving changes..."):

                st.session_state.job_tracker_data_frame.to_csv("auto_job/data/job_tracker/job_applications.csv", index=False)
            
                st.warning("Changes saved successfully!")
                st.session_state.dataframe_changed = False

if __name__ == "__main__":
    main()
