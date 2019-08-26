# Day of week of year
def dayOfWeek(yy,mm,dd):
	y0 = yy - (14 - mm) // 12
	x = y0 + y0//4 - y0//100 + y0//400
	m0 = mm + 12*((14 - mm)//12) - 2
	d0 = (dd + x + (31*m0)//12 ) % 7
	return d0-1