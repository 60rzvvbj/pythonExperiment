import os
import shutil
source_dir = 'resources/babynames/'
target_ir = 'resources/newfiles/'

for fileName in os.listdir(source_dir):
    source_file = os.path.join(source_dir, fileName)
    if os.path.isfile(source_file):
        shutil.copy(source_file, os.path.join(
            target_ir, fileName.replace('【瑞客论坛 www.ruike1.com】', '')))
