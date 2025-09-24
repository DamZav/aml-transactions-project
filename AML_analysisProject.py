# %%
import pandas as pd

df = pd.read_csv('SAML-D.csv')

print(df.info())
print(df.columns.to_list())

def general_info_df(df):
    print('General info about DataFtame')
    print(f'Number of rows and columns: {df.shape}')
    print('-'*50)
    print(f'First rows: \n{df.head()}')
    print('-'*50)
    print(f'Number of null data per column: \n{df.isnull().sum()}')
    print('-'*50)
    
general_info_df(df)


# ====== DB CLEANING ======
# df = df.drop(['Sender_account',
#               'Receiver_account'
#               ])


transactions_per_payment_type = df['Payment_type'].value_counts()
# number of laundering transcations per paymet type
laundering_transactions_per_payment_type = df[df['Is_laundering'] == 
                                              1].groupby('Payment_type').size()
print(f'>> Transactions per payment type: \n{transactions_per_payment_type}')
print('-'*50)
print(f'>> Number of laundering transcations per paymet type: \n{laundering_transactions_per_payment_type}')

laundering_transactions_per_country = df[df['Is_laundering'] == 1].groupby('Sender_bank_location').size()
print(laundering_transactions_per_country.sort_values(ascending=False))
# %%
