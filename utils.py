import json

def generate_output(results):
    errors = []
    output = {}
    for result in results:
        for key,value in zip(result.keys(),result.values()):
            if value != None:
                output[key] = len(value)
            else:
                 errors.append(f"{key} returned an error")

    return output,errors

URLtoSiteNameMapper = {"https://takehome.io/twitter":"twitter","https://takehome.io/facebook":"facebook","https://takehome.io/instagram":"instagram"}

URLs = ["https://takehome.io/twitter","https://takehome.io/facebook","https://takehome.io/instagram"]
            

