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

#FOR PlotQA
mapping = {"bar": 0,
             "dot_line": 1,
             "legend_label": 2,
             "line": 3,
             "preview": 4,
             "title": 5,
             "xlabel": 6,
             "xticklabel": 7,
             "ylabel": 8,
             "yticklabel":9
            }


def generate_detections(source_directory,json_filename,dest_dir):

    json_file = os.path.join(source_directory,json_filename)
    destination_directory = dest_dir

    if not os.path.exists(destination_directory):
        os.mkdir(destination_directory)

    with open(json_file,"r") as f:
        bbox = json.load(f)

    inv_mapping = {v: k for k, v in mapping.iteritems()}
    # print(bbox[0])
    detections_filename = os.path.join(destination_directory, str(bbox['frame']) + ".txt")
    # print(detections_filename)
    tmp_list = []
    for index, box in enumerate(bbox['bboxes']):
      left = box[0]
      top = box[1]
      right = box[2] 
      bottom = box[3] 
      score = bbox['scores'][index]
      cls = inv_mapping[bbox['categories'][index]]

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
