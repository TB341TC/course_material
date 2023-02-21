import pandas as pd
import numpy as np

def generate_synthetic_data(BETA_TIME, BETA_COSTS):
  df = pd.read_csv('https://raw.githubusercontent.com/TB341TC/course_material/main/ica_2_incomplete_synthetic_data.csv')
  df['V_1'] = BETA_TIME * df['TIME_ROUTE_1'] + BETA_COSTS * df['COST_ROUTE_1']
  df['V_2'] = BETA_TIME * df['TIME_ROUTE_2'] + BETA_COSTS * df['COST_ROUTE_2']
  df['e_1'] = np.random.gumbel(size=df.shape[0])
  df['e_2'] = np.random.gumbel(size=df.shape[0])
  df['U_1'] = df['V_1'] + df['e_1']
  df['U_2'] = df['V_2'] + df['e_2']
  df['y_1'] = df['U_1'] > df['U_2']
  df['y_1'] = df['y_1'].astype(int)
  df['y_2'] = df['U_1'] <= df['U_2']
  df['y_2'] = df['y_2'].astype(int)
  df['CHOICE'] = df['y_2'] + 1
  df['P_1'] = np.exp(df['V_1']) / (np.exp(df['V_1']) + np.exp(df['V_2']))
  df['P_2'] = np.exp(df['V_2']) / (np.exp(df['V_1']) + np.exp(df['V_2']))
  return df