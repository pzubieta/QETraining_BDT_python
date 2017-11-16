def before_all(context):
    print("*******BEFORE ALL**********")

def before_scenario(context, scenario):
    if 'tag_scenario' in scenario.tags:
        print("*******tag scenrio**********")
    else: print("******ther tag*****")