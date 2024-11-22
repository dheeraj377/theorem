import streamlit as st
def calculate_nortans(vth,rth,rl):
  vn=in_ * In
  il=in_ - vn/In
  pl=il**2*rl
  return il,pl
st.title("nortans theorem")
tab1,tab2=st.tabs(["compute","explanation"])
with tab1:
  col1,col2=st.columns(2)
  with col1:
    with st.container(border=True):
      in_=st.number_input("In(a)",value=1)
      In=st.number_input("rn(ohms)",value=1)
      rl=st.number_input("rl(ohms)",value=1)
      compute=st.button("compute")
  with col2:
    with st.container(border=True):
      if compute:
        il,pi=calculate_nortans(in_,In,rl)
        st.write(f"IL={il:2f}A")
        st.write(f"PI={pi:2f}W")
with tab2:
  st.write("Norton's theorem states that any linear circuit can be simplified to an equivalent circuit consisting of a single current source and parallel resistance that is connected to a load.")
