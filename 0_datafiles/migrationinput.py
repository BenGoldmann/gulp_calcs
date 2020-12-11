for i in range(0, 52, 1):
    filename = (str(i) + ".inp")
    target = open(filename, 'w+')
    pos = 0.25 + i * (0.5 / 50)
    target.write("""opti conp comp dist defe
cutd 4.0
title 1
Zirconia doped with calcium
name ZrO2
cell
5.070 5.070 5.070 90.0 90.0 90.0
frac
Zr core 0.0 0.0 0.0
Zr shel 0.0 0.0 0.0
O core 0.25 0.25 0.25
O shel 0.25 0.25 0.25
space
225
""")
    target.write("centre " + str(pos) + " 0.25 0.25")
    target.write("""
size 12 24
vacancy 0.25 0.25 0.25
vacancy 0.75 0.25 0.25
""")
    target.write("intersitial O " + str(pos) + " 0.25 0.25 fix x")
    target.write("""
buck
O shel Zr shel 985.869 0.3760 0.0 0 12
buck
O shel O shel 22764.3 0.149 27.89 0 12
spring
Zr 169.617
spring
O 27.29
species
Zr core 2.65
Zr shel 1.35
O core 0.077
O shel -2.077
dump ZrO2.grs
""")
    
magic = open('input.txt', 'w+')

for i in range(0, 51, 1):
    magic.write('gulp < ' + str(i) + '.inp > ' + str(i) + '.out; ')
    
magic.close()