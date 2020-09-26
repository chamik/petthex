#!/usr/bin/env python3

from PIL import Image
import argparse as ap

path_to_hand = 'hand/'
size = (112, 112)
distortions = [(112, 112), (118, 108), (124, 104), (120, 106), (114, 108)]

pr = ap.ArgumentParser(description='PET THE X')
pr.add_argument('-i', '--input', help='The input image file', required=True)
pr.add_argument('-o', '--output', help='The output gif file', required=True)
args = pr.parse_args()

oface = Image.open(args.input).convert('RGBA')
face = oface.resize(size)
slate = Image.new('RGBA', size, (255, 255, 255, 0,))


hands = []
for i in range(0, 5):
    hands.append(Image.open(path_to_hand + str(i) + '.png').convert('RGBA'))

frames = []
for i in range(0, 5):
    resface = face.resize(distortions[i])
    slate.paste(resface, tuple(map(lambda i, j: i - j, size, distortions[i])), resface)
    slate.paste(hands[i], (0, 0), hands[i])
    frames.append(slate)
    slate = Image.new('RGBA', size, (255, 255, 255, 0,))
    
frames[0].save(args.output, save_all=True, append_images=frames[1:], optimize=False, duration=60, loop=0)

