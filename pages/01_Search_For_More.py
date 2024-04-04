import streamlit as st
import pandas as pd
from calculateSynAny import get_synonyms_antonyms

st.header("Search for Synonyms and Antonyms")
with st.form('checkSyn'):
    checkWord= st.text_input("Enter Your Keyword to search for Synonyms and Antonyms", key="checkWord")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if checkWord.isalpha():
            syn, any = get_synonyms_antonyms(checkWord)
    
            if len(syn) != 0:
                syn = list(set(syn))
                new_Syn = pd.DataFrame(syn, columns=["Synonyms"])
                st.write(f'Synonyms for {checkWord}')
                st.dataframe(new_Syn, hide_index=True,use_container_width=True)
            else:
                st.error(f"No Synonyms available for {checkWord}")   
        
            if len(any) !=0:
                any = list(set(any))
                new_Ayn = pd.DataFrame(any, columns=['Antonyms'])
                st.write(f'Antonyms for {checkWord}')
                st.dataframe(new_Ayn, hide_index=True, use_container_width=True)
        
            else:
                st.error(f"No Antonyms available for {checkWord} ")
        else:
            st.error("Please enter a valid Keyword")
