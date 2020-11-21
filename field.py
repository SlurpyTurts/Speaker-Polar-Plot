import math

def dist(point_1, point_2):
	return math.pow(
					math.pow(point_1[0] - point_2[0], 2) +
					math.pow(point_1[1] - point_2[1], 2) 
				, 0.5)

speaker = [] #approximation of an ideal piston made up of speaker_points number of points spaced evenly inside the diameter of the speaker
speaker_diam = 0.254 # meters
speaker_points = 100
freq = 1200
wavelength = 343.0 / freq # 343m/s is accepted velocity of pressure wave propagation through air

grid = []
grid_spacing = 0.01 # meters
grid_points = 400
lower_db_threshold = -60
upper_db_threshold = 0

for x in range(0,speaker_points): # initialize the speaker
	speaker.append([0,speaker_diam*x/speaker_points-speaker_diam/2])

y = -grid_points/2
while y <= grid_points/2:
	x = -grid_points/2
	while x <= grid_points/2:
		sin = 0
		cos = 0
		for point in speaker:
			distance = dist(point, [x*grid_spacing, y*grid_spacing])
			if(distance != 0.0):
				sin += math.sin(2 * math.pi * distance / wavelength) / distance
				cos += math.cos(2 * math.pi * distance / wavelength) / distance
		
		resp = 20*math.log10((math.pow(sin, 2) + math.pow(cos, 2)	) / math.pow(len(speaker),2))

		resp = lower_db_threshold if resp < lower_db_threshold else resp
		resp = upper_db_threshold if resp > upper_db_threshold else resp

		grid.append([
						x*grid_spacing,
						y*grid_spacing,
						resp
					])
		x+=1
	y+=1

for point in grid:
	print(round(point[0], 3), end=", ")
	print(round(point[1], 3), end=", ")
	print(round(point[2], 3))


###this is for printing to a csv so that the cells can be conditionally formatted to show the field plot in excel because I'm at work
# print("", ",", end="")
# for x in range(0, grid_points+1):
# 	print(grid[x][0], ",", end="")
# print("")

# count = 0
# for point in grid:
# 	if(count%(grid_points+1) == 0):
# 		print(point[1], ",", end="")
# 	print(point[2], ",", end="")
# 	if((count+1)%(grid_points+1) == 0):
# 		print("")
# 	count+=1