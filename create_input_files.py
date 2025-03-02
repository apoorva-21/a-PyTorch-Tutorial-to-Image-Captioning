from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='../splits/dataset_coco.json',
                       image_folder='/datasets/COCO-2015',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/datasets/home/50/650/agokhale/285project/a-PyTorch-Tutorial-to-Image-Captioning/data_generated',
                       max_len=50)
