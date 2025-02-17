import numpy as np
import astropy.units as u

#This function is use numpy to added our new array, and we can easily
#take out the data we need by the coloum.
def particle_fucntion(filename,particle_type,particle_number):
    #Generate the array through np.genfromtxt function
    #Using index to represent the particles with a given property,
    #such as if we want type 1, then set the index equal to 1.
    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3)
    index = np.where(data['type'] == particle_type)
    #distance in x_axis = data[index]['x'][particle_number])
    #distance in y_axis = str(data[index]['y'][particle_number])
    #distance in z_axis = str(data[index]['z'][particle_number])
    #velocity in x_axis = str(data[index]['vx'][particle_number])
    #velocity in y_axis = str(data[index]['vy'][particle_number])
    #velocity in z_axis = str(data[index]['vz'][particle_number])
    #Well above I have seted one by one, it seems does not work, keep saying
    #'ParticleProperties.py:7: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison File "ParticleProperties.py", line 8, in particle_fucntion
    # x_d = data[index]['x'][particle_number]
    #  IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices


    #So I asked Yuanjew to help me check, seems only use np.mathfunction works, normally use float, int does not work.
    distance_in_3d =np.sqrt(data[index]['x'][particle_number]**2 + data[index]['y'][particle_number]**2 + data[index]['z'][particle_number]**2)*u.kpc
    #above is r = sqrt(x^2+y^2+z^2), which we can get the distance in 3D.
    
    velocity_in_3d = np.sqrt(data[index]['vx'][particle_number]**2 + data[index]['vy'][particle_number]**2 + data[index]['vz'][particle_number]**2)*(u.km/u.s)
    #above is v = sqrt(vx^2+vy^2+xz^2), which we can get 3d velocity
    #Mass with unit, and as 3rd line said mass should be in 1e10
    Mass = data[index]['m'][particle_number]*1e10*u.Msun

    return distance_in_3d,velocity_in_3d,Mass

#After defined the above function, now we can build our main function
#And bring our input in, which is more flexible.
def main():
    file_name = input("the file we need: \n")
    particle_type = int(input("please input the type you want: \n"))
    particle_number = int(input("please input the particle number: \n"))
    Distance_3d,Velocity_3d,mass = particle_fucntion (file_name, particle_type, particle_number)
    Distance_in_light_years = Distance_3d.to(u.lyr)
    #print("3D Distance: \n", round(Distance_3d,3))
    #print("3D Velocity: \n", round(Velocity_3d,3))
    #print("mass: \n", round(mass,3))
    #print("3D distance in light years: \n", round(Distance_in_light_years, 3))
    print("3D Distance:", np.around(Distance_3d,3),'\n')
    print("3D Velocity: ", np.around(Velocity_3d,3),'\n')
    print("mass: ", np.around(mass,3),'\n')
    print("3D distance in light years:", np.around(Distance_in_light_years, 3),'\n')
                
main()
