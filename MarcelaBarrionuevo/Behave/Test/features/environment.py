def before_all(context):
    print("*********Before All********")


def after_feature(context, feature):
    if 'try' in feature.tags:
        print("///////feature TRY ALL///////")
    if 'Test' in feature.name:
        print("///////feature TEST ALL///////")

def before_scenario(context, scenario):
    if 'Withdraw' in scenario.tags:
        print("///////Scenario tag///////")
    if 'Test' in scenario.name:
        print("///////feature TEST TEST///////")

def before_step(context, step):
    print("STEP", step.name)
    print("STEP", step.keyword)
    print("STEP", step.status)

