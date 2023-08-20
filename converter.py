from dictionary import odd_types
import json

#=== Foras ==========================================================================================================================================================================
def get_types(odd_types):

    results = []

    for odd in odd_types:
        # print(odd)
        if 'тотал' in odd:
            for i in range(-10, 11, 1):
                vodd = f"{odd} {i}"
                results.append(vodd)

        if 'тотал' in odd:
            results.append(vodd)


        if 'фора' in odd or 'фору' in odd or 'форой':
            for i in range(-10, 11, 1):
                if i in range(-10, 0, 1):
                    vodd = f"{odd} ({i})"
                else:
                    vodd = f"{odd} (+{i})"
                results.append(vodd)
            # results.append(odd)


        if 'победа' in odd or 'победу' in odd or 'победой' in odd:   
            results.append(odd)

        if 'не проиграет' in odd:   
            results.append(odd)

        if 'обе забьют' in odd:   
            results.append(odd)

        if 'пенальти (да)' in odd or "пенальти (нет)" in odd:   
            results.append(odd)

        if "угловых" in odd:   
            results.append(odd)

    # print(results)

    return results

