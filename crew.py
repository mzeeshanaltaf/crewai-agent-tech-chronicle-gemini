from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer
from util import *

st.sidebar.header("Configuration Options")
app_unlock = configure_apikey_sidebar()
st.sidebar.divider()
st.sidebar.subheader("About")
configure_about_sidebar()

# --- MAIN PAGE CONFIGURATION ---
# Display the lottie file
display_lottiefile("tech_chronicle.json")
st.title("Tech Chronicle")
st.write(":blue[***Crafting Stories of Tomorrow's Innovations -- Powered by CrewAI***]")
st.write("It's an innovative application designed to transform how you research and learn about emerging "
         "technologies. Simply input a topic, and Tech Explorer will delve into the latest advancements, uncover "
         "groundbreaking technologies, and craft a comprehensive article highlighting the most significant innovations."
         "")
st.subheader("Topic")
topic = st.text_input('Enter a Topic', placeholder="Topic Name", label_visibility="collapsed", disabled=not app_unlock)
submit = st.button("Submit", type='primary', disabled=not topic)

if submit:
    with st.spinner('Processing...'):
        crew = Crew(
            agents=[news_researcher, news_writer],
            tasks=[research_task, write_task],
            process=Process.sequential,
        )

        result = crew.kickoff(inputs={'topic': topic})
        container = st.container(border=True)
        container.write(result)
