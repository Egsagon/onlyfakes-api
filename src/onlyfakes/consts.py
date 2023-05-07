'''
Constants for the core module.
'''


# Website constants
char_limit = 750
target = 'https://onlyfakes.app/.netlify/functions/'

# Request headers
headers = {
    'accept': '*/*',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Access-Control-Allow-Origin': '*',
    'Connection': 'keep-alive',
    'Content-type': 'Application/json', # we are only sending jsons
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'
}

# Engine types and names
class Engine:
    '''
    Representation of all available backends,
    with their model Id and name.
    '''
    
    realistic_women_1 = { 'modelId': 'realistic-vision-v13',      'name': 'Realistic women 1' }
    realistic_women_2 = { 'modelId': 'realistic-vision-14',       'name': 'Realistic women 2' }
    realistic_porn    = { 'modelId': 'uber-realistic-porn-merge', 'name': 'Realistic Porn' }
    hentai            = { 'modelId': 'anything-v3',               'name': 'Hentai' }
    hentai_HD         = { 'modelId': 'anything-v4',               'name': 'HD Hentai' }
    digital_porn      = { 'modelId': 'perfect-world',             'name': 'Digital porn/nudes' }
    digital_realistic = { 'modelId': 'chilloutmix',               'name': 'Realistic, digital-like' }
    realistic_men     = { 'modelId': 'realistic-men',             'name': 'Realistic men' }
    realistic_3       = { 'modelId': 'hardblend',                 'name': 'Realistic 3' }
    furry             = { 'modelId': 'furry',                     'name': 'Furry' }

class Preset:
    pass # TODO

# EOF