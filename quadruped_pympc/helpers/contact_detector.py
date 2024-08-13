import numpy as np

from quadruped_pympc.helpers.quadruped_utils import GaitType


class ContactDetector:

    def __init__(self, ):
        
        print("ContactDetector init")

    
    
    def early_contact_update(self, estimated_contact_state, contact_sequence, 
                             current_contact, swing_time, swing_period, feet_GRF):
        
        if(contact_sequence[0][0] == 0 and estimated_contact_state.FL == 1
            and swing_time[0] > (swing_period / 2.)):
            current_contact[0] = 1

            for i in range(0, feet_GRF.FL.shape[0]):
                
                if(len(feet_GRF.FL.shape) > 1):
                    if(feet_GRF.FL[i][2] > -20.0):
                        current_contact[0] = 0
                else:
                    if(feet_GRF.FL[2] > -20.0):
                        current_contact[0] = 0


        if(contact_sequence[1][0] == 0 and estimated_contact_state.FR == 1
            and swing_time[1] > (swing_period / 2.)):
            current_contact[1] = 1

            for i in range(0, feet_GRF.FR.shape[0]):
                
                if(len(feet_GRF.FR.shape) > 1):
                    if(feet_GRF.FR[i][2] > -20.0):
                        current_contact[1] = 0
                else:
                    if(feet_GRF.FR[2] > -20.0):
                        current_contact[1] = 0


        if(contact_sequence[2][0] == 0 and estimated_contact_state.RL == 1
            and swing_time[2] > (swing_period / 2.)):
            current_contact[2] = 1

            for i in range(0, feet_GRF.RL.shape[0]):
                
                if(len(feet_GRF.RL.shape) > 1):
                    if(feet_GRF.RL[i][2] > -20.0):
                        current_contact[2] = 0
                else:
                    if(feet_GRF.RL[2] > -20.0):
                        current_contact[2] = 0

        
        if(contact_sequence[3][0] == 0 and estimated_contact_state.RR == 1
            and swing_time[3] > (swing_period / 2.)):
            current_contact[3] = 1

            for i in range(0, feet_GRF.RR.shape[0]):
                
                if(len(feet_GRF.RR.shape) > 1):
                    if(feet_GRF.RR[i][2] > -20.0):
                        current_contact[3] = 0
                else:
                    if(feet_GRF.RR[2] > -20.0):
                        current_contact[3] = 0

        
        return current_contact

