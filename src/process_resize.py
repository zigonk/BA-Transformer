import cv2
import os
import random
import torch
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt


def process_isic2018(
        dim=(512, 512), save_dir='/content/main/data/isic2018/'):
    image_dir_path = '/content/main/data/isic2018/ISIC2018_Task1-2_Training_Input/'
    mask_dir_path = '/content/main/data/isic2018/ISIC2018_Task1_Training_GroundTruth/'

    image_path_list = os.listdir(image_dir_path)
    mask_path_list = os.listdir(mask_dir_path)

    image_path_list = list(filter(lambda x: x[-3:] == 'jpg', image_path_list))
    mask_path_list = list(filter(lambda x: x[-3:] == 'png', mask_path_list))

    image_path_list.sort()
    mask_path_list.sort()

    print(len(image_path_list), len(mask_path_list))

    # ISBI Dataset
    for image_path, mask_path in zip(image_path_list, mask_path_list):
        if image_path[-3:] == 'jpg':
            print(image_path)
            assert os.path.basename(image_path)[:-4].split(
                '_')[1] == os.path.basename(mask_path)[:-4].split('_')[1]
            _id = os.path.basename(image_path)[:-4].split('_')[1]
            image_path = os.path.join(image_dir_path, image_path)
            mask_path = os.path.join(mask_dir_path, mask_path)
            image = plt.imread(image_path)
            mask = plt.imread(mask_path)

            image_new = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
            mask_new = cv2.resize(mask, dim, interpolation=cv2.INTER_NEAREST)

            save_dir_path = save_dir + '/Image'
            os.makedirs(save_dir_path, exist_ok=True)
            np.save(os.path.join(save_dir_path, _id + '.npy'), image_new)

            save_dir_path = save_dir + '/Label'
            os.makedirs(save_dir_path, exist_ok=True)
            np.save(os.path.join(save_dir_path, _id + '.npy'), mask_new)


def process_ph2():
    PH2_images_path = '/content/main/data/isic2016/PH2Dataset/PH2_Dataset_images'

    path_list = os.listdir(PH2_images_path)
    path_list.sort()

    for path in path_list:
        image_path = os.path.join(PH2_images_path, path,
                                  path + '_Dermoscopic_Image', path + '.bmp')
        label_path = os.path.join(PH2_images_path, path, path + '_lesion',
                                  path + '_lesion.bmp')
        image = plt.imread(image_path)
        label = plt.imread(label_path)
        label = label[:, :, 0]

        dim = (512, 512)
        image_new = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        label_new = cv2.resize(label, dim, interpolation=cv2.INTER_AREA)

        image_save_path = os.path.join(
            '/content/main/data/isic2016/PH2Dataset/PH2/Image',
            path + '.npy')
        label_save_path = os.path.join(
            '/content/main/data/isic2016/PH2Dataset/PH2/Label',
            path + '.npy')

        np.save(image_save_path, image_new)
        np.save(label_save_path, label_new)

def process_foot_ulcer(dim=(512,512)):
    for split in ['train', 'test', 'validation']:
        if split == 'train':
            save_dir = '/content/main/data/data/Foot Ulcer Segmentation Challenge/Train'
            image_dir_path = '/content/main/data/data/Foot Ulcer Segmentation Challenge/{}/images/'.format(split)
            mask_dir_path = '/content/main/data/data/Foot Ulcer Segmentation Challenge/{}/labels/'.format(split)

            image_path_list = os.listdir(image_dir_path)
            mask_path_list = os.listdir(mask_dir_path)

            image_path_list = list(filter(lambda x: x[-3:] == 'png', image_path_list))
            mask_path_list = list(filter(lambda x: x[-3:] == 'png', mask_path_list))

            image_path_list.sort()
            mask_path_list.sort()

            print(len(image_path_list), len(mask_path_list))

            # ISBI Dataset
            for image_path, mask_path in zip(image_path_list, mask_path_list):
                if image_path[-3:] == 'png':
                    print(image_path)
                    #assert os.path.basename(image_path)[:-4] == os.path.basename(mask_path)[:-4]
                    _id = os.path.basename(image_path)[:-4]
                    image_path = os.path.join(image_dir_path, image_path)
                    mask_path = os.path.join(mask_dir_path, mask_path)
                    image = plt.imread(image_path)
                    mask = plt.imread(mask_path)

                    image_new = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
                    mask_new = cv2.resize(mask, dim, interpolation=cv2.INTER_NEAREST)

                    save_dir_path = save_dir + '/Image'
                    os.makedirs(save_dir_path, exist_ok=True)
                    np.save(os.path.join(save_dir_path, _id + '.npy'), image_new)

                    save_dir_path = save_dir + '/Label'
                    os.makedirs(save_dir_path, exist_ok=True)
                    np.save(os.path.join(save_dir_path, _id + '.npy'), mask_new)
        elif split == 'validation':
            save_dir = '/content/main/data/data/Foot Ulcer Segmentation Challenge/Validation'
            image_dir_path = '/content/main/data/data/Foot Ulcer Segmentation Challenge/{}/images/'.format(split)
            mask_dir_path = '/content/main/data/data/Foot Ulcer Segmentation Challenge/{}/labels/'.format(split)

            image_path_list = os.listdir(image_dir_path)
            mask_path_list = os.listdir(mask_dir_path)

            image_path_list = list(filter(lambda x: x[-3:] == 'png', image_path_list))
            mask_path_list = list(filter(lambda x: x[-3:] == 'png', mask_path_list))

            image_path_list.sort()
            mask_path_list.sort()

            print(len(image_path_list), len(mask_path_list))

            # ISBI Dataset
            for image_path, mask_path in zip(image_path_list, mask_path_list):
                if image_path[-3:] == 'png':
                    print(image_path)
                    #assert os.path.basename(image_path)[:-4] == os.path.basename(mask_path)[:-4]
                    _id = os.path.basename(image_path)[:-4]
                    image_path = os.path.join(image_dir_path, image_path)
                    mask_path = os.path.join(mask_dir_path, mask_path)
                    image = plt.imread(image_path)
                    mask = plt.imread(mask_path)

                    image_new = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
                    mask_new = cv2.resize(mask, dim, interpolation=cv2.INTER_NEAREST)

                    save_dir_path = save_dir + '/Image'
                    os.makedirs(save_dir_path, exist_ok=True)
                    np.save(os.path.join(save_dir_path, _id + '.npy'), image_new)

                    save_dir_path = save_dir + '/Label'
                    os.makedirs(save_dir_path, exist_ok=True)
                    np.save(os.path.join(save_dir_path, _id + '.npy'), mask_new)
        '''
        elif split == 'test':
            save_dir = '/content/main/data/data/Foot Ulcer Segmentation Challenge/Test'
            image_dir_path = '/content/main/data/data/Foot Ulcer Segmentation Challenge/{}/images/'.format(split)
            mask_dir_path = '/content/main/data/data/Foot Ulcer Segmentation Challenge/{}/labels/'.format(split)

            image_path_list = os.listdir(image_dir_path)
            mask_path_list = os.listdir(mask_dir_path)

            image_path_list = list(filter(lambda x: x[-3:] == 'png', image_path_list))
            mask_path_list = list(filter(lambda x: x[-3:] == 'png', mask_path_list))

            image_path_list.sort()
            mask_path_list.sort()

            print(len(image_path_list), len(mask_path_list))

            # ISBI Dataset
            for image_path, mask_path in zip(image_path_list, mask_path_list):
                if image_path[-3:] == 'png':
                    print(image_path)
                    assert os.path.basename(image_path)[:-4] == os.path.basename(mask_path)[:-4]
                    _id = os.path.basename(image_path)[:-4]
                    image_path = os.path.join(image_dir_path, image_path)
                    mask_path = os.path.join(mask_dir_path, mask_path)
                    image = plt.imread(image_path)
                    mask = plt.imread(mask_path)

                    image_new = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
                    mask_new = cv2.resize(mask, dim, interpolation=cv2.INTER_NEAREST)

                    save_dir_path = save_dir + '/Image'
                    os.makedirs(save_dir_path, exist_ok=True)
                    np.save(os.path.join(save_dir_path, _id + '.npy'), image_new)

                    save_dir_path = save_dir + '/Label'
                    os.makedirs(save_dir_path, exist_ok=True)
                    np.save(os.path.join(save_dir_path, _id + '.npy'), mask_new)
        '''
if __name__ == '__main__':
    #process_isic2018()
    #process_ph2()
    process_foot_ulcer()
