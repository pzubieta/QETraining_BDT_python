

def before_all(context):
#The command to run behave skipping scenarios (test cases) with certain tags is:
#>  behave ATM_feature2Outline.feature -f plain --tags @pz --summary --no-capture

    print("******************BEFORE ALL******************")

def before_feature(context, feature):
    if 'tag_feature' in feature.tags:
        print("******************FEATURE tag_feature TAG******************")
    if 'Test' in feature.name:
        print("******************FEATURE TRY Test******************")
def before_scenario(context, scenario):
    if 'tag_scenario' in scenario.tags:
        print("******************BEFORE FEATURE******************")
    if 'Test' in scenario.name:
        print("_____________BEFORE scenario________________")

def before_step(context, step):
    if 'withdraw' in step.name:
        print("*------------BEFORE step withdraw-----------------*")
    if 'Test' in step.name:
        print("*------------BEFORE step test-----------------*")