
import numpy as np
import astropy.units as u

def Read(filename):
    
    
    # open the file 
    file = open(filename,'r')
    
    # read and store time
    line1 = file.readline()
    label, value = line1.split()
    time = float(value)*u.Myr

    # read and store total number of particles
    line2 = file.readline()
    label, value = line2.split()
    total = float(value)
    
    # close file
    file.close()

    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3)
    
    return time, total, data

