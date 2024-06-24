##funcao aux

def downcast_automatico_df(df):
    """
    Faz downcast automático de todas as colunas numéricas de um DataFrame para o menor tipo numérico possível sem perda de informação.
    """
    tipos_numericos = [np.int8, np.int16, np.int32, np.int64, np.float16, np.float32, np.float64]
    for coluna in df.columns:
        if df[coluna].dtype in [np.int64, np.float64]:  # Verifica se a coluna é numérica (int64 ou float64)
            for tipo in tipos_numericos:
                try:
                    df_copia = df.copy()
                    df_copia[coluna] = df_copia[coluna].astype(tipo)
                    if np.array_equal(df_copia[coluna].to_numpy(), df[coluna].to_numpy()):
                        df[coluna] = df_copia[coluna]
                        print(f"Coluna '{coluna}' convertida para {tipo}")
                        break
                except (ValueError, OverflowError):
                    pass

###########################
#df1
df1=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

df1['Flow Byts/s'] = df1['Flow Byts/s'].replace([np.nan,",,"],0)
df1['Flow Pkts/s'] = df1['Flow Pkts/s'].replace([np.nan,",,"],0)
df1['Flow Byts/s'] = df1['Flow Byts/s'].replace([np.inf,",,"],0)
df1['Flow Pkts/s'] = df1['Flow Pkts/s'].replace([np.inf,",,"],0)

for coluna in df1.columns:
  if coluna != 'Label':
    df1[coluna] = pd.to_numeric(df1[coluna], errors='coerce').fillna(0)

downcast_automatico_df(df1)

# Drop the specified columns
df1 = df1.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df1.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df1_modified.parquet'

###########################
#df2

df2=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

df2 = df2[df2['Label'] != 'Label']
df2['Label'].value_counts()

for coluna in df2.columns:
  if coluna != 'Label':
    df2[coluna] = pd.to_numeric(df2[coluna], errors='coerce').fillna(0)

downcast_automatico_df(df2)

# Drop the specified columns
df2 = df2.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df2.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df2_modified.parquet')

###########################
#df3
df3=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Friday-23-02-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

# Tratamento de NaN e inf
df3['Flow Byts/s'] = df3['Flow Byts/s'].replace([np.nan,",,"],0)
df3['Flow Pkts/s'] = df3['Flow Pkts/s'].replace([np.nan,",,"],0)
df3['Flow Byts/s'] = df3['Flow Byts/s'].replace([np.inf,",,"],0)
df3['Flow Pkts/s'] = df3['Flow Pkts/s'].replace([np.inf,",,"],0)

for coluna in df3.columns:
  if coluna != 'Label':
    df3[coluna] = pd.to_numeric(df3[coluna], errors='coerce').fillna(0)

downcast_automatico_df(df3)

# Drop the specified columns
df3 = df3.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df3.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df3_modified.parquet')

###########################
#df4
df4=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Thursday-01-03-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

df4 = df4[df4['Label'] != 'Label']
df4['Label'].value_counts()

for coluna in df4.columns:
  if coluna != 'Label':
    df4[coluna] = pd.to_numeric(df4[coluna], errors='coerce').fillna(0

# Tratamento de NaN e inf
df4['Flow Byts/s'] = df4['Flow Byts/s'].replace([np.nan,",,"],0)
df4['Flow Pkts/s'] = df4['Flow Pkts/s'].replace([np.nan,",,"],0)
df4['Flow Byts/s'] = df4['Flow Byts/s'].replace([np.inf,",,"],0)
df4['Flow Pkts/s'] = df4['Flow Pkts/s'].replace([np.inf,",,"],0)

downcast_automatico_df(df4)

# Drop the specified columns
df4 = df4.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df4.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df4_modified.parquet')

###########################
#df5
df5=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Thursday-15-02-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

# Tratamento de NaN e inf
df5['Flow Byts/s'] = df5['Flow Byts/s'].replace([np.nan,",,"],0)
df5['Flow Pkts/s'] = df5['Flow Pkts/s'].replace([np.nan,",,"],0)
df5['Flow Byts/s'] = df5['Flow Byts/s'].replace([np.inf,",,"],0)
df5['Flow Pkts/s'] = df5['Flow Pkts/s'].replace([np.inf,",,"],0)

for coluna in df5.columns:
  if coluna != 'Label':
    df5[coluna] = pd.to_numeric(df5[coluna], errors='coerce').fillna(0)


downcast_automatico_df(df5)

# Drop the specified columns
df5 = df5.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df5.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df5_modified.parquet')
###########################
#df6
df6=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Thursday-22-02-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

# Tratamento de NaN e inf


df6['Flow Byts/s'] = df6['Flow Byts/s'].replace([np.nan,",,"],0)
df6['Flow Pkts/s'] = df6['Flow Pkts/s'].replace([np.nan,",,"],0)
df6['Flow Byts/s'] = df6['Flow Byts/s'].replace([np.inf,",,"],0)
df6['Flow Pkts/s'] = df6['Flow Pkts/s'].replace([np.inf,",,"],0)

for coluna in df6.columns:
  if coluna != 'Label':
    df6[coluna] = pd.to_numeric(df6[coluna], errors='coerce').fillna(0)

downcast_automatico_df(df6)

# Drop the specified columns
df6 = df6.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df6.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df6_modified.parquet')

###########################
#df7
df7=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Wednesday-14-02-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

# Tratamento de NaN e inf
df7['Flow Byts/s'] = df7['Flow Byts/s'].replace([np.nan,",,"],0)
df7['Flow Pkts/s'] = df7['Flow Pkts/s'].replace([np.nan,",,"],0)
df7['Flow Byts/s'] = df7['Flow Byts/s'].replace([np.inf,",,"],0)
df7['Flow Pkts/s'] = df7['Flow Pkts/s'].replace([np.inf,",,"],0)

for coluna in df7.columns:
  if coluna != 'Label':
    df7[coluna] = pd.to_numeric(df7[coluna], errors='coerce').fillna(0)

downcast_automatico_df(df7)

# Drop the specified columns
df7 = df7.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df7.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df5_modified.parquet')
###########################
#df8
df8=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Wednesday-21-02-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

for coluna in df8.columns:
  if coluna != 'Label':
    df8[coluna] = pd.to_numeric(df8[coluna], errors='coerce').fillna(0)

downcast_automatico_df(df8)

# Drop the specified columns
df8 = df8.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df8.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df8_modified.parquet')

###########################
#df9
df9=pd.read_csv("/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Wednesday-28-02-2018_TrafficForML_CICFlowMeter.csv", low_memory=False)

df9 = df9[df9['Label'] != 'Label']
df9['Label'].value_counts()

for coluna in df9.columns:
  if coluna != 'Label':
    df9[coluna] = pd.to_numeric(df9[coluna], errors='coerce').fillna(0)

# Tratamento de NaN e inf
df9['Flow Byts/s'] = df9['Flow Byts/s'].replace([np.nan,",,"],0)
df9['Flow Pkts/s'] = df9['Flow Pkts/s'].replace([np.nan,",,"],0)
df9['Flow Byts/s'] = df9['Flow Byts/s'].replace([np.inf,",,"],0)
df9['Flow Pkts/s'] = df9['Flow Pkts/s'].replace([np.inf,",,"],0)

downcast_automatico_df(df9)

# Drop the specified columns
df9 = df9.drop(['Dst Port', 'Protocol', 'Timestamp'], axis=1)

# Save the modified DataFrame as a Parquet file
df9.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df9_modified.parquet')

###########################

# df10 → Muito grande → Manter apenas diferente de Benign

# Conjunto com muitos Benign
chunk_iter = pd.read_csv('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/01-RawDataset/Thuesday-20-02-2018_TrafficForML_CICFlowMeter.csv', chunksize=100000)

df_aux_list = []
for chunk in chunk_iter:
    df_aux_chunk = chunk[chunk['Label'] == 'DDoS attacks-LOIC-HTTP']
    df_aux_list.append(df_aux_chunk)


# Concatenate the filtered chunks into a single DataFrame
df_aux = pd.concat(df_aux_list)

for coluna in df_aux.columns:
  if coluna != 'Label':
    df_aux[coluna] = pd.to_numeric(df_aux[coluna], errors='coerce').fillna(0)


downcast_automatico_df(df_aux)

# Drop the specified columns
df10 = df_aux.drop(['Flow ID', 'Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Protocol','Timestamp'], axis=1)


# Save the modified DataFrame as a Parquet file
df10.to_parquet('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/df10_modified.parquet')

###########################
# Dados final

def dados_tratar(df):

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[()]', '', regex=True)

    return df

if __name__ == "__main__":
    # Obtém a hora atual antes da execução do programa
    pd.set_option('display.max_columns', None)
    hora_inicio = datetime.datetime.now()
    print("Loading dataset...")
    #Load Data
    dspaths = []

    for dirname, _, filenames in os.walk('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset'):
      for filename in filenames:
        if filename.endswith('.parquet'):
          pds = os.path.join(dirname, filename)
          dspaths.append(pds)
          print(pds)

    df = pd.concat([pd.read_parquet(dfp) for dfp in dspaths], ignore_index=True)

    print(f'Dados importados com shape: {df.shape}')
   
    df  = dados_tratar(df)
    print(f'Colunas: {df.columns}')
    print("Distribuição do label:")
    print(df['label'].value_counts())
    print(f'Dados para AL com shape: {df.shape}')
    print("Salvar dataset")
    #df.drop("label", axis=1).to_csv('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/CIC2018_features.csv', index=False,header=False )
    #df["label"].to_csv('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/CIC2018_labels.csv', index=False,header=False )
   
    # Cria um sample aleatório de 20% mantendo a proporção
    df_sample = df.groupby('label', group_keys=False).apply(lambda x: x.sample(frac=0.2, random_state=1))
    print("Distribuição do label de sample:")
    print(df_sample['label'].value_counts())
    df_sample.drop("label", axis=1).to_csv('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/CIC2018sample_features.csv', index=False,header=False )
    df_sample["label"].to_csv('/content/drive/MyDrive/IntrusionDetection/CICIDS2018/02-TreatedDataset/CIC2018sample_labels.csv', index=False,header=False )


    print("Salvar dataset... DONE")




