# statusPi: a tiny minimal e-Ink IoT dashboard
## Description:
A small little e-Ink dashboard that displays the online status of your IoT devices. Status is marked as **online** if pinging it results in a response and **offline** otherwise.
## Things needed:
- Raspberry Pi Zero 2 W
- 32 GB MicroSD card
- Pimoroni Inky PHat (red/white/black)
- Pimoroni Pibow Zero 2 W
- Binder Clip

## Display stand assembly:
1. Assemble Pibow Zero 2 W ([link to Pimoroni's guide](https://learn.pimoroni.com/article/pibow-zero-assembly))
2. Attach the Inky PHat to your pi, it should sit nicely on top of the Pibow case
   <Insert Images>
3. Remove one handle from the binder clip
   <Insert Images>
5. With an adhesive of your choice (hot glue works well) attach the bottom of the case to the side of the binder clip without a handle.
   <Insert Images>
      
## How to use:

1. Clone this repo to the home directory of your pi

   `git clone https://github.com/tshuenhau/statuspi.git`
2. You will need to edit status.py and input the ip addresses and name of IoT devices you want tracked.
3. From the root directory of this project, run:

   `python status.py`
4. To configure it to run periodically we will be using **crontab**
   - ### CronTab setup:
      1. Run `crontab -e`
      2. Paste this line into the file

            `*/15* ** * /usr/bin/python /home/pi/statuspi/status.py`
      1. Save the file, now the status.py python script will run every 15 minutes
