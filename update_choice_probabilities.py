import numpy as np

def update_choice_probabilities(observation):
  observation['U_1'] = observation['V_1'] + observation['e_1']
  observation['U_2'] = observation['V_2'] + observation['e_2']
  observation['y_1'] = observation['U_1'] > observation['U_2']
  observation['y_1'] = int(observation['y_1'])
  observation['y_2'] = observation['U_1'] <= observation['U_2']
  observation['y_2'] = int(observation['y_2'])
  observation['CHOICE'] = observation['y_2'] + 1
  observation['P_1'] = np.exp(observation['V_1']) / (np.exp(observation['V_1']) + np.exp(observation['V_2']))
  observation['P_2'] = np.exp(observation['V_2']) / (np.exp(observation['V_1']) + np.exp(observation['V_2']))
  return observation