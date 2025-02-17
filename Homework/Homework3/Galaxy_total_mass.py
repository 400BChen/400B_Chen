import numpy as np
import astropy.units as u
import math

#This function is use numpy to added our new array, and we can easily
#take out the data we need by the coloum.
def Galaxy_mass(filename,particle_type):
    #Generate the array through np.genfromtxt function
    #Using index to represent the particles with a given property,
    #such as if we want type 1, then set the index equal to 1.
    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3)
    index = np.where(data['type'] == particle_type)

    #Mass with unit, and as 3rd line said mass should be in 1e10
    #And Homework3 asked units as 10^12Msun
    standard_unit = 10**10/10**12
    Mass = data[index]['m']*standard_unit*u.Msun
    total_mass = np.around(np.sum(Mass),3)
    return total_mass


mass_halo_MW = Galaxy_mass('MW_000.txt',1) #Mass of Halo
mass_disk_MW = Galaxy_mass('MW_000.txt',2) #Mass of Disk
mass_bulge_MW = Galaxy_mass('MW_000.txt',3) #Mass of Bulge
Total_mass_of_MW =mass_halo_MW+mass_disk_MW+mass_bulge_MW
print('Halo Mass (type(1)) of MW:',mass_halo_MW)
print('Disk Mass (type(2)) of MW:',mass_disk_MW)
print('Bulge Mass (type(3)) of MW:',mass_bulge_MW)
print('Total Mass of MW:',Total_mass_of_MW)


mass_halo_M31 = Galaxy_mass('M31_000.txt',1) #Mass of Halo
mass_disk_M31 = Galaxy_mass('M31_000.txt',2) #Mass of Disk
mass_bulge_M31 = Galaxy_mass('M31_000.txt',3) #Mass of Bulge
Total_mass_of_M31 =mass_halo_M31+mass_disk_M31+mass_bulge_M31
print('Halo Mass (type(1)) of M31:',mass_halo_M31)
print('Halo Mass (type(2)) of M31:',mass_disk_M31)
print('Halo Mass (type(3)) of M31:',mass_bulge_M31)
print('Total Mass of M31:',Total_mass_of_M31)


mass_halo_M33 = Galaxy_mass('M33_000.txt',1) #Mass of Halo
mass_disk_M33 = Galaxy_mass('M33_000.txt',2) #Mass of Disk
mass_bulge_M33 = Galaxy_mass('M33_000.txt',3) #Mass of Bulge
Total_mass_of_M33 =mass_halo_M33+mass_disk_M33+mass_bulge_M33
print('Halo Mass (type(1)) of M33:',mass_halo_M33)
print('Halo Mass (type(2)) of M33:',mass_disk_M33)
print('Halo Mass (type(3)) of M33:',mass_bulge_M33)
print('Total Mass of M33:',Total_mass_of_M33)

