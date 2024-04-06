import streamlit as st
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')


def main():
    
    # Load the Excel files into DataFrames
    excel_file_products = 'data\\product_dataset.xlsx'  # Replace with your file path
    excel_file_cart = 'data\\customer_buy.xlsx'  # Replace with your file path
    df_products = pd.read_excel(excel_file_products)
    df_cart = pd.read_excel(excel_file_cart) if pd.read_excel(excel_file_cart).shape[0] > 0 else pd.DataFrame(columns=df_products.columns)
    st.title(":blue[Available Products:]")
    
    for index, product in df_products.iterrows():
        st.header(f"Product Name: {product['product_name']}")
        
        # Add to cart button for each product
        add_to_cart = st.button(f"Add {product['product_name']} to Cart")
        
        if add_to_cart:
            df2 = pd.DataFrame({
                'product_id': [product['product_id']],
                'product_name': [product['product_name']],
                'sub_category': [product['sub_category']],
                'main_category': [product['main_category']],
                'customer_id': 1
            })
            df_cart = pd.concat([df_cart, df2], ignore_index=True)
            df_cart.to_excel(excel_file_cart, index=False)  # Save the updated cart to Excel
            st.success(f"Added to cart: {product['product_name']}")
        
        st.write("---")
    
    # Display the cart contents
    if not df_cart.empty:
        st.write("\n\nYour Cart:")
        st.dataframe(df_cart, height=200)

if __name__ == "__main__":
    main()
