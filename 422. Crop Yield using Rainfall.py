def crop_yield_using_rainfall(const_a, const_b, rainfall):
    return [const_a*r+const_b for r in rainfall]

rainfall = [300, 400, 500]
const_a = 2
const_b = 100

print(crop_yield_using_rainfall(const_a, const_b, rainfall))