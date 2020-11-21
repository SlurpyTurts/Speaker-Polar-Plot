reset
set view map
set xlabel "x"
set ylabel "y"
set zlabel "dB"
set xrange [0:2]
set yrange [-2:2]
set key top
set size 1,1
set title "10 IN Speaker Disperion Pattern, 1.2kHz"
set palette rgbformulae 22,13,-31
splot "test.csv" with points palette pt 7