def before_all(context):
    print('before all!!!!!!!!!!!!!!!!!!!!!!')


def before_feature(context, feature):
    if 'mz' in feature.tags:
        print('feature try tags!!!!!!!!!!!!!!!')
    if 'Test' in feature.name:
        print('feature TEST %s' % feature.name)


def before_scenario(context, scenario):
    if 'tag_scenario' in scenario.tags:
        print('scenario tags!!!!!!!!!!!!!!')
    if 'Test' in scenario.name:
        print('scenario name!!!!!!!!!!!!!')