    import streamlit as st
    import pandas as pd
    from joblit import load
    
    model=load('model/mode.pk')
    st.title('PRAXIS')
    