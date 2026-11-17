# Simple reflec Model  01
# Temperature will be sensed by the sensor and appropriate
#  guiding message will be displayed
def thermostat_agent(temperature):
    if temperature < 18:
        return "HEAT ON" ;
    elif temperature > 26:
        return " COOLING ON ";
    else:
        return "IDLE";
# [-4, 45, 15, 67, 1, 23] its a list of possible temperture list
for t in [-4, 45, 15, 67, 1, 23]:
    print(f" For Temperature = {t} C -> {thermostat_agent(t)}")

