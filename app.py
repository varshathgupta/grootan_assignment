import streamlit as st     #importing libraries
import pandas as pd

st.set_option('deprecation.showPyplotGlobalUse', False)   #  setting warnings false

st.markdown(""" # _Grootan Assignment_ :fire:""")
st.subheader(" Upload dataset in csv :arrow_down:")
data = st.file_uploader("Upload a Dataset", type=["csv"])

def main():
    try:
        st.subheader("Heading of the dataset ::arrow_down:")
        df=pd.read_csv(data)                                         # data reads throught pandas
        
        st.write(df.columns)                                         # displaying header alone


        st.subheader("How much rows should display:question:")
        rows= df.shape[0]
        
        totalrows = range(0,rows+1)
       
        rowstoDisplay= st.select_slider("select number of rows from dataset",options=totalrows, value=50)
        
        st.dataframe(df.head(rowstoDisplay))
        st.write(" I hope i have done my best in my assignment :smiley:")



    except :
        print("!!! Upload the dataset !!!!")






if __name__ == '__main__':
	main()
