#Polar Response Plotter
This is a basic script that will plot a 2D approximation of a pure piston speaker element in a plane. The field.py fiel is run and then plotted using plot.plt in gnuplot.

##Config
- speaker_diam sets the speaker diameter in the field.
- speaker_points states that there are some finite number of points in the speaker that approximate the cone. The points are evenly spaced along the diameter of the cone (the cone is placed at the origin of the plane always, running along the y axis equally positive and negative).  A higher number of points will give a better approximation. Note that higher frequency response will suffer from fewer points, if the c2c spacing of the speaker points approaches the frequency being plotted there will be more apparent interference patterns shown that stray away from the pistonic ideal.
- freq sets the frequency to be plotted.
- grid_spacing and grid_points sets the spacing between measurements, and the grid_points set the number of measurements in the x and y axes.
- output the script to 'test.csv' (field.py > test.csv). This is the name of the data file that will be plotted in Gnuplot.

##Plotting
- run the plot.plt in Gnuplot, you're done!