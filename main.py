import argparse
from recbole.quick_start import run_recbole


def parse_arguments():
    parser = argparse.ArgumentParser('Recbole')

    parser.add_argument(
        '--config-file',
        type=str,
        required=True
    )

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    
    args = parse_arguments()
    run_recbole(model=None, dataset=None, config_file_list=[args.config_file])
