import numpy as np

config_file = open("--path to yaml", 'r')
config = yaml.safe_load(config_file)

num_epochs = config['parameters']['num_epochs']

class diff:
    def __innit__(self):
        self.b = config[diff][width]
        self.vL=0
        self.vR=0
        self.v_dif=np.array([0,0])
        self.r=config[diff][radius]

    #get angular velocities of wheels from velocity and angular vlocity of vehicle
    def get_acc_sig(self,v,av):
        self.vL=(v-self.b*av/2)/self.r
        self.vR = (v + self.b * av / 2)/self.r
        self.v_diff=np.array([self.vL,self.vR])
        return self.v_diff

    # get velocity and angular vlocity of vehicle from angular velocities of wheels
    def  get_vel(self,v_d):
        v=(v_d[0]+v_d[1])/2
        av=(v_d[0]-v_d[1])/self.b
        return v,av

class ackerman:
    def innit(self):

