# Dashboards sync
A server/client dashboard system for syncing a dashboard loops to multiple clients.
Clients are typically Raspbarry Pis with raspbarry OS.

On the server dashboards are fetch using *selenium* from the internet, where they are saved as pngs.
A dashboard loop is the created using *reveljs* and synced to the clients using *rsync*.

Clients are monitored using a dashboard-of-dashboard. A setup where screenshots of the clients
 outputs with an overlapping timestamp is sync back to the server. 



## Features
- With dashboard fetch from the internet, login information are only stored on the server
- Tollerant to bad wifi - no half loaded dashboards or partially rended content due to rsync
- RevelJS provides a flexible base to add all sort of info to the dashboard loop

## Technologies
- **SSH** for establishing a connection between the server and clients
- **RSync** for syncing the dashboards to clients, and dashboard overlays back to the server 
- **RevelJS** for displaying a dashboard loop using the browser on clients
- **Selenium** used for fetching the relevant dashboards from the web and saving then as pngs.
- **SystemMD** used for handling the automatic start and restart of the dashboard clients
- **Python** Scripting language used to tie it all together 

## Todos
- Actually run the code... the is just an idea scetched down.
- Run the clients using the Belana OS, to easily handle software updates, restarts ect. 
- Run the client as a docker image based on https://github.com/balena-io/resin-electronjs to ensure dependencies management (and starup, so we can get rid of systemMD).
- Implement screen on/off control using HDMI CEC (cec-client) [link](https://stackoverflow.com/questions/15315372/sending-cec-commands-via-command-line-over-hdmi)


## Credit
Jornh post [here]((https://discourse.metabase.com/t/displaying-data-on-tv-what-is-your-solution/5535/4).

