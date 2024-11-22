import streamlit as st
def calculate_thevenins(vth,rth,rl):
  il=vth/(rth*rl)
  pi=il**2*rl
  return il,pi
st.title("thevenin's theorem")
tab1,tab2=st.tabs(["compute","explanation"])
with tab1:
  col1,col2=st.columns(2)
  with col1:
    with st.container(border=True):
      vth=st.number_input("vth(v)",value=1)
      rth=st.number_input("rth(ohms)",value=1)
      rl=st.number_input("rl(ohms)",value=1)
      compute=st.button("compute")
  with col2:
    with st.container(border=True):
      if compute:
        il,pi=calculate_thevenins(vth,rth,rl)
        st.write(f"IL={il:2f}A")
        st.write(f"PI={pi:2f}W")
with tab2:
  st.write("Thevenin’s theorem states that it is possible to simplify any linear circuit, irrespective of how complex it is, to an equivalent circuit with a single voltage source and a series resistance.")