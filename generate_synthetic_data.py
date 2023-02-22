import pandas as pd
import numpy as np

def generate_synthetic_data(BETA_TIME, BETA_COST, n_observations=None):
  df = pd.read_csv('https://raw.githubusercontent.com/TB341TC/course_material/main/ica_2_incomplete_synthetic_data.csv')
  if n_observations:
    if (n_observations % 2) == 1:
        raise Exception('Only odd numbers of observations are supported')
    df = df.iloc[:2]
    df = pd.DataFrame(np.repeat(df.values, int(n_observations/2), axis=0), columns = df.columns)
    df['ID'] = list(range(1, int(n_observations/2)+1)) + list(range(1, int(n_observations/2)+1))
    df.sort_values('ID', inplace=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
  df['V_1'] = BETA_TIME * df['TIME_ROUTE_1'] + BETA_COST * df['COST_ROUTE_1']
  df['V_2'] = BETA_TIME * df['TIME_ROUTE_2'] + BETA_COST * df['COST_ROUTE_2']
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