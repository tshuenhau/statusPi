from inky.auto import auto
inky_display = auto()
inky_display.set_border(inky_display.WHITE)

from inky import InkyPHAT
inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw

img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))

draw = ImageDraw.Draw(img)


from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne, 18)

import textwrap
from check_ping import check_ping

rowHeight = inky_display.HEIGHT/4
columnWidth = (inky_display.WIDTH / 2) 

mainSectionYOffset = 3

x, y = font.getsize("A")
xMargin = (inky_display.WIDTH / 15)
yMargin = (rowHeight - y) /2 


circleDiameter = inky_display.HEIGHT/8
circleXStart = columnWidth + xMargin * 5
circleYMargin = (rowHeight - circleDiameter + yMargin)/2 + 1


activeColor = inky_display.WHITE
inactiveColor = inky_display.RED

def setStatusColor(status):
	if(status == 0):
		return activeColor
	else:
		return inactiveColor

#algotrading
algotradingStatus = check_ping("192.168.1.205")
draw.text((xMargin, yMargin + mainSectionYOffset), "algotrading", inky_display.BLACK, font)
draw.ellipse(((circleXStart, circleYMargin + mainSectionYOffset),(circleXStart + circleDiameter, circleYMargin + circleDiameter + mainSectionYOffset)),setStatusColor(algotradingStatus), inky_display.BLACK)

#autogate
autogateStatus = check_ping("192.168.1.76")
draw.text((xMargin, yMargin + rowHeight + mainSectionYOffset), "autogate",inky_display.BLACK,font)
draw.ellipse(((circleXStart, circleYMargin + rowHeight + mainSectionYOffset),(circleXStart + circleDiameter, circleYMargin + rowHeight + circleDiameter + mainSectionYOffset)),setStatusColor(autogateStatus), inky_display.BLACK)

#pihole
piholeStatus = check_ping("192.168.1.170")

draw.text((xMargin, yMargin+ rowHeight*2 + mainSectionYOffset), "pihole", inky_display.BLACK, font)
draw.ellipse(((circleXStart, circleYMargin + rowHeight*2 + mainSectionYOffset),(circleXStart + circleDiameter, circleYMargin + rowHeight*2 + circleDiameter + mainSectionYOffset)),setStatusColor(piholeStatus), inky_display.BLACK)

smallFont = ImageFont.truetype(FredokaOne, 12)
lastUpdatedYOffset = 5
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M")
lastUpdated = "Last Updated: " + current_time
lastUpdatedW, lastUpdatedH = smallFont.getsize(lastUpdated)
lastUpdatedX = (inky_display.WIDTH / 2) - (lastUpdatedW/2)
#lastUpdatedY = (rowHeight - lastUpdatedH) / 2
lastUpdatedY = yMargin*2 + rowHeight*3 + lastUpdatedYOffset
draw.text((lastUpdatedX,lastUpdatedY), lastUpdated, inky_display.BLACK, smallFont)

#draw.multiline_text((x,y),message, inky_display.BLACK, font, align ="center", spacing = 0)
#draw.multiline_text((x,y),message,inky_display.RED, font, align = "center", spacing =0)

img = img.rotate(180)
inky_display.set_image(img)
inky_display.show()

