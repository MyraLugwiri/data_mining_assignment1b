import streamlit as st
import pandas as pd


def image_cluster(data):
    grouped_img = data.groupby('cluster')
    for name, group in grouped_img:
        st.write(f'Cluster {name}:')
        col1, col2 = st.columns(2)
        for index, row in group.iterrows():
            if index % 2 == 0:
                with col1:
                    st.image(row['image_src'], width=300, caption=row['image_src'])
            else:
                with col2:
                    st.image(row['image_src'], width=300, caption=row['image_src'])
    return grouped_img


def main():
    st.write('Product Categories')
    st.write('Product Images grouped into multiple clusters')
    # reading the data
    data = pd.read_csv('product_details.csv')
    data = image_cluster(data)


if __name__ == '__main__':
    main()
