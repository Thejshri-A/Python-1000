def even_odd(temps):
    classify=[]
    for temp in temps:
        if temp%2==0:
            classify.append("Even")
        else:
            classify.append("Odd")
    return classify

temps = [22, 27, 31]
print(even_odd(temps))