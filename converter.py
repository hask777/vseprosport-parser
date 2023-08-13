from dictionary import odd_types

#=== Foras ==========================================================================================================================================================================
def get_types(odd_types):

    results = []

    for odd in odd_types:
        if 'тотал' in odd:
            for i in range(-10, 11, 1):
                vodd = f"{odd} {i}"
                results.append(vodd)


        if 'фора' in odd or 'фору' in odd or 'форой':
            for i in range(-10, 11, 1):
                if i in range(-10, 0, 1):
                    vodd = f"{odd} ({i})"
                else:
                    vodd = f"{odd} (+{i})"
                results.append(vodd)


        if 'победа' in odd or 'победу' in odd or 'победой' in odd:   
            results.append(odd)

        if 'обе забьют' in odd:   
            results.append(odd)

        if 'пенальти (да)' in odd or "пенальти (нет)" in odd:   
            results.append(odd)

    return results

