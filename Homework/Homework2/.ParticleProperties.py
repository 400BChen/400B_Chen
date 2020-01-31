import numpy as np
import astropy.units as u

#import from Numpy and AstroPy

#create a read function to read our documents.

'''Bring the file we need input the file name                                                                              
Open file, and readline by line.Not sure does the intruoduction of part 2                                                  
asked us to use for loop? or read a new index?                                                                             
So here I just did what it asked "Do the same for the 2nd line for                                                         
the total number of particles'''

def Read(filename):
    file = open(filename,'r')  #open the file
    line1 = file.readline()  #kinds of confused of readline  and readline
    label, value = line1.split()  #Here we split the line as "space" (split data by coloum)
    time = float(value)*u.Myr #cause we import astropy, so we make the value in float, and times units of Myr

    line2 = file.readline()#Do the same for the 2nd line.
    label,value1 = line2.split()#same as line1
    total_number_of_particles  = float(value1)
    #print(time,total_number_of_particles) #The test showed that our print test workes, which time is 0 Myr
    #total number of particles is 135000
    file.close()

    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3) #generate a array by the function and ignore first 3 lines.
    print(data['type'][1])
    #print(data['type'][100]) # The two values are 1, so we are correct
    return time, total_number_of_particles, data

#The command below we can use in future in other files

file = input("the file u need :")
Read(file)


#Read("MW_000.txt")

                                            
