def before_all(context):
    print("******************BEFORE ALL******************")

def before_feature(context, feature):
    if 'try' in feature.tags:
        print("******************FEATURE TRY TAG******************")
    if 'Test' in feature.name:
        print("******************FEATURE TRY Test******************")
def before_scenario(context, scenario):
    if 'tag_scenario' in scenario.tags:
        print("******************BEFORE FEATURE******************")
    if 'Test' in scenario.name:
        print("_____________BEFORE scenario________________")

def before_step(context, step):
    if 'tag_step' in step.tags:
        print("*------------BEFORE step tag-----------------*")
    if 'Test' in step.tags:
        print("*------------BEFORE step test-----------------*")