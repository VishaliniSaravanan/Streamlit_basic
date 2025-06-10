import streamlit as st 
from streamlit_option_menu import option_menu

st.title("🎓Vinsup Infotech🎓")

# with st.sidebar:
#     st.header("➤ Vinsup Infotech")                           #indent for sidebar
# st.write("- Vinsup")    #Bullet                               #no indent to display in main page
# st.write("_Vinsup_")   #Italics
# st.write("# Vinsup")    #Bold
# st.write("## Vinsup")  #Normal
# st.text_input("Enter Your Name")
# st.button("Submit")

with st.sidebar:
    data = option_menu( 
        menu_title="Vinsup",
        options=["Home","About us","Contact"],
        icons=["house-check","file-earmark-person","person-rolodex"],

    )
if data=="Home":
    st.header("Join us")
    st.write("Welcome to Vinsup Infotech")
    st.header("Registration Form")
   
    col1,col2=st.columns(2)
    with col1:
        name = st.text_input("Enter your name")
        phone =  st.text_input("Enter your number")
    with col2:
        mail = st.text_input("Enter your E-mail")
        password = st.text_input("Enter your password",type="password")
        
    if st.button("Confirm & Submit"):
        st.write(name,phone,mail,password) 
        st.success("Data inserted sucessfully")
        st.balloons()
    st.metric(label="Python",value="20",delta="20%")
    st.number_input("Rate us",min_value=0)
    st.radio(label=":rainbow[Gender]",options=["Male","Female"],index=None)
    st.selectbox(label="City",options=["Madurai","Chennai","Trichy","Coimabtore","Mumbai","Delhi"])
    st.multiselect(label="City Preferences",options=["Madurai","Chennai","Trichy","Coimabtore","Mumbai","Delhi"])
    st.slider("Age",0,100)
    st.file_uploader("Upload Resume")

elif data=="About us":
    st.header("About us Page")
elif data=="Contact":
    st.header("Contact Page")