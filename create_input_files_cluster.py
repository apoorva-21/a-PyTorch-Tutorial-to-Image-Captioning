from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='/apoorva-volume/captioning/andrejsplits/dataset_coco.json',
                       image_folder='/apoorva-volume/images.cocodataset.org/zips',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/apoorva-volume/captioning/data_generated',
                       max_len=50)
