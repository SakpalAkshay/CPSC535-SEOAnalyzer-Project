import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utility import validateURL, checkSelection, makeWorldCloud, makeBarPlot, keyWordsDensityFind
from DataScraper import getWebPageData
from findWordCount import getProcessTimeAndWordCount
from calculateSynAny import get_synonyms_antonyms_for_df

st.set_page_config()
st.title("SEO Optimize Guru")

if 'new_df' not in st.session_state:
    st.session_state.new_df = None
    
if 'top_10' not in st.session_state:
    st.session_state.top_10 = None
    
if 'process_time' not in st.session_state:
    st.session_state.process_time = None
if 'is_submitted' not in st.session_state:
    st.session_state.is_submitted = False

if 'len_filtered_words' not in st.session_state:
    st.session_state.len_filtered_words = None

if 'more_df' not in st.session_state:
    st.session_state.more_df = None
    


with st.form("my_form"):
    st.subheader("Start by entering your URL")
    url_input = st.text_input("Paste Your URL", key="name", help="e.g., https://example.com")
    options = ['Naive String Matching', 'KMP Algorithm','Rabin Karp','Suffix Array','Suffix Tree']
# Multiselect widget
    st.subheader("Choose Your Algorithms....")
    selected_options = st.multiselect('Select options:', options)
    selectAll = st.checkbox('Select All Algorithms') 
    st.divider()
    if selectAll:
        selected_options = options
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        try:
            
            if not validateURL(url_input):
                st.error("Please Enter Valid Url")
            elif checkSelection(selected_options):
                st.error("Please Select an Appropriate Algorithm")
            else:
                
                scrapped_data, st.session_state.len_filtered_words  = getWebPageData(st.session_state.name)
                if scrapped_data is not None:
                    wordCount, process_time = getProcessTimeAndWordCount(scrapped_data, selected_options)
                    sortedWordCount = dict(reversed(sorted(wordCount.items(), key=lambda item: item[1])))
                    df = pd.DataFrame(sortedWordCount.items(), columns=['Word', 'Word Count'])
                    st.dataframe(df, hide_index=True, width=1700, height=500)
                
                    #data for some further processing
                    st.session_state.new_df = sortedWordCount
                    st.session_state.process_time = process_time
                    st.session_state.top_10 = df.head(10)
                    st.session_state.more_df = df
                    st.session_state.is_submitted = True
                else:
                    st.error("Problem with URL, not able to Parse Data")
        except Exception as e:
            st.text("Error occurred:", e)




if st.button("Show Analysis"):
    # lower max_font_size, change the maximum number of word and lighten the background:
    if st.session_state.is_submitted:
        st.subheader("Word Cloud")
        makeWorldCloud(st.session_state.new_df)
        st.pyplot(plt)
        st.divider()
    
    #bar graph for top ten 10 words in Website
        st.subheader("Top Ten Words in Website")
        makeBarPlot(st.session_state.top_10) # Adjust layout to prevent overlap of labels
        st.pyplot(plt)
        st.divider()
        #bar plot for analysis
        st.subheader("Algorithm Efficiency Graph")
        keys = list(st.session_state.process_time.keys())
        values = list(st.session_state.process_time.values())

        # Create bar chart using matplotlib
        fig, ax = plt.subplots()
        ax.bar(keys, values)

        # Customize the plot
        ax.set_xlabel('Algorithms')
        ax.set_ylabel('Time (seconds)')
        ax.set_title('Execution Time for Various Algorithms')

        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right')

        # Display the plot in Streamlit
        st.pyplot(fig)
        st.divider()
        #Displaying Keyword Density
        st.subheader("Keyword Density (Good Range =  1% to 3%)")
        result_df = keyWordsDensityFind(st.session_state.more_df,st.session_state.len_filtered_words)
        st.dataframe(result_df, hide_index=True, use_container_width=True)
        results = get_synonyms_antonyms_for_df(st.session_state.top_10)
        st.subheader("Synonyms and Antonyms for Top 10 Keywords")
        st.dataframe(results, hide_index=True, use_container_width=True)
        st.divider()
        
    else:
        st.error("Fill the above form first to show Analysis")
    





