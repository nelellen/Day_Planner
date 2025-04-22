# Save this as `day_planner_app.py` and run with `streamlit run day_planner_app.py`

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Interactive Daily Planner", layout="wide")

st.title("Interactive Daily Planner")
st.markdown("Customize your schedule, add activities, and build your ideal day!")

# Sample default schedule
default_schedule = {
    "Time": [
        "7:00 – 7:45 AM", "7:45 – 8:30 AM", "8:30 – 10:30 AM", "10:30 – 12:00 PM",
        "12:00 – 1:00 PM", "1:00 – 3:00 PM", "3:00 – 5:00 PM",
        "6:00 – 6:45 PM", "6:45 – 7:30 PM", "7:30 – 9:00 PM"
    ],
    "Activity": [
        "Light workout (walk, yoga, or dance)",
        "Shower + breakfast",
        "Deep data work (project, tutorials)",
        "Practice (SQL, pandas, dashboards)",
        "Lunch + light walk or rest",
        "Learning session (course, reading)",
        "Fun solo date",
        "Stretch or gentle dance",
        "Dinner",
        "Chill & reflect (journal, reading)"
    ]
}

# Create editable DataFrame
df = pd.DataFrame(default_schedule)
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

st.markdown("### Add a New Activity")
with st.form("add_activity_form", clear_on_submit=True):
    new_time = st.text_input("Time (e.g. 9:00 – 10:00 AM)")
    new_activity = st.text_input("Activity")
    submit = st.form_submit_button("Add")

    if submit and new_time and new_activity:
        new_row = {"Time": new_time, "Activity": new_activity}
        edited_df = pd.concat([edited_df, pd.DataFrame([new_row])], ignore_index=True)
        st.success("Activity added! Scroll up to see it.")

# Option to download the edited schedule
st.markdown("### Download Your Schedule")
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(edited_df)
st.download_button("Download as CSV", csv, "custom_day_schedule.csv", "text/csv")

