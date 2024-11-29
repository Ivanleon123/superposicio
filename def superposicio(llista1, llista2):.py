def superposicio(llista1, llista2):
    """Retorna True si hi ha un element en comú entre dues llistes, False en cas contrari."""
    # Comprovem si hi ha intersecció entre les dues llistes
    for element in llista1:
        if element in llista2:
            return True
    return False

# Proves de la funció
print(superposicio([1, 2, 3], [4, 5, 6]))        # Retorna False
print(superposicio([1, 2, 3], [3, 4, 5]))        # Retorna True
print(superposicio(['a', 'b', 'c'], ['d', 'b']))  # Retorna True
print(superposicio([], [1, 2, 3]))                # Retorna False