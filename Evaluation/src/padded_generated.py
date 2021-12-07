"""
Example Usage : python2 generate_detections_for_fasterrcnn.py [OUTPUT_DIR]/test/coco_val/generalized_rcnn bbox_coco_val_results.json detections
"""

# Import necessary packages here
import numpy as np
import json
import os
import cv2
import logging
import time
import pandas as pd
from tqdm import tqdm
import click
from PIL import Image

#FOR PlotQA
mapping = {"bar": 1,
             "dot_line": 2,
             "legend_label": 3,
             "line": 4,
             "preview": 5,
             "title": 6,
             "xlabel": 7,
             "xticklabel": 8,
             "ylabel": 9,
             "yticklabel":10
            }


def generate_detections(source_directory,json_filename,dest_dir):

    json_file = os.path.join(source_directory,json_filename)
    destination_directory = os.path.join(source_directory,dest_dir)

    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)

    with open(json_file,"r") as f:
        bbox = json.load(f)

    #Reading json into DataFrame
    df = pd.DataFrame(bbox)

    #Getting list of image_ids
    image_ids = sorted(list(set(df['image_id'].values.tolist())))

    inv_mapping = {v: k for k, v in mapping.iteritems()}

    for idx in tqdm(image_ids):

        detections_filename = os.path.join(destination_directory, str(idx) + ".txt")
        new_df = df[df['image_id'] == idx]

        image = Image.open("/content/plotqa/TEST/png/"+str(idx)+'.png')
        image_width , image_height = image.size
        tmp_list = []
        for row in range(len(new_df)):
            box = new_df.iloc[row]['bbox']
            left = box[0] 
            top = box[1] 
            right = box[0] + box[2]
            bottom = box[1] + box[3]
            score = new_df.iloc[row]['score']
            cls = inv_mapping[new_df.iloc[row]['category_id']]

            if cls == 'title' or cls =='xlabel' or cls == 'ylabel' :

                left = max(0 , left - left*(0.05))
                
                #if left == 0 : print("left ",idx , cls)

                right = min(right + (0.008)*right , image_width)

                if cls != 'xlabel' :

                    bottom = min(image_height , bottom + (0.05)*bottom)
                    top = max(0 , top - top*(0.04))

               
                #if right == image_width : print("right " , idx, cls)

                #if bottom == image_height : print("bottom" , idx, cls)
                #if top == 0 : print("top" , idx, cls)

            tmp_list.append([cls,score,left,top,right,bottom])

        mod_df = pd.DataFrame(tmp_list, columns=['class', 'score', 'xmin', 'ymin', 'xmax', 'ymax'])

        mod_df.to_csv(detections_filename, index=False, header=None, sep=' ')

@click.command()
@click.argument("source_directory")
@click.argument("json_filename")
@click.argument("dest_dir")

def main(**kwargs):
    start_time = time.time()
    logging.basicConfig(level=logging.INFO)
    generate_detections(**kwargs)
    logging.info("--- %s seconds ---" % (time.time() - start_time))

if __name__=="__main__":
    main()
