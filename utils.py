import logging, sys, argparse


def str2bool(v):
    # copy from StackOverflow
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def get_entity(tag_seq, char_seq):
    PROD = get_PROD_entity(tag_seq, char_seq)
    return PROD

def get_PROD_entity(tag_seq, char_seq):
    length = len(char_seq)
    PROD = []
    for i, (char, tag) in enumerate(zip(char_seq, tag_seq)):
        if tag == 'B-产品':
            if 'prod' in locals().keys():
                PROD.append(prod)
                del prod
            prod = char
            if i+1 == length:
                PROD.append(prod)
        if tag == 'I-产品':
            prod += char
            if i+1 == length:
                PROD.append(prod)
        if tag not in ['I-产品', 'B-产品']:
            if 'prod' in locals().keys():
                PROD.append(prod)
                del prod
            continue
    return PROD


def get_logger(filename):
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
    logging.getLogger().addHandler(handler)
    return logger
