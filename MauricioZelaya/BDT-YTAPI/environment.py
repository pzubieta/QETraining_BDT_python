import yaml

global generic_data
generic_data = yaml.load(open('../configuration/config.yml'))


def before_all(context):
    context.host = generic_data['ENDPOINT']

