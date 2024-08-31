import argparse
import importlib
import os.path
import sys
import toml

CONFIG_PATH = 'config/config.toml'


def read_configuration(config_path: str):
    """
    Reads the project's configuration
    :param config_path: path to the config relative to root
    :return:
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(
            "Configuration file is not found. Please, make sure that your run configuration"
            " working directory is set to root"
        )

    _, conf_extension = os.path.splitext(config_path)
    if conf_extension != '.toml':
        raise ValueError('Only toml config file is supported')

    with open(config_path, 'r') as file:
        try:
            config_file = toml.load(file)
        except toml.TomlDecodeError as e:
            raise ValueError(f'Error loading TOML configuration file: {config_path}. Error: {e}')

    if not config_file:
        raise ValueError('configuration file is empty')
    return config_file


if __name__ == '__main__':
    config = read_configuration(config_path=CONFIG_PATH)
    script_location = config['EXECUTABLES']
    script_arguments = config['ARGUMENTS']

    parser_arg = argparse.ArgumentParser()
    parser_arg.add_argument('-p', '--project', required=True, type=str, metavar="project-name",
                            choices=tuple(script_location.keys()))
    project_var = str(sys.argv[2])

    if project_var not in script_location.keys():
        raise ValueError(
            f"The project does not exist. Please, check the list of "
            f"the available projects {list(script_location.keys())}"
        )

    if project_var not in script_arguments:
        raise ValueError(f"Project doesn't have arguments. Go to configuration file and add arguments for the project")

    project_arguments = script_arguments[project_var]
    if project_arguments != 'None':
        for argument, conf_argument in project_arguments.items():
            if 'choices' not in conf_argument.keys():
                conf_argument['choices'] = None
            if 'default' not in conf_argument.keys():
                conf_argument['default'] = None
            parser_arg.add_argument(conf_argument['shortcut'], conf_argument['fullname'],
                                    required=conf_argument['required'], type=type(conf_argument['type']),
                                    metavar=argument,
                                    choices=conf_argument['choices'], default=conf_argument['default'])
    arguments = parser_arg.parse_args()
    arguments = vars(arguments)
    bool_choices = {'False': False, 'True': True}
    arguments = {key: (bool_choices[value] if value in bool_choices else value) for key, value in arguments.items()}

    script = script_location[arguments['project']]
    run_module = importlib.import_module(script)
    local_main_function = getattr(run_module, "main")
    if len(arguments) > 1:
        arguments.pop("project")
        local_main_function(**arguments)
    else:
        local_main_function()