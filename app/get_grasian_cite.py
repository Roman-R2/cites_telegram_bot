import os.path

import xml.etree.ElementTree as ElementTree

from app import settings

if __name__ == '__main__':
    tree = ElementTree.parse(
        os.path.join(
            settings.BASE_DIR,
            r'data/data.xml'
        )
    )
    root = tree.getroot()

    count = 0

    for child in root:
        if child.tag == 'image':
            continue

        if child.tag == 'empty-line':
            continue

        if child.tag == 'p':
            try:
                if child[0].tag and child[0].tag == 'emphasis':
                    print(child[0].text)
            except IndexError:
                print(child.text.replace('\n', '').replace('        ',
                                                           ' '))
                print('------------------------------')

        # print(child.tag, child.attrib)
        #
        # if count > 5:
        #     break

        count += 1
