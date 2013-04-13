#!/usr/bin/python

import yaml
from blocketwatch import blocket

config_file = 'config.yaml'
base_url = 'http://www.blocket.se/goteborg?q={0}&cg=0&w={2}&st=s&ca={1}&is=1&l=0&md=th'

def main():
    # Load the config file
    config = open(config_file)
    y = yaml.load(config)
    config.close()

    for item in y['searches']:
        url = base_url.format(item['query'], item['category'], item['breadth'])

        item_id = blocket.check_url(url)

        # Check against the config file - send notification to all
        # keys if the value differs.
        if item['latest-item'] != item_id:
            item['latest-item'] = item_id
            for api_key in y['api-keys']:
                blocket.send_notification(api_key, 'Ny annons!', 'Det finns en ny annons på Blocket.', url)

    # Write the new values to the config
    config = open(config_file, 'w')
    yaml.dump(y, config)
    config.close()

if __name__ == '__main__':
    main()
