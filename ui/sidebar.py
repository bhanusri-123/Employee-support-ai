import streamlit as st


def render_sidebar(employee):

    with st.sidebar:

        st.title("Employee")

        st.markdown(
            f"""
<div class="employee-card">

<b>{employee["name"]}</b><br><br>

🆔 {employee["employee_id"]}<br>

💼 {employee["designation"]}<br>

🏢 {employee["department"]}<br>

📍 {employee["location"]}

</div>
""",
            unsafe_allow_html=True,
        )

        st.divider()

        st.caption("Employee Support AI \
        Intelligent Workplace Assistant")