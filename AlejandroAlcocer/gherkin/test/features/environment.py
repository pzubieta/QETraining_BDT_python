import yaml

global generic_data
generic_data = yaml.load(open("AlejandroAlcocer/gherkin/test/configuration/config.yaml"))



def before_all(context):
    context.host = generic_data["app"]["host"]
    context.method = generic_data["app"]["method"]
    context.code = generic_data["app"]["code"]
    print(context.host + "HOST!")
    print("inside the before all, this should be run once before anything is done")


def after_all(context):
    print("inside the after all, this should be run once after everything is done")


def before_scenario(context, scenario):
    if "tag" in scenario.tags:
        print("inside the tag scenario")
    if "Withdraw fixed amount" in scenario.name:
        print("inside the name scenario")


def before_feature(context, feature):
    if "try" in feature.tags:
        print("inside the feature tags")
    if "Withdraw" in feature.name:
        print("inside the name feature")


def before_steps(context, steps):
    # if "step_tag" in steps.tags:
    #     print("inside the feature tags")
    if "the balance of my account should be" in steps.name:
        print("inside the name steps")
