def CRT(numbers, modules):
    product_wo_smod = [] # Product without specific mod
    inverse_pwosmod = [] # Inverse of product_wo_smod % (specific mod)

    index = 0
    for module in modules:
        product_temp = product_list_without_number(modules, module)
        product_wo_smod.append(product_temp)
        inverse_pwosmod.append(pow(product_wo_smod[index], -1, module))
        index += 1
    
    result = 0
    for number, product, inverse in zip(numbers, product_wo_smod, inverse_pwosmod):
        result += number * product * inverse
    product_of_mods = product_list_without_number(modules, 1)
    result = result % product_of_mods

    return result

def product_list_without_number(numbers, number):
    product = 1
    for n in numbers:
        if n != number:
            product *= n
    return product
    

# Explanation source: http://www-math.ucdenver.edu/~wcherowi/courses/m5410/ctccrt.html
