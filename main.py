import streamlit as st
def another_page():

     st.write("This is another page")
st.image("sru_logo.png",use_container_width=True)
pages={
     "theorems":[
          st.Page("thevenins.py",title="thevenins theorem"),
          st.Page("nortans.py",title="nortans theorem"),
     ],
     
}
pg=st.navigation(pages)
pg.run()
