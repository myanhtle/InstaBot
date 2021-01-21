import configparser

def init_config(file_path_name):
    """
    Initializes configuration

    Args:
        file_path_name:str: name of .ini file 
    """
    config = configparser.ConfigParser()
    config.read(file_path_name)
    return config
