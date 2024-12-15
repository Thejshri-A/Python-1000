def albedo_effects(sensitivity, incoming_solar, reflected_radiation):
    return sensitivity*(incoming_solar-reflected_radiation)

sensitivity = 0.2
incoming_solar = 300
reflected_radiation = 150

print(albedo_effects(sensitivity, incoming_solar, reflected_radiation))