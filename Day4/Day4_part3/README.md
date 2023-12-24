## install streamlit

```shell
pip install streamlit
```

```shell
streamlit run page.py
```

```py
import streamlit as st
import pandas as pd

my_dataframe = pd.read_csv("cities.csv")
st.dataframe(my_dataframe)
st.image("./profile.jpg", width=100)

st.title("กิตติศักดิ์ หาญเหี้ยม")
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex("r\'\'\' e^{i\pi} + 1 = 0 \'\'\'")
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
```