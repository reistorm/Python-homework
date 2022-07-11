# Проверить истинность утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат

result = True
for x in True, False:
    for y in True, False:
        for z in True, False:
            result = result and (not (x or y or z) == (not x and not y and not z))
                
print(result)